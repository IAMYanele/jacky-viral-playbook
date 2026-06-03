"""Deterministic temporal + market-cycle stats. ZERO API calls.

Uses packaging_input.json (now has taken_at) + packaging_labels.json (format per reel) to compute:
  - temporal: per-month volume, median views, win-rate, and per-format share over time (trends.md)
  - market-cycles: per-creator baselines, format saturation, cadence, engagement-rate baselines

Writes temporal-market.json + a console summary.
"""
import json, statistics as st, datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
reels = json.loads((HERE / "packaging_input.json").read_text(encoding="utf-8"))
labels = {L["sc"]: L for L in json.loads((HERE / "packaging_labels.json").read_text(encoding="utf-8"))}
for r in reels:
    r["fmt"] = labels.get(r["sc"], {}).get("primary", "")
    r["month"] = dt.date.fromtimestamp(r["taken_at"]).strftime("%Y-%m") if r["taken_at"] else "?"


def wr(rs):
    return round(sum(1 for r in rs if r["cls"] == "winner") / len(rs), 3) if rs else 0


def med(rs, k):
    return int(st.median([r[k] for r in rs])) if rs else 0


# ---- temporal: by month ----
months = sorted({r["month"] for r in reels if r["month"] != "?"})
by_month = {m: [r for r in reels if r["month"] == m] for m in months}
temporal = []
for m in months:
    rs = by_month[m]
    temporal.append({"month": m, "n": len(rs), "median_views": med(rs, "views"),
                     "win_rate": wr(rs), "median_shares": med(rs, "shares")})

# ---- format share over time (is a format rising/falling?) ----
fmt_by_month = defaultdict(lambda: defaultdict(int))
for r in reels:
    if r["month"] != "?":
        fmt_by_month[r["fmt"]][r["month"]] += 1
fmt_trend = {}
for f, mc in fmt_by_month.items():
    series = [mc.get(m, 0) for m in months]
    half = len(months) // 2
    early = sum(series[:half]) or 0
    late = sum(series[half:]) or 0
    fmt_trend[f] = {"by_month": dict(zip(months, series)), "early": early, "late": late,
                    "direction": "rising" if late > early * 1.3 else ("cooling" if late < early * 0.7 else "steady")}

# ---- market-cycles: per creator ----
creators = {}
by_creator = defaultdict(list)
for r in reels:
    by_creator[r["a"]].append(r)
for a, rs in by_creator.items():
    vs = sorted(r["views"] for r in rs)
    span_days = round((max(r["taken_at"] for r in rs) - min(r["taken_at"] for r in rs)) / 86400, 1)
    creators[a] = {"n": len(rs), "median_views": vs[len(vs)//2], "max_views": vs[-1],
                   "span_days": span_days, "cadence_per_week": round(len(rs) / (span_days/7), 1) if span_days else 0,
                   "win_rate": wr(rs),
                   "median_share_rate": round(st.median([r["sr"] for r in rs])*100, 2)}

# ---- format saturation (share of total volume) ----
fmt_counts = Counter(r["fmt"] for r in reels)
total = len(reels)
saturation = {f: {"n": n, "pct": round(n/total*100, 1), "win_rate": wr([r for r in reels if r["fmt"]==f]),
                  "direction": fmt_trend.get(f, {}).get("direction", "?")}
              for f, n in fmt_counts.most_common()}

out = {"date_range": [dt.date.fromtimestamp(min(r["taken_at"] for r in reels if r["taken_at"])).isoformat(),
                      dt.date.fromtimestamp(max(r["taken_at"] for r in reels if r["taken_at"])).isoformat()],
       "temporal": temporal, "format_trend": fmt_trend, "creators": creators, "saturation": saturation,
       "n_reels": total}
(HERE / "temporal-market.json").write_text(json.dumps(out, ensure_ascii=True, indent=1), encoding="utf-8")

print("DATE RANGE:", out["date_range"])
print("\nTEMPORAL (by month):")
for t in temporal:
    print(f"  {t['month']}: {t['n']:3d} reels | median {t['median_views']:>7,}v | win {int(t['win_rate']*100):3d}% | med shares {t['median_shares']}")
print("\nFORMAT DIRECTION (early vs late half):")
for f, d in sorted(fmt_trend.items(), key=lambda x: -(x[1]['late']-x[1]['early'])):
    if fmt_counts[f] >= 8:
        print(f"  {d['direction']:7s} {f:30s} early={d['early']:2d} late={d['late']:2d}")
print("\nCREATORS:")
for a, c in sorted(creators.items(), key=lambda x: -x[1]['median_views']):
    print(f"  @{a:18s} n={c['n']:3d} med={c['median_views']:>7,}v cadence={c['cadence_per_week']}/wk win{int(c['win_rate']*100):3d}% sr{c['median_share_rate']}%")
