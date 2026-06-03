"""v4 — SPOKEN-HOOK-ONLY pattern analysis. ZERO API calls, no re-transcription.

Fixes from v3 per user direction:
  1. The hook = the first ~5 seconds of SPOKEN audio (≈12 words at ~2.5 wps), taken from the
     transcripts we already have. No caption text enters the hook.
  2. Hook detectors read the 5s spoken hook ONLY.
  3. comment_keyword_cta is REMOVED from the hook ranking (it's a caption mechanic, reported
     separately, not a spoken hook).

Outputs: research/pattern-report-v4.md (every reel cited) + research/hooks-5s.md (the 5s hook list).
Ranking = consistency (win-rate + low flop-rate + sample size), not single biggest hit.
"""
from __future__ import annotations
import json, re, sys, time, statistics as st
from pathlib import Path

WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
sys.path.insert(0, str(WF / "shared"))
from scraper import parse_reel, _extract_items  # noqa

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
TRANS = HERE / "transcripts"
SINCE = int(time.time()) - 90 * 86400
WORDS_5S = 13   # ~2.5 words/sec * 5s ≈ 12-13 words = the spoken hook window


def full_transcript(sc):
    p = TRANS / f"{sc}.json"
    if not p.exists():
        return ""
    try:
        return (json.loads(p.read_text(encoding="utf-8")).get("transcript") or "").strip()
    except Exception:
        return ""


def hook_5s(transcript: str) -> str:
    """First ~5 seconds of speech ≈ first WORDS_5S words."""
    return " ".join(transcript.split()[:WORDS_5S]).strip()


# ---- build reel set ----
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
        tr = full_transcript(sc)
        reels.append({
            "account": acct, "sc": sc, "link": f"https://www.instagram.com/reel/{sc}/",
            "views": r["combined_views"], "shares": r["shares"],
            "sr": (r["shares"] / r["combined_views"]) if r["combined_views"] else 0.0,
            "caption": r["transcript"] or "",         # kept only for the SEPARATE cta report
            "full": tr, "hook": hook_5s(tr),
            "music_only": not tr,
        })

# ---- classify winner/mid/flop by per-account median ----
bya = {}
for r in reels:
    bya.setdefault(r["account"], []).append(r)
med = {a: (sorted(x["views"] for x in rs)[len(rs) // 2] or 1) for a, rs in bya.items()}
for r in reels:
    m = med[r["account"]]
    r["mult"] = r["views"] / m
    r["cls"] = "winner" if r["views"] >= 3 * m else ("flop" if r["views"] < 0.5 * m else "mid")


# ---- SPOKEN-HOOK detectors (read r['hook'] ONLY) ----
def H(r, *pats):
    return any(re.search(p, r["hook"], re.I) for p in pats)


NUM = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b"
PROF = r"\bf+u+c+k|\bshit\b|\bdick\b|slapped their|\bass\b\b"

HOOK_DETECTORS = {
    "rhetorical_question": lambda r: "?" in r["hook"] or H(r,
        r"\bhow (would|do|did|can|to)\b", r"\bwhat (should|would|if|format|kind|is|happens|'s)\b",
        r"\bis it (still )?worth\b", r"\bdid you know\b", r"\bhave you ever\b", r"\bwhy (is|do|did|are)\b",
        r"\bwhich (one|video|format|grows)\b", r"\bwhat'?s the\b", r"\bguess\b", r"\bcash or pass\b"),
    "outcome_timebox": lambda r: H(r, r"in under \w+ seconds?", r"in \d+ (seconds|minutes|days)",
        r"\bfastest way\b", r"\b30 days\b", r"\b60 (seconds|minutes)\b", r"\bunder a minute\b",
        r"next 30 days", r"in 30 minutes"),
    "negative_command": lambda r: H(r, r"\bnever\b", r"^\s*stop\b", r"\bdon'?t (ever|post|do|start|use|go)\b",
        r"\bdo not\b", r"\bstop (trying|making|posting|using)\b"),
    "negcmd_plus_number": lambda r: H(r, r"\bnever\b", r"\bstop\b") and H(r, NUM)
        and H(r, r"setting|thing|step|reason|sign|hook|mistake|way|tip|word"),
    "youll_never_if": lambda r: H(r, r"you('| wi)ll never\b", r"you'?re never going", r"will never (go viral|grow|ever)"),
    "numbered_list": lambda r: bool(re.match(r"\s*\d+\b", r["hook"])) or H(r,
        rf"{NUM}\s+(things|ways|steps|settings|reasons|signs|types|hooks|tips|mistakes|tools|foods|rules|secrets)"),
    "shock_profanity": lambda r: H(r, PROF),
    "feature_update_news": lambda r: H(r, r"instagram (just|seriously|dropped|finally)",
        r"\bnew update\b", r"just dropped", r"cheat ?code", r"new (ig|instagram) (update|feature)"),
    "comparison_ab": lambda r: H(r, r"\bvs\b", r"\bversus\b", r"which (one|video|grows|did|got|is)\b",
        r"\bor pass\b", r"\bA or B\b"),
    "strip_back_reframe": lambda r: H(r, r"if i (take off|remove|swap)\b",
        r"it'?s not (about|only|what)", r"no matter the (niche|account|creator)",
        r"\bthis is not\b.*\bit'?s\b"),
    "save_steal_cmd": lambda r: H(r, r"\bsave this\b", r"\bsteal (this|my)\b", r"\bbookmark\b",
        r"\bdelete (your|that)\b"),
    "callout_negative": lambda r: H(r, r"this means your .* sucks", r"you'?re (doing|making) .* wrong",
        r"the (reason|biggest mistake)", r"this is why (you|your|no one)"),
    # ANTI (spoken)
    "personal_flex": lambda r: H(r, r"\bi (make|made|built|earn)\b", r"six figures", r"\$\d+k?\b.*\bi\b",
        r"i'?ve (built|made|saved)", r"traveled to \d+"),
    "generic_motivation": lambda r: H(r, r"stop consuming", r"ready is", r"your future self",
        r"believe in yourself", r"\bshow up\b", r"be kind", r"\bmindset\b", r"\bdiscipline\b") and not H(r, NUM),
}
ANTI = {"personal_flex", "generic_motivation"}

for r in reels:
    r["pats"] = [n for n, fn in HOOK_DETECTORS.items() if not r["music_only"] and fn(r)]


def agg(name):
    g = [r for r in reels if name in r["pats"]]
    if not g:
        return None
    w = [r for r in g if r["cls"] == "winner"]
    f = [r for r in g if r["cls"] == "flop"]
    return {"pattern": name, "n": len(g), "creators": sorted({r["account"] for r in g}),
            "n_creators": len({r["account"] for r in g}),
            "winners": len(w), "flops": len(f), "win_rate": round(len(w)/len(g), 3),
            "flop_rate": round(len(f)/len(g), 3),
            "median_views": int(st.median([r["views"] for r in g])),
            "median_mult": round(st.median([r["mult"] for r in g]), 2),
            "median_share": round(st.median([r["sr"] for r in g])*100, 2),
            "max_views": max(r["views"] for r in g),
            "reels": sorted(g, key=lambda r: -r["views"])}


results = {n: agg(n) for n in HOOK_DETECTORS}
results = {k: v for k, v in results.items() if v}
base = 0.18
for v in results.values():
    n = v["n"]
    shrunk = (v["winners"] + base*5) / (n + 5)
    v["score"] = round(shrunk * min(n, 25)/25 * (1 - v["flop_rate"]), 3)
    v["is_anti"] = v["pattern"] in ANTI
    v["promising_flag"] = (n <= 12) and v["win_rate"] >= 0.4   # high win but small N

proven = sorted([v for v in results.values() if not v["is_anti"]], key=lambda v: -v["score"])
anti = [v for v in results.values() if v["is_anti"]]


# ---- comment-keyword CTA reported SEPARATELY (caption mechanic, not a hook) ----
def has_cta(r):
    return bool(re.search(r"comment ['\"“]?\w+['\"”]?|comment the word|dm me\b", r["caption"], re.I))
cta = [r for r in reels if has_cta(r)]
cta_w = sum(1 for r in cta if r["cls"] == "winner")
cta_f = sum(1 for r in cta if r["cls"] == "flop")


def cite(r):
    return (f'    - {r["views"]:,}v · {r["sr"]*100:.2f}%sh · {r["mult"]:.1f}x · {r["cls"]} · '
            f'@{r["account"]} · [{r["sc"]}]({r["link"]})\n      HOOK(0-5s): "{r["hook"]}"')


md = ["# SPOKEN-HOOK Pattern Analysis v4 — first 5 seconds only, every reel cited\n",
      f"The hook = the **first ~5 seconds of spoken audio** (~{WORDS_5S} words) from the transcript. "
      f"Detectors read the spoken hook ONLY — never the caption. Caption-only mechanics (comment-keyword "
      f"CTA) are reported separately, not ranked as hooks.\n",
      f"All {len(reels)} reels (8 creators, ~90d). Winner/mid/flop vs each account's own median "
      f"(winner ≥3×, flop <0.5×). Ranked by consistency, not biggest hit.\n",
      "\n## Spoken-hook ranking\n",
      "| Pattern | N | Creators | Win% | Flop% | Med mult | Med share% | Max views | Score | Flag |",
      "|---|---|---|---|---|---|---|---|---|---|"]
for v in proven:
    flag = "⚠️ promising (small N)" if v["promising_flag"] else ""
    md.append(f"| **{v['pattern']}** | {v['n']} | {v['n_creators']} | {int(v['win_rate']*100)}% | "
              f"{int(v['flop_rate']*100)}% | {v['median_mult']} | {v['median_share']} | "
              f"{v['max_views']:,} | {v['score']} | {flag} |")
md.append("\n### Anti-patterns (spoken)\n| Pattern | N | Win% | Flop% | Med mult |\n|---|---|---|---|---|")
for v in anti:
    md.append(f"| **{v['pattern']}** | {v['n']} | {int(v['win_rate']*100)}% | {int(v['flop_rate']*100)}% | {v['median_mult']} |")
md.append(f"\n### Caption-layer mechanic (NOT a hook — reported separately)\n"
          f"- **comment_keyword_cta**: N={len(cta)} · {cta_w} winners / {cta_f} flops · "
          f"win {round(cta_w/len(cta)*100) if cta else 0}%. It rides on top of a spoken hook; it is not a stop-scroll itself.")

md.append("\n---\n## Full evidence per spoken-hook pattern (ALL reels)\n")
for v in proven + anti:
    md.append(f"\n### {v['pattern']} — N={v['n']} · {v['n_creators']} creators · "
              f"win {int(v['win_rate']*100)}% / flop {int(v['flop_rate']*100)}% · "
              f"med {v['median_views']:,}v ({v['median_mult']}x) · score {v['score']}"
              + ("  ⚠️ PROMISING, SMALL N" if v["promising_flag"] else ""))
    md.append(f"  creators: {', '.join('@'+c for c in v['creators'])}")
    for r in v["reels"]:
        md.append(cite(r))

(HERE / "pattern-report-v4.md").write_text("\n".join(md), encoding="utf-8")

# the plain 5s-hook list for reference
hl = ["# 5-second spoken hooks (all reels)\n"]
for r in sorted(reels, key=lambda r: -r["views"]):
    hl.append(f'- {r["views"]:,}v {r["cls"]} @{r["account"]} [{r["sc"]}]({r["link"]})\n  "{r["hook"]}"')
(HERE / "hooks-5s.md").write_text("\n".join(hl), encoding="utf-8")

print(f"reels={len(reels)} (music-only={sum(r['music_only'] for r in reels)})")
print("\nSPOKEN-HOOK RANKING (consistency):")
for v in proven:
    fl = "  <-- promising, small N" if v["promising_flag"] else ""
    print(f"  {v['score']:.3f}  {v['pattern']:20s} N={v['n']:3d} {v['n_creators']}cr "
          f"win{int(v['win_rate']*100):3d}% flop{int(v['flop_rate']*100):3d}% medmult{v['median_mult']:>5}{fl}")
print("\nANTI:")
for v in anti:
    print(f"         {v['pattern']:20s} N={v['n']:3d} win{int(v['win_rate']*100):3d}% flop{int(v['flop_rate']*100):3d}%")
print(f"\nCAPTION-LAYER comment_keyword_cta: N={len(cta)} win{round(cta_w/len(cta)*100) if cta else 0}% (reported separately, not a hook)")
