"""Build formats.md as a swipe file: packaging format -> how it's delivered -> evidence.

Same structure as hooks.md, but the unit is HOW THE INFORMATION IS PACKAGED AND DELIVERED (the whole
reel's delivery structure), discovered by the packaging workflow and ranked by engagement
(views/likes/shares/share-rate) + win-rate, descending. Every reel cited. ZERO API calls.
"""
import json, statistics as st
from pathlib import Path

HERE = Path(__file__).resolve().parent
rank = json.loads((HERE / "format-ranking.json").read_text(encoding="utf-8"))["ranked"]
inp = {r["sc"]: r for r in json.loads((HERE / "packaging_input.json").read_text(encoding="utf-8"))}


def title(name):
    return name.replace("-", " ").upper()


def first_words(t, n=14):
    return " ".join((t or "").split()[:n])


def tier_label(g):
    wr, fr, n = g["win_rate"], g["flop_rate"], g["n"]
    if g.get("small_n"):
        return "⚠️ PROMISING (small N)"
    if wr >= 0.45 and fr <= 0.20:
        return "S — PROVEN (consistent winner)"
    if wr >= 0.25 and fr <= 0.22:
        return "A — solid, reliable"
    if g["median_views"] >= 30000 and wr < 0.20:
        return "B — high reach, inconsistent (big hits + big flops)"
    if fr >= 0.35:
        return "C — over-used / high flop"
    return "B — works, execution-dependent"


lines = [
    "# Information-Packaging Swipe File — Jacky Niche",
    "",
    "*How the information is PACKAGED AND DELIVERED — the recurring delivery structures across the whole",
    "reel (not the hook, not the topic). Discovered from 707 transcripts, classified, then ranked by",
    "**engagement** (median views/likes/shares + share-rate) and **win-rate**, descending. Same swipe-file",
    "shape as hooks.md: each format = how it's delivered, the verbal signals, and every source reel that",
    "used it. Win/Flop = vs each account's own median. Reproduce: `python research/rank_formats.py` (0 API calls).*",
    "",
    "> **Ranking logic:** a format ranks high when it wins *consistently across many reels* (win-rate + low",
    "> flop-rate + sample size), not off one viral hit. Where a format gets big **reach** but inconsistent",
    "> results, that's stated explicitly — reach ≠ reliability.",
    "",
    "## Quick ranking (by consistency-weighted engagement)",
    "",
    "| # | Packaging format | N | Creators | Win% | Flop% | Median views | Median shares | Share% |",
    "|---|------------------|---|----------|------|-------|--------------|---------------|--------|",
]
for i, g in enumerate(rank, 1):
    lines.append(f"| {i} | **{title(g['format'])}** | {g['n']} | {g['creators']} | {int(g['win_rate']*100)}% | "
                 f"{int(g['flop_rate']*100)}% | {g['median_views']:,} | {g['median_shares']:,} | {g['median_share_rate']}% |")
lines.append("\n---")

for i, g in enumerate(rank, 1):
    reels = sorted((inp[sc] for sc in g["reel_scs"] if sc in inp), key=lambda r: -r["views"])
    lines.append(f"\n## {i}. {title(g['format'])}")
    lines.append(f"**Tier:** {tier_label(g)}  ·  **N={g['n']} reels · {g['creators']} creators · "
                 f"{int(g['win_rate']*100)}% win · {int(g['flop_rate']*100)}% flop**")
    lines.append(f"**Engagement (median):** {g['median_views']:,} views · {g['median_likes']:,} likes · "
                 f"{g['median_shares']:,} shares · {g['median_share_rate']}% share-rate · {g['median_mult']}× own-median")
    lines.append("")
    lines.append(f"**HOW IT'S PACKAGED:** {g['definition']}")
    lines.append("")
    if g.get("signals"):
        lines.append("**VERBAL SIGNALS (how they actually say it):**")
        for s in g["signals"]:
            lines.append(f'- "{s}"')
        lines.append("")
    lines.append(f"**EVIDENCE** ({len(reels)} reels, by views — real opening words quoted):")
    for r in reels:
        tag = {"winner": "✅ winner", "mid": "· mid", "flop": "✗ flop"}[r["cls"]]
        lines.append(f'- {tag} · {r["views"]:,}v · {r["likes"]:,}L · {r["shares"]:,}sh · '
                     f'{round(r["sr"]*100,2)}% · @{r["a"]}')
        lines.append(f'  https://www.instagram.com/reel/{r["sc"]}/')
        lines.append(f'  > "{first_words(r["transcript"])}"')
    lines.append("")
    lines.append("---")

out = HERE.parent / "playbook" / "formats.md"
out.write_text("\n".join(lines), encoding="utf-8")
total = sum(len(g["reel_scs"]) for g in rank)
print(f"wrote {out} | {len(rank)} formats · {total} cited reels")
