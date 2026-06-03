"""Merge Whisper transcripts into the dataset and emit a spoken-hook analysis digest.

Reads transcripts/<shortcode>.json (real spoken audio) and dataset.json (metrics + captions),
attaches spoken_transcript to every reel, and writes:
  - dataset_spoken.json   : full dataset with spoken_transcript + spoken_hook (first ~2 sentences)
  - spoken-hooks.md       : winners & flops with SPOKEN hook vs CAPTION, divergence flagged
ZERO API calls.
"""
from __future__ import annotations
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRANS = HERE / "transcripts"
ds = json.loads((HERE / "dataset.json").read_text(encoding="utf-8"))


def load_transcript(sc: str) -> str:
    p = TRANS / f"{sc}.json"
    if not p.exists():
        return ""
    try:
        return (json.loads(p.read_text(encoding="utf-8")).get("transcript") or "").strip()
    except Exception:
        return ""


def first_sentences(text: str, n: int = 2, cap: int = 220) -> str:
    if not text:
        return ""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    hook = " ".join(parts[:n]).strip()
    return hook[:cap]


def norm(s: str) -> set:
    return set(re.findall(r"[a-z']+", (s or "").lower()))


def diverges(spoken: str, caption: str) -> bool:
    """True if the spoken hook is materially different from the caption (low word overlap)."""
    a, b = norm(first_sentences(spoken)), norm(caption)
    if not a:
        return False
    if not b:
        return True
    overlap = len(a & b) / len(a)
    return overlap < 0.4


n_with = 0
for acct, a in ds["accounts"].items():
    for bucket in ("winners", "flops"):
        for r in a.get(bucket, []):
            t = load_transcript(r["shortcode"])
            r["spoken_transcript"] = t
            r["spoken_hook"] = first_sentences(t)
            r["caption"] = (r.get("transcript") or "").strip()
            r["hook_diverges"] = diverges(t, r["caption"])
            if t:
                n_with += 1

(HERE / "dataset_spoken.json").write_text(json.dumps(ds, ensure_ascii=False, indent=1), encoding="utf-8")

# Build the human-readable digest
out = ["# Jacky — Spoken-hook analysis (Whisper transcripts)\n",
       f"708/713 reels transcribed via OpenAI Whisper. Below: winners & flops with the **real spoken "
       f"hook** vs the **caption**. ⚡ = spoken hook materially differs from caption (the caption was a "
       f"CTA/label, the spoken line is the actual stop-scroll).\n"]

for acct, a in ds["accounts"].items():
    out.append(f"\n## @{acct} — median {a['median']:,}v")
    out.append("\n### Winners")
    for r in a["winners"][:10]:
        flag = " ⚡" if r["hook_diverges"] else ""
        out.append(f"- **{r['combined_views']:,}v · {r['share_rate']*100:.2f}%sh**{flag} "
                   f"[{r['shortcode']}]({r['link']})")
        out.append(f"  - CAPTION: {r['caption'][:90] or '(none)'}")
        out.append(f"  - SPOKEN : {r['spoken_hook'] or '(no speech)'}")
    out.append("\n### Flops")
    for r in a["flops"][:6]:
        flag = " ⚡" if r["hook_diverges"] else ""
        out.append(f"- **{r['combined_views']:,}v**{flag} [{r['shortcode']}]({r['link']})")
        out.append(f"  - CAPTION: {r['caption'][:90] or '(none)'}")
        out.append(f"  - SPOKEN : {r['spoken_hook'] or '(no speech)'}")

(HERE / "spoken-hooks.md").write_text("\n".join(out), encoding="utf-8")
print(f"merged. reels with spoken transcript (winners+flops): {n_with}")
print("wrote dataset_spoken.json + spoken-hooks.md")
