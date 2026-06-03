# Jacky — research tooling

Budget-capped Instagram scrape + dataset builder behind Jacky's playbook.

## What's here
- `scrape_jacky.py` — paginates `/userreels/` ONLY (no per-reel calls). Counts every RapidAPI call
  and **hard-stops at `--max-calls`** (default 70). Caches each raw page to `../playbook/.raw/`.
- `build_dataset.py` — classifies reels (winner ≥3× the account's median, flop <0.5×) and writes
  `dataset.json` + `dataset-digest.md`. **Zero API calls.**
- `../playbook/.raw/*.json` — cached raw pages from the 2026-06-03 scrape (70 pages, 8 accounts).
- `../playbook/.raw/_callcount.json` — persisted global call counter.

## The 2026-06-03 run
70/70 RapidAPI calls used (budget cap reached on the 8th account). 713 reels, 8 accounts, ~90d.
`@iamaayushswamy` is partial (cut at the cap); `@loganforsyth` reached ~39d (heavy poster).

## Re-run for FREE (no API calls)
```bash
python build_dataset.py                       # rebuild dataset.json from cache
python scrape_jacky.py --from-cache           # re-summarize from cache
```

## Re-scrape (spends RapidAPI budget — check quota first)
```bash
# resume the saved counter; full 90d per account; stops at 70 total
python scrape_jacky.py --resume --max-calls 70 --since-days 90 --max-pages 18
# finish just the partial account when budget refreshes:
python scrape_jacky.py --accounts iamaayushswamy --max-calls 70 --since-days 90 --max-pages 18
```
Cost ≈ ~1 call per page (~12 reels/page). 8 light-posting accounts over 90d ≈ 40–65 calls.

## Key handling
The RapidAPI key is read at runtime from `…/ai.agents/workflow-agents/scraping agent/config.json`
(`rapidapi_key`). It is never printed or copied into this repo.

## Transcription (v2 — real spoken audio, $0 RapidAPI)
The Instagram CDN audio/video URLs come back **free** in the cached `/userreels/` payloads, so we
Whisper-transcribed the actual spoken audio without spending any RapidAPI budget.
- `extract_media_urls.py` → `media_urls.json` (audio/video URLs from `.raw/` cache). **URLs expire in
  hours** — re-run this right before transcribing.
- `transcribe_swarm.py` → `transcripts/<shortcode>.json` (one per reel; resumable, crash-safe).
  - `--engine api` (OpenAI Whisper, needs `OPENAI_API_KEY` w/ quota) — ~10 min for 713 via threads.
  - `--engine local` (faster-whisper, CPU, $0) — ~60–90 min; auto-fallback if the API is out of quota.
  - `--only winners,flops` to limit scope; `--retry-empty` to redo music-only/expired ones.
- `merge_transcripts.py` → `dataset_spoken.json` + `spoken-hooks.md` (spoken hook vs caption, ⚡=diverges).

### Re-run transcription (free)
```bash
python extract_media_urls.py                       # refresh URLs from cache (0 API calls)
python transcribe_swarm.py --engine api --workers 12 --model base   # or --engine local for $0
python merge_transcripts.py                         # rebuild spoken dataset + digest
```
The 2026-06-03 run: 708/713 transcribed (5 music-only), 10.2 min, ~$2–3 OpenAI, $0 RapidAPI.

## Known limitations (reflected in the playbook caveats)
- ~~captions only~~ ✅ v2 has **708 real spoken transcripts** (Whisper).
- **No comment data** (`/postcomments/` skipped to protect budget).
- Two accounts have very low medians → use **share rate** as the cross-account signal, not raw views.
- `@iamaayushswamy` partial (budget cap) — finish at full 90d when quota refreshes.
