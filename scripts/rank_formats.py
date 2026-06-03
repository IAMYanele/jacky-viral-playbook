"""Aggregate + rank packaging formats by engagement. ZERO API calls.

Inputs:
  packaging_input.json         — all reels with full engagement (views/likes/shares/comments/cls/mult)
  packaging_labels.json        — [{sc, primary, secondary}] from the workflow classifier
  packaging_taxonomy.json      — [{name, definition, verbal_signals}] canonical taxonomy

Output:
  format-ranking.json + format-ranking.md — each packaging format with: N, creators, win-rate,
  median views/likes/shares, median share-rate, and ALL reels cited (for the swipe file).
  Ranked DESCENDING by a consistency-aware engagement score.
"""
import json, statistics as st
from pathlib import Path

HERE = Path(__file__).resolve().parent
reels = {r["sc"]: r for r in json.loads((HERE / "packaging_input.json").read_text(encoding="utf-8"))}
labels = json.loads((HERE / "packaging_labels.json").read_text(encoding="utf-8"))
tax = {t["name"]: t for t in json.loads((HERE / "packaging_taxonomy.json").read_text(encoding="utf-8"))}

# attach primary label to each reel
for L in labels:
    r = reels.get(L["sc"])
    if r:
        r["primary"] = L.get("primary", "")
        r["secondary"] = L.get("secondary", "")

groups = {}
for r in reels.values():
    p = r.get("primary")
    if p:
        groups.setdefault(p, []).append(r)


def agg(name, rs):
    n = len(rs)
    w = sum(1 for r in rs if r["cls"] == "winner")
    f = sum(1 for r in rs if r["cls"] == "flop")
    cr = len({r["a"] for r in rs})
    med_v = int(st.median([r["views"] for r in rs]))
    med_l = int(st.median([r["likes"] for r in rs]))
    med_s = int(st.median([r["shares"] for r in rs]))
    med_sr = round(st.median([r["sr"] for r in rs]) * 100, 2)
    med_mult = round(st.median([r["mult"] for r in rs]), 2)
    base = 0.23  # winner base rate in this transcript set (165/707)
    shrunk = (w + base * 6) / (n + 6)
    flop_rate = f / n
    # engagement-weighted, consistency-aware score
    score = round(shrunk * (1 - flop_rate) * min(n, 30) / 30, 3)
    return {
        "format": name, "definition": tax.get(name, {}).get("definition", ""),
        "signals": tax.get(name, {}).get("verbal_signals", []),
        "n": n, "creators": cr, "winners": w, "flops": f,
        "win_rate": round(w / n, 3), "flop_rate": round(flop_rate, 3),
        "median_views": med_v, "median_likes": med_l, "median_shares": med_s,
        "median_share_rate": med_sr, "median_mult": med_mult, "score": score,
        "reels": sorted(rs, key=lambda r: -r["views"]),
        "small_n": n <= 8,
    }


ranked = sorted((agg(n, rs) for n, rs in groups.items()), key=lambda x: -x["score"])

slim = [{k: v for k, v in g.items() if k != "reels"} | {"reel_scs": [r["sc"] for r in g["reels"]]} for g in ranked]
(HERE / "format-ranking.json").write_text(json.dumps({"ranked": slim}, ensure_ascii=True, indent=1), encoding="utf-8")

# console summary
total = sum(len(rs) for rs in groups.values())
print(f"classified reels grouped: {total} across {len(groups)} formats\n")
print(f"{'FORMAT':32s} N  cr  win%  flop%  medViews  medShares  medSR%  score")
for g in ranked:
    flag = " (small N)" if g["small_n"] else ""
    print(f"{g['format']:32s} {g['n']:3d} {g['creators']:2d}  {int(g['win_rate']*100):3d}%  "
          f"{int(g['flop_rate']*100):3d}%  {g['median_views']:>8,}  {g['median_shares']:>8,}  "
          f"{g['median_share_rate']:>5}  {g['score']}{flag}")
