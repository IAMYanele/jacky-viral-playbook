"""Swarm transcription of cached reels. ZERO RapidAPI calls (uses CDN media URLs from cache).

Parallelizes across processes (faster-whisper isn't thread-safe, but each worker process loads its
own model). Downloads each reel's audio/video from the signed Instagram CDN URL and transcribes with
faster-whisper. Writes one JSON per reel to transcripts/ so the run is resumable and crash-safe —
re-running skips reels already done.

Usage:
  python transcribe_swarm.py --workers 6 --model base            # all reels with a URL
  python transcribe_swarm.py --workers 6 --model base --only winners,flops
  python transcribe_swarm.py --retry-empty                       # re-do only the empties
"""
from __future__ import annotations
import argparse, json, sys, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "transcripts"
OUT.mkdir(exist_ok=True)
SHARED = r"C:/Users/yanel/Documents/ai.agents/workflow-agents/shared"


def worker(task: dict) -> dict:
    """Transcribe one reel. engine='api' -> OpenAI Whisper (I/O-bound, high concurrency ok);
    engine='local' -> faster-whisper (CPU, each process loads its own model)."""
    sys.path.insert(0, SHARED)
    import logging
    logging.disable(logging.WARNING)
    sc = task["shortcode"]
    t0 = time.time()
    txt = ""
    url = task.get("audio_url") or task.get("video_url") or ""
    try:
        if task["engine"] == "api":
            import transcriber as T  # OpenAI-first, auto local fallback
            txt = T.transcribe_audio_url(url, model_size=task["model"], task="transcribe") or ""
        else:
            import transcriber_local as T
            txt = T.transcribe_reel(None, task.get("audio_url") or None,
                                    task.get("video_url") or None, model_size=task["model"]) or ""
    except Exception as e:
        txt = ""
        task["error"] = str(e)[:160]
    rec = {"shortcode": sc, "account": task["account"], "views": task["views"],
           "link": task["link"], "transcript": txt, "chars": len(txt),
           "secs": round(time.time() - t0, 1), "error": task.get("error", "")}
    (OUT / f"{sc}.json").write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")
    return {"shortcode": sc, "chars": len(txt), "secs": rec["secs"]}


def load_targets(only: str | None) -> list[dict]:
    urls = json.load(open(HERE / "media_urls.json", encoding="utf-8"))
    select = None
    if only:
        ds = json.load(open(HERE / "dataset.json", encoding="utf-8"))
        select = set()
        want = set(only.split(","))
        for a in ds["accounts"].values():
            if "winners" in want:
                select |= {r["shortcode"] for r in a["winners"]}
            if "flops" in want:
                select |= {r["shortcode"] for r in a["flops"]}
    tasks = []
    for sc, r in urls.items():
        if select is not None and sc not in select:
            continue
        if not (r.get("audio_url") or r.get("video_url")):
            continue
        tasks.append(r)
    return tasks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--model", default="base")
    ap.add_argument("--engine", choices=["api", "local"], default="api",
                    help="api = OpenAI Whisper (fast, I/O-bound); local = faster-whisper (CPU)")
    ap.add_argument("--only", default="", help="subset: winners,flops (default = all)")
    ap.add_argument("--retry-empty", action="store_true")
    args = ap.parse_args()

    tasks = load_targets(args.only or None)
    for t in tasks:
        t["model"] = args.model
        t["engine"] = args.engine

    # resume: skip reels already transcribed (non-empty), unless retry-empty
    done_ok, redo = set(), set()
    for f in OUT.glob("*.json"):
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if rec.get("chars", 0) > 0:
            done_ok.add(rec["shortcode"])
        else:
            redo.add(rec["shortcode"])

    if args.retry_empty:
        tasks = [t for t in tasks if t["shortcode"] in redo]
    else:
        tasks = [t for t in tasks if t["shortcode"] not in done_ok]

    total = len(tasks)
    print(f"swarm: {total} reels to do | {len(done_ok)} already done | "
          f"{args.workers} workers | engine={args.engine} | model={args.model}", flush=True)
    if not total:
        print("nothing to do."); return

    # API = network/IO bound -> threads (lighter, no model reload). Local = CPU -> processes.
    Executor = ThreadPoolExecutor if args.engine == "api" else ProcessPoolExecutor
    t0 = time.time()
    done = empties = 0
    with Executor(max_workers=args.workers) as ex:
        futs = [ex.submit(worker, t) for t in tasks]
        for fut in as_completed(futs):
            r = fut.result()
            done += 1
            if r["chars"] == 0:
                empties += 1
            if done % 10 == 0 or done == total:
                el = time.time() - t0
                rate = el / done
                eta = (total - done) * rate
                print(f"  {done}/{total} | {empties} empty | "
                      f"{el/60:.1f}min elapsed | ETA {eta/60:.1f}min", flush=True)

    print(f"\nDONE: {done} reels, {empties} empty, {(time.time()-t0)/60:.1f} min total", flush=True)
    print(f"transcripts in: {OUT}")


if __name__ == "__main__":
    main()
