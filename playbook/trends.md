# trends.md — Jacky Niche Trends Tracker
*Last updated: 2026-06-04 (v4 — from real timestamps, not a snapshot)*

Built from the actual post dates of **707 reels over ~90 days (2026-03-06 → 2026-06-03)**. "Rising/
cooling" = measured change in a format's share of volume between the early half and late half of the
window. Reproduce: `python research/temporal_market.py` (0 API calls).

---

## 📈 The macro signal: the bar is rising
Win-rate (reels beating 3× their creator's median) climbed steadily across the window:

| Month | Reels | Median views | Win-rate | Median shares |
|-------|-------|--------------|----------|---------------|
| 2026-03 | 198 | 10,219 | **12%** | 39 |
| 2026-04 | 226 | 12,703 | **23%** | 60 |
| 2026-05 | 261 | 10,248 | **29%** | 43 |
| 2026-06 (partial) | 22 | 8,723 | **40%** | 25 |

**Reading:** the niche is maturing — a *larger share* of reels are over-performing over time, which means
creators are converging on what works and the audience is rewarding it. Generic content has a shrinking
window. (Median views are flat, so this is about *hit-rate*, not a rising tide.)

---

## 🟢 Rising (gaining share of volume)
- **offer-cta-promo** — the only clearly rising format (7 → 11 reels, early→late). Creators are pushing
  monetization/lead-gen harder. It also carries the 2nd-highest share-rate (1.33%).

## 🟡 Steady (holding share)
- **myth-bust-directive**, **tier-rating-rundown**, **hypothetical-reset-blueprint**, **settings-walkthrough**,
  **spoken-take/interview-rant** — stable presence across the window.

## 🟠 Cooling (losing share — saturating/fatiguing)
- **toolkit-swipe-file-handout** — sharpest drop (25 → 7). The "comment for my list of tools/templates"
  format is fatiguing fast.
- **numbered-how-to-tutorial** (79 → 42), **category-taxonomy-explainer** (31 → 16),
  **comparison-juxtaposition** (34 → 21), **personal-proof-case-study** (27 → 16),
  **annotated-teardown-demo** (28 → 18). The "list / catalog / teardown" family is broadly cooling.

## 🔴 Structurally weak (not a trend — just consistently underperforms)
- **mindset/philosophy topic** (1,508 median views), **relatability trigger** (10% win),
  **hooks-and-scripting topic** (10% win / 38% flop). High volume, low payoff — see what-fails.md.

---

## What the audience is rewarding more over time (inferred)
- **Tactical, shown-on-screen reach content** (settings/algorithm) holds up as the list-formats cool.
- **Monetization framing** is rising on the creator side (offer-cta-promo) — watch whether the audience
  sustains it or it saturates like the toolkit format did.

## Saturation signals (act on these)
- The **list / catalog / teardown** family is cooling together → differentiate with **shown-on-screen
  tactical** formats (settings-walkthrough) and **"if I started over" blueprints**, which are steady.
- **Comment-keyword CTA** is on ~25% of all reels → the *mechanic* is saturated; the edge is a fresher
  resource + a stronger spoken hook, not the CTA itself.

## Watch list (confirm on the next scrape)
| Signal | Why | Confirms if… |
|--------|-----|--------------|
| Rising win-rate | 12%→40% over 90d | next window sustains >30% — the bar keeps rising |
| offer-cta-promo rising | only rising format | it keeps climbing OR saturates like toolkit did |
| toolkit/list cooling | sharp drop | these keep losing share next window |

*This is now two-point-in-time-capable: re-run `temporal_market.py` on a fresh scrape to extend the
trend lines. Numbers from `research/temporal-market.json` (0 API calls).*
