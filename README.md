# Jacky — Viral Content Playbook

A data-backed playbook for the **content / marketing-for-business-owners** niche on Instagram, built
by scraping 8 creators, classifying ~713 reels as winners vs. flops, transcribing the spoken audio
with Whisper, and distilling the patterns into a reusable strategy reference.

## What's here

```
playbook/        The strategy reference (start here)
  PLAYBOOK.md      Master doc — market state, top winning/anti patterns, specs, format rankings
  what-works.md    Confirmed winning patterns (hooks, formats, triggers)
  what-fails.md    Anti-patterns from the flop set
  hooks.md         Hook patterns ranked S–F, with verbatim SPOKEN-hook templates + evidence
  formats.md       Format rankings + lifecycle
  trends.md        Hot / rising / cooling / dead
  market-cycles.md Per-creator baselines + saturation signals

data/            Evidence appendix — every reel as: metrics · link · transcription
  all-reels.md     All 712 reels, grouped by account, sorted by views
  <account>.md     One file per creator
  formatted.json   Machine-readable version

scripts/         The research toolkit that produced this (Python)
  scrape_jacky.py        Budget-capped Instagram scrape (only /userreels/, hard call cap)
  extract_media_urls.py  Pull free CDN audio/video URLs from cached pages
  transcribe_swarm.py    Whisper transcription (OpenAI API or local faster-whisper)
  merge_transcripts.py   Merge transcripts → spoken-hook analysis
  format_data.py         Emit the metrics/link/transcription records in data/
  build_dataset.py       Classify winners/flops by per-account median
  RESEARCH-NOTES.md      How the run was done + how to re-run
```

## Method (how the playbook was built)

1. **Scrape** 8 creators' last ~90 days of reels via RapidAPI (`/userreels/` only — one payload
   carries views/likes/comments/shares + caption, so no per-reel calls). Budget-capped at 70 total
   calls; raw pages cached so re-runs cost zero.
2. **Classify** each reel by its creator's own **median views**: winner = ≥3× median, flop = <0.5×.
3. **Transcribe** the spoken audio with Whisper using the CDN media URLs already in the cached
   payloads (zero extra scraping cost). 708/713 transcribed.
4. **Analyze** winners vs. flops — and crucially, compare the **spoken hook vs. the caption** (they
   differ on most winners: the caption is the CTA, the spoken open is the real stop-scroll).
5. **Distil** into the 7 playbook files, every claim backed by a quote + metrics + reel link.

## Key finding

**The spoken hook ≠ the caption on most winners.** Captions harvest comments ("Comment GEAR"); the
*spoken first 2 seconds* is the actual hook (a rhetorical question, a shock interrupt, a strip-it-back
reveal). Optimize them as two separate jobs. See `playbook/hooks.md`.

## Data caveats

- ~713 reels, 8 creators, ~90-day window. One account (@iamaayushswamy) is partial (scrape hit the
  budget cap). Two accounts have very low medians — **share rate** is the cleanest cross-account signal.
- **Saves** read 0: the `/userreels/` endpoint doesn't reliably expose save counts.
- No comment-theme data (omitted to protect API budget).
- This is **directional intelligence from a single snapshot**, not gospel. Re-scrape for trend lines.

## Reproducing it

The scripts depend on an external scraper/transcriber module and a RapidAPI key that live **outside
this repo** (read at runtime from a local config — never committed). The scripts are published for
transparency and as a template; running them as-is requires that local setup. See
`scripts/RESEARCH-NOTES.md`. **No API keys or secrets are included in this repository.**

---
*Niche: content/marketing for business owners · Sources: @loganforsyth, @realskytan,
@personalbrandlaunch, @sam.gaudet, @alinamerkelcoach, @bhavinipanjwanii, @devinjatho, @iamaayushswamy*
