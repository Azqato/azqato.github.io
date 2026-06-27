// fetch-screener-data.mjs
//
// Builds data/screener.json for the Nasdaq 100 screener (screener.html).
// Runs in GitHub Actions on a daily cron. No npm dependencies — uses Node 20+
// global fetch and the Financial Modeling Prep "stable" API.
//
// Strategy (keeps a single daily run under the FMP free tier's 250 req/day):
//   Each run fully refreshes a rotating slice of the stalest symbols, oldest
//   first. A full refresh is 4 requests/symbol (quote, balance-sheet,
//   financial-growth, analyst-estimates). At the default of 50 symbols/run that
//   is ~200 requests, and the whole 100-name list cycles every ~2 days.
//
// Env:
//   FMP_API_KEY  (required)  - your FMP key (a GitHub Actions secret)
//   DAILY_COUNT  (optional)  - symbols to fully refresh per run (default 50)
//   REQ_BUDGET   (optional)  - hard cap on API requests this run (default 240)

import fs from "node:fs/promises";

const KEY = process.env.FMP_API_KEY;
if (!KEY) { console.error("ERROR: FMP_API_KEY is not set."); process.exit(1); }

const BASE = "https://financialmodelingprep.com/stable";
const DAILY_COUNT = parseInt(process.env.DAILY_COUNT || "50", 10);
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

  // Order by the stalest of a symbol's two timestamps (0 = never fetched), so
  // each run fully refreshes the least-recently-updated names first.
  const stalestMs = (t) => {
    const s = stocks[t];
    const a = s.priceUpdated ? Date.parse(s.priceUpdated) : 0;
    const b = s.fundamentalsUpdated ? Date.parse(s.fundamentalsUpdated) : 0;
    return Math.min(a, b);
  };
  const slice = list.map((i) => i.t).sort((a, b) => stalestMs(a) - stalestMs(b)).slice(0, DAILY_COUNT);

  let refreshed = 0;
  for (const t of slice) {
    if (stopped) break;
    try {
      await updatePrice(stocks[t]);
      await updateFundamentals(stocks[t]);
      refreshed++;
    } catch (e) {
      if (e.code === "auth" || e.code === "rate" || e.code === "budget") { stopped = e; break; }
      console.warn(`${t}: ${e.code || ""} ${e.message}`);
    }
  }

  const out = { updated: new Date().toISOString(), source: "fmp", requests: reqs, stocks: stocks };
  await fs.writeFile(OUT_PATH, JSON.stringify(out, null, 2) + "\n");

  const withFund = Object.values(stocks).filter((s) => s.fundamentalsUpdated).length;
  console.log(`Wrote ${OUT_PATH}: refreshed ${refreshed}/${slice.length} this run, ${withFund}/${Object.keys(stocks).length} have fundamentals, ${reqs} API requests.`);
  if (stopped) {
    console.log(`Stopped early (${stopped.code}: ${stopped.message}). Progress saved; the next run resumes.`);
    if (stopped.code === "auth") process.exit(1); // surface bad key as a failed job
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
