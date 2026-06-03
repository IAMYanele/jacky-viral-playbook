"""Build the analysis dataset from cached .raw/ pages. ZERO API calls.

Emits brands/jacky/research/dataset.json: per account, the classified reels (winner/mid/flop by
that account's median views) with metrics + transcript, plus the top winners and worst flops with
full text for the playbook. Also writes a compact markdown digest for fast reading.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path

WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
sys.path.insert(0, str(WF / "shared"))
from scraper import parse_reel, _extract_items  # noqa

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
SINCE = int(time.time()) - 90 * 86400

ACCOUNTS = ["loganforsyth","realskytan","personalbrandlaunch","sam.gaudet",
            "alinamerkelcoach","bhavinipanjwanii","devinjatho","iamaayushswamy"]

def load_account(acct):
    seen, reels = set(), []
    for pg in sorted(RAW.glob(f"{acct}-p*.json")):
        data = json.loads(pg.read_text(encoding="utf-8"))
        for it in _extract_items(data):
            r = parse_reel(it)
            if r["shortcode"] and r["shortcode"] not in seen and r["taken_at"] >= SINCE:
                seen.add(r["shortcode"]); reels.append(r)
    return reels

def classify(reels):
    if not reels: return reels, 0
    vs = sorted(r["combined_views"] for r in reels)
    median = vs[len(vs)//2] or 1
    for r in reels:
        v = r["combined_views"]
        r["share_rate"] = round(r["shares"]/v, 4) if v else 0
        r["save_rate"]  = round(r["saves"]/v, 4) if v else 0
        r["mult"] = round(v/median, 2) if median else 0
        r["class"] = "winner" if v >= 3*median else ("flop" if v < 0.5*median else "mid")
    return reels, median

def clip(t, n=600):
    t = (t or "").replace("\n"," ").strip()
    return t[:n]

out = {"generated_for":"jacky","since_days":90,"accounts":{}}
digest = ["# Jacky dataset digest (from cache, 0 API calls)\n"]
for acct in ACCOUNTS:
    reels = load_account(acct)
    reels, median = classify(reels)
    if not reels:
        continue
    winners = sorted([r for r in reels if r["class"]=="winner"], key=lambda r:-r["combined_views"])
    flops   = sorted([r for r in reels if r["class"]=="flop"], key=lambda r:r["combined_views"])
    span = (max(r["taken_at"] for r in reels)-min(r["taken_at"] for r in reels))/86400
    out["accounts"][acct] = {
        "reels": len(reels), "median": median, "span_days": round(span,1),
        "n_winners": len(winners), "n_flops": len(flops),
        "winners": [{k:r[k] for k in ("shortcode","link","combined_views","likes","comments","saves","shares","share_rate","mult","transcript")} for r in winners[:12]],
        "flops":   [{k:r[k] for k in ("shortcode","link","combined_views","likes","comments","saves","shares","share_rate","mult","transcript")} for r in flops[:8]],
    }
    digest.append(f"\n## @{acct} — {len(reels)} reels | median {median:,} | {len(winners)}W/{len(flops)}F | ~{span:.0f}d")
    digest.append("\n**Top winners:**")
    for r in winners[:8]:
        digest.append(f"- {r['combined_views']:,}v · {r['share_rate']*100:.2f}% sh · {r['mult']}x · [{r['shortcode']}]({r['link']})\n  > {clip(r['transcript'],240)}")
    digest.append("\n**Worst flops:**")
    for r in flops[:5]:
        digest.append(f"- {r['combined_views']:,}v · {r['mult']}x · [{r['shortcode']}]({r['link']})\n  > {clip(r['transcript'],160)}")

(HERE/"dataset.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
(HERE/"dataset-digest.md").write_text("\n".join(digest), encoding="utf-8")
tot = sum(a["reels"] for a in out["accounts"].values())
print(f"dataset.json written | {len(out['accounts'])} accounts | {tot} reels total")
