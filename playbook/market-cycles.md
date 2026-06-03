# Market Cycles — Jacky Niche (Baselines + Saturation + Cadence)
*Last updated: 2026-06-04 (v4 — measured, per-creator)*

Per-creator baselines, format saturation, and cadence economics from **707 reels over ~90 days
(2026-03-06 → 2026-06-03)**. Reproduce: `python research/temporal_market.py` (0 API calls).

---

## Per-creator baselines

| Creator | Reels | Median views | Max | Cadence/wk | Win-rate | Share-rate |
|---------|-------|--------------|-----|------------|----------|-----------|
| @personalbrandlaunch | 144 | 74,025 | 1.72M | 11.3 | 4% | 0.74% |
| @devinjatho | 37 | 27,318 | 4.69M | **3.0** | **40%** | 1.24% |
| @sam.gaudet | 155 | 16,243 | 2.22M | 12.2 | 12% | 0.41% |
| @bhavinipanjwanii | 23 | 13,590 | 769K | 2.1 | 21% | 0.43% |
| @realskytan | 41 | 11,042 | 42K | 3.6 | 7% | 0.26% |
| @alinamerkelcoach | 64 | 6,116 | 1.34M | 5.7 | 20% | 0.62% |
| @loganforsyth | 90 | 312 | 40K | 16.2 | 36%* | 0.0% |
| @iamaayushswamy | 153 | 265 | 221K | 13.9 | 45%* | 0.0% |

\*Low-median accounts: high "win-rate" vs a tiny own-median is not the same as reach. Their wins are
small in absolute views. Use **share-rate** and absolute views to compare across creators — medians
range ~280× between accounts, so cross-account comparison must normalize.

---

## 💡 The cadence finding: quality beats spray-and-pray

The data directly contradicts "post as much as possible":

- **@devinjatho posts only ~3×/week and wins 40%** (median 27K views, top share-rate 1.24%). Low volume,
  high hit-rate.
- **@sam.gaudet (12/wk) and @personalbrandlaunch (11/wk) flood the feed and win 12% / 4%.** High volume,
  low hit-rate — most of it underperforms their own (high) median.

**Takeaway for Jacky:** fewer, better, tactical reels (the @devinjatho model) beat high-volume
opinion/list content. Cadence is not the lever — hit-rate is.

---

## Format lifecycle (share of volume, early → late half)

| Format | Direction | Note |
|--------|-----------|------|
| offer-cta-promo | **Rising** | only rising format — monetization push |
| settings-walkthrough | Steady | and it's the #1 win-rate format → durable edge |
| hypothetical-reset-blueprint | Steady | 50% win, durable |
| myth-bust / tier-rating / interview-rant | Steady | stable presence |
| toolkit-swipe-file-handout | **Cooling** | 25→7, fatiguing fastest |
| numbered-how-to / category / comparison / teardown / case-study | **Cooling** | the list/catalog family broadly declining |

---

## Engagement-rate baselines (use as your "is this good?" yardstick)
- **Share-rate is the cleanest cross-account signal.** Niche-wide, **>1.5% share = a strong winner**
  regardless of raw views. Top formats: settings-walkthrough (1.35%), offer-cta-promo (1.33%).
- **Median shares** is a better quality read than views on low-median accounts (which can have 0 shares
  on 200K-view reels — bot/loop views vs genuine forwards).

---

## Saturation map (where the opportunity is)
| Crowded (avoid the easy default) | Under-served (the opening) |
|----------------------------------|----------------------------|
| mindset/philosophy (132 reels, 1.5K views) | algorithm/reach mechanics (50% win) |
| hooks-and-scripting topic (121, 10% win) | profile & posting setup (58% win, only 17 reels) |
| numbered-how-to / interview-rant formats | settings-walkthrough format (53% win) |
| comment-keyword CTA (~25% of all reels) | "if I started over" reset-blueprints |

---

## How to use this file
1. **Benchmark a new reel** against its creator's median + the >1.5% share-rate bar.
2. **Pick under-served lanes** (right column above) over the crowded defaults.
3. **Don't chase cadence** — @devinjatho's 3/wk @ 40% win is the model, not 12/wk @ 4%.
4. **Re-scrape in ~30 days** and re-run `temporal_market.py` to extend the lifecycle lines.

*Numbers from `research/temporal-market.json` (0 API calls).*
