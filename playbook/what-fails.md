# What Fails — Jacky Niche Playbook
*Last updated: 2026-06-04 (v4 — measured flop-rates across all 4 dimensions + killer combinations)*

Ranked by how *consistently* things fail (flop-rate + low win-rate across a real sample), not by one bad
example. 707 reels, 8 creators, ~90 days. Flop = reel under 0.5× its creator's median. Reproduce from
`research/` (0 API calls). Per-dimension detail in [`hooks.md`](hooks.md) / [`formats.md`](formats.md).

---

## The killer COMBINATIONS (highest flop-rates, real samples)

| Flop% | Win% | N | Median views | The losing stack |
|-------|------|---|--------------|------------------|
| **60%** | **0%** | 25 | 1,765 | **hooks-and-scripting topic × numbered-how-to list** — "5 hooks that always work" as a generic list |
| **56%** | 0% | 14 | 5,166 | **hooks-and-scripting × myth-bust-directive** — "stop using hooks like this" with no demo |
| **50%** | 12% | 8 | 4,439 | **monetization × numbered-how-to** — "5 ways to get clients" listicle |
| **50%** | 38% | 8 | 1,360 | **personal-brand × numbered-how-to** |
| **39%** | 6% | 18 | 14,577 | **content-strategy × comparison** — abstract "this vs that" strategy talk |

The pattern across every killer combo: **a meta/abstract topic delivered as a generic list or vague
comparison.** It's the easy-to-make, everyone-makes-it content — and it reliably dies.

---

## Worst by DIMENSION (each measured)

### Topics that fail
| Topic | N | Win% | Flop% | Median views | Why |
|-------|---|------|-------|--------------|-----|
| **hooks-and-scripting** | 121 | **10%** | **38%** | 11,986 | The most-taught topic, the worst win-rate. Meta + saturated — teaching hooks rarely hooks. |
| **content-strategy-and-planning** | 118 | 18% | 26% | 16,959 | Abstract "content systems" talk; high volume, low conversion to wins. |
| **editing-and-production** | 77 | 23% | 31% | 6,537 | Crowded craft content; flops more than it wins. |
| **mindset-and-business-philosophy** | 132 | 22% | 17% | **1,508** | Biggest category, near-zero reach. Wins "consistently" only because the bar (its own median) is tiny. |

### Triggers that fail
| Trigger | N | Win% | Flop% | Median views | Why |
|---------|---|------|-------|--------------|-----|
| **relatability-validation** | 112 | **10%** | 18% | **1,455** | "We've all been there" feelings with no tactic. Lowest reach in the set. |
| **fear-of-mistake** | 78 | 26% | **42%** | 2,471 | "You're doing it wrong" — highest flop-rate of the big triggers. Anxiety without a fix doesn't travel. |
| **authority-formula-credibility** | 200 | 20% | 24% | 17,012 | The default trigger (most common). Average at best — credibility alone isn't a reason to share. |

### Packaging formats that fail (from formats.md)
| Format | N | Win% | Flop% | Why |
|--------|---|------|-------|-----|
| **numbered-how-to-tutorial** | 121 | 18% | **35%** | The default format; over-used, below-average. A number isn't a hook. |
| **spoken-take/interview-rant** | 136 | 25% | 19% | The single most common format, yet **~1,600 median views, ~0 shares.** Talking-head opinion rarely travels. |
| **myth-bust-directive** | 57 | 21% | 40% | "Everyone says X, do Y" with no demonstration flops 2× as often as it wins. |

### Spoken hooks that fail (from hooks.md)
- **Bare negative command** ("Never/Stop…") with no number — 36% flop (the number fixes it).
- **Generic motivation** spoken openers — no tactic, no save.

---

## Execution failures (sink an otherwise-good reel)

| Failure | Evidence | Lesson |
|---------|----------|--------|
| **CTA in the spoken open** | 153v @sam.gaudet [DVmsSneEqPl](https://www.instagram.com/reel/DVmsSneEqPl/) — opened with "Comment 'hook'" | Spoken open must hook; CTA goes in the caption. |
| **Reposting a winner unchanged** | 322v @devinjatho [DVtNsdyjRJf](https://www.instagram.com/reel/DVtNsdyjRJf/) — verbatim re-cut of his 521K reel | Rotate, don't recycle. |
| **Foreign-language repost to EN audience** | 208v @alinamerkelcoach [DV1XgBTjU49](https://www.instagram.com/reel/DV1XgBTjU49/) — Korean audio under EN caption | Don't recycle another language's winner. |
| **Spray-and-pray cadence** | @sam.gaudet 12/wk → 12% win; @personalbrandlaunch 11/wk → 4% win | Volume ≠ wins. @devinjatho posts 3/wk and wins 40%. |

---

## ⚠️ Don't over-learn from true zeros
Some 0–3 view reels have strong hooks (shadowban / new-account window = distribution failures, not
content failures). Weight flops with a real view base (hundreds–thousands) over true zeros — otherwise
you'll kill a hook that actually works.

---

## The test before you post
**"Is this a tactical topic, shown on screen, with a fast specific payoff — or is it a meta/abstract
take delivered as a list?"** The first wins; the second is the crowded default that reliably flops.

*All figures reproducible from `research/` (0 API calls).*
