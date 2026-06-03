# What Fails — Jacky Niche Playbook
*Last updated: 2026-06-03 (v3 — every anti-pattern measured across all 712 reels)*

Patterns ranked by how *consistently* they fail (high flop-rate + low win-rate across a real sample), not
by one bad example. Winner/mid/flop vs each account's own median. Full evidence:
[`research/pattern-report.md`](../research/pattern-report.md).

---

## The two confirmed killers

### 1. Personal Flex / Journey — **N=16 · 6% win · 68% flop · median 0.31×** — WORST PATTERN
Talking about *your* income/lifestyle/journey. The single most reliable way to flop: more than two-thirds
of these reels fell below half their creator's median. The audience is outcome-selfish — they don't reward
your success, only their transferable result.
**Evidence (all flops):**
- 208v · @alinamerkelcoach [DV1XgBTjU49](https://www.instagram.com/reel/DV1XgBTjU49/) — caption "I make six figures at 26"; spoken audio is a **Korean repost** (wrong-language recycled content).
- 190v · @alinamerkelcoach [DV1qrOnjVr1](https://www.instagram.com/reel/DV1qrOnjVr1/) — "at 15 I moved to another country alone…"
- 345v · @alinamerkelcoach [DV4UQiKjX9i](https://www.instagram.com/reel/DV4UQiKjX9i/)
- The rare exceptions only worked when wrapped in a *tactic* ("I'm a 6-fig owner, steal this template" — the template, not the flex, carried it).

### 2. Generic Motivation — **N=18 · 5% win · 44% flop · median 408 views**
"Stop consuming start creating", "ready is a decision", "mindset/discipline" with no tactic. Lowest win-rate
in the dataset. Nothing to save, nothing to act on.
**Evidence:**
- 194v · @devinjatho [DYPdLGBSCOF](https://www.instagram.com/reel/DYPdLGBSCOF/) — caption "stop consuming, start creating"; spoken open is unrelated filler.
- 2v · @loganforsyth [DXqYX37jQ3f](https://www.instagram.com/reel/DXqYX37jQ3f/) — "ready is not a feeling but a decision" (music-only).
- @loganforsyth's mindset one-liners cluster at the bottom.

---

## Volatile / unreliable (not a clean fail, but don't rely on it)

### Shock / Profanity Interrupt — **N=48 · 27% win · 43% flop** — DOWNGRADED from v2
I previously called this a top pattern off one 3.44%-share hit. The full data corrects that: it **flops more
often than it wins** and has the lowest median share rate (0.17%). It can spike for a brash creator on a big
news beat, but the median reel does 0.90× median. **Use sparingly; never as the default.**
- Spike: 629,687v @devinjatho [DXo0c5bkn53](https://www.instagram.com/reel/DXo0c5bkn53/).
- But 43% of its 48 reels flopped — high variance, not a reliable winner.

---

## Execution failures that sink otherwise-good patterns

| Failure | Evidence | Lesson |
|---------|----------|--------|
| **CTA in the spoken open** | 153v @sam.gaudet [DVmsSneEqPl](https://www.instagram.com/reel/DVmsSneEqPl/) — opened spoken with "Comment 'hook'", no actual hook | The spoken open must hook; the caption carries the CTA. |
| **Bare negative command, no number/payoff** | 283v @sam.gaudet [DWPGIrnyDv1](https://www.instagram.com/reel/DWPGIrnyDv1/) — "No setting will make you go viral" | "Never/Stop" needs a number + a fix (lifts win 28%→46%). |
| **Reposting a winner unchanged** | 322v @devinjatho [DVtNsdyjRJf](https://www.instagram.com/reel/DVtNsdyjRJf/) — verbatim re-cut of his 521K winner | The hook isn't the problem; repeating it is. Rotate, don't recycle. |
| **Foreign-language repost to EN audience** | 208v @alinamerkelcoach [DV1XgBTjU49](https://www.instagram.com/reel/DV1XgBTjU49/) — Korean audio, English caption | Don't recycle another language's winner. |
| **Vague items under a good structure** | numbered-list flop tail (24% flop) | A number/format is not a hook — the items must be specific. |

---

## ⚠️ Don't over-learn from true zeros
Several 0–3 view reels have **strong hooks** (e.g. @iamaayushswamy [DWHac7qDAVd](https://www.instagram.com/reel/DWHac7qDAVd/) — "Why is it so hard to write a good hook? Good thing I have five that rarely fail" → 0v). These read like
**distribution failures (shadowban / brand-new-account window)**, not content failures. When judging flops,
**weight reels with a real view base** (hundreds–thousands) over true zeros — otherwise you'll "learn" the
wrong lesson and kill a hook that actually works.

---

## The one-line test
Before posting: **"What does the viewer DO differently on their next reel because of this — and how fast?"**
If there's no concrete, account-level, fast action, it's a flop risk. Every confirmed winner passes this;
every confirmed killer fails it.

*All figures reproducible: `python research/pattern_analysis.py` (0 API calls).*
