# hooks.md — Jacky Hook Pattern Playbook

**Niche:** Content / Marketing / Social-Media-Growth for Business Owners
**Last Updated:** 2026-06-03 (v3 — **systematic, evidence-ranked**: every pattern classified across all
712 reels, ranked by consistency, every reel cited)
**Data Sources:** @loganforsyth, @realskytan, @personalbrandlaunch, @sam.gaudet, @alinamerkelcoach, @bhavinipanjwanii, @devinjatho, @iamaayushswamy
**Method:** Every reel's **spoken hook** (Whisper) + caption run through deterministic detectors. Each
pattern is scored on how *consistently* it wins, not on its single biggest hit. Full per-reel evidence:
[`research/pattern-report.md`](../research/pattern-report.md) · machine data: `research/pattern-stats.json`.

---

## How patterns are ranked (read this first)

A pattern is **PROVEN** when it wins *consistently across many videos* — high win-rate **and** low
flop-rate **and** a real sample size (N). A single viral video does **not** prove a hook. We measure:

- **N** = how many reels used the pattern (sample size)
- **Win% / Flop%** = share of those reels that beat 3× / fell below 0.5× their creator's median
- **Median mult** = the *typical* multiple of median (not the best one — the middle one)
- **Creators** = how many of the 8 accounts it shows up on (breadth)
- **Tier** is assigned from this, with small-N patterns explicitly capped as "Promising, not proven."

> **Winner/mid/flop** is judged against **each account's own median views** — so a small account and a
> large one are compared fairly. **Share rate** (shares/views) is the cleanest cross-account signal.

## Master ranking table (all hook patterns)

| Tier | Pattern | N | Creators | Win% | Flop% | Median mult | Median share% | Verdict |
|------|---------|---|----------|------|-------|-------------|---------------|---------|
| **S** | Outcome + time-box | 16 | 4 | **56%** | **6%** | 4.06× | 1.23% | Proven — best win/flop ratio in the set |
| **A** | Comment-keyword CTA *(caption layer)* | 180 | 6 | 28% | 17% | 1.37× | 0.81% | Proven at scale — most-used, reliably positive |
| **A** | Rhetorical-question open | 123 | 8 | 25% | 20% | 1.04× | 0.37% | Proven & universal — every creator, big sample |
| **A** | Save / "steal this" command | 15 | 4 | **46%** | 20% | 2.22× | 1.01% | Proven — strong win-rate, decent N |
| **B+** | Numbered list ("N things/steps") | 57 | 7 | 26% | 24% | 0.86× | 0.50% | Proven-broad but average — execution-dependent |
| **B+** | Negative command ("Never/Stop…") | 74 | 8 | 28% | 31% | 1.10× | 0.43% | High ceiling, **high flop** — needs the number |
| **B** | Negative command **+ number** | 13 | 4 | **46%** | 30% | 1.72× | 0.72% | The fix for the above — but small N |
| **B** | A/B comparison ("which did better?") | 64 | 5 | 23% | 21% | 1.00× | 0.59% | Reliable-average; a few huge hits |
| **B** | Strip-it-back / reframe | 12 | 5 | 41% | 25% | 1.12× | 0.21% | Good win-rate, small N |
| **C↑** | Feature/update news | 11 | 3 | **66%** | 25% | typ. mid | 1.65% | ⚠️ Promising — tiny N (11), 3 creators |
| **C↑** | "You'll never go viral if…" | 6 | 3 | **83%** | 16% | — | 0.31% | ⚠️ Mostly **1 creator reposting 1 line** — see below |
| **C↓** | Shock / profanity interrupt | 48 | 6 | 27% | **43%** | 0.90× | 0.17% | ⚠️ Volatile — flops as often as wins |

---

## The patterns, with FULL evidence

### S-TIER

#### 1. Outcome + Time-Box — *"[result] in [time], with [effort]"*
**N=16 · 4 creators · 56% win · 6% flop · typical 4.06× median.** The most *consistent* winner in the
dataset: more than half its reels beat 3× median and almost none flopped. Pairs a concrete result with
an explicit speed/effort frame.

**Templates (verbatim from winners):**
```
"This is the fastest way to [result] with no extra effort. Explained in under 30 seconds."
"If I wanted to reach [goal] in the next 30 days, these are the only [N] things I'd focus on…"
"How do you [outcome] in [60 minutes / 30 days]? Step one…"
"Let's plan your next 30 days of content in 30 minutes. It's called the [named] strategy."
```
**Evidence (all 16 reels in `pattern-report.md`; representative spread):**
- 220,761v · winner · @iamaayushswamy [DXPlUuDDNTk](https://www.instagram.com/reel/DXPlUuDDNTk/) — *"the fastest way to double your views… in under 30 seconds."*
- 35,590v · winner · @realskytan [DYOLB7BCSC3](https://www.instagram.com/reel/DYOLB7BCSC3/) — *"plan your next 30 days of content in 30 minutes — the 7-4 strategy."*
- 31,186v · winner · @alinamerkelcoach [DY8LM_NtVoF](https://www.instagram.com/reel/DY8LM_NtVoF/) — *"10 hooks that always work…"*
- 13,751v · winner · @iamaayushswamy [DYf-dKgsCNm](https://www.instagram.com/reel/DYf-dKgsCNm/) — *"reach 10K followers in the next 30 days, the only two things I'd focus on."*
- 133,638v · mid · @personalbrandlaunch [DX9Sj-HO89h](https://www.instagram.com/reel/DX9Sj-HO89h/) — *"a month of content ideas in 60 minutes."*
- (only flop: 2v · @iamaayushswamy [DWUSmz0jNHH](https://www.instagram.com/reel/DWUSmz0jNHH/) — a 0-view/distribution failure, not a hook failure.)
**Why it's #1:** works for 4 different creators, large *and* tiny accounts, with the lowest flop-rate. This is the one to copy first.

---

### A-TIER (proven, reliable)

#### 2. Comment-Keyword CTA — *caption layer, not a spoken hook*
**N=180 · 6 creators · 28% win · 17% flop.** The most-used mechanic in the niche and reliably net-positive
(wins 1.6× as often as it flops, across 180 reels). **Important:** this is a **caption/CTA layer** that
rides on top of a spoken hook — it is *not itself the stop-scroll*. The biggest hits pair it with a
strong spoken open and waste none of the spoken line on the CTA.
**Evidence (180 reels; top + the lesson):**
- 4,686,071v · winner · @devinjatho [DXsJznEEsHp](https://www.instagram.com/reel/DXsJznEEsHp/) — caption "Comment GEAR", spoken hook is the strip-back reveal.
- 1,720,374v · winner · @personalbrandlaunch [DWBm-iAlZb4](https://www.instagram.com/reel/DWBm-iAlZb4/)
- 900,041v · winner · @alinamerkelcoach [DXMU-n7tGgR](https://www.instagram.com/reel/DXMU-n7tGgR/)
- **Lesson reel:** 153v · flop · @sam.gaudet [DVmsSneEqPl](https://www.instagram.com/reel/DVmsSneEqPl/) — "Comment 'hook'" on a flat spoken open. **The CTA can't save a weak hook.**

#### 3. Rhetorical-Question Open
**N=123 · ALL 8 creators · 25% win · 20% flop.** The most *universal* hook — every creator uses it, large
sample, net-positive. Open by asking the exact question the viewer wants answered, then answer fast.
**Templates:**
```
"How would you [achieve X] if you had to? Step one…"
"What's the [name] rule? [Immediate answer]."
"Is it still worth it to [common decision]? [Contrarian answer]."
"Did you know [surprising fact]?"
```
**Evidence (123 reels; spread across creators):**
- 2,215,348v · winner · @sam.gaudet [DV3n5CvEjNQ](https://www.instagram.com/reel/DV3n5CvEjNQ/) — *"If I wanted to go from 0 to $1M with AI, what should I do?"*
- 427,550v · winner · @personalbrandlaunch [DWUYjHal4XN](https://www.instagram.com/reel/DWUYjHal4XN/) — *"If you had to go from 0 to a million followers in 6 months, how would you do it?"*
- 156,928v · winner · @sam.gaudet [DXsI2HIDLys](https://www.instagram.com/reel/DXsI2HIDLys/) — *"What's the $50 to fix it rule?"*
- 28,087v · winner · @iamaayushswamy [DXacxAyCalY](https://www.instagram.com/reel/DXacxAyCalY/) — *"Posting 3× a day vs 3× a week — which grows faster?"*
- Flops exist too (20%) — generic questions ("want more views?") underperform. Specificity decides it.

#### 4. Save / "Steal This" Command
**N=15 · 4 creators · 46% win · 20% flop · typical 2.22× median.** A direct save/steal command tied to a
concrete asset. Strong win-rate on a respectable sample.
**Evidence (15 reels):**
- 1,278,571v · winner · @devinjatho [DX0M0rOyEwI](https://www.instagram.com/reel/DX0M0rOyEwI/) — "save this before posting" + 5 settings.
- 768,857v · winner · @bhavinipanjwanii [DYRa7qQqtSc](https://www.instagram.com/reel/DYRa7qQqtSc/) — "save this video so you never make that mistake."
- 311,153v · winner · @bhavinipanjwanii [DY4p39tskeY](https://www.instagram.com/reel/DY4p39tskeY/)
- 131,109v · winner · @alinamerkelcoach [DXci7n2tu8x](https://www.instagram.com/reel/DXci7n2tu8x/) — "delete your highlights if they look like this."

---

### B-TIER (works, but execution-dependent)

#### 5. Numbered List — N=57 · 7 creators · 26% win · 24% flop
Broad and frequently used, but **average** — wins and flops nearly balance. The number sets expectation;
what decides it is whether the items are genuinely specific. Best fused with a negative command (#7) or a save (#4).
- Wins: 304,477v @personalbrandlaunch [DVq-bkuAEPw](https://www.instagram.com/reel/DVq-bkuAEPw/); 1,278,571v @devinjatho [DX0M0rOyEwI](https://www.instagram.com/reel/DX0M0rOyEwI/).
- Flops: generic lists with vague items (24% flop rate). A number alone is not a hook.

#### 6. Negative Command — N=74 · 8 creators · 28% win · **31% flop**
"Never/Stop…" has a **high ceiling but the highest flop-rate of the broad patterns.** On its own it's a
coin-flip-plus. It becomes reliable when paired with a number (see #7).
- Win: 1,278,571v @devinjatho [DX0M0rOyEwI](https://www.instagram.com/reel/DX0M0rOyEwI/) — *"Never post until you fix these five settings."*
- Flop: 283v @sam.gaudet [DWPGIrnyDv1](https://www.instagram.com/reel/DWPGIrnyDv1/) — *"No setting will make you go viral"* (negative with no payoff).

#### 7. Negative Command **+ Number** — N=13 · 4 creators · **46% win** · 30% flop
The upgrade to #6: the prohibition + a finite numbered fix nearly doubles the win-rate (28%→46%). Smaller
sample, so B not A, but the mechanism is clear and reused successfully across 4 creators.
- 1,278,571v @devinjatho [DX0M0rOyEwI](https://www.instagram.com/reel/DX0M0rOyEwI/) · 433,179v @devinjatho [DX0MuRvSFV2](https://www.instagram.com/reel/DX0MuRvSFV2/) · 21,370v @iamaayushswamy [DW5DTTQDHWX](https://www.instagram.com/reel/DW5DTTQDHWX/) — *"Never turn on these three settings."*

#### 8. A/B Comparison — N=64 · 5 creators · 23% win · 21% flop
"Which did better, A or B?" / "vs". Reliable average with occasional huge hits; forces a guess-comment.
- Wins: 558,649v @personalbrandlaunch [DWE72LsIGQy](https://www.instagram.com/reel/DWE72LsIGQy/); 243,264v @sam.gaudet [DYdEfR1oCGg](https://www.instagram.com/reel/DYdEfR1oCGg/) ("CASH or PASS").
- Flop: 745v @realskytan [DY27u2qJVNK](https://www.instagram.com/reel/DY27u2qJVNK/) — same format, small account, no payoff. Execution + reach decide it.

#### 9. Strip-It-Back / Reframe — N=12 · 5 creators · 41% win · 25% flop
Remove what everyone assumes matters to prove what actually does. Good win-rate, small N → B.
- 4,686,071v @devinjatho [DXsJznEEsHp](https://www.instagram.com/reel/DXsJznEEsHp/) — *"If I take off all my clothes, remove this background…"*
- 231,699v @personalbrandlaunch [DW6QSgcFCYL](https://www.instagram.com/reel/DW6QSgcFCYL/) — *"No matter the niche… it's always the clone format."*

---

### ⚠️ C-TIER — PROMISING BUT NOT PROVEN (small N or single-creator)

These have eye-catching win-rates but **do not yet clear the bar** — exactly the "one video got views so I
called it a winner" trap. Treat as experiments, not rules.

#### Feature/Update News — N=11 · 3 creators · 66% win
High win-rate, but only **11 reels across 3 creators**, and the format is **time-sensitive** (it only
works the week a feature ships). Promising and worth testing on every real IG update, but N is too small to
call proven. *Also note:* these double as the highest share-rate reels (1.65% median) — when they hit, they
travel. All 11: see `pattern-report.md`. Wins incl. 629,687v @devinjatho [DXo0c5bkn53](https://www.instagram.com/reel/DXo0c5bkn53/), 277,926v @alinamerkelcoach [DWq2mazNwlP](https://www.instagram.com/reel/DWq2mazNwlP/), 120,998v @iamaayushswamy [DWXjctoiQ-W](https://www.instagram.com/reel/DWXjctoiQ-W/).

#### "You'll Never Go Viral If…" — N=6 · 83% win — **but it's basically one creator, one line, reposted**
This is the clearest example of why raw win-rate lies. 5 of the 6 wins are **@devinjatho reposting the
*identical* hook** *"You will never go viral if you don't learn how to speak on camera"* (2.15M, then
326K/129K/121K on re-uploads), plus 1 win from @iamaayushswamy on a different line, and 1 flop from
@alinamerkelcoach. So it's **proven for that one creator's one line** — strong evidence the line works, but
**not** a broadly validated pattern across the niche. Worth adapting; don't treat the 83% as portable.
Reels: [DY5rxTQSxLy](https://www.instagram.com/reel/DY5rxTQSxLy/), [DZD6ivySIP0](https://www.instagram.com/reel/DZD6ivySIP0/), [DZD6v0HyxSQ](https://www.instagram.com/reel/DZD6v0HyxSQ/), [DZECbQvy7q7](https://www.instagram.com/reel/DZECbQvy7q7/), [DYZiOoZMqsY](https://www.instagram.com/reel/DYZiOoZMqsY/) (win), [DWgjd1AjUMr](https://www.instagram.com/reel/DWgjd1AjUMr/) (flop).

#### Shock / Profanity Interrupt — N=48 · 6 creators · 27% win · **43% flop** — DOWNGRADED
I previously over-ranked this off one 3.44%-share hit. The full data says it **flops more often than it
wins (43% vs 27%)** and has the *lowest* median share rate (0.17%). It can spike (devinjatho's cheat-code
reels), but it is **volatile, not reliable**, and brand-dependent. Use sparingly, never as the default.
- Spikes: 629,687v @devinjatho [DXo0c5bkn53](https://www.instagram.com/reel/DXo0c5bkn53/).
- But 43% of its 48 reels flopped — the median reel does 0.90× (below median).

---

## F-TIER — AVOID (see what-fails.md for full evidence)
- **Personal flex** — N=16 · **6% win · 68% flop** · median 0.31×. The single worst pattern.
- **Generic motivation** — N=18 · **5% win · 44% flop** · median 408 views.

---

## What to actually do (ranked by the data)
1. **Lead with Outcome + Time-Box** (S, 56% win) — your highest-probability hook.
2. **Default to Rhetorical-Question opens** (A, universal) for everyday content.
3. **Add a Save command** (A, 46% win) to any tactical/list reel.
4. **If using "Never/Stop", always attach a number** (lifts 28%→46% win).
5. **Layer Comment-Keyword CTA in the caption** — never in the spoken open.
6. **Test Feature-News the week IG ships anything** (promising, time-boxed).
7. **Avoid** personal flexes, generic motivation, and shock-for-shock's-sake.

*Every number here is reproducible from `research/pattern_analysis.py` over the cached data — 0 API calls.*
