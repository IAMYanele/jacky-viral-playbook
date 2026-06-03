# PLAYBOOK.md — Jacky (Content/Marketing for Business Owners)
*Last updated: 2026-06-03 (v3 — systematic, evidence-ranked) | Master reference document*

> ⚠️ **Data Caveat & Method:** Built from **712 reels across 8 creators**, last ~90 days
> (@iamaayushswamy partial — scrape hit the API budget cap at 70 calls). **v3: every reel is classified
> by its spoken hook (Whisper) + caption, and every pattern is ranked by how *consistently* it wins —
> win-rate + flop-rate across a real sample — NOT by its single biggest hit.** A lone viral video does
> not make a "proven" pattern; small-N patterns are flagged "promising, not proven." Winner/mid/flop is
> judged vs **each creator's own median** (winner ≥3×, flop <0.5×). **Key insight the captions hid: the
> spoken hook ≠ the caption on most winners** (caption = CTA layer, spoken open = the real stop-scroll).
> Two low-median accounts inflate multipliers → **share rate** is the safer cross-account signal. No
> comment-theme data (budget). **Full per-reel evidence for every claim:**
> [`research/pattern-report.md`](../research/pattern-report.md) — reproducible via
> `python research/pattern_analysis.py` (0 API calls).

---

## 1. Current State of the Market

This is the **"grow your business with content / social-media-marketing education"** niche — creators
teaching business owners how to get views, followers, and leads on Instagram. It is an **active,
lead-gen-driven niche** where the content itself is a funnel: the best-performing posts don't just
teach, they **trade a tactic for a comment** (the comment triggers an automated DM with a free
resource). Median views vary wildly by account (265 to 74,025), but the *pattern* of what wins is
remarkably consistent across all 8 creators: **specific, tactical, save-able Instagram/algorithm
tips delivered fast, with a comment-to-DM call to action.** Generic motivation and personal-journey
brags reliably flop.

---

## 2. Top Winning SPOKEN HOOKS — first 5 seconds, ranked by *consistency*

> The hook = **what's spoken in the first ~5 seconds** (captions excluded). Ranked by win-rate + flop-rate
> across all reels using it (N), not by one viral example. Full breakdown + every cited reel in `hooks.md`
> and [`research/pattern-report-v4.md`](../research/pattern-report-v4.md). (Win/Flop = vs each creator's own median.)

| Rank | Spoken hook (0–5s) | N | Creators | Win% | Flop% | Med mult | Why it's ranked here |
|------|--------------------|---|----------|------|-------|----------|----------------------|
| 1 | **Outcome + time-box** ("[result] in 30 days / under 30s") | 13 | 4 | **69%** | **0%** | 6.65× | Best ratio in the set — zero flops; works on tiny & mid accounts |
| 2 | **Rhetorical-question open** | 106 | **8** | 29% | 18% | 1.07× | Only hook used by ALL 8 creators; the universal safe default |
| 3 | **Negative command** ("Never/Stop…") | 55 | 7 | 27% | 36% | 0.96× | Broad & high-ceiling, but **high flop** — needs a number |
| 4 | **Numbered list** spoken ("5 things…") | 40 | 7 | 17% | 27% | 0.76× | Broad but below-average alone — items must be specific |
| 5 | **Shock / profanity interrupt** | 20 | 5 | 40% | 40% | 0.85× | Volatile — wins and flops equally; brand-dependent |

**⚠️ Promising but NOT proven** (high win-rate, small/narrow sample — don't treat as the above):
*Feature-news* 72% win but N=11/3 creators & time-locked. *Neg-command+number* 55% win, N=9 (the fix for
plain "Never"). *Strip-back reframe* 62% win, N=8 (half is one creator's one line). *A/B* 43% win but only
2 creators. *"You'll never go viral if…"* 83% win but it's essentially **one creator reposting one line.**

> **Not hooks:** **comment-keyword CTA** (N=180) is a *caption mechanic*, not a spoken hook — it rides on
> top of a hook and is reported separately (it can't save a weak opener). **"Save/steal this"** is almost
> always in the caption too (only N=2 spoken). Both were wrongly counted as hooks in earlier versions.

---

## 3. Top 5 Anti-Patterns

> Run every piece against this before posting.

| # | Anti-Pattern | Why It Kills Reach |
|---|-------------|-------------------|
| 1 | **Personal flex / journey brag** ("I make six figures at 26", "traveled to 43 countries") | @alinamerkelcoach's worst flops (190–510 views) vs her 1.3M tactical winner. Owners don't follow you for *your* life; they follow for *their* result. |
| 2 | **Reposting the same winner too often** | @devinjatho's "Comment GEAR" hit 4.7M, but later re-posts of the same reel cratered (194–322 views). The algorithm and audience fatigue fast. |
| 3 | **Generic motivation / mindset one-liners** ("stop consuming, start creating", "ready is a decision") | @devinjatho 194v, @loganforsyth flops. No tactic, no specificity, no reason to save. |
| 4 | **Vague "Breaking news" with no concrete payoff** | @loganforsyth's repeated "Breaking:" posts flopped (0–3 views) when the news wasn't actionable for the viewer's own account. |
| 5 | **Lead-magnet CTA on content nobody watched** | @sam.gaudet "Comment 'hook' for my hook bank" → 153 views. The CTA only works *after* the tip earns the watch; CTA-first with a weak hook dies. |

---

## 4. Optimal Technical Specs

| Spec | Recommendation | Notes |
|------|---------------|-------|
| **Duration** | 15–40 seconds | Tactical tips and list formats; long enough to deliver the fix, short enough to rewatch. |
| **Hook window** | First 1–2 seconds | Lead with the specific outcome or the number ("Fix these 5…", "Comment GEAR for…"). No throat-clearing. |
| **On-screen text** | Always — bold tactic/number up top | Most winners pair a spoken/visual hook with large on-screen text stating the tactic. Save-able = readable. |
| **CTA** | Comment-keyword → DM the resource | The dominant conversion mechanic in this niche. Put the keyword in caption AND on screen. |
| **"Save this" prompt** | Add it to tactical posts | Saves correlate with reach here ("Save this before posting"). Explicitly ask. |
| **Posting cadence** | Daily-ish, but **don't repost winners back-to-back** | Heavy posters (@sam.gaudet, @personalbrandlaunch) sustain reach; repost fatigue is real (see anti-pattern 2). |
| **Production** | Low — talking head / screen-record | Creator + screen recording of the actual setting/tactic outperforms high production. The *information* is the product. |

---

## 5. Emotional Playbook

### ✅ Triggers That Work

| Trigger | How to Use It |
|---------|--------------|
| **Curiosity / open loop** | "Which video did better?" / "You'll never go viral if…" — withhold the answer to drive watch-through + comments. |
| **Control / agency** | "Fix these 5 settings" — give owners a lever they can pull *today* on their own account. |
| **FOMO / novelty** | "New IG update" — frame a feature as an edge they're missing right now. |
| **Aspiration + specificity** | "5 steps to make $1M with AI" — big outcome anchored to a concrete, numbered path. |
| **Reciprocity** | "Comment WORD and I'll send you…" — the free resource feels like a gift, lowering the ask of commenting. |

### ❌ Triggers to Avoid

| Trigger | Why |
|---------|-----|
| **Self-aggrandizement** | Personal income/lifestyle flexes flop hard here — the audience is outcome-selfish. |
| **Vague inspiration** | "Stop consuming, start creating" has no tactic to save or act on. |
| **Manufactured urgency with no payoff** | "Breaking news" that doesn't change what the viewer should *do* gets ignored. |

### Audience Psychology
This audience is **business owners and aspiring creators who want results on their own account, fast.**
They are tactic-hungry and skeptical of fluff. They reward content that hands them a **specific,
implementable lever** (a setting, a prompt, a template, an update) and that makes the next step
frictionless (comment a word, get the thing). They do **not** care about the creator's personal
success unless it's immediately transferable to *them*. Every winning post answers "what do I do
differently on my next reel?" — and offers to hand over the tool.

---

## 6. Format Rankings

| Tier | Format | Status |
|------|--------|--------|
| ⭐⭐⭐ **Top** | Lead-magnet tactical tip ("Comment WORD for the [list/prompt/template]") | Peak — dominates winners, but watch for keyword-CTA fatigue |
| ⭐⭐⭐ **Top** | Numbered "Fix these N settings/things" + "Save this" | Rising — high save signal, evergreen |
| ⭐⭐ **Strong** | IG feature / algorithm-update news | Rising — recurring big hits, time-sensitive |
| ⭐⭐ **Strong** | A/B comparison / "which did better?" curiosity | Stable — reliable mid-to-high performer |
| ⭐⭐ **Strong** | AI-tool / "make $X with AI" big-outcome how-to | Rising — rides the AI trend |
| ⭐ **Weak** | Personal journey / income flex | Declining — consistent flop |
| ⭐ **Weak/Dead** | Generic motivational one-liner | Dead for this niche |

---

## 7. What's Trending vs. What's Dying

| 🟢 Trending | 🔴 Dying |
|------------|---------|
| Comment-to-DM lead-magnet tips | Personal "I made $200k at 26" flexes |
| "Fix these N settings" + Save this | Generic motivation ("ready is a decision") |
| Instagram feature/update breakdowns | Reposting the same winning reel repeatedly |
| AI tools / AI-money angles | Vague "Breaking news" with no actionable payoff |
| A/B "which did better?" curiosity loops | CTA-first posts with weak hooks |
| Numbered, specific, save-able tactics | Aspirational fluff with no tactic |

---

*Next review trigger: re-scrape when budget refreshes (full 90d on @iamaayushswamy + @loganforsyth at
higher page caps), or when a new pattern appears in 3+ creators. Upgrade EMERGING → CONFIRMED at 3+
posts. Add comment-theme analysis if budget allows /postcomments/.*
