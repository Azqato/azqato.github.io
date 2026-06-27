// fetch-screener-data.mjs
//
// Builds data/screener.json for the Nasdaq 100 screener (screenapp.html).
// Runs in GitHub Actions on a daily cron. No npm dependencies — uses Node 20+
// global fetch and the Financial Modeling Prep "stable" API.
//
// Strategy (keeps a single daily run under the FMP free tier's 250 req/day):
//   - PRICE phase: refresh price + market cap for ALL symbols (1 req each, ~100).
//     Forward P/E and PEG are recomputed from the cached forward EPS so they
//     track the latest price every day.
//   - FUNDAMENTALS phase: refresh a rotating slice of the symbols whose
//     fundamentals are stalest (default 15/run, 3 reqs each, ~45). Over ~7 runs
//     every symbol's fundamentals refresh, i.e. a weekly cadence.
//
// Env:
//   FMP_API_KEY  (required)  - your FMP key (a GitHub Actions secret)
//   FUND_SLICE   (optional)  - symbols to refresh fundamentals for per run (default 15)
//   REQ_BUDGET   (optional)  - hard cap on API requests this run (default 240)

import fs from "node:fs/promises";

const KEY = process.env.FMP_API_KEY;
if (!KEY) { console.error("ERROR: FMP_API_KEY is not set."); process.exit(1); }

const BASE = "https://financialmodelingprep.com/stable";
const FUND_SLICE = parseInt(process.env.FUND_SLICE || "15", 10);
const REQ_BUDGET = parseInt(process.env.REQ_BUDGET || "240", 10);
const LIST_PATH = "data/nasdaq100.json";
const OUT_PATH = "data/screener.json";

let reqs = 0;

function classify(body, status) {
  let msg = "";
  if (typeof body === "string") msg = body;
  else if (body && typeof body === "object" && !Array.isArray(body)) msg = body["Error Message"] || body.message || "";
  else return null; // array = success
  if (/invalid api key|legacy endpoint/i.test(msg)) return "auth";
  if (/limit reached|rate limit|too many requests/i.test(msg)) return "rate";
  if (/restricted|premium|subscription|special endpoint|not available under/i.test(msg)) return "premium";
  if (status === 401 || status === 403) return "auth";
  if (status === 429) return "rate";
  if (status === 402) return "premium";
  if (msg) return "http";
  return null;
}

async function fmp(pathq) {
  if (reqs >= REQ_BUDGET) { const e = new Error("request budget reached"); e.code = "budget"; throw e; }
  reqs++;
  const url = `${BASE}${pathq}${pathq.includes("?") ? "&" : "?"}apikey=${encodeURIComponent(KEY)}`;
  const res = await fetch(url);
  const txt = await res.text();
  let body;
  try { body = JSON.parse(txt); } catch { body = txt; }
  const code = classify(body, res.status);
  if (code) {
    const err = new Error(typeof body === "string" ? body : (body && body["Error Message"]) || ("HTTP " + res.status));
    err.code = code;
    throw err;
  }
  return body;
}

const isNum = (n) => typeof n === "number" && isFinite(n);

function nearestForwardPair(est) {
  if (!Array.isArray(est) || !est.length) return null;
  const s = [...est].sort((a, b) => new Date(a.date) - new Date(b.date));
  const now = Date.now();
  let idx = s.findIndex((e) => new Date(e.date).getTime() >= now);
  if (idx === -1) idx = s.length - 1;
  let fy0 = s[idx], fy1 = s[idx + 1] || null;
  if (!fy1 && idx > 0) { fy1 = fy0; fy0 = s[idx - 1]; }
  return { fy0, fy1 };
}

function recomputeValuation(rec) {
  if (isNum(rec.price) && isNum(rec.fwdEps) && rec.fwdEps > 0) {
    rec.peFwd = rec.price / rec.fwdEps;
    rec.pegFwd = isNum(rec.epsFwd) && rec.epsFwd > 0 ? rec.peFwd / rec.epsFwd : null;
  }
}

async function updatePrice(rec) {
  const q = await fmp(`/quote?symbol=${rec.t}`);
  if (q && q[0]) {
    if (isNum(q[0].price)) rec.price = q[0].price;
    if (isNum(q[0].marketCap)) rec.marketCap = q[0].marketCap;
  }
  recomputeValuation(rec);
  rec.priceUpdated = new Date().toISOString();
}

async function updateFundamentals(rec) {
  const bs = await fmp(`/balance-sheet-statement?symbol=${rec.t}&period=annual&limit=1`);
  if (bs && bs[0]) {
    rec.cash = isNum(bs[0].cashAndShortTermInvestments) ? bs[0].cashAndShortTermInvestments : null;
    rec.debt = isNum(bs[0].totalDebt) ? bs[0].totalDebt : null;
  }
  const fg = await fmp(`/financial-growth?symbol=${rec.t}&period=annual&limit=1`);
  if (fg && fg[0]) {
    rec.revTTM = isNum(fg[0].revenueGrowth) ? fg[0].revenueGrowth * 100 : null;
    rec.epsTTM = isNum(fg[0].epsgrowth) ? fg[0].epsgrowth * 100 : null;
  }
  const est = await fmp(`/analyst-estimates?symbol=${rec.t}&period=annual&limit=8`);
  const pair = nearestForwardPair(est);
  if (pair && pair.fy0) {
    const e0 = pair.fy0, e1 = pair.fy1;
    rec.fwdEps = isNum(e0.epsAvg) ? e0.epsAvg : null;
    if (e1 && isNum(e0.epsAvg) && e0.epsAvg !== 0 && isNum(e1.epsAvg)) rec.epsFwd = (e1.epsAvg / Math.abs(e0.epsAvg) - 1) * 100;
    if (e1 && isNum(e0.revenueAvg) && e0.revenueAvg > 0 && isNum(e1.revenueAvg)) rec.revFwd = (e1.revenueAvg / e0.revenueAvg - 1) * 100;
  }
  recomputeValuation(rec);
  rec.fundamentalsUpdated = new Date().toISOString();
}

async function main() {
  const list = JSON.parse(await fs.readFile(LIST_PATH, "utf8"));

  let prev = { stocks: {} };
  try { prev = JSON.parse(await fs.readFile(OUT_PATH, "utf8")); } catch { /* first run */ }

  const stocks = {};
  for (const item of list) {
    const t = item.t;
    stocks[t] = Object.assign({ t: t, name: item.n }, prev.stocks[t] || {});
    stocks[t].t = t; stocks[t].name = item.n;
  }

  let stopped = null;

  const byOldest = (field) => (a, b) => {
    const ta = stocks[a][field] ? Date.parse(stocks[a][field]) : 0;
    const tb = stocks[b][field] ? Date.parse(stocks[b][field]) : 0;
    return ta - tb; // oldest / never-fetched first
  };

  // --- PRICE phase: all symbols, stalest price first ---
  const priceOrder = list.map((i) => i.t).sort(byOldest("priceUpdated"));
  for (const t of priceOrder) {
    if (stopped) break;
    try { await updatePrice(stocks[t]); }
    catch (e) {
      if (e.code === "auth" || e.code === "rate" || e.code === "budget") { stopped = e; break; }
      console.warn(`price ${t}: ${e.code || ""} ${e.message}`);
    }
  }

  // --- FUNDAMENTALS phase: stalest slice ---
  if (!stopped) {
    const order = list.map((i) => i.t).sort(byOldest("fundamentalsUpdated"));
    const slice = order.slice(0, FUND_SLICE);
    for (const t of slice) {
      if (stopped) break;
      try { await updateFundamentals(stocks[t]); }
      catch (e) {
        if (e.code === "auth" || e.code === "rate" || e.code === "budget") { stopped = e; break; }
        console.warn(`fundamentals ${t}: ${e.code || ""} ${e.message}`);
      }
    }
  }

  const out = { updated: new Date().toISOString(), source: "fmp", requests: reqs, stocks: stocks };
  await fs.writeFile(OUT_PATH, JSON.stringify(out, null, 2) + "\n");

  const withFund = Object.values(stocks).filter((s) => s.fundamentalsUpdated).length;
  console.log(`Wrote ${OUT_PATH}: ${Object.keys(stocks).length} symbols, ${withFund} with fundamentals, ${reqs} API requests.`);
  if (stopped) {
    console.log(`Stopped early (${stopped.code}: ${stopped.message}). Progress saved; the next run resumes.`);
    if (stopped.code === "auth") process.exit(1); // surface bad key as a failed job
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
