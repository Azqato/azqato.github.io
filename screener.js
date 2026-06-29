  (function () {
    "use strict";

    // The ticker universe comes from the loaded feed (data/screener.json), whose
    // constituents are sourced from data/nasdaq100.json -- a single source of truth,
    // so there is no embedded list to drift out of sync.
    function universe() {
      return Object.keys(data).map(function (t) { return [t, (data[t] && data[t].name) || t]; });
    }

    // The daily feeds are the single source of truth. Pull them straight from
    // GitHub (raw) so they work even when this file is opened locally; fall back
    // to the same-origin copy, then to a localStorage cache if the network is down.
    // The Nasdaq 100 is the default view; the S&P 500 feed is lazy-loaded only
    // when the user clicks "Expand to S&P 500".
    var RAW_BASE = "https://raw.githubusercontent.com/Azqato/stocks/main/data/";
    var UNIVERSES = {
      nasdaq100: {
        label: "Nasdaq 100",
        paths: [RAW_BASE + "screener.json", "data/screener.json"],
        cacheKey: "azq_screener_cache",
        store: null    // { stocks, updated, source } once loaded this session
      },
      sp500: {
        label: "S&P 500",
        paths: [RAW_BASE + "screener_sp500.json", "data/screener_sp500.json"],
        cacheKey: "azq_screener_sp500_cache",
        store: null
      }
    };

    // ---- State ----
    var universeMode = "nasdaq100"; // active universe key
    var data = {};       // ticker -> metrics object (active universe)
    var meta = {};       // { updated: ISOString, source }
    var filter = "all";
    var sortKey = "score";
    var sortDir = -1;    // -1 desc, 1 asc
    var query = "";
    var feedDone = false; // true once the active universe's fetch has finished
    var toggling = false; // guard against double-clicks while a feed loads

    // ---- DOM ----
    var $ = function (id) { return document.getElementById(id); };
    var tbody = $("tbody");

    // ---- Cache (offline fallback only; one key per universe) ----
    function readCache(key) {
      try { var c = JSON.parse(localStorage.getItem(key)); return (c && c.stocks) ? c : null; } catch (e) { return null; }
    }
    function writeCache(key, feed) {
      try { localStorage.setItem(key, JSON.stringify({ updated: feed.updated, source: feed.source, stocks: feed.stocks })); } catch (e) {}
    }
    function loadState() {
      // Seed the active universe from its offline cache so the table isn't blank
      // while the network fetch is in flight.
      var u = UNIVERSES[universeMode];
      var c = readCache(u.cacheKey);
      if (c) {
        u.store = { stocks: c.stocks, updated: c.updated, source: "cache" };
        data = c.stocks;
        meta = { updated: c.updated, source: "cache" };
      }
    }

    // ---- Number helpers ----
    function isNum(n) { return typeof n === "number" && isFinite(n); }
    function fmtPct(n) { return isNum(n) ? n.toFixed(1) + "%" : "—"; }
    function fmtNum(n) { return isNum(n) ? n.toFixed(2) : "—"; }
    function fmtMoney(n) {
      if (!isNum(n)) return "—";
      var a = Math.abs(n);
      if (a >= 1e12) return "$" + (n / 1e12).toFixed(2) + "T";
      if (a >= 1e9)  return "$" + (n / 1e9).toFixed(2) + "B";
      if (a >= 1e6)  return "$" + (n / 1e6).toFixed(1) + "M";
      if (a >= 1e3)  return "$" + (n / 1e3).toFixed(1) + "K";
      return "$" + n.toFixed(0);
    }
    function fmtPrice(n) { return isNum(n) ? "$" + n.toFixed(2) : "—"; }
    function freshestMs(a, b) {
      var ta = a ? Date.parse(a) : 0, tb = b ? Date.parse(b) : 0;
      var m = Math.max(ta, tb);
      return m || null;
    }
    function fmtAge(ms) {
      if (!ms) return "—";
      var diff = Math.max(0, Date.now() - ms);
      var mins = Math.floor(diff / 60000);
      if (mins < 60) return mins + "m";
      var hrs = Math.floor(mins / 60);
      if (hrs < 24) return hrs + "h";
      return Math.floor(hrs / 24) + "d";
    }
    function clsAge(ms) { return (ms && Date.now() - ms > 8 * 86400000) ? "cau" : "muted"; }
    function ageTitle(d) {
      var p = d.priceUpdated ? new Date(d.priceUpdated).toLocaleString() : "—";
      var f = d.fundamentalsUpdated ? new Date(d.fundamentalsUpdated).toLocaleString() : "—";
      return "Price: " + p + "  •  Fundamentals: " + f;
    }

    // ---- Scoring: relative percentile model ----
    // Each of five forward metrics is scored 0-20 by a stock's percentile rank
    // among its loaded peers. Points ramp from 0 (bottom quartile) to 20 (top
    // quartile); the median sits at 10. The five sum to a score out of 100,
    // rescaled across whichever metrics a stock actually has.
    function clamp(x, lo, hi) { return x < lo ? lo : (x > hi ? hi : x); }
    function pointsFromPct(p) { return clamp(40 * (p - 0.25), 0, 20); } // 0-25% -> 0, 75%+ -> 20

    // `scored` metrics feed the Score; the others (TTM growth) are ranked only
    // so their cells can be colored by percentile like everything else.
    var METRICS = [
      { key: "revTTM",   scored: false, higher: true,  get: function (d) { return isNum(d.revTTM) ? d.revTTM : null; } },
      { key: "revFwd",   scored: true,  higher: true,  get: function (d) { return isNum(d.revFwd) ? d.revFwd : null; } },
      { key: "epsTTM",   scored: false, higher: true,  get: function (d) { return isNum(d.epsTTM) ? d.epsTTM : null; } },
      { key: "epsFwd",   scored: true,  higher: true,  get: function (d) { return isNum(d.epsFwd) ? d.epsFwd : null; } },
      { key: "peVsG",    scored: true,  higher: false, get: function (d) {
          if (!isNum(d.peFwd) || !isNum(d.epsFwd)) return null;
          // Unprofitable (P/E <= 0) or shrinking earnings (growth <= 0) rank worst, not best/dropped.
          return (d.peFwd <= 0 || d.epsFwd <= 0) ? Infinity : d.peFwd / d.epsFwd;
        } },
      { key: "pegFwd",   scored: true,  higher: false, get: function (d) {
          if (isNum(d.peFwd) && d.peFwd <= 0) return Infinity; // unprofitable: Yahoo PEG is unreliable, rank worst
          return (isNum(d.pegFwd) && d.pegFwd > 0) ? d.pegFwd : null;
        } },
      { key: "cashDebt", scored: true,  higher: true,  get: function (d) { if (!isNum(d.cash) || !isNum(d.debt)) return null; return d.debt === 0 ? (d.cash > 0 ? Infinity : null) : d.cash / d.debt; } }
    ];

    // Rank every loaded stock on each metric, convert ranks to points, and sum.
    function computeScoreMap() {
      var tickers = Object.keys(data);
      var pts = {};   // ticker -> { metricKey: points }
      var pcts = {};  // ticker -> { metricKey: percentile 0..1 }
      tickers.forEach(function (t) { pts[t] = {}; pcts[t] = {}; });

      METRICS.forEach(function (m) {
        var vals = [];
        tickers.forEach(function (t) {
          var d = data[t];
          if (!d) return;
          var v = m.get(d);
          if (v === null || v === undefined) return;
          vals.push({ t: t, v: v });
        });
        var n = vals.length;
        if (!n) return;
        vals.sort(function (a, b) { return a.v === b.v ? 0 : (a.v < b.v ? -1 : 1); });
        var i = 0;
        while (i < n) {
          var j = i;
          while (j + 1 < n && vals[j + 1].v === vals[i].v) j++; // average-rank ties
          var perc = n > 1 ? ((i + j) / 2) / (n - 1) : 0.5;
          if (!m.higher) perc = 1 - perc; // lower-is-better metrics invert
          var p = pointsFromPct(perc);
          for (var k = i; k <= j; k++) { pts[vals[k].t][m.key] = p; pcts[vals[k].t][m.key] = perc; }
          i = j + 1;
        }
      });

      var out = {};
      tickers.forEach(function (t) {
        var got = [];
        METRICS.forEach(function (m) { if (m.scored && pts[t][m.key] !== undefined) got.push(pts[t][m.key]); });
        if (!got.length) { out[t] = { pct: null, passes: 0, total: 0, parts: pts[t], pctiles: pcts[t] }; return; }
        var sum = got.reduce(function (a, b) { return a + b; }, 0);
        out[t] = {
          pct: Math.round(sum / (got.length * 20) * 100),
          passes: got.filter(function (p) { return p >= 15; }).length,
          total: got.length,
          parts: pts[t],   // percentile points per metric, for cell coloring
          pctiles: pcts[t] // raw percentiles, for the per-stock breakdown popup
        };
      });
      return out;
    }
    // Cell color from a metric's percentile points: top quartile green, bottom red, middle amber.
    function colorFromPts(p) {
      if (p === undefined || p === null) return "muted";
      if (p >= 20) return "pos";
      if (p <= 0) return "neg";
      return "cau";
    }
    function verdictOf(pct) {
      if (pct === null) return "none";
      if (pct >= 80) return "pass";
      if (pct >= 50) return "watch";
      return "fail";
    }

    // ---- Value + format helpers (cell colors are percentile-based; see colorFromPts) ----
    // For unprofitable companies (negative forward P/E), Yahoo's positive PEG is
    // misleading, so display our own forward PEG = P/E / EPS growth (negative).
    function pegDisplay(d) {
      if (isNum(d.peFwd) && d.peFwd <= 0 && isNum(d.epsFwd) && d.epsFwd > 0) return d.peFwd / d.epsFwd;
      return isNum(d.pegFwd) ? d.pegFwd : null;
    }
    function cashDebtRatio(d) {
      if (!isNum(d.cash) || !isNum(d.debt)) return null;
      if (d.debt > 0) return d.cash / d.debt;
      return d.cash > 0 ? Infinity : null; // no debt = effectively unbounded
    }
    function fmtRatio(n) {
      if (n === null || n === undefined || (typeof n === "number" && isNaN(n))) return "—";
      if (!isFinite(n)) return "∞"; // no debt
      return n.toFixed(2) + "x";
    }
    function scoreColor(pct) {
      if (pct === null) return "var(--color-border)";
      if (pct >= 80) return "var(--color-positive)";
      if (pct >= 50) return "var(--color-warning)";
      return "var(--color-negative)";
    }

    // ---- Build a renderable row model ----
    function rows() {
      var sm = computeScoreMap();
      return universe().map(function (s) {
        var t = s[0];
        var d = data[t] || {};
        var sc = sm[t] || { pct: null, passes: 0, total: 0, parts: {} };
        return {
          ticker: t, name: s[1], d: d, parts: sc.parts || {},
          score: sc.pct, passes: sc.passes, total: sc.total,
          verdict: verdictOf(sc.pct),
          revTTM: d.revTTM, revFwd: d.revFwd, epsTTM: d.epsTTM, epsFwd: d.epsFwd,
          peFwd: d.peFwd, pegFwd: pegDisplay(d), cash: d.cash, debt: d.debt,
          cashDebt: cashDebtRatio(d),
          price: d.price, marketCap: d.marketCap,
          updated: freshestMs(d.priceUpdated, d.fundamentalsUpdated)
        };
      });
    }

    var VERDICT_RANK = { pass: 3, watch: 2, fail: 1, none: 0 };

    function sortRows(rs) {
      var k = sortKey, dir = sortDir;
      return rs.slice().sort(function (a, b) {
        var av, bv;
        if (k === "ticker") { return a.ticker.localeCompare(b.ticker) * dir; }
        if (k === "verdict") { av = VERDICT_RANK[a.verdict]; bv = VERDICT_RANK[b.verdict]; }
        else if (k === "factors") { av = a.total ? a.passes / a.total : -1; bv = b.total ? b.passes / b.total : -1; }
        else { av = a[k]; bv = b[k]; }
        // For valuation columns a negative P/E or PEG is "worst" (unprofitable),
        // so sort it like a very high value rather than a cheap low one.
        if (k === "peFwd" || k === "pegFwd") {
          if (typeof av === "number" && av <= 0) av = Infinity;
          if (typeof bv === "number" && bv <= 0) bv = Infinity;
        }
        // "present" = a real number, including Infinity (e.g. cash/debt with no debt)
        var an = typeof av === "number" && !isNaN(av);
        var bn = typeof bv === "number" && !isNaN(bv);
        if (!an && !bn) return 0;
        if (!an) return 1;   // missing always sinks to bottom
        if (!bn) return -1;
        if (av === bv) return 0;
        return (av - bv) * dir;
      });
    }

    // ---- Render ----
    function render() {
      var rs = rows();

      // verdict counts
      var counts = { all: rs.length, pass: 0, watch: 0, fail: 0 };
      rs.forEach(function (r) { if (counts[r.verdict] !== undefined) counts[r.verdict]++; });
      $("cnt-all").textContent = counts.all;
      $("cnt-pass").textContent = counts.pass;
      $("cnt-watch").textContent = counts.watch;
      $("cnt-fail").textContent = counts.fail;

      // filter
      var view = rs.filter(function (r) {
        if (filter !== "all" && r.verdict !== filter) return false;
        if (query) {
          var q = query.toLowerCase();
          if (r.ticker.toLowerCase().indexOf(q) === -1 && r.name.toLowerCase().indexOf(q) === -1) return false;
        }
        return true;
      });
      view = sortRows(view);

      tbody.innerHTML = view.map(rowHtml).join("");

      // summary + placeholder
      var loaded = Object.keys(data).length;
      $("placeholder").style.display = (feedDone && loaded === 0) ? "flex" : "none";
      var scored = rs.filter(function (r) { return r.score !== null; }).length;
      if (loaded === 0) {
        $("summary").innerHTML = feedDone ? "No data" : "Loading the " + UNIVERSES[universeMode].label + "&hellip;";
      } else {
        $("summary").innerHTML = "<b>" + counts.pass + "</b> pass &middot; <b>" + counts.watch +
          "</b> watch &middot; <b>" + counts.fail + "</b> fail &middot; " + scored + "/" + loaded + " scored";
      }
      $("asOf").textContent = meta.updated ? "as of " + new Date(meta.updated).toLocaleString() : "no data loaded";

      applyColumnVisibility();
      updateSortIndicators();
      checkStale();
    }

    // ---- Daily feed (data/screener.json, refreshed by the GitHub Action) ----
    function isStale(ts) {
      if (!ts) return true;
      return (Date.now() - new Date(ts).getTime()) > 24 * 3600 * 1000;
    }

    function checkStale() {
      var has = Object.keys(data).length > 0;
      var stale = has && isStale(meta.updated);
      $("staleBanner").classList.toggle("on", stale);
      if (stale) {
        $("staleText").innerHTML = meta.updated
          ? "This data is from " + new Date(meta.updated).toLocaleString() + " (more than 24 hours old). The daily refresh may not have run yet."
          : "This data has no timestamp and may be out of date.";
      }
    }

    // Fetch a universe's feed from GitHub (works locally too), caching it for
    // offline use. Returns the in-memory store {stocks, updated, source} or null
    // if every source failed. Does not change the active view by itself.
    async function fetchUniverse(key) {
      var u = UNIVERSES[key];
      for (var i = 0; i < u.paths.length; i++) {
        try {
          var res = await fetch(u.paths[i], { cache: "no-store" });
          if (!res.ok) continue;
          var feed = await res.json();
          if (feed && feed.stocks && Object.keys(feed.stocks).length) {
            u.store = { stocks: feed.stocks, updated: feed.updated, source: feed.source || "feed" };
            writeCache(u.cacheKey, feed);
            return u.store;
          }
        } catch (e) { /* try the next source */ }
      }
      return null;
    }

    // Point data/meta at a universe's dataset, swap the on-screen labels, repaint.
    function activate(key, store) {
      universeMode = key;
      data = {};
      Object.keys(store.stocks).forEach(function (k) { data[k] = store.stocks[k]; });
      meta = { updated: store.updated, source: store.source };
      setUniverseLabel(UNIVERSES[key].label);
      updateToggleButton();
      render();
    }

    // Swap every "Nasdaq 100"/"S&P 500" label (and the page title) to match the view.
    function setUniverseLabel(label) {
      document.querySelectorAll(".universe-name").forEach(function (el) { el.textContent = label; });
      document.title = label + " Screener";
    }

    function updateToggleButton() {
      $("universeToggle").textContent =
        universeMode === "nasdaq100" ? "Expand to S&P 500" : "Back to Nasdaq 100";
    }

    // Initial page load: fetch the default Nasdaq 100 feed.
    async function loadInitial() {
      var store = await fetchUniverse("nasdaq100");
      feedDone = true;
      if (store) activate("nasdaq100", store);
      else render(); // network failed: keep whatever the startup cache gave us
    }

    // Button: switch between the Nasdaq 100 and S&P 500 universes, lazy-loading
    // the S&P 500 feed on first use.
    async function toggleUniverse() {
      if (toggling) return;
      var target = universeMode === "nasdaq100" ? "sp500" : "nasdaq100";
      var u = UNIVERSES[target];

      if (u.store) { activate(target, u.store); return; } // already in memory -> instant

      toggling = true;
      var btn = $("universeToggle");
      var prevLabel = btn.textContent;
      btn.disabled = true;
      btn.textContent = "Loading " + u.label + "…";

      var store = await fetchUniverse(target);
      toggling = false;
      btn.disabled = false;

      if (store) {
        activate(target, store);
      } else {
        // Feed not generated yet (or offline): stay on the current view, explain why.
        btn.textContent = prevLabel;
        $("summary").innerHTML = u.label + " data isn’t available yet — it’s generated by " +
          "the daily update. Check back after the next refresh.";
      }
    }

    function rowHtml(r) {
      var d = r.d;
      var verdictLabel = { pass: "✓ PASS", watch: "WATCH", fail: "✕ FAIL", none: "NO DATA" }[r.verdict];
      var scoreCell;
      if (r.score === null) {
        scoreCell = '<span class="muted">—</span>';
      } else {
        scoreCell = '<span class="score-bar-wrap"><span class="score-val">' + r.score + '</span>' +
          '<span class="score-track"><span class="score-fill" style="width:' + r.score + '%;background:' +
          scoreColor(r.score) + '"></span></span></span>';
      }
      var factorsCell = r.total ? '<span class="factors">' + r.passes + "/" + r.total + "</span>" : '<span class="muted">—</span>';

      return '<tr data-ticker="' + r.ticker + '">' +
        '<td class="col-ticker"><span class="tkr">' + r.ticker + '</span><span class="tkr-name">' + r.name + '</span></td>' +
        '<td class="left group-start"><span class="verdict v-' + r.verdict + '">' + verdictLabel + '</span></td>' +
        '<td>' + scoreCell + '</td>' +
        '<td>' + factorsCell + '</td>' +
        '<td class="grp-growth group-start ' + colorFromPts(r.parts.revTTM) + '">' + fmtPct(r.revTTM) + '</td>' +
        '<td class="grp-growth ' + colorFromPts(r.parts.revFwd) + '">' + fmtPct(r.revFwd) + '</td>' +
        '<td class="grp-growth ' + colorFromPts(r.parts.epsTTM) + '">' + fmtPct(r.epsTTM) + '</td>' +
        '<td class="grp-growth ' + colorFromPts(r.parts.epsFwd) + '">' + fmtPct(r.epsFwd) + '</td>' +
        '<td class="grp-valuation group-start ' + colorFromPts(r.parts.peVsG) + '">' + fmtNum(r.peFwd) + '</td>' +
        '<td class="grp-valuation ' + colorFromPts(r.parts.pegFwd) + '">' + fmtNum(r.pegFwd) + '</td>' +
        '<td class="grp-balance group-start ' + colorFromPts(r.parts.cashDebt) + '">' + fmtMoney(r.cash) + '</td>' +
        '<td class="grp-balance">' + fmtMoney(r.debt) + '</td>' +
        '<td class="grp-balance ' + colorFromPts(r.parts.cashDebt) + '">' + fmtRatio(r.cashDebt) + '</td>' +
        '<td class="grp-snapshot group-start">' + fmtPrice(r.price) + '</td>' +
        '<td class="grp-snapshot">' + fmtMoney(r.marketCap) + '</td>' +
        '<td class="grp-snapshot ' + clsAge(r.updated) + '" title="' + ageTitle(d) + '">' + fmtAge(r.updated) + '</td>' +
        '</tr>';
    }

    function updateSortIndicators() {
      var ths = document.querySelectorAll("tr.head-row th");
      ths.forEach(function (th) {
        var k = th.getAttribute("data-sort");
        var existing = th.querySelector(".arrow");
        if (existing) existing.remove();
        if (k === sortKey) {
          var span = document.createElement("span");
          span.className = "arrow";
          span.textContent = sortDir === -1 ? "▼" : "▲";
          th.appendChild(span);
        }
      });
    }

    // ---- Column visibility ----
    function applyColumnVisibility() {
      ["growth", "valuation", "balance", "snapshot"].forEach(function (g) {
        var cb = document.querySelector('#colsMenu input[data-group="' + g + '"]');
        var show = cb ? cb.checked : true;
        document.querySelectorAll(".grp-" + g).forEach(function (el) {
          el.classList.toggle("col-hidden", !show);
        });
      });
    }

    // ---- Per-stock breakdown popup ----
    var POPUP_METRICS = [
      { key: "revTTM",   label: "Revenue Growth TTM", scored: false, fmt: function (d) { return fmtPct(d.revTTM); } },
      { key: "revFwd",   label: "Revenue Growth FWD", scored: true,  fmt: function (d) { return fmtPct(d.revFwd); } },
      { key: "epsTTM",   label: "EPS Growth TTM",     scored: false, fmt: function (d) { return fmtPct(d.epsTTM); } },
      { key: "epsFwd",   label: "EPS Growth FWD",     scored: true,  fmt: function (d) { return fmtPct(d.epsFwd); } },
      { key: "peVsG",    label: "P/E vs Growth",      scored: true,  fmt: function (d) { return fmtNum(d.peFwd); } },
      { key: "pegFwd",   label: "PEG FWD",            scored: true,  fmt: function (d) { return fmtNum(pegDisplay(d)); } },
      { key: "cashDebt", label: "Cash vs Debt",       scored: true,  fmt: function (d) { return fmtRatio(cashDebtRatio(d)); } }
    ];

    function ordinal(p) {
      if (p === undefined || p === null) return "—";
      var n = Math.round(p * 100);
      var s = (n % 10 === 1 && n % 100 !== 11) ? "st" : (n % 10 === 2 && n % 100 !== 12) ? "nd" : (n % 10 === 3 && n % 100 !== 13) ? "rd" : "th";
      return n + s;
    }

    function openStock(ticker) {
      var d = data[ticker];
      if (!d || !Object.keys(d).length) return;
      var nm = (data[ticker] && data[ticker].name) || ticker;
      var sc = computeScoreMap()[ticker] || { pct: null, parts: {}, pctiles: {}, total: 0 };
      var verdict = verdictOf(sc.pct);
      var vlabel = { pass: "PASS", watch: "WATCH", fail: "FAIL", none: "NO DATA" }[verdict];

      $("stockTitle").textContent = ticker;
      $("stockSub").innerHTML = nm + ' &middot; <span class="verdict v-' + verdict + '">' + vlabel +
        '</span> &middot; Score ' + (sc.pct === null ? "—" : sc.pct) + "/100";

      $("stockRows").innerHTML = POPUP_METRICS.filter(function (m) { return m.scored; }).map(function (m) {
        var pp = sc.parts[m.key];
        var color = colorFromPts(pp);
        var ptsTxt = (pp === undefined || pp === null) ? "—" : pp.toFixed(1);
        return "<tr>" +
          "<td>" + m.label + "</td>" +
          '<td class="num ' + color + '">' + m.fmt(d) + "</td>" +
          '<td class="num">' + ordinal(sc.pctiles[m.key]) + "</td>" +
          '<td class="num ' + color + '">' + ptsTxt + "</td>" +
          "</tr>";
      }).join("");

      $("stockNote").innerHTML = "Scored on <b>" + sc.total + "</b> of the 5 forward metrics. " +
        "Each metric's points come from its percentile rank vs the Nasdaq 100 (green = top quartile, red = bottom). " +
        'Open <b>Methodology</b> for the full method.';

      $("stockModal").hidden = false;
    }
    function closeStock() { $("stockModal").hidden = true; }

    // ---- Modals ----
    function openMethodology() { $("methodologyModal").hidden = false; }
    function closeMethodology() { $("methodologyModal").hidden = true; }

    // ---- Events ----
    function bind() {
      // verdict filter chips
      document.querySelectorAll(".chip").forEach(function (c) {
        c.addEventListener("click", function () {
          document.querySelectorAll(".chip").forEach(function (x) { x.classList.remove("active"); });
          c.classList.add("active");
          filter = c.getAttribute("data-filter");
          render();
        });
      });

      // sort
      document.querySelectorAll("tr.head-row th").forEach(function (th) {
        th.addEventListener("click", function () {
          var k = th.getAttribute("data-sort");
          if (!k) return;
          if (sortKey === k) { sortDir = -sortDir; }
          else { sortKey = k; sortDir = (k === "ticker") ? 1 : -1; }
          render();
        });
      });

      // search
      $("search").addEventListener("input", function () { query = this.value.trim(); render(); });

      // row click -> per-stock breakdown
      tbody.addEventListener("click", function (e) {
        var tr = e.target.closest("tr");
        if (tr && tr.dataset.ticker) openStock(tr.dataset.ticker);
      });

      // columns menu
      $("colsBtn").addEventListener("click", function (e) {
        e.stopPropagation();
        $("colsMenu").hidden = !$("colsMenu").hidden;
      });
      document.addEventListener("click", function () { $("colsMenu").hidden = true; });
      $("colsMenu").addEventListener("click", function (e) { e.stopPropagation(); });
      document.querySelectorAll("#colsMenu input").forEach(function (cb) {
        cb.addEventListener("change", applyColumnVisibility);
      });

      // universe toggle (Nasdaq 100 <-> S&P 500)
      $("universeToggle").addEventListener("click", toggleUniverse);

      // modals
      $("methodologyBtn").addEventListener("click", openMethodology);
      $("methodologyClose").addEventListener("click", closeMethodology);
      $("methodologyModal").addEventListener("click", function (e) { if (e.target === $("methodologyModal")) closeMethodology(); });
      $("stockClose").addEventListener("click", closeStock);
      $("stockModal").addEventListener("click", function (e) { if (e.target === $("stockModal")) closeStock(); });

      document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeMethodology(); closeStock(); } });
    }

    // ---- Init ----
    loadState();
    bind();
    render();
    loadInitial();
  })();
