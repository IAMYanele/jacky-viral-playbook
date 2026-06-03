"""Build hooks.md in the swipe-file format (hook -> format -> evidence links), Jacky data only.

Mirrors the STRUCTURE of the reference Google Doc (category > hook template > the source links that
follow that hook), but uses ONLY our scraped Jacky reels. Each pattern = one "hook structure":
  - the HOOK (a template abstracted from the real spoken openers)
  - the FORMAT (how the hook is built + how it performs, with the stats)
  - the EVIDENCE (every reel that used it, linked, with its real 0-5s spoken hook)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
groups = json.loads((HERE / "hook_groups.json").read_text(encoding="utf-8"))


def stats(rs):
    n = len(rs)
    w = sum(1 for r in rs if r["cls"] == "winner")
    f = sum(1 for r in rs if r["cls"] == "flop")
    cr = len({r["a"] for r in rs})
    import statistics as st
    mm = round(st.median([r["mult"] for r in rs]), 1)
    return n, cr, w, f, round(w / n * 100), round(f / n * 100), mm


def link(r):
    return f"https://www.instagram.com/reel/{r['sc']}/"


# (key, CATEGORY title, tier, the abstracted hook templates, the format text)
SPEC = [
    ("outcome_timebox", "OUTCOME + TIME-BOX", "S — PROVEN (best ratio, zero flops)",
     ['This is the fastest way to (insert result) with no extra effort.',
      'If I wanted to (insert dream result) in the next 30 days, these are the only (insert #) things I’d focus on.',
      'How do you (insert outcome) in 60 minutes? Step one…',
      'Let’s plan your next 30 days of (insert thing) in 30 minutes.'],
     "A concrete result wrapped in an explicit speed/effort frame, said in the first 5 seconds. The viewer "
     "is told the payoff is fast and low-effort before they decide to scroll. Lead with the outcome, then "
     "the time box, then deliver."),
    ("rhetorical_question", "RHETORICAL QUESTION", "A — PROVEN (universal, all 8 creators)",
     ['How would you (insert goal) if you had to?',
      'What’s the (insert name) rule?',
      'Is it still worth it to (insert common decision)?',
      'Did you know (insert surprising fact)?',
      'Which grows faster — (insert A) or (insert B)?'],
     "Open by asking the exact question the viewer wants answered, then answer it fast. The question itself "
     "is the hook. Specificity decides it — a precise, high-stakes question wins; a generic one ('want more "
     "views?') is where this flops."),
    ("negcmd_number", "NEGATIVE COMMAND + NUMBER", "A — the fix for a bare 'Never' (small N)",
     ['Never (insert action) until you fix these (insert #) (insert thing).',
      'Never turn on these (insert #) (insert settings).',
      'Stop doing these (insert #) things if you want (insert result).'],
     "A prohibition fused with a finite number. The number makes it concrete and save-able. Adding the "
     "number lifts a bare 'Never/Stop' from 27% to 55% win — always attach the count."),
    ("negative_command", "NEGATIVE COMMAND", "B — high ceiling, high flop (needs a number)",
     ['Never (insert action).',
      'Stop (insert action) if you want (insert result).',
      'Don’t (insert action) until you (insert fix).'],
     "A prohibition that triggers loss-aversion. High ceiling but the highest flop-rate of the broad hooks "
     "on its own — it only becomes reliable when you attach a number and a payoff (see above)."),
    ("numbered_list", "NUMBERED LIST", "B — broad but below-average alone",
     ['(insert #) things that (insert result).',
      '(insert #) (insert tools/settings/mistakes) you need to know.',
      'Here are (insert #) ways to (insert outcome).'],
     "A finite, numbered promise. Broad and familiar, but below-average as a spoken opener on its own — a "
     "number is not a hook. Works only when the items are genuinely specific, and is stronger fused with a "
     "negative command or an outcome+time-box."),
    ("shock", "SHOCK / PATTERN-INTERRUPT", "B — volatile (wins and flops equally)",
     ['(insert platform) just (insert outrageous claim).',
      '(insert blunt/profane reaction to a new thing).'],
     "An outrageous or blunt spoken opener that breaks the polished-creator pattern. It can spike hard, but "
     "it flops as often as it wins and is brand-dependent — never a default. Only use it when the shock is "
     "immediately followed by a real tactic."),
    ("feature_news", "FEATURE / UPDATE NEWS", "⚠️ PROMISING (small N, time-locked)",
     ['(insert platform) just dropped a new update.',
      '(insert platform) just gave you a cheat code and you didn’t notice.'],
     "Frame a brand-new platform feature as an edge the viewer is missing right now. High win-rate but a "
     "small sample and time-locked to real releases — post it the day the platform ships something, then it "
     "decays. Promising, not yet proven."),
    ("comparison", "A/B COMPARISON", "⚠️ PROMISING (only 2 creators)",
     ['Which (insert thing) did better — (insert A) or (insert B)?',
      '(insert A) vs (insert B).',
      'Cash or pass: (insert thing).'],
     "Show two options and make the viewer guess which won, then reveal. Forces a guess-comment and a "
     "watch-to-the-end. Reliable for the two creators who use it, but not yet broad."),
    ("strip_reframe", "STRIP-IT-BACK / REFRAME", "⚠️ PROMISING (small N, one repeated line)",
     ['If I (insert removing the thing everyone assumes matters), I’ll still (insert outcome) — because (insert real reason).',
      'No matter the (insert niche/size/creator), it’s always (insert the real factor).'],
     "Open by removing what everyone assumes matters, to prove what actually does — cognitive tension. "
     "Strong when it lands, but the sample is small and half the wins are one creator’s one repeated line."),
    ("youll_never", "“YOU’LL NEVER … IF”", "⚠️ PROMISING (one creator, one line, reposted)",
     ['You will never (insert dream result) if you don’t (insert action).',
      'If you don’t (insert action), you will never (insert result).'],
     "A negative-stakes prohibition tied to the dream outcome. Eye-catching win-rate, but it’s essentially "
     "one creator reposting one line — proven for that line, not as a portable structure. Adapt, don’t bank "
     "on the win-rate transferring."),
]

lines = [
    "# 1000-Style Hook Swipe File — Jacky Niche (spoken hooks, first 5 seconds)",
    "",
    "*Same format as a viral-hook swipe file: each entry is a **hook structure**, the **format** that makes",
    "it work, and the **evidence** — every reel from our 8-creator / ~712-reel scrape whose first 5 spoken",
    "seconds used that hook. Built ONLY from our scraped data. Ranked by consistency (win-rate + low flop +",
    "sample size), not by one big hit. Win/Flop = vs each account's own median. Reproduce:",
    "`python research/pattern_analysis_v4.py` (0 API calls).*",
    "",
    "> The hook = what's **spoken in the first ~5 seconds** (captions excluded). The comment-keyword CTA is a",
    "> caption mechanic, not a hook, and is intentionally not listed here.",
    "",
    "---",
]

for key, title, tier, templates, fmt in SPEC:
    rs = groups.get(key, [])
    if not rs:
        continue
    n, cr, w, f, wr, fr, mm = stats(rs)
    lines.append(f"\n## {title}")
    lines.append(f"**Tier:** {tier}  ·  **N={n} reels · {cr} creators · {wr}% win · {fr}% flop · median {mm}× own-median**")
    lines.append("")
    lines.append("**HOOK:**")
    for t in templates:
        lines.append(f"- {t}")
    lines.append("")
    lines.append(f"**FORMAT:** {fmt}")
    lines.append("")
    lines.append("**EVIDENCE** (every reel that opened with this hook — real first-5s in quotes):")
    for r in rs:
        tag = {"winner": "✅ winner", "mid": "· mid", "flop": "✗ flop"}[r["cls"]]
        lines.append(f'- {tag} · {r["v"]:,}v · {r["sr"]}% sh · {r["mult"]}× · @{r["a"]}')
        lines.append(f'  {link(r)}')
        lines.append(f'  > "{r["hook"]}"')
    lines.append("")
    lines.append("---")

out = HERE.parent / "playbook" / "hooks.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {out} | {sum(len(groups.get(k,[])) for k,*_ in SPEC)} cited reels across {len(SPEC)} hook structures")
