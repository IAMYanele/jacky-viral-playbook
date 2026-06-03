"""Extract audio/video CDN URLs from cached /userreels/ pages. ZERO API calls.

These signed Instagram CDN URLs come back in the raw reel payload (no extra RapidAPI cost) but
EXPIRE within hours. Emits media_urls.json mapping shortcode -> {audio_url, video_url, views, ...}
so we can download + Whisper-transcribe the ones we care about.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path

WF = Path(r"C:/Users/yanel/Documents/ai.agents/workflow-agents")
sys.path.insert(0, str(WF / "shared"))
from scraper import parse_reel, extract_audio_url, extract_video_url, _extract_items  # noqa

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "playbook" / ".raw"
SINCE = int(time.time()) - 90 * 86400

rows = {}
have_audio = have_video = 0
for pg in sorted(RAW.glob("*-p*.json")):
    acct = pg.name.split("-p")[0]
    data = json.loads(pg.read_text(encoding="utf-8"))
    for it in _extract_items(data):
        node = it.get("node", it) if isinstance(it, dict) else it
        r = parse_reel(it)
        sc = r["shortcode"]
        if not sc or r["taken_at"] < SINCE or sc in rows:
            continue
        a = extract_audio_url(node) or extract_audio_url(it)
        v = extract_video_url(node) or extract_video_url(it)
        if a: have_audio += 1
        if v: have_video += 1
        rows[sc] = {
            "account": acct, "shortcode": sc, "views": r["combined_views"],
            "shares": r["shares"], "link": r["link"],
            "audio_url": a or "", "video_url": v or "", "caption": (r["transcript"] or "")[:120],
        }

(HERE / "media_urls.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"reels: {len(rows)} | with audio_url: {have_audio} | with video_url: {have_video}")
# show a couple sample URL hosts (not full signed URLs)
import urllib.parse as up
hosts = set()
for r in rows.values():
    for u in (r["audio_url"], r["video_url"]):
        if u:
            hosts.add(up.urlparse(u).netloc)
print("CDN hosts:", sorted(hosts)[:5])
