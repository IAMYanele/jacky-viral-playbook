"""Budget-capped Instagram scrape for Jacky's viral-research playbook.

Reuses the existing InstagramScraper (shared/scraper.py) — paginates ONLY /userreels/, which
returns views/likes/comments/saves/shares/caption/transcript per reel in one payload. No
/postdetail/, /postcomments/, or /userinfo/ calls (those are the budget killers).

Hard budget guard: a global call counter wraps every API call and ABORTS the run at --max-calls,
saving whatever was already fetched. Every raw page is cached to .raw/ so re-runs and playbook
regeneration cost ZERO additional API calls.

Usage:
  python scrape_jacky.py --accounts loganforsyth --max-calls 70 --since-days 90
  python scrape_jacky.py --accounts a,b,c --max-calls 70 --resume     # continue, respect prior count
  python scrape_jacky.py --from-cache                                  # rebuild from .raw/, 0 calls

The RapidAPI key is read at runtime from the existing scraping-agent config; it is never printed.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

# --- locate + import the existing scraper (reuse, don't reinvent) -----------
WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
SHARED = WF / "shared"
CONFIG = WF / "scraping agent" / "config.json"
sys.path.insert(0, str(SHARED))

import scraper as _scraper  # noqa: E402  (shared/scraper.py)
from scraper import InstagramScraper, parse_reel, _extract_items, _extract_pagination  # noqa: E402

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
RAW.mkdir(parents=True, exist_ok=True)
COUNTER_FILE = RAW / "_callcount.json"

ALL_ACCOUNTS = [
    "loganforsyth", "realskytan", "personalbrandlaunch", "sam.gaudet",
    "alinamerkelcoach", "bhavinipanjwanii", "devinjatho", "iamaayushswamy",
]


class BudgetExceeded(Exception):
    pass


class BudgetGuard:
    """Wraps InstagramScraper.api_get to count calls and hard-stop at max_calls."""

    def __init__(self, scraper: InstagramScraper, max_calls: int, start_at: int = 0):
        self.scraper = scraper
        self.max_calls = max_calls
        self.count = start_at
        self._orig = scraper.api_get
        scraper.api_get = self._counted

    def _counted(self, endpoint, params):
        if self.count >= self.max_calls:
            raise BudgetExceeded(f"Hit max-calls={self.max_calls}; aborting to protect budget.")
        self.count += 1
        print(f"  [call {self.count}/{self.max_calls}] GET {endpoint} {params.get('username_or_id','')}",
              flush=True)
        return self._orig(endpoint, params)


def load_keys() -> tuple[str, str, str]:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    key = cfg.get("rapidapi_key") or ""
    fb = cfg.get("rapidapi_key_fallback") or ""
    host = cfg.get("rapidapi_host") or "instagram-scraper-20251.p.rapidapi.com"
    if not key:
        raise SystemExit("No rapidapi_key found in scraping agent/config.json")
    return key, fb, host


def cache_page(account: str, page: int, data: dict) -> None:
    (RAW / f"{account}-p{page}.json").write_text(
        json.dumps(data, ensure_ascii=False), encoding="utf-8")


def scrape_account(scraper, account, since_ts, max_pages, guard):
    """Paginate /userreels/, caching each raw page. Returns parsed reels >= since_ts."""
    raw_items, seen, ptoken = [], set(), None
    for page in range(1, max_pages + 1):
        params = {"username_or_id": account}
        if ptoken:
            params["pagination_token"] = ptoken
        data = scraper.api_get("/userreels/", params)   # counted by guard
        cache_page(account, page, data)
        items = _extract_items(data)
        if not items:
            break
        all_dupes = True
        for it in items:
            node = it.get("node", it) if isinstance(it, dict) else it
            code = (node.get("code") or node.get("shortcode") or "") if isinstance(node, dict) else ""
            if code and code not in seen:
                seen.add(code)
                raw_items.append(it)
                all_dupes = False
        if all_dupes and page > 1:
            break
        # stop once a whole page is older than the cutoff
        ts = [parse_reel(it).get("taken_at", 0) for it in items]
        if ts and all(t and t < since_ts for t in ts):
            break
        ptoken = _extract_pagination(data)
        if not ptoken:
            break
        time.sleep(scraper.rate_limit_delay)

    reels = []
    for it in raw_items:
        r = parse_reel(it)
        if r["taken_at"] >= since_ts:
            reels.append(r)
    reels.sort(key=lambda r: r["combined_views"], reverse=True)
    return reels


def summarize(account, reels):
    if not reels:
        return {"account": account, "reels": 0}
    views = sorted(r["combined_views"] for r in reels)
    median = views[len(views) // 2]
    span_days = (max(r["taken_at"] for r in reels) - min(r["taken_at"] for r in reels)) / 86400
    winners = [r for r in reels if median and r["combined_views"] >= 3 * median]
    flops = [r for r in reels if median and r["combined_views"] < 0.5 * median]
    return {
        "account": account, "reels": len(reels), "median_views": median,
        "max_views": views[-1], "span_days": round(span_days, 1),
        "winners": len(winners), "flops": len(flops),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--accounts", default="", help="comma list; default = all 8")
    ap.add_argument("--limit-accounts", type=int, default=0)
    ap.add_argument("--max-calls", type=int, default=70)
    ap.add_argument("--since-days", type=int, default=90)
    ap.add_argument("--max-pages", type=int, default=8)
    ap.add_argument("--resume", action="store_true", help="carry the saved global call count")
    ap.add_argument("--from-cache", action="store_true", help="rebuild from .raw/, no API calls")
    args = ap.parse_args()

    accounts = [a.strip() for a in args.accounts.split(",") if a.strip()] or list(ALL_ACCOUNTS)
    if args.limit_accounts:
        accounts = accounts[: args.limit_accounts]
    since_ts = int(time.time()) - args.since_days * 86400

    if args.from_cache:
        return rebuild_from_cache(accounts, since_ts)

    start_at = 0
    if args.resume and COUNTER_FILE.exists():
        start_at = json.loads(COUNTER_FILE.read_text()).get("count", 0)

    key, fb, host = load_keys()
    scraper = InstagramScraper(api_key=key, api_host=host, fallback_api_key=fb or None,
                               rate_limit_delay=0.5)
    guard = BudgetGuard(scraper, args.max_calls, start_at=start_at)

    print(f"Budget: {start_at} used coming in, hard stop at {args.max_calls}.")
    print(f"Accounts this run: {accounts}\nSince: {args.since_days}d ago | max {args.max_pages} pages/acct\n")

    summaries, aborted = [], False
    for acct in accounts:
        print(f"=== @{acct} ===", flush=True)
        try:
            reels = scrape_account(scraper, acct, since_ts, args.max_pages, guard)
        except BudgetExceeded as e:
            print(f"!! {e}")
            aborted = True
            break
        s = summarize(acct, reels)
        summaries.append(s)
        print(f"   -> {s.get('reels',0)} reels, median {s.get('median_views',0):,} views, "
              f"{s.get('winners',0)} winners / {s.get('flops',0)} flops, ~{s.get('span_days',0)}d span\n")

    COUNTER_FILE.write_text(json.dumps({"count": guard.count}), encoding="utf-8")
    print("\n================ BUDGET REPORT ================")
    print(f"total RapidAPI calls = {guard.count}")
    print(f"raw pages cached     = {len(list(RAW.glob('*-p*.json')))}")
    print(f"aborted on budget    = {aborted}")
    for s in summaries:
        print(f"  @{s['account']}: {s.get('reels',0)} reels | "
              f"{s.get('winners',0)}W/{s.get('flops',0)}F | median {s.get('median_views',0):,}")


def rebuild_from_cache(accounts, since_ts):
    print("Rebuilding from .raw/ cache — 0 API calls.")
    summaries = []
    for acct in accounts:
        pages = sorted(RAW.glob(f"{acct}-p*.json"))
        seen, reels = set(), []
        for pg in pages:
            data = json.loads(pg.read_text(encoding="utf-8"))
            for it in _extract_items(data):
                r = parse_reel(it)
                if r["shortcode"] and r["shortcode"] not in seen and r["taken_at"] >= since_ts:
                    seen.add(r["shortcode"])
                    reels.append(r)
        reels.sort(key=lambda r: r["combined_views"], reverse=True)
        summaries.append(summarize(acct, reels))
    for s in summaries:
        print(f"  @{s['account']}: {s.get('reels',0)} reels | {s.get('winners',0)}W/{s.get('flops',0)}F "
              f"| median {s.get('median_views',0):,}")
    print("total RapidAPI calls = 0 (cache)")


if __name__ == "__main__":
    main()
