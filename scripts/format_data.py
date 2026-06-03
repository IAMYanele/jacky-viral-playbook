"""Format the scraped raw data into the requested per-video structure. ZERO API calls.

For every reel (from cached .raw/ pages), emit:
  - metrics: views, likes, shares, comments, saves
  - link:    https://www.instagram.com/reel/<shortcode>/
  - transcription: the spoken audio (Whisper; falls back to '' if music-only)

Outputs (in research/formatted/):
  - formatted.json                 : flat list of all reels in the structure above
  - <account>.md                   : human-readable, one block per reel, per account
  - all-reels.md                   : everything in one file
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path

WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
sys.path.insert(0, str(WF / "shared"))
from scraper import parse_reel, _extract_items  # noqa

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
TRANS = HERE / "transcripts"
OUT = HERE / "formatted"
OUT.mkdir(exist_ok=True)
SINCE = int(time.time()) - 90 * 86400


def transcript_for(sc: str) -> str:
    p = TRANS / f"{sc}.json"
    if not p.exists():
        return ""
    try:
        return (json.loads(p.read_text(encoding="utf-8")).get("transcript") or "").strip()
    except Exception:
        return ""


# Collect, dedup by shortcode, per account
by_account: dict[str, list] = {}
seen: set[str] = set()
for pg in sorted(RAW.glob("*-p*.json")):
    acct = pg.name.split("-p")[0]
    data = json.loads(pg.read_text(encoding="utf-8"))
    for it in _extract_items(data):
        r = parse_reel(it)
        sc = r["shortcode"]
        if not sc or sc in seen or r["taken_at"] < SINCE:
            continue
        seen.add(sc)
        rec = {
            "account": acct,
            "metrics": {
                "views": r["combined_views"],
                "likes": r["likes"],
                "shares": r["shares"],
                "comments": r["comments"],
                "saves": r["saves"],
            },
            "link": f"https://www.instagram.com/reel/{sc}/",
            "transcription": transcript_for(sc),
        }
        by_account.setdefault(acct, []).append(rec)

# Sort each account's reels by views desc
flat = []
for acct in by_account:
    by_account[acct].sort(key=lambda x: x["metrics"]["views"], reverse=True)
    flat.extend(by_account[acct])

(OUT / "formatted.json").write_text(json.dumps(flat, ensure_ascii=False, indent=1), encoding="utf-8")


def block(rec: dict) -> str:
    m = rec["metrics"]
    t = rec["transcription"] or "(no spoken audio — music only)"
    return (
        f"### {rec['link']}\n"
        f"- **Metrics:** {m['views']:,} views | {m['likes']:,} likes | {m['shares']:,} shares | "
        f"{m['comments']:,} comments | {m['saves']:,} saves\n"
        f"- **Transcription:** {t}\n"
    )


# Per-account markdown
for acct, reels in by_account.items():
    lines = [f"# @{acct} — {len(reels)} reels (last ~90d)\n"]
    for rec in reels:
        lines.append(block(rec))
    (OUT / f"{acct}.md").write_text("\n".join(lines), encoding="utf-8")

# Combined
alllines = ["# Jacky — all scraped reels (metrics · link · transcription)\n",
            f"{len(flat)} reels across {len(by_account)} accounts. Source: cached scrape 2026-06-03.\n"]
for acct, reels in by_account.items():
    alllines.append(f"\n## @{acct} — {len(reels)} reels\n")
    for rec in reels:
        alllines.append(block(rec))
(OUT / "all-reels.md").write_text("\n".join(alllines), encoding="utf-8")

with_t = sum(1 for r in flat if r["transcription"])
print(f"formatted {len(flat)} reels | {with_t} with transcription | {len(by_account)} accounts")
print(f"-> research/formatted/  (formatted.json, all-reels.md, <account>.md)")
