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
    // The Nasdaq 100 is the default view; the other universes are lazy-loaded on
    // first use. Growth, Value, and Dividend share one combined feed file
    // (screener_gvd.json) keyed by `feedKey`, so one fetch fills all three.
    var RAW_BASE = "https://raw.githubusercontent.com/Azqato/stocks/main/data/";
    var GVD_PATHS = [RAW_BASE + "screener_gvd.json", "data/screener_gvd.json"];
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
      },
      growth: {
        label: "Growth 100",           // top 100 VUG holdings
        paths: GVD_PATHS, feedKey: "growth",
        cacheKey: "azq_screener_growth_cache",
        store: null
      },
      value: {
        label: "Value 100",            // top 100 VTV holdings
        paths: GVD_PATHS, feedKey: "value",
        cacheKey: "azq_screener_value_cache",
        store: null
      },
      dividend: {
        label: "Dividend 100",         // top 100 VIG holdings
        paths: GVD_PATHS, feedKey: "dividend",
        cacheKey: "azq_screener_dividend_cache",
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
    function fmtChange(n) { return isNum(n) ? (n > 0 ? "+" : "") + n.toFixed(2) + "%" : "—"; }
    function clsChange(n) {
      if (!isNum(n) || n === 0) return "muted";
      return n > 0 ? "pos" : "neg";
    }
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

    // ---- Scoring: relative percentile model v2 (v3.30.0-v3.31.0, three pillars) ----
    // Six metrics in three pillars: Growth 60 (Rev TTM 10, Rev FWD 20, EPS TTM
    // 10, EPS FWD 20 -- forward growth counts double, owner weights v3.31.0),
    // Valuation 20 (PEG FWD), Balance sheet 20 (cash vs debt). Each metric's
    // points ramp with the stock's percentile rank among its loaded peers,
    // clamped at the top/bottom 22%: only the top 22% of a metric earns full
    // marks. The clamp is calibrated on live feeds so a perfect 100 stays
    // rare: roughly 1 stock in the Nasdaq 100 and 5 in the S&P 500, with more
    // only when rounded scores tie. Missing data scores a hard ZERO for that
    // metric -- the denominator stays 100, so an incomplete stock can never
    // outscore a complete one (its missing cell renders dark red).
    function clamp(x, lo, hi) { return x < lo ? lo : (x > hi ? hi : x); }
    var CLAMP_Q = 0.22; // full marks at the (1-q)th percentile, zero below the qth
    function pointsFromPct(p) { return clamp(20 * (p - CLAMP_Q) / (1 - 2 * CLAMP_Q), 0, 20); }

    // `weight` > 0 metrics feed the Score; weight-0 metrics (the P/E-vs-growth
    // context ratio) are ranked only so their cells can be colored by percentile.
    var METRICS = [
      { key: "revTTM",   weight: 10, higher: true,  get: function (d) { return isNum(d.revTTM) ? d.revTTM : null; } },
      { key: "revFwd",   weight: 20, higher: true,  get: function (d) { return isNum(d.revFwd) ? d.revFwd : null; } },
      { key: "epsTTM",   weight: 10, higher: true,  get: function (d) { return isNum(d.epsTTM) ? d.epsTTM : null; } },
      { key: "epsFwd",   weight: 20, higher: true,  get: function (d) { return isNum(d.epsFwd) ? d.epsFwd : null; } },
      { key: "peVsG",    weight: 0,  higher: false, get: function (d) {
          if (!isNum(d.peFwd) || !isNum(d.epsFwd)) return null;
          // Unprofitable (P/E <= 0) or shrinking earnings (growth <= 0) rank worst, not best/dropped.
          return (d.peFwd <= 0 || d.epsFwd <= 0) ? Infinity : d.peFwd / d.epsFwd;
        } },
      { key: "pegFwd",   weight: 20, higher: false, get: function (d) {
          if (isNum(d.peFwd) && d.peFwd <= 0) return Infinity; // unprofitable: Yahoo PEG is unreliable, rank worst
          return (isNum(d.pegFwd) && d.pegFwd > 0) ? d.pegFwd : null;
        } },
      { key: "cashDebt", weight: 20, higher: true,  get: function (d) { if (!isNum(d.cash) || !isNum(d.debt)) return null; return d.debt === 0 ? (d.cash > 0 ? Infinity : null) : d.cash / d.debt; } }
    ];
    var TOTAL_WEIGHT = METRICS.reduce(function (s, m) { return s + m.weight; }, 0); // 100
    var SCORED_COUNT = METRICS.filter(function (m) { return m.weight > 0; }).length; // 6

    // Rank every loaded stock on each metric, convert ranks to points, and sum.
    // `parts` keeps every metric's points on a 0-20 scale (for cell colors and
    // the popup); the total applies each metric's weight.
    function computeScoreMap() {
      var tickers = Object.keys(data);
      var pts = {};   // ticker -> { metricKey: points 0-20 }
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
        var sum = 0, have = 0, passes = 0;
        METRICS.forEach(function (m) {
          if (!m.weight) return;
          var p = pts[t][m.key];
          if (p === undefined) return; // missing = hard zero (adds nothing, denominator stays 100)
          have++;
          sum += p * (m.weight / 20);
          if (p >= 15) passes++; // upper part of the pack on that metric
        });
        if (!have) { out[t] = { pct: null, passes: 0, total: 0, parts: pts[t], pctiles: pcts[t] }; return; }
        out[t] = {
          pct: Math.round(sum / TOTAL_WEIGHT * 100),
          passes: passes,
          total: SCORED_COUNT, // fixed /6: a missing metric is a miss, not a pass
          parts: pts[t],   // percentile points per metric (0-20 scale), for cell coloring
          pctiles: pcts[t] // raw percentiles, for the per-stock breakdown popup
        };
      });
      return out;
    }
    // Cell color from a metric's percentile points: top of the pack green,
    // bottom red, middle amber.
    function colorFromPts(p) {
      if (p === undefined || p === null) return "muted";
      if (p >= 20) return "pos";
      if (p <= 0) return "neg";
      return "cau";
    }
    // Scored metrics: missing data is a hard zero, so a "—" renders dark red.
    function colorScored(p) {
      if (p === undefined || p === null) return "neg";
      return colorFromPts(p);
    }
    // Tier list by rank (v3.29.0): S = top 10% of the scored stocks in the
    // loaded list, A = next 10%, B = 20-50%, C = 50-75%, F = bottom 25%.
    // A ranking, not a buy/sell rating. Boundary ties round UP: every stock
    // whose (rounded) score matches the last stock inside a band joins that
    // band, so a tier only stretches past its quota on identical scores.
    // On top of the bands, a perfect 100/100 earns S+ (v3.30.0) -- those
    // stocks come out of the S band's headcount, they don't push it down.
    var TIER_CUTS = [["s", 0.10], ["a", 0.20], ["b", 0.50], ["c", 0.75]]; // f = the rest
    function computeTierMap(sm) {
      var order = Object.keys(sm)
        .filter(function (t) { return sm[t].pct !== null; })
        .sort(function (a, b) { return sm[b].pct - sm[a].pct; });
      var n = order.length;
      var tiers = {};
      if (!n) return tiers;
      var cuts = TIER_CUTS.map(function (c) { return Math.max(1, Math.round(c[1] * n)); });
      for (var k = 0; k < cuts.length; k++) {
        var j = Math.min(cuts[k], n) - 1;              // last stock inside the band
        var boundary = sm[order[j]].pct;
        while (j + 1 < n && sm[order[j + 1]].pct === boundary) j++; // ties round up
        cuts[k] = j + 1;
        if (k > 0 && cuts[k] < cuts[k - 1]) cuts[k] = cuts[k - 1];
      }
      var ci = 0;
      for (var i = 0; i < n; i++) {
        while (ci < cuts.length && i >= cuts[ci]) ci++;
        tiers[order[i]] = sm[order[i]].pct >= 100 ? "sp"
          : (ci < TIER_CUTS.length ? TIER_CUTS[ci][0] : "f");
      }
      return tiers;
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
    // The score bar takes its color from the stock's tier (tiers are ranks,
    // so the same score can be a different color in a different universe).
    var TIER_COLOR = {
      sp: "var(--color-tier-splus)",
      s: "var(--color-tier-s)", a: "var(--color-tier-a)", b: "var(--color-tier-b)",
      c: "var(--color-tier-c)", f: "var(--color-negative)", none: "var(--color-border)"
    };

    // ---- Build a renderable row model ----
    function rows() {
      var sm = computeScoreMap();
      var tiers = computeTierMap(sm);
      return universe().map(function (s) {
        var t = s[0];
        var d = data[t] || {};
        var sc = sm[t] || { pct: null, passes: 0, total: 0, parts: {} };
        return {
          ticker: t, name: s[1], d: d, parts: sc.parts || {},
          score: sc.pct, passes: sc.passes, total: sc.total,
          tier: sc.pct === null ? "none" : tiers[t],
          revTTM: d.revTTM, revFwd: d.revFwd, epsTTM: d.epsTTM, epsFwd: d.epsFwd,
          peFwd: d.peFwd, pegFwd: pegDisplay(d), cash: d.cash, debt: d.debt,
          cashDebt: cashDebtRatio(d),
          price: d.price, marketCap: d.marketCap,
          changePct: isNum(d.changePct) ? d.changePct : null,
          updated: freshestMs(d.priceUpdated, d.fundamentalsUpdated)
        };
      });
    }

    var TIER_RANK = { sp: 6, s: 5, a: 4, b: 3, c: 2, f: 1, none: 0 };

    function sortRows(rs) {
      var k = sortKey, dir = sortDir;
      return rs.slice().sort(function (a, b) {
        var av, bv;
        if (k === "ticker") { return a.ticker.localeCompare(b.ticker) * dir; }
        if (k === "tier") { av = TIER_RANK[a.tier]; bv = TIER_RANK[b.tier]; }
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

      // tier counts
      var counts = { all: rs.length, sp: 0, s: 0, a: 0, b: 0, c: 0, f: 0 };
      rs.forEach(function (r) { if (counts[r.tier] !== undefined) counts[r.tier]++; });
      $("cnt-all").textContent = counts.all;
      ["sp", "s", "a", "b", "c", "f"].forEach(function (t) { $("cnt-" + t).textContent = counts[t]; });

      // filter
      var view = rs.filter(function (r) {
        if (filter !== "all" && r.tier !== filter) return false;
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
        $("summary").innerHTML = (counts.sp ? "<b>" + counts.sp + "</b> S+ &middot; " : "") +
          "<b>" + counts.s + "</b> S &middot; <b>" + counts.a + "</b> A &middot; <b>" +
          counts.b + "</b> B &middot; <b>" + counts.c + "</b> C &middot; <b>" + counts.f + "</b> F &middot; " +
          scored + "/" + loaded + " scored";
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
    // Universes with a `feedKey` live inside the combined GVD file: the wanted
    // universe is extracted, and the siblings that came along in the same file
    // are stored and cached too, so switching between them needs no new fetch.
    async function fetchUniverse(key) {
      var u = UNIVERSES[key];
      for (var i = 0; i < u.paths.length; i++) {
        try {
          var res = await fetch(u.paths[i], { cache: "no-store" });
          if (!res.ok) continue;
          var body = await res.json();
          var feed = u.feedKey ? (body && body.universes && body.universes[u.feedKey]) : body;
          if (feed && feed.stocks && Object.keys(feed.stocks).length) {
            u.store = { stocks: feed.stocks, updated: feed.updated, source: feed.source || "feed" };
            writeCache(u.cacheKey, feed);
            if (u.feedKey) {
              Object.keys(UNIVERSES).forEach(function (k) {
                var o = UNIVERSES[k];
                if (k === key || !o.feedKey) return;
                var sib = body.universes[o.feedKey];
                if (sib && sib.stocks && Object.keys(sib.stocks).length) {
                  o.store = { stocks: sib.stocks, updated: sib.updated, source: sib.source || "feed" };
                  writeCache(o.cacheKey, sib);
                }
              });
            }
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
      updateUniverseButtons();
      render();
    }

    // Swap every universe label (and the page title) to match the view.
    function setUniverseLabel(label) {
      document.querySelectorAll(".universe-name").forEach(function (el) { el.textContent = label; });
      document.title = label + " Screener";
    }

    // Light up the active universe's button.
    function updateUniverseButtons() {
      document.querySelectorAll("#universeGroup .u-btn").forEach(function (b) {
        b.classList.toggle("active", b.getAttribute("data-universe") === universeMode);
      });
    }

    function setUniverseButtonsDisabled(on) {
      document.querySelectorAll("#universeGroup .u-btn").forEach(function (b) { b.disabled = on; });
    }

    // Initial page load: fetch the default Nasdaq 100 feed.
    async function loadInitial() {
      var store = await fetchUniverse("nasdaq100");
      feedDone = true;
      if (store) activate("nasdaq100", store);
      else render(); // network failed: keep whatever the startup cache gave us
    }

    // Buttons: switch to a universe, lazy-loading its feed on first use.
    async function selectUniverse(target) {
      if (toggling || target === universeMode || !UNIVERSES[target]) return;
      var u = UNIVERSES[target];

      if (u.store) { activate(target, u.store); return; } // already in memory -> instant

      toggling = true;
      setUniverseButtonsDisabled(true);
      $("summary").innerHTML = "Loading the " + u.label + "&hellip;";

      var store = await fetchUniverse(target);
      toggling = false;
      setUniverseButtonsDisabled(false);

      if (store) {
        activate(target, store);
      } else {
        // Feed not generated yet (or offline): stay on the current view, explain why.
        render();
        $("summary").innerHTML = u.label + " data isn’t available yet — it’s generated by " +
          "the daily update. Check back after the next refresh.";
      }
    }

    var TIER_LABEL = { sp: "S+", s: "S", a: "A", b: "B", c: "C", f: "F", none: "NO DATA" };

    function rowHtml(r) {
      var d = r.d;
      var tierLabel = TIER_LABEL[r.tier];
      var scoreCell;
      if (r.score === null) {
        scoreCell = '<span class="muted">—</span>';
      } else {
        scoreCell = '<span class="score-bar-wrap"><span class="score-val">' + r.score + '</span>' +
          '<span class="score-track"><span class="score-fill" style="width:' + r.score + '%;background:' +
          TIER_COLOR[r.tier] + '"></span></span></span>';
      }
      var factorsCell = r.total ? '<span class="factors">' + r.passes + "/" + r.total + "</span>" : '<span class="muted">—</span>';

      return '<tr data-ticker="' + r.ticker + '">' +
        '<td class="col-ticker"><span class="tkr">' + r.ticker + '</span><span class="tkr-name">' + r.name + '</span></td>' +
        '<td class="left group-start"><span class="verdict v-' + r.tier + '">' + tierLabel + '</span></td>' +
        '<td>' + scoreCell + '</td>' +
        '<td>' + factorsCell + '</td>' +
        '<td class="grp-snapshot group-start">' + fmtMoney(r.marketCap) + '</td>' +
        '<td class="grp-snapshot">' + fmtPrice(r.price) + '</td>' +
        '<td class="grp-snapshot ' + clsChange(r.changePct) + '">' + fmtChange(r.changePct) + '</td>' +
        '<td class="grp-growth group-start ' + colorScored(r.parts.revTTM) + '">' + fmtPct(r.revTTM) + '</td>' +
        '<td class="grp-growth ' + colorScored(r.parts.revFwd) + '">' + fmtPct(r.revFwd) + '</td>' +
        '<td class="grp-growth ' + colorScored(r.parts.epsTTM) + '">' + fmtPct(r.epsTTM) + '</td>' +
        '<td class="grp-growth ' + colorScored(r.parts.epsFwd) + '">' + fmtPct(r.epsFwd) + '</td>' +
        '<td class="grp-valuation group-start ' + colorFromPts(r.parts.peVsG) + '">' + fmtNum(r.peFwd) + '</td>' +
        '<td class="grp-valuation ' + colorScored(r.parts.pegFwd) + '">' + fmtNum(r.pegFwd) + '</td>' +
        '<td class="grp-balance group-start ' + colorScored(r.parts.cashDebt) + '">' + fmtMoney(r.cash) + '</td>' +
        '<td class="grp-balance">' + fmtMoney(r.debt) + '</td>' +
        '<td class="grp-balance ' + colorScored(r.parts.cashDebt) + '">' + fmtRatio(r.cashDebt) + '</td>' +
        '<td class="grp-snapshot group-start ' + clsAge(r.updated) + '" title="' + ageTitle(d) + '">' + fmtAge(r.updated) + '</td>' +
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
      { key: "revTTM",      label: "Revenue Growth TTM", weight: 10, fmt: function (d) { return fmtPct(d.revTTM); } },
      { key: "revFwd",      label: "Revenue Growth FWD", weight: 20, fmt: function (d) { return fmtPct(d.revFwd); } },
      { key: "epsTTM",      label: "EPS Growth TTM",     weight: 10, fmt: function (d) { return fmtPct(d.epsTTM); } },
      { key: "epsFwd",      label: "EPS Growth FWD",     weight: 20, fmt: function (d) { return fmtPct(d.epsFwd); } },
      { key: "pegFwd",      label: "PEG FWD",            weight: 20, fmt: function (d) { return fmtNum(pegDisplay(d)); } },
      { key: "cashDebt",    label: "Cash vs Debt",       weight: 20, fmt: function (d) { return fmtRatio(cashDebtRatio(d)); } }
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
      var sm = computeScoreMap();
      var sc = sm[ticker] || { pct: null, parts: {}, pctiles: {}, total: 0 };
      var tier = sc.pct === null ? "none" : computeTierMap(sm)[ticker];
      var tlabel = tier === "none" ? "NO DATA" : "Tier " + TIER_LABEL[tier];

      $("stockTitle").textContent = ticker;
      $("stockSub").innerHTML = nm + ' &middot; <span class="verdict v-' + tier + '">' + tlabel +
        '</span> &middot; Score ' + (sc.pct === null ? "—" : sc.pct) + "/100";

      $("stockRows").innerHTML = POPUP_METRICS.map(function (m) {
        var pp = sc.parts[m.key];
        var color = colorScored(pp);
        var ptsTxt = (pp === undefined || pp === null)
          ? "0.0/" + m.weight                              // missing data = hard zero
          : (pp / 20 * m.weight).toFixed(1) + "/" + m.weight;
        return "<tr>" +
          "<td>" + m.label + "</td>" +
          '<td class="num ' + color + '">' + m.fmt(d) + "</td>" +
          '<td class="num">' + ordinal(sc.pctiles[m.key]) + "</td>" +
          '<td class="num ' + color + '">' + ptsTxt + "</td>" +
          "</tr>";
      }).join("");

      $("stockNote").innerHTML = "Each metric's points come from its percentile rank vs the " +
        UNIVERSES[universeMode].label + " (green = top of the pack, red = bottom), weighted by pillar: " +
        "Growth 60, Valuation 20, Balance sheet 20. A missing metric (—) scores zero. " +
        "Open <b>Methodology</b> for the full method.";

      $("stockModal").hidden = false;
    }
    function closeStock() { $("stockModal").hidden = true; }

    // ---- Modals ----
    function openMethodology() { $("methodologyModal").hidden = false; }
    function closeMethodology() { $("methodologyModal").hidden = true; }

    // ---- Events ----
    function bind() {
      // tier filter chips
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

      // universe buttons (Nasdaq 100 / S&P 500 / Growth / Value / Dividend)
      document.querySelectorAll("#universeGroup .u-btn").forEach(function (b) {
        b.addEventListener("click", function () { selectUniverse(b.getAttribute("data-universe")); });
      });

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
