"""Systematic, auditable hook/format pattern analysis over ALL reels. ZERO API calls.

Builds the full reel set from cached .raw/ pages + Whisper transcripts, classifies EVERY reel by
hook pattern (deterministic keyword/regex detectors over the spoken opening + caption), then
aggregates per pattern:
  - N reels using it, and how many distinct creators
  - win-rate (winner/mid/flop by each account's own median: winner>=3x, flop<0.5x)
  - median views, median share rate, max views
  - FULL citation list (every reel link) so every claim is backed by sources

A pattern is "PROVEN" when it appears in enough reels AND wins consistently — whether across many
creators or repeatedly for one. Single-video flukes are flagged, not promoted.

Outputs research/pattern-report.md (human) + pattern-stats.json (machine).
"""
from __future__ import annotations
import json, re, sys, time, statistics as stats
from pathlib import Path

WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
sys.path.insert(0, str(WF / "shared"))
from scraper import parse_reel, _extract_items  # noqa

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
TRANS = HERE / "transcripts"
SINCE = int(time.time()) - 90 * 86400


# ---------- load full reel set + transcripts ----------
def transcript_for(sc):
    p = TRANS / f"{sc}.json"
    if not p.exists():
        return ""
    try:
        return (json.loads(p.read_text(encoding="utf-8")).get("transcript") or "").strip()
    except Exception:
        return ""


reels, seen = [], set()
for pg in sorted(RAW.glob("*-p*.json")):
    acct = pg.name.split("-p")[0]
    data = json.loads(pg.read_text(encoding="utf-8"))
    for it in _extract_items(data):
        r = parse_reel(it)
        sc = r["shortcode"]
        if not sc or sc in seen or r["taken_at"] < SINCE:
            continue
        seen.add(sc)
        spoken = transcript_for(sc)
        caption = (r["transcript"] or "")
        reels.append({
            "account": acct, "shortcode": sc, "link": f"https://www.instagram.com/reel/{sc}/",
            "views": r["combined_views"], "shares": r["shares"], "likes": r["likes"],
            "comments": r["comments"],
            "share_rate": (r["shares"] / r["combined_views"]) if r["combined_views"] else 0.0,
            "spoken": spoken, "caption": caption,
            # the "hook" = first ~2 spoken sentences (fallback to caption if music-only)
            "hook": " ".join(re.split(r'(?<=[.!?])\s+', spoken.strip())[:2])[:240] if spoken else caption[:160],
        })

# ---------- classify winner/mid/flop by per-account median ----------
by_acct = {}
for r in reels:
    by_acct.setdefault(r["account"], []).append(r)
acct_median = {}
for acct, rs in by_acct.items():
    vs = sorted(x["views"] for x in rs)
    acct_median[acct] = vs[len(vs) // 2] or 1
for r in reels:
    m = acct_median[r["account"]]
    r["median"] = m
    r["mult"] = r["views"] / m if m else 0
    r["class"] = "winner" if r["views"] >= 3 * m else ("flop" if r["views"] < 0.5 * m else "mid")


# ---------- hook/format pattern detectors (applied to spoken hook + caption) ----------
def has(s, *pats):
    return any(re.search(p, s, re.I) for p in pats)


PROFANITY = r"\bf+u+c+k|\bshit\b|\bdick\b|\bass\b|\bdamn\b|slapped their"
NUMWORD = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b"

DETECTORS = {
    # spoken-hook patterns
    "rhetorical_question": lambda r: r["hook"].count("?") > 0 or has(r["hook"],
        r"\bhow (would|do|did|can) you\b", r"\bwhat (should|would|if|format|kind|is) ",
        r"\bis it (still )?worth\b", r"\bdid you know\b", r"\bhave you ever\b", r"\bwhy (is|do|did)\b",
        r"\bwhich (one|video|format)\b", r"\bwhat's the\b"),
    "negative_command": lambda r: has(r["hook"], r"\bnever\b", r"\bstop\b", r"\bdon'?t (ever|post|do|start)\b",
        r"\bdo not\b"),
    "negcmd_plus_number": lambda r: has(r["hook"], r"\bnever\b", r"\bstop\b") and has(r["hook"], NUMWORD)
        and has(r["hook"], r"setting|thing|step|reason|sign|hook|mistake|way|tip"),
    "youll_never_if": lambda r: has(r["hook"], r"you('| wi)ll never\b", r"you'?re never going"),
    "numbered_list": lambda r: bool(re.match(r"\s*\d+\b", r["hook"])) or has(r["hook"],
        rf"\b{NUMWORD}\s+(things|ways|steps|settings|reasons|signs|types|hooks|tips|mistakes|tools|foods|rules)\b"),
    "shock_profanity": lambda r: has(r["hook"], PROFANITY),
    "feature_update_news": lambda r: has(r["hook"]+ " "+r["caption"],
        r"instagram (just|seriously|dropped)", r"new update", r"just dropped", r"new feature",
        r"cheat ?code", r"new ig update", r"\bupdate\b.*\b(views|reach|feature)"),
    "comparison_ab": lambda r: has(r["hook"]+" "+r["caption"], r"\bvs\b|\bversus\b",
        r"which (one|video|did|got|is)\b", r"\bA or B\b", r"cash or pass", r"\bor pass\b"),
    "strip_back_reframe": lambda r: has(r["hook"], r"if i (take off|remove|swap)\b",
        r"it'?s not (about|only|what).*it'?s (about|who|also)", r"\bstop trying to\b",
        r"no matter the (niche|account|creator)"),
    "outcome_timebox": lambda r: has(r["hook"], r"in under \w+ seconds", r"in \d+ (seconds|minutes|days)",
        r"\bfastest way\b", r"\b30 days\b", r"\bunder a minute\b"),
    "save_steal_cmd": lambda r: has(r["hook"]+" "+r["caption"], r"\bsave this\b", r"\bsteal (this|my)\b",
        r"\bbookmark\b"),
    # caption CTA (separate from spoken hook)
    "comment_keyword_cta": lambda r: has(r["caption"], r"comment ['\"“]?\w+['\"”]?", r"comment the word",
        r"dm me\b"),
    # anti-pattern detectors
    "personal_flex": lambda r: has(r["hook"]+" "+r["caption"], r"\bi (make|made|built|earn)\b.*\$|\$\d+k",
        r"six figures", r"\bat 2\d\b.*\$", r"traveled to \d+ countries", r"i'?ve built \$"),
    "generic_motivation": lambda r: has(r["hook"]+" "+r["caption"], r"stop consuming", r"ready is (not )?a",
        r"your future self", r"\bmindset\b", r"\bdiscipline\b", r"show up", r"be kind to",
        r"believe in yourself") and not has(r["hook"], r"\d"),
    "no_speech_musiconly": lambda r: not r["spoken"],
}

for r in reels:
    r["patterns"] = [name for name, fn in DETECTORS.items() if fn(r)]


# ---------- aggregate per pattern ----------
def agg(name):
    grp = [r for r in reels if name in r["patterns"]]
    if not grp:
        return None
    winners = [r for r in grp if r["class"] == "winner"]
    flops = [r for r in grp if r["class"] == "flop"]
    creators = sorted({r["account"] for r in grp})
    views = [r["views"] for r in grp]
    return {
        "pattern": name, "n": len(grp), "creators": creators, "n_creators": len(creators),
        "winners": len(winners), "mid": len(grp) - len(winners) - len(flops), "flops": len(flops),
        "win_rate": round(len(winners) / len(grp), 3),
        "flop_rate": round(len(flops) / len(grp), 3),
        "median_views": int(stats.median(views)),
        "median_mult": round(stats.median([r["mult"] for r in grp]), 2),
        "median_share": round(stats.median([r["share_rate"] for r in grp]) * 100, 2),
        "max_views": max(views),
        "reels": sorted(grp, key=lambda r: -r["views"]),
    }


ANTI = {"personal_flex", "generic_motivation", "no_speech_musiconly"}
results = {name: agg(name) for name in DETECTORS}
results = {k: v for k, v in results.items() if v}

# proven score: rewards BOTH frequency and consistent winning. Single-hit flukes score low.
for v in results.values():
    n = v["n"]
    # win-rate weighted by sample size (Wilson-ish shrink toward base rate for tiny N)
    base = 0.18  # rough overall winner base rate
    shrunk = (v["winners"] + base * 5) / (n + 5)
    v["proven_score"] = round(shrunk * min(n, 25) / 25 * (1 - v["flop_rate"]), 3)
    v["is_anti"] = v["pattern"] in ANTI
    v["single_hit_flag"] = n <= 2 and v["max_views"] > 50 * v["median_views"]


# ---------- write reports ----------
def cite(r):
    sh = (r["hook"] or "(music only)").replace("\n", " ")
    return f'    - {r["views"]:,}v · {r["share_rate"]*100:.2f}%sh · {r["mult"]:.1f}x · {r["class"]} · @{r["account"]} · [{r["shortcode"]}]({r["link"]})\n      > "{sh[:160]}"'


order = sorted(results.values(), key=lambda v: (-v["is_anti"] == 0, -v["proven_score"]))
proven = sorted([v for v in results.values() if not v["is_anti"]], key=lambda v: -v["proven_score"])
anti = [v for v in results.values() if v["is_anti"]]

md = ["# Pattern Analysis — full evidence (every reel cited)\n",
      f"All {len(reels)} reels (8 creators, ~90d) classified by deterministic detectors over the "
      f"**spoken hook** (Whisper) + caption. A reel can match multiple patterns. "
      f"Winner/mid/flop = vs each account's own median (winner ≥3×, flop <0.5×).\n",
      "**Ranking = `proven_score`:** rewards patterns that win *consistently across many videos* "
      "(frequency × sample-shrunk win-rate × (1−flop-rate)). Single-video flukes are flagged, not "
      "promoted.\n",
      "\n## Summary table (proven hooks/formats, ranked)\n",
      "| Pattern | N | Creators | Win% | Flop% | Median views | Median mult | Median share% | Max views | Score |",
      "|---|---|---|---|---|---|---|---|---|---|"]
for v in proven:
    flag = " ⚠️single-hit" if v["single_hit_flag"] else ""
    md.append(f"| **{v['pattern']}**{flag} | {v['n']} | {v['n_creators']} | {int(v['win_rate']*100)}% | "
              f"{int(v['flop_rate']*100)}% | {v['median_views']:,} | {v['median_mult']} | "
              f"{v['median_share']} | {v['max_views']:,} | {v['proven_score']} |")

md.append("\n## Anti-patterns (what fails)\n")
md.append("| Pattern | N | Win% | Flop% | Median views | Median mult |")
md.append("|---|---|---|---|---|---|")
for v in anti:
    md.append(f"| **{v['pattern']}** | {v['n']} | {int(v['win_rate']*100)}% | {int(v['flop_rate']*100)}% | "
              f"{v['median_views']:,} | {v['median_mult']} |")

md.append("\n---\n## Full evidence per pattern (ALL reels cited)\n")
for v in proven + anti:
    md.append(f"\n### {v['pattern']}  —  N={v['n']} · {v['n_creators']} creators · "
              f"win {int(v['win_rate']*100)}% / flop {int(v['flop_rate']*100)}% · "
              f"median {v['median_views']:,}v ({v['median_mult']}x) · score {v['proven_score']}"
              + ("  ⚠️ SINGLE-HIT FLUKE" if v["single_hit_flag"] else ""))
    md.append(f"  creators: {', '.join('@'+c for c in v['creators'])}")
    for r in v["reels"]:
        md.append(cite(r))

(HERE / "pattern-report.md").write_text("\n".join(md), encoding="utf-8")
# machine version (without the bulky reel bodies)
slim = {k: {kk: vv for kk, vv in v.items() if kk != "reels"} | {
    "reel_links": [r["link"] for r in v["reels"]]} for k, v in results.items()}
(HERE / "pattern-stats.json").write_text(json.dumps(slim, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"analyzed {len(reels)} reels across {len(by_acct)} accounts")
print(f"patterns detected: {len(results)}")
print("\nPROVEN (by score):")
for v in proven:
    flag = " <-- SINGLE-HIT, do not promote" if v["single_hit_flag"] else ""
    print(f"  {v['proven_score']:.3f}  {v['pattern']:22s} N={v['n']:3d} {v['n_creators']}cr "
          f"win{int(v['win_rate']*100):3d}% flop{int(v['flop_rate']*100):3d}% "
          f"med{v['median_views']:>7,}v{flag}")
print("\nANTI:")
for v in anti:
    print(f"         {v['pattern']:22s} N={v['n']:3d} win{int(v['win_rate']*100):3d}% flop{int(v['flop_rate']*100):3d}%")
