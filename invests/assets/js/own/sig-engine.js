/*
 * Azqato Invests: the Signal plan calculator's engine (9 Sig, also 3 and 6).
 * Pure functions, no page access, so tools/invests/browser.py can test the
 * numbers on their own. The rules are the ones published on this site's 9 Sig
 * page (invests/leveraged/9sig.html); docs/9SIG-CALCULATOR.md explains each.
 *
 *   SigEngine.compute(settings, quarters) -> { rows, summary }
 *
 * settings: { stock, bond, contribution, target, throttle, stockTicker, bondTicker }
 *   stock, bond   starting amounts; their split is the plan's base allocation
 *   contribution  new cash each quarter, after the first
 *   target        quarterly growth target: 0.03, 0.06 or 0.09
 *   throttle      reserve kept in bonds on a buy: 0.10 means a buy uses at
 *                 most 90% of the bond balance (the 90% Buying Power Throttle)
 * quarters: [{ date, price, bondPrice, command, fill, bondFill, income }]
 *   date          "YYYY-MM-DD", quarter end
 *   price         stock fund's quarter-end close
 *   bondPrice     bond fund's quarter-end close
 *   command       "auto" (follow the suggestion), "signal" (trade the signal
 *                 even if a rule says otherwise), "hold" or "rebalance"
 *   fill          optional: the price the stock trade filled at
 *   bondFill      optional: the price the bond trade filled at
 *   income        optional: dividends or interest received this quarter
 *
 * Rounding, as in the community sheet this replaces: stock shares are
 * fractional; bond shares are whole, the trade truncated toward zero, and the
 * remainder kept as cash.
 */
(function (root) {
  "use strict";

  var DOWN_LOOKBACK = 8; // quarters: "the rolling past two years"
  var DOWN_DROP = 0.30;  // 30 Down: at least 30% below that high
  var DOWN_IGNORES = 2;  // sells ignored before the reset
  var SPIKE_GAIN = 1.0;  // Spike Reset: a quarterly gain of 100% or more

  function num(v, d) {
    var n = typeof v === "number" ? v : parseFloat(v);
    return isFinite(n) ? n : d;
  }

  function days(a, b) {
    return (Date.parse(b) - Date.parse(a)) / 86400000;
  }

  function compute(settings, quarters) {
    var s = {
      stock: num(settings.stock, 0),
      bond: num(settings.bond, 0),
      contribution: num(settings.contribution, 0),
      target: num(settings.target, 0.09),
      throttle: num(settings.throttle, 0.10)
    };
    var base = s.stock + s.bond > 0 ? s.stock / (s.stock + s.bond) : 0.6;
    var rows = [];
    var shares = 0, bondShares = 0, cash = 0;
    var stockCost = 0, totalCost = 0, income = 0, peak = 0;
    var down = { active: false, since: -1, ignored: 0 };
    var prev = null;

    quarters.forEach(function (q, i) {
      var price = num(q.price, NaN);
      var bondPrice = num(q.bondPrice, NaN);
      var fill = num(q.fill, price);
      var bondFill = num(q.bondFill, bondPrice);
      var inc = num(q.income, 0);
      var r = { i: i, round: i, date: q.date, price: price, bondPrice: bondPrice, fill: fill, bondFill: bondFill,
                income: inc, command: q.command || "auto", notes: [] };

      if (!(price > 0) || !(bondPrice > 0)) {
        r.error = "Needs a stock price and a bond price";
        rows.push(r);
        return;
      }

      if (i === 0) {
        // The starting position: no signal, no contribution.
        shares = s.stock / fill;
        bondShares = Math.floor(s.bond / bondFill);
        cash = s.bond - bondShares * bondFill;
        stockCost = s.stock;
        totalCost = s.stock + s.bond;
        r.contribution = 0;
        r.change = 0;
        r.balance = s.stock;
        r.signal = s.stock;
        r.expected = 0;
        r.trade = s.stock;
        r.tradeShares = shares;
        r.bondTrade = bondShares;
        r.suggested = "start";
        r.action = "start";
        r.bondValueBefore = 0;
        r.bondSharesBefore = 0;
      } else {
        var c = s.contribution;
        r.contribution = c;
        r.change = price / prev.price - 1;
        r.balance = shares * price;
        r.bondSharesBefore = bondShares;
        r.bondValueBefore = bondShares * bondPrice;
        r.signal = prev.stockValue * (1 + s.target) + c / 2;
        r.expected = r.signal - r.balance;

        // 30 Down: the close is at least 30% below the highest quarterly close
        // of the past two years. The window includes this quarter.
        var hi = 0;
        for (var k = Math.max(0, i - DOWN_LOOKBACK); k <= i; k++) {
          if (rows[k] && rows[k].price > hi) hi = rows[k].price;
          if (k === i && price > hi) hi = price;
        }
        r.high = hi;
        r.down = price <= hi * (1 - DOWN_DROP);
        if (down.active && i - down.since >= DOWN_LOOKBACK) {
          down = { active: false, since: -1, ignored: 0 };
          r.notes.push("30 Down ended after two years");
        }
        if (r.down && !down.active) {
          down = { active: true, since: i, ignored: 0 };
          r.notes.push("30 Down started");
        }
        r.downActive = down.active;
        r.downIgnored = down.ignored;

        // The suggestion, from the rules.
        var sell = r.expected < 0;
        var suggested = "signal";
        if (down.active && sell) {
          suggested = down.ignored < DOWN_IGNORES ? "hold" : "rebalance";
        }
        var total = r.balance + r.bondValueBefore + cash + c + inc;
        var available = r.bondValueBefore * (1 - s.throttle) + cash + c + inc;
        if (suggested === "signal" && !down.active && r.change >= SPIKE_GAIN) {
          // Spike Reset: after the normal trade, the stock share is 60% to 100%.
          var after = Math.min(r.expected, available);
          var share = (r.balance + after) / total;
          if (share >= base && share <= 1) suggested = "spike";
        }
        r.suggested = suggested;

        var cmd = r.command === "auto" ? suggested : r.command;
        if (cmd === "spike") cmd = "rebalance";
        r.action = cmd;

        // The trade, in dollars at the fill price. Positive buys stock.
        var balFill = shares * fill;
        var want;
        if (cmd === "rebalance") {
          want = base * (balFill + r.bondValueBefore + cash + c + inc) - balFill;
          r.signal = base * (balFill + r.bondValueBefore + cash + c + inc);
          r.expected = r.signal - r.balance;
        } else if (cmd === "hold" && sell) {
          want = 0;
        } else {
          want = r.signal - balFill;
        }
        var trade = want;
        if (cmd !== "rebalance" && trade > available) {
          trade = Math.max(0, available);
          r.throttled = true;
          r.notes.push(bondShares === 0 ? "No bonds left to buy with" : "Buy cut to the throttle limit");
        }
        if (cmd !== "rebalance" && trade > 0 && bondShares === 0 && r.bondValueBefore === 0) r.cashShort = true;
        if (r.throttled && !r.cashShort) r.bondShort = true;

        // The 30 Down state follows what was actually done.
        if (down.active && sell && cmd === "hold") down.ignored++;
        if (cmd === "rebalance") {
          if (down.active) r.notes.push("30 Down ended: reset to the base split");
          down = { active: false, since: -1, ignored: 0 };
        }

        r.trade = trade;
        r.tradeShares = trade / fill;
        shares += r.tradeShares;
        stockCost += trade;
        totalCost += c;

        // Bonds: new cash and income in, the stock trade out (or in).
        var pool = c + inc - trade;
        var delta = Math.trunc(pool / bondFill);
        var left = cash + pool - delta * bondFill;
        if (left < -1e-9) { delta -= 1; left += bondFill; }
        if (bondShares + delta < 0) { left += (bondShares + delta) * bondFill; delta = -bondShares; }
        bondShares += delta;
        cash = left;
        r.bondTrade = delta;
      }

      income += inc;
      r.shares = shares;
      r.bondShares = bondShares;
      r.cash = cash;
      r.stockValue = shares * price;
      r.bondValue = bondShares * bondPrice;
      r.total = r.stockValue + r.bondValue + cash;
      r.stockShare = r.total > 0 ? r.stockValue / r.total : 0;
      r.bondShare = 1 - r.stockShare;
      r.stockCost = stockCost;
      r.avgPrice = shares > 0 ? stockCost / shares : 0;
      r.unrealized = r.stockValue - stockCost;
      r.stockGrowth = stockCost > 0 ? r.unrealized / stockCost : 0;
      r.totalCost = totalCost;
      r.gain = r.total - totalCost;
      r.roi = totalCost > 0 ? r.gain / totalCost : 0;
      r.netValue = totalCost > 0 ? r.total / totalCost : 0;
      r.period = prev ? r.total - prev.total - r.contribution : 0;
      r.quarterReturn = prev && prev.total > 0 ? r.period / prev.total : 0;
      r.incomeTotal = income;
      peak = Math.max(peak, r.total);
      r.drawdown = peak > 0 ? 1 - r.total / peak : 0;
      rows.push(r);
      prev = r;
    });

    var ok = rows.filter(function (r) { return !r.error; });
    var last = ok[ok.length - 1];
    var summary = null;
    if (last) {
      var span = days(ok[0].date, last.date);
      var count = function (a) { return ok.filter(function (r) { return r.i > 0 && r.action === a; }).length; };
      summary = {
        rounds: last.round,
        start: ok[0].date,
        end: last.date,
        total: last.total,
        stockValue: last.stockValue,
        bondValue: last.bondValue,
        cash: last.cash,
        shares: last.shares,
        bondShares: last.bondShares,
        stockCost: last.stockCost,
        avgPrice: last.avgPrice,
        unrealized: last.unrealized,
        totalCost: last.totalCost,
        gain: last.gain,
        roi: last.roi,
        // Annualized on money put in, as the community sheet does. It
        // flatters a plan with large late contributions; the page says so.
        annualized: span > 0 && last.totalCost > 0 && last.total > 0 ? Math.pow(last.total / last.totalCost, 365.25 / span) - 1 : 0,
        maxDrawdown: ok.reduce(function (m, r) { return Math.max(m, r.drawdown); }, 0),
        peakStock: ok.reduce(function (m, r) { return Math.max(m, r.stockValue); }, 0),
        peakTotal: ok.reduce(function (m, r) { return Math.max(m, r.total); }, 0),
        holds: count("hold"),
        rebalances: count("rebalance"),
        signals: count("signal"),
        bondShortages: ok.filter(function (r) { return r.bondShort; }).length,
        cashShortages: ok.filter(function (r) { return r.cashShort; }).length,
        upRounds: ok.filter(function (r) { return r.i > 0 && r.period > 0; }).length,
        downRounds: ok.filter(function (r) { return r.i > 0 && r.period < 0; }).length,
        income: last.incomeTotal,
        downActive: last.downActive || false,
        downIgnored: last.downIgnored || 0
      };
    }
    return { rows: rows, summary: summary, base: base, settings: s };
  }

  /* What to do next quarter, given a new close: the same rules, one row ahead.
     Used by the "This quarter" card before the user commits the row. */
  function preview(settings, quarters, next) {
    var out = compute(settings, quarters.concat([next]));
    return out.rows[out.rows.length - 1];
  }

  root.SigEngine = { compute: compute, preview: preview };
})(typeof window !== "undefined" ? window : this);
