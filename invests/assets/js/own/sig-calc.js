/*
 * Azqato Invests: the 9 Sig Calculator page (invests/leveraged/9sig-calculator.html).
 * The numbers come from SigEngine (sig-engine.js); files from SigXlsx
 * (sig-xlsx.js). Plans are kept in this browser's localStorage under one key;
 * docs/9SIG-CALCULATOR.md has the plan behind this page.
 */
(function () {
  "use strict";

  var KEY = "azqato-sig-calc-v1";
  var $ = function (id) { return document.getElementById(id); };
  if (!$("sc-add") || !window.SigEngine) return;

  /* ---------- storage ---------- */

  var DEFAULTS = { stock: 6000, bond: 4000, contribution: 3000, target: 0.09, throttle: 0.10, stockTicker: "TQQQ", bondTicker: "AGG" };

  function newPlan(name) {
    return { name: name, settings: Object.assign({}, DEFAULTS), quarters: [] };
  }

  function uid() {
    return "p" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
  }

  var store = (function () {
    try {
      var s = JSON.parse(localStorage.getItem(KEY));
      if (s && s.plans && s.current && s.plans[s.current]) return s;
    } catch (e) { /* private window or bad data: start fresh */ }
    var id = uid(), plans = {};
    plans[id] = newPlan("My 9 Sig plan");
    return { version: 1, current: id, plans: plans };
  })();

  var saveWarned = false;
  function save() {
    try {
      localStorage.setItem(KEY, JSON.stringify(store));
    } catch (e) {
      if (!saveWarned) {
        saveWarned = true;
        flash("This browser isn't saving (private window or storage full). Download a backup before you leave.");
      }
    }
  }

  function plan() { return store.plans[store.current]; }

  /* ---------- formatting ---------- */

  function money(v, cents) {
    if (!isFinite(v)) return "";
    var s = Math.abs(v).toLocaleString("en-US", { minimumFractionDigits: cents ? 2 : 0, maximumFractionDigits: cents ? 2 : 0 });
    return (v < 0 ? "−$" : "$") + s;
  }
  function price(v) { return isFinite(v) ? "$" + v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : ""; }
  function pct(v, signed) {
    if (!isFinite(v)) return "";
    var s = (Math.abs(v) * 100).toFixed(2) + "%";
    return v < 0 ? "−" + s : (signed && v > 0 ? "+" + s : s);
  }
  function shares(v, whole) {
    if (!isFinite(v)) return "";
    return v.toLocaleString("en-US", { minimumFractionDigits: whole ? 0 : 3, maximumFractionDigits: whole ? 0 : 3 });
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;" }[c]; });
  }
  function tone(v) { return v > 0 ? "sc-up" : v < 0 ? "sc-down" : ""; }
  function prettyDate(iso) {
    var d = new Date(iso + "T00:00:00");
    return isNaN(d) ? iso : d.toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
  }

  var ACTION = { start: "Start", signal: "Signal", hold: "Hold", rebalance: "Reset", spike: "Spike Reset", auto: "Suggested" };

  function flash(msg) {
    var el = $("sc-add-error");
    el.textContent = msg;
  }

  /* ---------- settings ---------- */

  var sForm = $("sc-settings");
  function fillSettings() {
    var s = plan().settings;
    $("sc-stock").value = s.stock;
    $("sc-bond").value = s.bond;
    $("sc-contribution").value = s.contribution;
    $("sc-target").value = String(s.target);
    if ($("sc-target").value !== String(s.target)) $("sc-target").value = "0.09";
    $("sc-throttle").value = String(s.throttle);
    if ($("sc-throttle").value !== String(s.throttle)) $("sc-throttle").value = "0.1";
    $("sc-stock-ticker").value = s.stockTicker;
    $("sc-bond-ticker").value = s.bondTicker;
  }
  sForm.addEventListener("input", function () {
    var s = plan().settings;
    var n = function (id) { var v = parseFloat($(id).value); return isFinite(v) && v >= 0 ? v : 0; };
    s.stock = n("sc-stock");
    s.bond = n("sc-bond");
    s.contribution = n("sc-contribution");
    s.target = parseFloat($("sc-target").value);
    s.throttle = parseFloat($("sc-throttle").value);
    s.stockTicker = ($("sc-stock-ticker").value || "TQQQ").trim().toUpperCase().slice(0, 12);
    s.bondTicker = ($("sc-bond-ticker").value || "AGG").trim().toUpperCase().slice(0, 12);
    save();
    render();
  });
  sForm.addEventListener("submit", function (e) { e.preventDefault(); });

  /* ---------- plans ---------- */

  function fillPlans() {
    var sel = $("sc-plan");
    sel.textContent = "";
    Object.keys(store.plans).forEach(function (id) {
      var o = document.createElement("option");
      o.value = id;
      o.textContent = store.plans[id].name;
      sel.appendChild(o);
    });
    sel.value = store.current;
  }
  $("sc-plan").addEventListener("change", function () {
    store.current = this.value;
    save();
    cancelEdit();
    fillSettings();
    render();
  });
  $("sc-plan-new").addEventListener("click", function () {
    var name = prompt("Name the new plan", "Plan " + (Object.keys(store.plans).length + 1));
    if (!name) return;
    var id = uid();
    store.plans[id] = newPlan(name.slice(0, 60));
    store.current = id;
    save();
    fillPlans(); fillSettings(); render();
  });
  $("sc-plan-rename").addEventListener("click", function () {
    var name = prompt("Rename this plan", plan().name);
    if (!name) return;
    plan().name = name.slice(0, 60);
    save();
    fillPlans();
    render();
  });

  /* ---------- the quarter form ---------- */

  var aForm = $("sc-add");
  var editing = -1;

  function formQuarter() {
    var v = function (id) { var x = parseFloat($(id).value); return isFinite(x) && x > 0 ? x : undefined; };
    var q = { date: $("sc-date").value, price: v("sc-price"), bondPrice: v("sc-bond-price"), command: $("sc-command").value };
    var inc = parseFloat($("sc-income").value);
    if (isFinite(inc) && inc > 0) q.income = inc;
    if (v("sc-fill")) q.fill = v("sc-fill");
    if (v("sc-bond-fill")) q.bondFill = v("sc-bond-fill");
    return q;
  }

  function sorted(qs) {
    return qs.slice().sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : 0; });
  }

  // The quarters the form's row would sit among: all of them, minus the one being edited.
  function others() {
    return plan().quarters.filter(function (q, i) { return i !== editing; });
  }

  function previewRow(q) {
    var list = sorted(others().concat([q]));
    var out = SigEngine.compute(plan().settings, list);
    return out.rows[list.indexOf(q)];
  }

  function tradeText(r, s, short) {
    if (!r) return "";
    if (r.action === "start") {
      return "Start with " + shares(r.shares) + " shares of " + esc(s.stockTicker) + " and " + shares(r.bondShares, true) + " of " + esc(s.bondTicker) + ".";
    }
    var amt = Math.abs(r.trade);
    if (amt < 0.005) {
      return r.action === "hold" ? "Hold: the sell signal of " + money(-r.expected, true) + " is skipped (30 Down)." : "No trade: the balance is on the signal line.";
    }
    var verb = r.trade > 0 ? "Buy" : "Sell";
    var t = verb + " " + money(amt, true) + " of " + esc(s.stockTicker) + " (" + shares(Math.abs(r.tradeShares)) + " shares at " + price(r.fill) + ")";
    if (!short) {
      t += r.trade > 0 ? ", funded by selling " + shares(Math.abs(r.bondTrade), true) + " " + esc(s.bondTicker)
                       : ", and buy " + shares(Math.abs(r.bondTrade), true) + " " + esc(s.bondTicker);
      if (r.trade > 0 && r.bondTrade > 0) t = t.replace(/, funded by selling [^ ]+ /, ", and new cash buys " + shares(r.bondTrade, true) + " ");
    }
    return t + ".";
  }

  function ruleText(r) {
    var out = [];
    if (r.action === "rebalance") out.push(r.suggested === "spike" ? "Spike Reset: back to the base split." : "Reset to the base split.");
    if (r.downActive && r.action !== "rebalance") out.push("30 Down is on: " + r.downIgnored + " of 2 sells skipped so far.");
    if (r.throttled) out.push(r.cashShort ? "No bonds left to buy with." : "The buy is cut to the bond reserve limit.");
    if (r.command !== "auto" && r.suggested && r.suggested !== "start") {
      var sug = r.suggested === "spike" ? "rebalance" : r.suggested;
      if (sug !== r.command) out.push("You chose " + ACTION[r.command] + "; the rules suggest " + ACTION[r.suggested] + ".");
    }
    return out;
  }

  function showPreview() {
    var box = $("sc-preview");
    var q = formQuarter();
    if (!q.date || !q.price || !q.bondPrice) { box.textContent = ""; return; }
    var r = previewRow(q);
    if (!r || r.error) { box.textContent = ""; return; }
    var s = plan().settings;
    box.innerHTML = "<p><strong>" + tradeText(r, s) + "</strong></p>" +
      (r.i > 0 ? "<p>Signal line " + money(r.signal) + "; balance before " + money(r.balance) + ".</p>" : "") +
      ruleText(r).map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("");
  }
  aForm.addEventListener("input", showPreview);

  aForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var q = formQuarter();
    var err = !q.date ? "Enter the quarter's end date." : !q.price ? "Enter the stock's closing price." : !q.bondPrice ? "Enter the bond fund's closing price." : "";
    var clash = others().some(function (o) { return o.date === q.date; });
    if (!err && clash) err = "There's already a quarter on " + prettyDate(q.date) + ".";
    if (err) { flash(err); return; }
    flash("");
    if (editing >= 0) plan().quarters[editing] = q;
    else plan().quarters.push(q);
    plan().quarters = sorted(plan().quarters);
    save();
    cancelEdit();
    render();
    $("sc-date").focus();
  });

  function cancelEdit() {
    editing = -1;
    aForm.reset();
    $("sc-add-btn").textContent = "Add quarter";
    $("sc-cancel").hidden = true;
    $("sc-preview").textContent = "";
    flash("");
    nextDate();
  }
  $("sc-cancel").addEventListener("click", cancelEdit);

  function startEdit(i) {
    var q = plan().quarters[i];
    editing = i;
    $("sc-date").value = q.date;
    $("sc-price").value = q.price;
    $("sc-bond-price").value = q.bondPrice;
    $("sc-income").value = q.income || "";
    $("sc-command").value = q.command || "auto";
    $("sc-fill").value = q.fill || "";
    $("sc-bond-fill").value = q.bondFill || "";
    if (q.fill || q.bondFill) aForm.querySelector(".sc-more").open = true;
    $("sc-add-btn").textContent = "Save quarter";
    $("sc-cancel").hidden = false;
    showPreview();
    $("add-quarter").scrollIntoView({ behavior: "smooth", block: "start" });
    $("sc-price").focus({ preventScroll: true });
  }

  // The next quarter end after the last row, as a starting guess.
  function nextDate() {
    var qs = plan().quarters;
    if (!qs.length || $("sc-date").value) return;
    var d = new Date(qs[qs.length - 1].date + "T00:00:00");
    if (isNaN(d)) return;
    var m = d.getMonth() + 3, y = d.getFullYear() + Math.floor(m / 12);
    m %= 12;
    var end = new Date(y, Math.floor(m / 3) * 3 + 3, 0);
    var pad = function (n) { return n < 10 ? "0" + n : n; };
    $("sc-date").value = end.getFullYear() + "-" + pad(end.getMonth() + 1) + "-" + pad(end.getDate());
  }

  /* ---------- rendering ---------- */

  var result = null;

  function render() {
    var p = plan();
    result = SigEngine.compute(p.settings, p.quarters);
    var s = p.settings;
    Array.prototype.forEach.call(document.querySelectorAll("[data-ticker]"), function (el) {
      el.textContent = el.getAttribute("data-ticker") === "stock" ? s.stockTicker : s.bondTicker;
    });
    $("sc-settings-hint").textContent = s.stockTicker + " / " + s.bondTicker + ", " + Math.round(s.target * 100) + "% a quarter, " + money(s.contribution) + " new cash";
    $("sc-add-help").textContent = p.quarters.length
      ? "Enter the closing prices on the last trading day of the quarter. The action is filled in from the rules; change it if you did something else."
      : "Start with the date and prices of the day you set the plan up. That first row is your starting position; each later row is a quarter end.";
    renderNow();
    renderDashboard();
    renderTable();
  }

  function renderNow() {
    var box = $("sc-now");
    var s = plan().settings;
    var rows = result.rows.filter(function (r) { return !r.error; });
    if (!rows.length) {
      box.innerHTML = "<p>No quarters yet. Check the settings, then add your starting position below.</p>";
      return;
    }
    var r = rows[rows.length - 1];
    var lines = ["<p class=\"sc-now-date\">Latest: " + esc(prettyDate(r.date)) + " (round " + r.round + ")</p>",
                 "<p class=\"sc-now-action\">" + tradeText(r, s) + "</p>"];
    if (r.i > 0) lines.push("<p>Signal line " + money(r.signal) + " against a balance of " + money(r.balance) + ".</p>");
    ruleText(r).forEach(function (t) { lines.push("<p>" + esc(t) + "</p>"); });
    var nextSig = r.stockValue * (1 + s.target) + s.contribution / 2;
    lines.push("<p class=\"sc-now-next\">Next quarter's signal line will be <strong>" + money(nextSig) + "</strong>" +
               " (now " + money(r.stockValue) + " in " + esc(s.stockTicker) + " &times; " + (1 + s.target).toFixed(2) + " + half of " + money(s.contribution) + ").</p>");
    box.innerHTML = lines.join("");
  }

  function tile(label, value, cls, sub) {
    return "<div class=\"sc-tile\"><p class=\"sc-tile-label\">" + label + "</p><p class=\"sc-tile-value " + (cls || "") + "\">" + value + "</p>" +
      (sub ? "<p class=\"sc-tile-sub\">" + sub + "</p>" : "") + "</div>";
  }

  function renderDashboard() {
    var sm = result.summary, s = plan().settings;
    var dash = $("dashboard");
    dash.hidden = !sm;
    if (!sm) return;
    $("sc-headline").textContent = sm.rounds
      ? plan().name + " ran " + sm.rounds + (sm.rounds === 1 ? " quarter" : " quarters") + ", from " + money(result.rows[0].total) + " to " + money(sm.total) +
        ". Total invested " + money(sm.totalCost) + "; return " + pct(sm.roi) + ", about " + pct(sm.annualized) + " a year."
      : plan().name + " starts at " + money(sm.total) + ". Add the next quarter end to see results.";
    $("sc-tiles").innerHTML =
      tile("Total assets", money(sm.total), "", "invested " + money(sm.totalCost)) +
      tile("Total gain", money(sm.gain), tone(sm.gain), pct(sm.roi, true) + " return") +
      tile("Annualized", pct(sm.annualized, true), tone(sm.annualized), "on money put in") +
      tile("Max drawdown", pct(-sm.maxDrawdown), sm.maxDrawdown > 0 ? "sc-down" : "", "from the highest total") +
      tile(esc(s.stockTicker), money(sm.stockValue), "", pct(sm.total ? sm.stockValue / sm.total : 0) + " of the plan") +
      tile(esc(s.bondTicker) + " and cash", money(sm.bondValue + sm.cash), "", pct(sm.total ? (sm.bondValue + sm.cash) / sm.total : 0) + " of the plan");
    renderCharts();
    var stat = function (k, v) { return "<tr><th scope=\"row\">" + k + "</th><td>" + v + "</td></tr>"; };
    $("sc-stats").innerHTML = "<table class=\"sc-stats\"><tbody>" +
      stat(esc(s.stockTicker) + " shares", shares(sm.shares)) +
      stat(esc(s.stockTicker) + " cost (net of sells)", money(sm.stockCost)) +
      stat("Average cost per share", price(sm.avgPrice)) +
      stat("Unrealized gain on " + esc(s.stockTicker), money(sm.unrealized)) +
      stat(esc(s.bondTicker) + " shares", shares(sm.bondShares, true)) +
      stat("Cash", money(sm.cash, true)) +
      stat("Dividends and interest", money(sm.income)) +
      stat("Highest " + esc(s.stockTicker) + " value", money(sm.peakStock)) +
      stat("Highest total", money(sm.peakTotal)) +
      stat("Signal quarters", sm.signals) +
      stat("Hold quarters", sm.holds) +
      stat("Resets", sm.rebalances) +
      stat("Buys cut by the reserve", sm.bondShortages) +
      stat("Buys with no bonds left", sm.cashShortages) +
      stat("Quarters up / down", sm.upRounds + " / " + sm.downRounds) +
      stat("30 Down", sm.downActive ? "On (" + sm.downIgnored + " of 2 sells skipped)" : "Off") +
      "</tbody></table>";
  }

  /* ---------- charts (SVG, colors from the theme) ---------- */

  var W = 560, H = 220, PAD = { l: 64, r: 12, t: 12, b: 28 };

  function axis(min, max, fmt) {
    if (min === max) { max = min + 1; }
    var span = max - min, step = Math.pow(10, Math.floor(Math.log10(span / 4)));
    [1, 2, 2.5, 5, 10].some(function (m) { if (span / (step * m) <= 5) { step *= m; return true; } return false; });
    var lo = Math.floor(min / step) * step, hi = Math.ceil(max / step) * step, ticks = [];
    for (var v = lo; v <= hi + step / 2; v += step) ticks.push(v);
    return { lo: lo, hi: hi, ticks: ticks, fmt: fmt };
  }

  function frame(title, desc, ax, rows, body) {
    var iw = W - PAD.l - PAD.r, ih = H - PAD.t - PAD.b;
    var y = function (v) { return PAD.t + ih - (v - ax.lo) / (ax.hi - ax.lo) * ih; };
    var grid = ax.ticks.map(function (t) {
      return "<line class=\"sc-gridline\" x1=\"" + PAD.l + "\" x2=\"" + (W - PAD.r) + "\" y1=\"" + y(t) + "\" y2=\"" + y(t) + "\"/>" +
        "<text class=\"sc-tick\" x=\"" + (PAD.l - 6) + "\" y=\"" + (y(t) + 4) + "\" text-anchor=\"end\">" + ax.fmt(t) + "</text>";
    }).join("");
    var n = rows.length, xs = [];
    var labels = rows.map(function (r, i) {
      var x = PAD.l + (n === 1 ? iw / 2 : i * iw / (n - 1));
      xs.push(x);
      var every = Math.ceil(n / 6);
      return i % every === 0 || i === n - 1 ? "<text class=\"sc-tick\" x=\"" + x + "\" y=\"" + (H - 8) + "\" text-anchor=\"middle\">" + r.date.slice(0, 7) + "</text>" : "";
    }).join("");
    return "<figure class=\"sc-chart\"><figcaption>" + title + "</figcaption><svg viewBox=\"0 0 " + W + " " + H + "\" role=\"img\" aria-label=\"" + esc(desc) + "\">" +
      grid + body(xs, y, iw) + labels + "</svg></figure>";
  }

  function line(rows, key, ax, cls, area) {
    return function (xs, y) {
      var pts = rows.map(function (r, i) { return xs[i].toFixed(1) + "," + y(r[key]).toFixed(1); });
      var a = area ? "<path class=\"" + cls + "-area\" d=\"M" + xs[0] + "," + y(0) + "L" + pts.join("L") + "L" + xs[xs.length - 1] + "," + y(0) + "Z\"/>" : "";
      return a + "<polyline class=\"" + cls + "\" points=\"" + pts.join(" ") + "\"/>" +
        rows.map(function (r, i) { return "<circle class=\"" + cls + "-dot\" cx=\"" + xs[i] + "\" cy=\"" + y(r[key]) + "\" r=\"2.5\"><title>" + r.date + ": " + ax.fmt(r[key]) + "</title></circle>"; }).join("");
    };
  }

  function renderCharts() {
    var rows = result.rows.filter(function (r) { return !r.error; });
    var box = $("sc-charts");
    if (rows.length < 2) { box.innerHTML = "<p class=\"sc-help\">Charts appear once there are two quarters.</p>"; return; }
    var last = rows[rows.length - 1], s = plan().settings;
    var pctFmt = function (v) { var t = Math.round(v * 1000) / 10; return (t % 1 ? t.toFixed(1) : t) + "%"; };
    var moneyFmt = function (v) { return Math.abs(v) >= 1e6 ? "$" + (v / 1e6).toFixed(1) + "M" : Math.abs(v) >= 1e3 ? "$" + Math.round(v / 1e3) + "K" : "$" + Math.round(v); };
    var roiAx = axis(Math.min(0, Math.min.apply(null, rows.map(function (r) { return r.roi; }))), Math.max(0, Math.max.apply(null, rows.map(function (r) { return r.roi; }))), pctFmt);
    var ddRows = rows.map(function (r) { return Object.assign({}, r, { dd: -r.drawdown }); });
    var ddAx = axis(Math.min(-0.01, Math.min.apply(null, ddRows.map(function (r) { return r.dd; }))), 0, pctFmt);
    var totAx = axis(0, Math.max.apply(null, rows.map(function (r) { return r.total; })), moneyFmt);
    var bars = function (xs, y, iw) {
      var bw = Math.max(2, Math.min(28, iw / rows.length * 0.7));
      return rows.map(function (r, i) {
        var top = y(r.stockValue + r.bondValue + r.cash), mid = y(r.bondValue + r.cash), base = y(0);
        return "<g><title>" + r.date + ": " + money(r.total) + " (" + s.stockTicker + " " + money(r.stockValue) + ", " + s.bondTicker + " and cash " + money(r.bondValue + r.cash) + ")</title>" +
          "<rect class=\"sc-bar-stock\" x=\"" + (xs[i] - bw / 2) + "\" y=\"" + top + "\" width=\"" + bw + "\" height=\"" + Math.max(0, mid - top) + "\"/>" +
          "<rect class=\"sc-bar-bond\" x=\"" + (xs[i] - bw / 2) + "\" y=\"" + mid + "\" width=\"" + bw + "\" height=\"" + Math.max(0, base - mid) + "\"/></g>";
      }).join("");
    };
    var share = last.stockShare, ang = share * 2 * Math.PI, R = 70, cx = 90, cy = 90;
    var arc = share >= 0.9999 ? "<circle class=\"sc-pie-stock\" cx=\"" + cx + "\" cy=\"" + cy + "\" r=\"" + R + "\"/>"
      : share <= 0.0001 ? "<circle class=\"sc-pie-bond\" cx=\"" + cx + "\" cy=\"" + cy + "\" r=\"" + R + "\"/>"
      : "<circle class=\"sc-pie-bond\" cx=\"" + cx + "\" cy=\"" + cy + "\" r=\"" + R + "\"/><path class=\"sc-pie-stock\" d=\"M" + cx + "," + cy + "L" + cx + "," + (cy - R) +
        "A" + R + "," + R + " 0 " + (share > 0.5 ? 1 : 0) + " 1 " + (cx + R * Math.sin(ang)).toFixed(2) + "," + (cy - R * Math.cos(ang)).toFixed(2) + "Z\"/>";
    box.innerHTML =
      frame("Return on money invested", "Return over time, latest " + pct(last.roi), roiAx, rows, line(rows, "roi", roiAx, "sc-line")) +
      frame("Drawdown from the highest total", "Drawdown over time, worst " + pct(-result.summary.maxDrawdown), ddAx, ddRows, line(ddRows, "dd", ddAx, "sc-dd", true)) +
      frame("Total assets", "Total assets each quarter, latest " + money(last.total), totAx, rows, bars) +
      "<figure class=\"sc-chart sc-chart-pie\"><figcaption>Split today</figcaption><div class=\"sc-pie-wrap\"><svg viewBox=\"0 0 180 180\" role=\"img\" aria-label=\"" +
        esc(s.stockTicker) + " " + pct(share) + ", " + esc(s.bondTicker) + " and cash " + pct(1 - share) + "\">" + arc + "</svg>" +
        "<ul class=\"sc-legend\"><li><span class=\"sc-key sc-key-stock\"></span>" + esc(s.stockTicker) + " " + pct(share) + "<br><small>" + money(last.stockValue) + "</small></li>" +
        "<li><span class=\"sc-key sc-key-bond\"></span>" + esc(s.bondTicker) + " and cash " + pct(1 - share) + "<br><small>" + money(last.bondValue + last.cash) + "</small></li></ul></div></figure>";
  }

  /* ---------- the table ---------- */

  // [heading, group, value(row), class, key column?]
  function columns() {
    var s = plan().settings;
    return [
      ["Date", "stock", function (r) { return esc(r.date); }, "sc-sticky", true],
      ["Round", "stock", function (r) { return r.round; }, "", true],
      [s.stockTicker + " close", "stock", function (r) { return price(r.price); }, "", true],
      ["Change", "stock", function (r) { return r.i ? "<span class=\"" + tone(r.change) + "\">" + pct(r.change, true) + "</span>" : ""; }, "", false],
      ["Balance before", "stock", function (r) { return money(r.balance); }, "", false],
      ["Signal line", "stock", function (r) { return money(r.signal); }, "sc-col-signal", true],
      ["30 Down", "stock", function (r) { return r.down ? "<span class=\"sc-flag\">30% drop</span>" : r.downActive ? "on" : ""; }, "", false],
      ["Action", "stock", function (r) {
        var a = ACTION[r.action] || r.action;
        return "<span class=\"sc-action sc-action-" + r.action + "\">" + a + "</span>" + (r.command !== "auto" && r.i ? " <span class=\"sc-mine\" title=\"Chosen by you\">(yours)</span>" : "");
      }, "", true],
      [s.bondTicker + " close", "bond", function (r) { return price(r.bondPrice); }, "", false],
      [s.bondTicker + " shares before", "bond", function (r) { return r.i ? shares(r.bondSharesBefore, true) : ""; }, "", false],
      [s.bondTicker + " value before", "bond", function (r) { return r.i ? money(r.bondValueBefore) : ""; }, "", false],
      ["Expected trade", "trade", function (r) { return r.i ? "<span class=\"" + tone(r.expected) + "\">" + money(r.expected) + "</span>" : ""; }, "", false],
      [s.stockTicker + " trade price", "trade", function (r) { return price(r.fill); }, "", false],
      ["Trade", "trade", function (r) { return "<span class=\"" + tone(r.trade) + "\">" + money(r.trade) + "</span>" + (r.throttled ? " <span class=\"sc-flag\" title=\"Cut to the bond reserve\">cut</span>" : ""); }, "", true],
      [s.stockTicker + " shares traded", "trade", function (r) { return shares(r.tradeShares); }, "", false],
      [s.stockTicker + " shares", "trade", function (r) { return shares(r.shares); }, "", false],
      [s.bondTicker + " trade price", "bondadj", function (r) { return price(r.bondFill); }, "", false],
      [s.bondTicker + " shares traded", "bondadj", function (r) { return r.bondTrade ? (r.bondTrade > 0 ? "+" : "−") + shares(Math.abs(r.bondTrade), true) : "0"; }, "", false],
      [s.bondTicker + " shares", "bondadj", function (r) { return shares(r.bondShares, true); }, "", false],
      [s.stockTicker + " value", "value", function (r) { return money(r.stockValue); }, "", true],
      [s.bondTicker + " value", "value", function (r) { return money(r.bondValue); }, "", true],
      ["Cash", "value", function (r) { return money(r.cash); }, "", false],
      ["Total assets", "value", function (r) { return "<strong>" + money(r.total) + "</strong>"; }, "", true],
      [s.bondTicker + " and cash share", "value", function (r) { return pct(r.bondShare); }, "", false],
      ["New cash", "perf", function (r) { return money(r.contribution); }, "", false],
      ["Gain this quarter", "perf", function (r) { return r.i ? "<span class=\"" + tone(r.period) + "\">" + money(r.period) + "</span>" : ""; }, "", false],
      ["Quarter return", "perf", function (r) { return r.i ? "<span class=\"" + tone(r.quarterReturn) + "\">" + pct(r.quarterReturn, true) + "</span>" : ""; }, "", false],
      ["Unrealized gain", "perf", function (r) { return "<span class=\"" + tone(r.unrealized) + "\">" + money(r.unrealized) + "</span>"; }, "", false],
      [s.stockTicker + " growth", "perf", function (r) { return pct(r.stockGrowth, true); }, "", false],
      ["Total gain", "perf", function (r) { return "<span class=\"" + tone(r.gain) + "\">" + money(r.gain) + "</span>"; }, "", false],
      ["Return", "perf", function (r) { return "<span class=\"" + tone(r.roi) + "\">" + pct(r.roi, true) + "</span>"; }, "", true],
      [s.stockTicker + " cost", "cost", function (r) { return money(r.stockCost); }, "", false],
      ["Average cost", "cost", function (r) { return price(r.avgPrice); }, "", false],
      ["Total invested", "cost", function (r) { return money(r.totalCost); }, "", false],
      ["Net value", "cost", function (r) { return r.netValue.toFixed(3) + "&times;"; }, "", false],
      ["Drawdown", "risk", function (r) { return r.drawdown > 0 ? "<span class=\"sc-down\">" + pct(-r.drawdown) + "</span>" : "0.00%"; }, "", true],
      ["Dividends and interest", "risk", function (r) { return r.income ? money(r.income, true) : ""; }, "", false],
      ["Income to date", "risk", function (r) { return money(r.incomeTotal); }, "", false]
    ];
  }

  var GROUPS = { stock: "Stock", bond: "Bonds before the trade", trade: "Trade", bondadj: "Bond trade", value: "After the trade", perf: "Performance", cost: "Cost", risk: "Drawdown and income" };

  function renderTable() {
    var table = $("sc-table");
    var all = $("sc-all-cols").checked;
    var cols = columns().filter(function (c) { return all || c[4]; });
    var rows = result.rows;
    if (!rows.length) {
      table.innerHTML = "<tbody><tr><td class=\"sc-empty\">No quarters yet.</td></tr></tbody>";
      return;
    }
    var groupRow = "", lastG = null, span = 0;
    var flush = function () { if (lastG !== null) groupRow += "<th scope=\"colgroup\" colspan=\"" + span + "\" class=\"sc-g sc-g-" + lastG + "\">" + GROUPS[lastG] + "</th>"; };
    cols.forEach(function (c) {
      if (c[1] !== lastG) { flush(); lastG = c[1]; span = 0; }
      span++;
    });
    flush();
    var head = "<thead>" + (all ? "<tr>" + groupRow + "<th></th></tr>" : "") + "<tr>" +
      cols.map(function (c) { return "<th scope=\"col\" class=\"sc-g-" + c[1] + " " + c[3] + "\">" + esc(c[0]) + "</th>"; }).join("") +
      "<th scope=\"col\"><span class=\"site-vh\">Edit</span></th></tr></thead>";
    var body = rows.map(function (r) {
      if (r.error) {
        return "<tr class=\"sc-row-error\"><td class=\"sc-sticky\">" + esc(r.date || "") + "</td><td colspan=\"" + (cols.length - 1) + "\">" + esc(r.error) + "</td>" + editCell(r.i) + "</tr>";
      }
      return "<tr class=\"sc-row-" + r.action + "\">" + cols.map(function (c) { return "<td class=\"" + c[3] + "\">" + c[2](r) + "</td>"; }).join("") + editCell(r.i) + "</tr>";
    }).join("");
    table.innerHTML = head + "<tbody>" + body + "</tbody>";
  }

  function editCell(i) {
    return "<td class=\"sc-edit\"><button type=\"button\" class=\"sc-link\" data-edit=\"" + i + "\">Edit</button> " +
      "<button type=\"button\" class=\"sc-link sc-danger\" data-del=\"" + i + "\">Delete</button></td>";
  }

  $("sc-table").addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.hasAttribute("data-edit")) startEdit(+b.getAttribute("data-edit"));
    if (b.hasAttribute("data-del")) {
      var i = +b.getAttribute("data-del"), q = plan().quarters[i];
      if (!confirm("Delete the quarter on " + prettyDate(q.date) + "? Every later quarter is recalculated.")) return;
      plan().quarters.splice(i, 1);
      if (editing === i) cancelEdit();
      save();
      render();
    }
  });
  $("sc-all-cols").addEventListener("change", function () {
    try { localStorage.setItem(KEY + "-cols", this.checked ? "1" : ""); } catch (e) { /* not saved */ }
    renderTable();
  });

  /* ---------- export ---------- */

  function stamp() { return new Date().toISOString().slice(0, 10); }
  function fileName(ext) {
    return (plan().name || "plan").replace(/[^\w\- ]+/g, "").trim().replace(/\s+/g, "-").toLowerCase() + "-" + stamp() + "." + ext;
  }
  function download(blob, name) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  }

  // The export's Quarters sheet: inputs first (what Import reads back), then results.
  var EXPORT_COLS = [
    ["Date", "date", "date"], ["Price", "price", "price"], ["Bond price", "bondPrice", "price"], ["Order Adjust", "command", null],
    ["Stock Price at Adjustment", "fill", "price"], ["Adjustment of bond prices", "bondFill", "price"], ["Cash Income", "income", "money"],
    ["Round", "round", "int"], ["Change", "change", "pct"], ["Balance Before Action", "balance", "money"], ["Sig Line", "signal", "money"],
    ["30 Down", "down", null], ["Action taken", "action", null], ["Suggested", "suggested", null],
    ["Bond shares before", "bondSharesBefore", "int"], ["Bond value before", "bondValueBefore", "money"],
    ["Expected Investment", "expected", "money"], ["Adjusted Amount", "trade", "money"], ["Adjusted Shares", "tradeShares", "shares"],
    ["Accumulated Shares", "shares", "shares"], ["Bond Adjustment", "bondTrade", "int"], ["Bond shares", "bondShares", "int"],
    ["Stock value", "stockValue", "money"], ["Bond value", "bondValue", "money"], ["Cash", "cash", "money"], ["Total Assets", "total", "money"],
    ["Bond and cash share", "bondShare", "pct"], ["Contributions", "contribution", "money"], ["Gain this quarter", "period", "money"],
    ["Quarter return", "quarterReturn", "pct"], ["Unrealized Gain/Loss", "unrealized", "money"], ["Stock Growth", "stockGrowth", "pct"],
    ["Total Gain/Loss", "gain", "money"], ["ROI", "roi", "pct"], ["Stock Cost Price", "stockCost", "money"], ["Average Price", "avgPrice", "price"],
    ["Total Investment Cost", "totalCost", "money"], ["Net Value", "netValue", "shares"], ["Drawdown", "drawdown", "pct"],
    ["Accumulated Cash Income", "incomeTotal", "money"]
  ];
  var CMD_OUT = { auto: "AUTO", signal: "N/A", hold: "HOLD", rebalance: "REBALANCE" };

  function quarterRows(forCsv) {
    var head = EXPORT_COLS.map(function (c) { return forCsv ? c[0] : { v: c[0], bold: true }; });
    var p = plan();
    var body = result.rows.map(function (r) {
      var q = p.quarters[r.i];
      return EXPORT_COLS.map(function (c) {
        var v = c[1] === "command" ? CMD_OUT[q.command || "auto"] : c[1] === "fill" ? q.fill : c[1] === "bondFill" ? q.bondFill
          : c[1] === "income" ? q.income : c[1] === "down" ? (r.down ? "30% drop" : r.downActive ? "on" : "")
          : c[1] === "action" || c[1] === "suggested" ? (ACTION[r[c[1]]] || "") : r[c[1]];
        if (v === undefined || v === null || (typeof v === "number" && !isFinite(v))) return null;
        return forCsv || !c[2] ? v : { v: v, fmt: c[2] };
      });
    });
    return [head].concat(body);
  }

  function settingsRows() {
    var s = plan().settings;
    return [[{ v: "Setting", bold: true }, { v: "Value", bold: true }],
      ["Plan", plan().name], ["Stock positions", { v: s.stock, fmt: "money" }], ["Bond positions", { v: s.bond, fmt: "money" }],
      ["Investment Amount", { v: s.contribution, fmt: "money" }], ["Quarterly target", { v: s.target, fmt: "pct" }],
      ["Buying Power Throttle", { v: s.throttle, fmt: "pct" }], ["Stock", s.stockTicker], ["Bonds", s.bondTicker],
      [], ["Made with the Azqato Invests 9 Sig Calculator", "https://azqato.com/invests/leveraged/9sig-calculator"],
      ["Educational use only. Not financial advice.", null]];
  }

  function summaryRows() {
    var sm = result.summary;
    if (!sm) return [["No quarters yet."]];
    var r = function (k, v, f) { return [k, f ? { v: v, fmt: f } : v]; };
    return [[{ v: "Statistic", bold: true }, { v: "Value", bold: true }],
      r("Rounds", sm.rounds, "int"), r("From", sm.start, "date"), r("To", sm.end, "date"), r("Total Assets", sm.total, "money"),
      r("Stock Value", sm.stockValue, "money"), r("Bond balance", sm.bondValue, "money"), r("Cash", sm.cash, "money"),
      r("Total Investment Cost", sm.totalCost, "money"), r("Total Profit P/L", sm.gain, "money"), r("ROI", sm.roi, "pct"),
      r("Annualized Rate of Return (on money put in)", sm.annualized, "pct"), r("Max Drawdown", sm.maxDrawdown, "pct"),
      r("Shares", sm.shares, "shares"), r("Stock Cost Price", sm.stockCost, "money"), r("Average Price", sm.avgPrice, "price"),
      r("Unrealized Gain/Loss", sm.unrealized, "money"), r("Highest stock value", sm.peakStock, "money"), r("Highest total assets", sm.peakTotal, "money"),
      r("HOLD", sm.holds, "int"), r("REBALANCE", sm.rebalances, "int"), r("Signal (N/A)", sm.signals, "int"),
      r("Bond Shortage Count", sm.bondShortages, "int"), r("Cash Shortage Count", sm.cashShortages, "int"),
      r("Profitable Rounds", sm.upRounds, "int"), r("Unprofitable Rounds", sm.downRounds, "int"), r("Dividends and interest", sm.income, "money")];
  }

  $("sc-export-xlsx").addEventListener("click", function () {
    var widths = EXPORT_COLS.map(function (c) { return Math.max(11, Math.min(26, c[0].length + 3)); });
    download(SigXlsx.write([
      { name: "Quarters", rows: quarterRows(false), widths: widths, freeze: [1, 1] },
      { name: "Summary", rows: summaryRows(), widths: [44, 18] },
      { name: "Settings", rows: settingsRows(), widths: [44, 50] }
    ]), fileName("xlsx"));
  });
  $("sc-export-csv").addEventListener("click", function () {
    var s = plan().settings;
    var rows = quarterRows(true);
    rows.unshift(["# Settings", "Stock positions", s.stock, "Bond positions", s.bond, "Investment Amount", s.contribution,
                  "Quarterly target", s.target, "Buying Power Throttle", s.throttle, "Stock", s.stockTicker, "Bonds", s.bondTicker]);
    download(new Blob(["﻿" + SigXlsx.csv(rows)], { type: "text/csv;charset=utf-8" }), fileName("csv"));
  });
  $("sc-export-json").addEventListener("click", function () {
    var data = { app: "azqato-sig-calc", version: 1, exported: new Date().toISOString(), plan: plan() };
    download(new Blob([JSON.stringify(data, null, 1)], { type: "application/json" }), fileName("json"));
  });
  $("sc-clear").addEventListener("click", function () {
    if (!confirm("Delete “" + plan().name + "” and all its quarters from this browser? Download a backup first if you might want it back.")) return;
    delete store.plans[store.current];
    var ids = Object.keys(store.plans);
    if (!ids.length) { var id = uid(); store.plans[id] = newPlan("My 9 Sig plan"); ids = [id]; }
    store.current = ids[0];
    save();
    cancelEdit(); fillPlans(); fillSettings(); render();
  });

  /* ---------- import ---------- */

  // Header names, lowercased with spaces and punctuation removed, to fields.
  var HEADERS = {
    date: ["date", "quarterend", "quarter", "day", "日期"],
    price: ["price", "close", "stockprice", "stockclose", "closingprice", "adjclose", "價格", "股價"],
    bondPrice: ["bondprice", "bondprices", "bondclose", "bondpricebeforeadjustment", "債券價格"],
    command: ["orderadjust", "action", "command", "order", "signal", "指令"],
    fill: ["stockpriceatadjustment", "tradeprice", "fillprice", "stockfill", "stocktradeprice"],
    bondFill: ["adjustmentofbondprices", "bondtradeprice", "bondfill", "bondfillprice"],
    income: ["cashincome", "income", "dividends", "dividend", "interest", "dividendsandinterest"]
  };
  var SETTING_KEYS = {
    stock: ["stockpositions", "startingstockamount", "stock"], bond: ["bondpositions", "startingbondamount", "bond"],
    contribution: ["investmentamount", "newcasheachquarter", "contribution"],
    target: ["quarterlytarget", "monthlygrowthrate", "target"], throttle: ["buyingpowerthrottle", "throttle", "bondreserveonabuy"],
    stockTicker: ["stockfund", "stockticker"], bondTicker: ["bondfund", "bondticker", "bonds"]
  };
  function norm(h) { return String(h == null ? "" : h).toLowerCase().replace(/[\s_\-\/().:%$#]+/g, ""); }

  function toDate(v) {
    if (v && typeof v === "object" && "date" in v) v = v.date;
    if (typeof v === "number" && isFinite(v) && v > 20000 && v < 80000) {
      return new Date(Math.round((v - 25569) * 86400000)).toISOString().slice(0, 10);
    }
    var s = String(v == null ? "" : v).trim();
    var m = /^(\d{4})[\/\-.](\d{1,2})[\/\-.](\d{1,2})/.exec(s);
    if (m) return m[1] + "-" + ("0" + m[2]).slice(-2) + "-" + ("0" + m[3]).slice(-2);
    m = /^(\d{1,2})[\/\-.](\d{1,2})[\/\-.](\d{4})$/.exec(s);
    if (m) return m[3] + "-" + ("0" + m[1]).slice(-2) + "-" + ("0" + m[2]).slice(-2); // US month/day/year
    var t = Date.parse(s);
    return s && isFinite(t) ? new Date(t - new Date(t).getTimezoneOffset() * 60000).toISOString().slice(0, 10) : null;
  }
  function toNum(v) {
    if (typeof v === "number") return v;
    if (v && typeof v === "object" && "date" in v) return v.date;
    var s = String(v == null ? "" : v).replace(/[$,\s]/g, "").replace(/^\((.*)\)$/, "-$1").replace(/−/g, "-");
    var pctv = /%$/.test(s);
    var n = parseFloat(s);
    return isFinite(n) ? (pctv ? n / 100 : n) : undefined;
  }
  function toCommand(v) {
    var s = norm(v);
    if (/^hold/.test(s)) return "hold";
    if (/^rebal|^reset/.test(s)) return "rebalance";
    if (s === "na" || s === "n/a" || s === "signal" || s === "trade") return "signal";
    return "auto";
  }

  // Find the header row and map its columns. Returns null if no date and price columns.
  function mapSheet(rows) {
    for (var h = 0; h < Math.min(rows.length, 15); h++) {
      var map = {}, used = [], ignored = [];
      (rows[h] || []).forEach(function (cell, c) {
        var n = norm(cell);
        if (!n) return;
        var hit = Object.keys(HEADERS).filter(function (f) { return !(f in map) && HEADERS[f].indexOf(n) > -1; })[0];
        if (hit) { map[hit] = c; used.push(String(cell).trim()); } else ignored.push(String(cell).trim());
      });
      if ("date" in map && "price" in map) return { header: h, map: map, used: used, ignored: ignored };
    }
    return null;
  }

  function readSettings(sheets) {
    var out = {};
    sheets.forEach(function (sh) {
      sh.rows.forEach(function (row) {
        if (!row) return;
        for (var c = 0; c < row.length - 1; c++) {
          var k = norm(row[c]);
          Object.keys(SETTING_KEYS).forEach(function (f) {
            if (f in out || SETTING_KEYS[f].indexOf(k) < 0) return;
            var raw = row[c + 1];
            if (f === "stockTicker" || f === "bondTicker") {
              if (typeof raw === "string" && /^[A-Za-z.]{1,10}$/.test(raw.trim())) out[f] = raw.trim().toUpperCase();
              return;
            }
            var n = toNum(raw);
            if (n === undefined) return;
            if ((f === "target" || f === "throttle") && n > 1) n /= 100;
            out[f] = n;
          });
        }
      });
    });
    return out;
  }

  function importRows(sheets) {
    var best = null;
    sheets.forEach(function (sh) {
      var m = mapSheet(sh.rows);
      if (m && (!best || sh.name === "Quarters")) best = { sheet: sh, m: m };
    });
    if (!best) throw new Error("No sheet with a Date column and a Price column was found. Check the header names (see the list below the Import button).");
    var quarters = [], problems = [], seen = {};
    best.sheet.rows.slice(best.m.header + 1).forEach(function (row, k) {
      var line = best.m.header + k + 2, M = best.m.map;
      var get = function (f) { return f in M ? row[M[f]] : undefined; };
      if (!row || row.every(function (v) { return v === null || v === undefined || String(v).trim() === ""; })) return;
      var date = toDate(get("date"));
      if (!date) { if (get("date") !== undefined && String(get("date")).trim() !== "") problems.push("Row " + line + ": can't read the date “" + get("date") + "”"); return; }
      var q = { date: date, price: toNum(get("price")), bondPrice: toNum(get("bondPrice")), command: "fill" };
      q.command = "command" in M ? toCommand(get("command")) : "auto";
      if (!(q.price > 0)) { problems.push("Row " + line + " (" + date + "): no stock price; skipped"); return; }
      if (!(q.bondPrice > 0)) { problems.push("Row " + line + " (" + date + "): no bond price; skipped"); return; }
      var f = toNum(get("fill")), bf = toNum(get("bondFill")), inc = toNum(get("income"));
      if (f > 0 && Math.abs(f - q.price) > 1e-9) q.fill = f;
      if (bf > 0 && Math.abs(bf - q.bondPrice) > 1e-9) q.bondFill = bf;
      if (inc > 0) q.income = inc;
      if (seen[date]) { problems.push("Row " + line + ": a second row for " + date + "; skipped"); return; }
      seen[date] = true;
      quarters.push(q);
    });
    var ordered = sorted(quarters);
    if (ordered.some(function (q, i) { return q !== quarters[i]; })) problems.push("The rows weren't in date order; they've been sorted.");
    if (!quarters.length) throw new Error("The " + best.sheet.name + " sheet has the right columns but no rows with a date and prices.");
    return { quarters: ordered, problems: problems, used: best.m.used, ignored: best.m.ignored, sheet: best.sheet.name };
  }

  var pending = null;

  function showImport(found, fileLabel) {
    pending = found;
    var box = $("sc-import-preview");
    var s = Object.assign({}, plan().settings, found.settings || {});
    var first = found.quarters[0], last = found.quarters[found.quarters.length - 1];
    var settingsNote = found.settings && Object.keys(found.settings).length
      ? "<li>Settings found: " + Object.keys(found.settings).map(function (k) { return esc(k) + " " + esc(found.settings[k]); }).join(", ") + ".</li>"
      : "<li>No settings in the file; the current plan's settings will be used. Check them after importing.</li>";
    box.innerHTML = "<h3>Import " + esc(fileLabel) + "</h3><ul>" +
      "<li><strong>" + found.quarters.length + " quarters</strong>, " + esc(prettyDate(first.date)) + " to " + esc(prettyDate(last.date)) +
        (found.sheet ? " (sheet “" + esc(found.sheet) + "”)" : "") + ".</li>" +
      (found.used ? "<li>Columns read: " + found.used.map(esc).join(", ") + ".</li>" : "") +
      (found.ignored && found.ignored.length ? "<li>Recalculated, not read: " + found.ignored.slice(0, 12).map(esc).join(", ") + (found.ignored.length > 12 ? " and " + (found.ignored.length - 12) + " more" : "") + ".</li>" : "") +
      settingsNote + "</ul>" +
      (found.problems.length ? "<p class=\"sc-error\">Check these:</p><ul class=\"sc-problems\">" + found.problems.slice(0, 20).map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") +
        (found.problems.length > 20 ? "<li>And " + (found.problems.length - 20) + " more.</li>" : "") + "</ul>" : "") +
      "<fieldset class=\"sc-choice\"><legend>Where should it go?</legend>" +
      "<label><input type=\"radio\" name=\"sc-into\" value=\"new\" checked> A new plan" + (found.name ? " (“" + esc(found.name) + "”)" : "") + "</label>" +
      "<label><input type=\"radio\" name=\"sc-into\" value=\"replace\"> Replace “" + esc(plan().name) + "”</label></fieldset>" +
      "<p class=\"sc-actions\"><button type=\"button\" class=\"pp-btn pp-btn--solid\" id=\"sc-import-go\">Import " + found.quarters.length + " quarters</button> " +
      "<button type=\"button\" class=\"pp-btn\" id=\"sc-import-cancel\">Cancel</button></p>";
    box.hidden = false;
    void s;
    $("sc-import-go").addEventListener("click", commitImport);
    $("sc-import-cancel").addEventListener("click", function () { pending = null; box.hidden = true; });
    $("sc-import-go").focus();
  }

  function importError(msg) {
    var box = $("sc-import-preview");
    box.innerHTML = "<p class=\"sc-error\" role=\"alert\">" + esc(msg) + "</p>";
    box.hidden = false;
  }

  function commitImport() {
    if (!pending) return;
    var into = (document.querySelector("input[name=sc-into]:checked") || {}).value;
    var settings = Object.assign({}, into === "replace" ? plan().settings : DEFAULTS, pending.settings || {});
    if (into === "replace") {
      plan().quarters = pending.quarters;
      plan().settings = settings;
    } else {
      var id = uid();
      store.plans[id] = { name: (pending.name || "Imported plan").slice(0, 60), settings: settings, quarters: pending.quarters };
      store.current = id;
    }
    pending = null;
    $("sc-import-preview").hidden = true;
    save();
    cancelEdit(); fillPlans(); fillSettings(); render();
    $("sc-headline").scrollIntoView({ behavior: "smooth", block: "center" });
  }

  $("sc-import-btn").addEventListener("click", function () { $("sc-import-file").click(); });
  $("sc-import-file").addEventListener("change", function () {
    var file = this.files[0];
    this.value = "";
    if (!file) return;
    if (file.size > 20 * 1024 * 1024) { importError("That file is over 20 MB, which is far more than a plan needs. Is it the right file?"); return; }
    var name = file.name.replace(/\.[^.]+$/, "");
    var ext = (file.name.split(".").pop() || "").toLowerCase();
    var go = function (p) {
      p.then(function (found) { showImport(found, file.name); }).catch(function (e) { importError(e.message || String(e)); });
    };
    if (ext === "json") {
      go(file.text().then(function (t) {
        var d;
        try { d = JSON.parse(t); } catch (e) { throw new Error("This .json file can't be read."); }
        var p = d && d.plan;
        if (!p || !Array.isArray(p.quarters)) throw new Error("This isn't a 9 Sig Calculator backup.");
        var qs = p.quarters.filter(function (q) { return q && toDate(q.date) && q.price > 0 && q.bondPrice > 0; }).map(function (q) {
          var o = { date: toDate(q.date), price: +q.price, bondPrice: +q.bondPrice, command: ["auto", "signal", "hold", "rebalance"].indexOf(q.command) > -1 ? q.command : "auto" };
          if (q.fill > 0) o.fill = +q.fill;
          if (q.bondFill > 0) o.bondFill = +q.bondFill;
          if (q.income > 0) o.income = +q.income;
          return o;
        });
        if (!qs.length) throw new Error("The backup has no quarters.");
        var st = {};
        Object.keys(DEFAULTS).forEach(function (k) { if (p.settings && p.settings[k] !== undefined) st[k] = typeof DEFAULTS[k] === "number" ? +p.settings[k] : String(p.settings[k]).toUpperCase().slice(0, 12); });
        return { quarters: sorted(qs), settings: st, name: p.name, problems: qs.length < p.quarters.length ? [(p.quarters.length - qs.length) + " quarters were incomplete and skipped."] : [] };
      }));
    } else if (ext === "csv" || ext === "txt") {
      go(file.text().then(function (t) {
        var rows = SigXlsx.parseCsv(t), st = {};
        if (rows[0] && /^#\s*settings/i.test(rows[0][0] || "")) {
          var r0 = rows.shift();
          st = readSettings([{ rows: [r0.slice(1)] }]);
          // pairs: name, value, name, value
          for (var i = 1; i < r0.length - 1; i += 2) {
            var one = readSettings([{ rows: [[r0[i], r0[i + 1]]] }]);
            Object.assign(st, one);
          }
        }
        var found = importRows([{ name: name, rows: rows }]);
        found.settings = st;
        found.name = name;
        found.sheet = null;
        return found;
      }));
    } else if (ext === "xlsx" || ext === "xlsm") {
      go(file.arrayBuffer().then(SigXlsx.read).then(function (sheets) {
        var found = importRows(sheets);
        found.settings = readSettings(sheets.filter(function (s) { return s.name !== found.sheet || /setting/i.test(s.name); }).concat(
          sheets.filter(function (s) { return s.name === found.sheet; }).map(function (s) { return { rows: s.rows.slice(0, 12).map(function (r) { return (r || []).slice(0, 4); }) }; })));
        found.name = name;
        return found;
      }));
    } else if (ext === "xls" || ext === "numbers" || ext === "ods") {
      importError("That format can't be read here. Save the file as .xlsx or .csv and import that.");
    } else {
      importError("Import takes .xlsx, .csv or a backup .json file.");
    }
  });

  /* ---------- start ---------- */

  try { $("sc-all-cols").checked = localStorage.getItem(KEY + "-cols") === "1"; } catch (e) { /* default view */ }
  fillPlans();
  fillSettings();
  if (plan().quarters.length) $("sc-settings-box").open = false;
  render();
  nextDate();
})();
