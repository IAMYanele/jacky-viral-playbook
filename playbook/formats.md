# Information-Packaging Swipe File — Jacky Niche

*How the information is PACKAGED AND DELIVERED — the recurring delivery structures across the whole
reel (not the hook, not the topic). Discovered from 707 transcripts, classified, then ranked by
**engagement** (median views/likes/shares + share-rate) and **win-rate**, descending. Same swipe-file
shape as hooks.md: each format = how it's delivered, the verbal signals, and every source reel that
used it. Win/Flop = vs each account's own median. Reproduce: `python research/rank_formats.py` (0 API calls).*

> **Ranking logic:** a format ranks high when it wins *consistently across many reels* (win-rate + low
> flop-rate + sample size), not off one viral hit. Where a format gets big **reach** but inconsistent
> results, that's stated explicitly — reach ≠ reliability.

### Consistency vs reach (read both together)
- **Most consistent winners** (default to these): **Settings-walkthrough** (53% win) and
  **Hypothetical-reset-blueprint** "if I had 0 followers…" (50% win, lowest flop 14%, 0.94% share).
- **Big reach, inconsistent** (swing knowingly): **Category-taxonomy-explainer** ("there are 5 types of
  content…") has the **highest median views (51K) + shares (437)** but only **14% win** — travels far or
  flops. **Personal-proof-case-study** similar (41K median views, 9% win).
- **Over-used & weak** (where most people default — don't): **Numbered-howto-tutorial** (N=121, 35% flop)
  and **Spoken-take/interview-rant** (N=136, the most common, yet ~1,600 median views, ~0 shares).
  Popularity ≠ performance.
- **Most forwardable** (top share-rates): Settings-walkthrough (1.35%), Offer/CTA-promo (1.33%),
  Category-taxonomy (0.98%), Hypothetical-reset (0.94%).

## Quick ranking (by consistency-weighted engagement)

| # | Packaging format | N | Creators | Win% | Flop% | Median views | Median shares | Share% |
|---|------------------|---|----------|------|-------|--------------|---------------|--------|
| 1 | **SETTINGS WALKTHROUGH** | 26 | 4 | 53% | 19% | 15,749 | 174 | 1.35% |
| 2 | **TIER RATING RUNDOWN** | 37 | 7 | 27% | 18% | 19,082 | 108 | 0.39% |
| 3 | **MECHANISM EXPLAINER** | 70 | 7 | 25% | 20% | 8,730 | 42 | 0.32% |
| 4 | **SPOKEN TAKE INTERVIEW RANT** | 136 | 8 | 25% | 19% | 1,616 | 2 | 0.11% |
| 5 | **COMPARISON JUXTAPOSITION** | 55 | 7 | 21% | 21% | 24,613 | 134 | 0.43% |
| 6 | **HYPOTHETICAL RESET BLUEPRINT** | 14 | 4 | 50% | 14% | 11,766 | 111 | 0.94% |
| 7 | **TOOLKIT SWIPE FILE HANDOUT** | 32 | 5 | 25% | 40% | 10,408 | 91 | 0.85% |
| 8 | **ANNOTATED TEARDOWN DEMO** | 46 | 8 | 19% | 30% | 14,144 | 43 | 0.33% |
| 9 | **OFFER CTA PROMO** | 18 | 5 | 27% | 16% | 26,024 | 446 | 1.33% |
| 10 | **MYTH BUST DIRECTIVE** | 57 | 7 | 21% | 40% | 6,868 | 24 | 0.27% |
| 11 | **CATEGORY TAXONOMY EXPLAINER** | 47 | 5 | 14% | 21% | 51,136 | 437 | 0.98% |
| 12 | **NUMBERED HOWTO TUTORIAL** | 121 | 8 | 18% | 35% | 6,424 | 39 | 0.59% |
| 13 | **PERSONAL PROOF CASE STUDY** | 43 | 6 | 9% | 16% | 41,527 | 49 | 0.15% |
| 14 | **DIALOGUE GUESSING GAME** | 5 | 3 | 60% | 0% | 165,746 | 93 | 0.16% |

---

## 1. SETTINGS WALKTHROUGH
**Tier:** S — PROVEN (consistent winner)  ·  **N=26 reels · 4 creators · 53% win · 19% flop**
**Engagement (median):** 15,749 views · 359 likes · 174 shares · 1.35% share-rate · 4.69× own-median

**HOW IT'S PACKAGED:** Delivers value as literal in-app navigation — a sequence of taps, toggles, and menu paths the viewer executes on their own phone to unlock a hidden setting or platform feature. The steps ARE the button presses (not conceptual advice), usually framed as leaking a platform cheat code.

**VERBAL SIGNALS (how they actually say it):**
- "go to settings, then X, then tap Y"
- "turn on / turn off / make sure all three are checked"
- "cheat code / Instagram just gave you"
- "you didn't even notice this setting"
- "save it as a draft then duplicate it"
- "all for free, do this every time"

**EVIDENCE** (26 reels, by views — real opening words quoted):
- ✅ winner · 1,278,571v · 35,777L · 35,217sh · 2.75% · @devinjatho
  https://www.instagram.com/reel/DX0M0rOyEwI/
  > "Never post on Instagram until you fix these five settings. Number one, make sure"
- ✅ winner · 629,687v · 29,748L · 20,223sh · 3.21% · @devinjatho
  https://www.instagram.com/reel/DXo0c5bkn53/
  > "Instagram seriously just gave you the biggest fucking cheat code and you didn't even"
- ✅ winner · 433,179v · 11,498L · 10,384sh · 2.4% · @devinjatho
  https://www.instagram.com/reel/DX0MuRvSFV2/
  > "Never post to Instagram again without turning on these five settings. Number one, make"
- ✅ winner · 244,720v · 7,418L · 4,063sh · 1.66% · @devinjatho
  https://www.instagram.com/reel/DVjDzE9Ekya/
  > "Two people get 100,000 views, but person A's audience looks like this, and person"
- ✅ winner · 152,834v · 3,326L · 2,882sh · 1.89% · @devinjatho
  https://www.instagram.com/reel/DY2C22yyHLk/
  > "Never post on Instagram until you fix these five settings. Number one, make sure"
- ✅ winner · 120,998v · 2,902L · 2,113sh · 1.75% · @iamaayushswamy
  https://www.instagram.com/reel/DWXjctoiQ-W/
  > "Instagram just dropped a massive new update. And while these creators will only tell"
- ✅ winner · 103,611v · 3,894L · 3,315sh · 3.2% · @devinjatho
  https://www.instagram.com/reel/DXm0_9kkiS-/
  > "Instagram seriously just gave you the biggest fucking cheat code and Didn't even notice"
- · mid · 79,025v · 1,562L · 822sh · 1.04% · @personalbrandlaunch
  https://www.instagram.com/reel/DXMSLqImhbH/
  > "Here's a crazy AI use case for content. First, go to Facebook, click on"
- · mid · 51,404v · 945L · 462sh · 0.9% · @personalbrandlaunch
  https://www.instagram.com/reel/DYDGXO5E9GS/
  > "You know what's come to my attention that you don't know how to stalk"
- · mid · 46,431v · 1,446L · 785sh · 1.69% · @devinjatho
  https://www.instagram.com/reel/DXmXUChkt2C/
  > "If you could double your views on Instagram for free with zero extra effort,"
- · mid · 23,504v · 764L · 566sh · 2.41% · @devinjatho
  https://www.instagram.com/reel/DX0NJMfyUSk/
  > "Never, ever post on Instagram if you do not have these five settings fixed."
- ✅ winner · 21,370v · 370L · 154sh · 0.72% · @iamaayushswamy
  https://www.instagram.com/reel/DW5DTTQDHWX/
  > "Never, ever, ever turn on these three settings to increase your privacy on Instagram."
- ✅ winner · 16,748v · 353L · 268sh · 1.6% · @iamaayushswamy
  https://www.instagram.com/reel/DX4owf8MjiO/
  > "This is the fastest way to double your views with no extra effort explained"
- · mid · 14,751v · 365L · 190sh · 1.29% · @devinjatho
  https://www.instagram.com/reel/DY3BjdDSUjg/
  > "Two people get 100,000 views, but person A's audience looks like this, and person"
- ✅ winner · 13,422v · 265L · 121sh · 0.9% · @iamaayushswamy
  https://www.instagram.com/reel/DWmopAOEmtN/
  > "You shouldn't post on Instagram again till you know the right time to post."
- ✅ winner · 10,217v · 290L · 158sh · 1.55% · @iamaayushswamy
  https://www.instagram.com/reel/DWZU54vDIrE/
  > "Instagram just dropped another massive new update and while all of these creators will"
- ✗ flop · 8,797v · 209L · 109sh · 1.24% · @devinjatho
  https://www.instagram.com/reel/DY0vtsCSWnA/
  > "Instagram seriously just gave you the biggest fucking cheat code and you didn't even"
- · mid · 5,756v · 55L · 58sh · 1.01% · @alinamerkelcoach
  https://www.instagram.com/reel/DYXv_IAtwai/
  > "Free AI in Instagram Stories. Now you can generate images or change outfits for"
- ✗ flop · 5,103v · 112L · 36sh · 0.71% · @devinjatho
  https://www.instagram.com/reel/DVjDp5BEoCo/
  > "Two people get 100,000 views, but person A's audience looks like this, and person"
- ✅ winner · 3,906v · 79L · 55sh · 1.41% · @iamaayushswamy
  https://www.instagram.com/reel/DWmTyn3jPXG/
  > "Instagram just solved a major issue. You can now give your account access to"
- ✅ winner · 1,909v · 34L · 17sh · 0.89% · @iamaayushswamy
  https://www.instagram.com/reel/DX4qL1TJBNn/
  > "This is the fastest way to double your views with no extra effort explained"
- ✅ winner · 1,761v · 38L · 15sh · 0.85% · @iamaayushswamy
  https://www.instagram.com/reel/DX4og1-sxyJ/
  > "This is the fastest way to double your views with no extra effort explained"
- ✗ flop · 322v · 10L · 5sh · 1.55% · @devinjatho
  https://www.instagram.com/reel/DVtNsdyjRJf/
  > "Instagram just slapped their dick on the table with this new update. Because look,"
- · mid · 317v · 5L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW1203ADLeW/
  > "Never, ever, EVER post on Instagram again without using this brand new feature. Instagram"
- ✗ flop · 22v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWhMbLUDGPp/
  > "Never, ever, ever turn on these three settings to increase your privacy on Instagram."
- ✗ flop · 8v · 0L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW5Ov5PDNoy/
  > "Instagram just dropped a massive new update. And while these creators will only tell"

---

## 2. TIER RATING RUNDOWN
**Tier:** A — solid, reliable  ·  **N=37 reels · 7 creators · 27% win · 18% flop**
**Engagement (median):** 19,082 views · 521 likes · 108 shares · 0.39% share-rate · 1.18× own-median

**HOW IT'S PACKAGED:** Runs through a set of items and assigns each a snap verdict on a fixed scale — tier letters (S/A/F), numeric scores (1-10), or binary pass/cash, important/not-important — in a fast staccato sweep. The packaging is judgment-per-item across many items measured against a standard.

**VERBAL SIGNALS (how they actually say it):**
- "Hashtags F tier, editing C tier, hooks A tier"
- "Pass / Cash"
- "Not important. Important. Very important."
- "score out of 10 / it's a seven, a little saturated"
- "X. Pass. Y. Cash."
- "rate each on a scale"

**EVIDENCE** (37 reels, by views — real opening words quoted):
- ✅ winner · 243,465v · 5,622L · 2,769sh · 1.14% · @personalbrandlaunch
  https://www.instagram.com/reel/DWws2behzma/
  > "Hashtags. Not important. Reposting your new reels on stories. Not important. Honestly, wouldn't really"
- ✅ winner · 243,264v · 2,901L · 887sh · 0.36% · @sam.gaudet
  https://www.instagram.com/reel/DYdEfR1oCGg/
  > "Airbnb. It's a pass. Boutique hotels is the future. I think Airbnbs were an"
- · mid · 150,602v · 3,218L · 1,679sh · 1.11% · @personalbrandlaunch
  https://www.instagram.com/reel/DV87SeqDWxp/
  > "Hashtags. Zero hashtags don't do crap. I mean, you can use them as keywords"
- · mid · 134,228v · 2,590L · 1,405sh · 1.05% · @personalbrandlaunch
  https://www.instagram.com/reel/DWJUxOphGN5/
  > "Hashtags. A hundred view rule. Hashtags don't get you views. You have to have"
- · mid · 121,231v · 1,691L · 360sh · 0.3% · @personalbrandlaunch
  https://www.instagram.com/reel/DXCuWc2hvDb/
  > "Fitness. Seven, it's a little saturated, but that means if you do something really"
- ✅ winner · 97,718v · 3,549L · 1,632sh · 1.67% · @sam.gaudet
  https://www.instagram.com/reel/DXKltAWSvPb/
  > "Hashtags F tier they don't matter editing. I'd say c-tier I think really good"
- · mid · 90,720v · 6,306L · 567sh · 0.63% · @personalbrandlaunch
  https://www.instagram.com/reel/DXSLGBHBOhf/
  > "Hashtags. Zero hashtags don't do crap. I mean, you can use them as keywords"
- · mid · 70,445v · 1,075L · 254sh · 0.36% · @personalbrandlaunch
  https://www.instagram.com/reel/DYAhki7E2GT/
  > "Hashtags. Red flag. They do not work like they used to. Sometimes they're good"
- · mid · 70,282v · 1,010L · 238sh · 0.34% · @personalbrandlaunch
  https://www.instagram.com/reel/DYcGJGGBUSp/
  > "Kiss, marry, kill, written hook, verbal hook, visual hook. Kill, visual hook. Like if"
- · mid · 58,406v · 949L · 342sh · 0.59% · @personalbrandlaunch
  https://www.instagram.com/reel/DXFTpU3GWAz/
  > "Learn versus don't learn, content edition 2026. Researching outlier videos for viral hooks, topics,"
- · mid · 52,256v · 558L · 195sh · 0.37% · @personalbrandlaunch
  https://www.instagram.com/reel/DY7AEU_PXlE/
  > "Trend, outdated, timeless. Trend, outdated, timeless. Trend, outdated, timeless. Trend, outdated, timeless. Follow for"
- · mid · 45,975v · 842L · 246sh · 0.54% · @personalbrandlaunch
  https://www.instagram.com/reel/DV54D7mBBsw/
  > "If the first line of your video raises curiosity and promises a payoff, you're"
- · mid · 40,826v · 993L · 322sh · 0.79% · @sam.gaudet
  https://www.instagram.com/reel/DV8oaxyEpUG/
  > "For research, good, better, best. For script writing, horrible, good, great. For AI thumbnails,"
- ✅ winner · 31,296v · 670L · 992sh · 3.17% · @alinamerkelcoach
  https://www.instagram.com/reel/DY5e9wbt79f/
  > "TokenHeadVideos Few Reviews, Lots of Followers, Lots of Sales Memes Lots of Views, Few"
- · mid · 21,030v · 740L · 108sh · 0.51% · @sam.gaudet
  https://www.instagram.com/reel/DXRqqfoScQr/
  > "Topic or thumbnail? Topic, easy. Apps or analytics? Analytics for sure. Gear or formats?"
- · mid · 20,444v · 545L · 34sh · 0.17% · @sam.gaudet
  https://www.instagram.com/reel/DYXM-BxSg9H/
  > "Thumbnails. C-tier. 90% of your traffic comes from the feed or the reels tab."
- ✅ winner · 20,258v · 530L · 224sh · 1.11% · @iamaayushswamy
  https://www.instagram.com/reel/DWPY7hDkt_7/
  > "Hashtags. Not important. They died over a year ago. SEO is king. Reposting Reels"
- · mid · 20,194v · 358L · 178sh · 0.88% · @realskytan
  https://www.instagram.com/reel/DYRKpVWiGgK/
  > "Rate these formats from 1-10. Selfie app. 5. A lot of people aren't really"
- · mid · 19,082v · 521L · 84sh · 0.44% · @sam.gaudet
  https://www.instagram.com/reel/DXwvqHqyFD-/
  > "All right, ranking advice you see on social media starting with hashtags. Honestly D"
- · mid · 18,900v · 587L · 142sh · 0.75% · @sam.gaudet
  https://www.instagram.com/reel/DWblAZ2y-Zc/
  > "This is the content creation iceberg to know if your content strategist is full"
- · mid · 16,030v · 353L · 282sh · 1.76% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYwWIN8S2Fq/
  > "Buying followers Not important Looks good for a second but kills your back end"
- · mid · 12,597v · 133L · 49sh · 0.39% · @realskytan
  https://www.instagram.com/reel/DYlz_yJihZW/
  > "Rate these formats from 1 to 10. It's still ranking. I'll give it a"
- · mid · 11,986v · 91L · 4sh · 0.03% · @realskytan
  https://www.instagram.com/reel/DY43eCgCl78/
  > "I've gotten my ass eaten around 17 times by now, just because a lot"
- ✅ winner · 11,097v · 186L · 36sh · 0.32% · @iamaayushswamy
  https://www.instagram.com/reel/DWkK5slEt1K/
  > "Fitness. Eight. I've made a ton of people go viral in this niche, but"
- · mid · 7,572v · 60L · 8sh · 0.11% · @realskytan
  https://www.instagram.com/reel/DY2qMOdCV9T/
  > "Men want to aim high without feeling insufficient if they fall short. Men want"
- · mid · 6,861v · 91L · 96sh · 1.4% · @bhavinipanjwanii
  https://www.instagram.com/reel/DZA7hdDxmsG/
  > "Buying followers Not important Looks good for a second but kills your back end"
- ✗ flop · 6,771v · 232L · 13sh · 0.19% · @sam.gaudet
  https://www.instagram.com/reel/DZIEk5VSuTC/
  > "What to focus on when building a personal brand. Hooks or thumbnails? Hooks. Hooks"
- ✗ flop · 4,420v · 37L · 3sh · 0.07% · @realskytan
  https://www.instagram.com/reel/DZC6kiXi6AF/
  > "Canva just made the thing that I have been waiting for somebody to make."
- ✅ winner · 2,900v · 42L · 14sh · 0.48% · @loganforsyth
  https://www.instagram.com/reel/DY77OaBihMD/
  > "YouTube. YouTube, I'll put it two. For people who crack YouTube, it's their number"
- ✗ flop · 1,938v · 26L · 9sh · 0.46% · @sam.gaudet
  https://www.instagram.com/reel/DV7FMC-gXsS/
  > "For research, good, better, best. For script writing, horrible, good, great. For AI thumbnails,"
- ✅ winner · 1,926v · 19L · 7sh · 0.36% · @loganforsyth
  https://www.instagram.com/reel/DY-yVzXiBMC/
  > "Sort feed. Sort feed is gonna be number five. It used to be great."
- ✅ winner · 1,898v · 21L · 2sh · 0.11% · @loganforsyth
  https://www.instagram.com/reel/DY5bwxvic3l/
  > "Swipe right or left, post every day. Swipe right, but only if you're looking"
- ✗ flop · 1,418v · 19L · 2sh · 0.14% · @sam.gaudet
  https://www.instagram.com/reel/DYU8eEEyt6X/
  > "Thumbnails. C-tier. 90% of your traffic comes from the feed or the reels tab."
- ✅ winner · 1,162v · 12L · 1sh · 0.09% · @loganforsyth
  https://www.instagram.com/reel/DZGuUM8xGip/
  > "DMs. DMs, I'll put at a two. I've made a lot of money receiving"
- ✗ flop · 42v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWPAu9PDGhs/
  > "Hashtags. Not important. They died over a year ago. SEO is king. Reposting Reels"
- ✗ flop · 10v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWreSZXjJ1C/
  > "Hashtags. Zero. They won't get you views. Combine them with keywords. Visual hooks. Ten."
- ✗ flop · 5v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWhS83RjLF1/
  > "Hashtags. Zero. They won't get you views. Combine them with keywords. Visual hooks. Ten."

---

## 3. MECHANISM EXPLAINER
**Tier:** A — solid, reliable  ·  **N=70 reels · 7 creators · 25% win · 20% flop**
**Engagement (median):** 8,730 views · 164 likes · 42 shares · 0.32% share-rate · 1.0× own-median

**HOW IT'S PACKAGED:** Explains HOW a system works or WHY an outcome happens by laying out the underlying logic — algorithm rules, the contrasting mechanics of platform surfaces (stories vs carousels vs reels), the psychology that makes a tactic work — often ending in usage rules. Value is understanding a principle, not executing steps or rating items.

**VERBAL SIGNALS (how they actually say it):**
- "here's why / the reason is"
- "Stories reach followers, Carousels go to X, Reels are shown to non-followers"
- "what makes them work is"
- "this basically means / so what's that"
- "100k on TikTok is worth 10k on Instagram"
- "post Stories X times a week, Carousels Y times"

**EVIDENCE** (70 reels, by views — real opening words quoted):
- ✅ winner · 4,686,071v · 176,287L · 12,312sh · 0.26% · @devinjatho
  https://www.instagram.com/reel/DXsJznEEsHp/
  > "If I take off all my clothes, if I remove this luxurious background behind"
- ✅ winner · 1,253,511v · 41,489L · 3,548sh · 0.28% · @devinjatho
  https://www.instagram.com/reel/DYo0KHFSQrS/
  > "If I take off all my clothes, if I remove this luxurious background behind"
- ✅ winner · 900,041v · 20,382L · 22,499sh · 2.5% · @alinamerkelcoach
  https://www.instagram.com/reel/DXMU-n7tGgR/
  > "Stories reach your followers. Carousels go to followers first, then non-followers. Reels are shown"
- ✅ winner · 708,776v · 19,801L · 1,169sh · 0.16% · @devinjatho
  https://www.instagram.com/reel/DY1v8ckS6Af/
  > "If I take off all my clothes, if I remove this luxurious background behind"
- ✅ winner · 231,699v · 3,899L · 2,445sh · 1.06% · @personalbrandlaunch
  https://www.instagram.com/reel/DW6QSgcFCYL/
  > "What format goes the most viral? No matter the niche, no matter the account"
- · mid · 217,953v · 7,589L · 4,747sh · 2.18% · @personalbrandlaunch
  https://www.instagram.com/reel/DVtfPHvCYRW/
  > "Okay, you know what's crazy? If you have one main niche, five sub niches,"
- ✅ winner · 213,413v · 5,527L · 5,394sh · 2.53% · @iamaayushswamy
  https://www.instagram.com/reel/DWUCCNVjCYT/
  > "Stories get shown to followers. Carousels gets shown to followers, and then non-followers. Reels"
- · mid · 168,714v · 3,929L · 1,303sh · 0.77% · @personalbrandlaunch
  https://www.instagram.com/reel/DXfEKHHDLDm/
  > "100,000 followers on TikTok is worth 10,000 followers on Instagram, and that's worth 1,000"
- · mid · 108,563v · 2,190L · 822sh · 0.76% · @personalbrandlaunch
  https://www.instagram.com/reel/DWMpsfNBksm/
  > "This creator posted the same hook nine times and it went viral every single"
- · mid · 98,549v · 2,643L · 747sh · 0.76% · @personalbrandlaunch
  https://www.instagram.com/reel/DYwtBIkB44h/
  > "100,000 followers on TikTok is worth 10,000 followers on Instagram, and that's worth 1,000"
- · mid · 96,021v · 2,056L · 1,038sh · 1.08% · @personalbrandlaunch
  https://www.instagram.com/reel/DXJs0eIkcWY/
  > "Always remember, for followers, post reels. For leads, post stories. For nurture slash engagement,"
- · mid · 93,026v · 1,930L · 1,054sh · 1.13% · @personalbrandlaunch
  https://www.instagram.com/reel/DXr8AuFD4Up/
  > "If you have zero to a thousand followers, three Tofu top of funnel pieces"
- · mid · 82,502v · 2,164L · 445sh · 0.54% · @personalbrandlaunch
  https://www.instagram.com/reel/DXZJqq_DkNl/
  > "Okay, when you start an Instagram account from zero, I typically see two things."
- · mid · 77,403v · 1,689L · 724sh · 0.94% · @personalbrandlaunch
  https://www.instagram.com/reel/DYK0shtAlpH/
  > "This hook is going very viral right now. I call it the iceberg effect."
- · mid · 67,357v · 1,129L · 504sh · 0.75% · @personalbrandlaunch
  https://www.instagram.com/reel/DWPPHNjDkFg/
  > "Reels get shown to non followers plus some current followers. Carousels get shown to"
- · mid · 63,860v · 1,204L · 540sh · 0.85% · @personalbrandlaunch
  https://www.instagram.com/reel/DXNB3ZkGg_z/
  > "They call it like the broad narrow niche framework, a super broad hook to"
- · mid · 55,566v · 940L · 321sh · 0.58% · @personalbrandlaunch
  https://www.instagram.com/reel/DVn2eqdkYDX/
  > "Okay, but be for real. Why do some creators get millions of views but"
- · mid · 45,963v · 433L · 89sh · 0.19% · @personalbrandlaunch
  https://www.instagram.com/reel/DVtAuuejfLJ/
  > "A hundred followers, 10,000 followers, 100,000 followers, 100 followers, 10,000 followers, 100,000 followers, 100"
- · mid · 36,352v · 946L · 186sh · 0.51% · @devinjatho
  https://www.instagram.com/reel/DXsLJAUEj1V/
  > "If I take off all my clothes, if I remove this luxurious background behind"
- · mid · 36,316v · 379L · 80sh · 0.22% · @sam.gaudet
  https://www.instagram.com/reel/DWZLC_tSnfV/
  > "The position Dan is in, the position Hormozy is in, Ryan Serhant, Simon Squibb,"
- · mid · 34,688v · 1,280L · 202sh · 0.58% · @sam.gaudet
  https://www.instagram.com/reel/DYrwZ0sSYHr/
  > "Did the blue shirt create Dan Martell or did Dan Martell create the blue"
- ✅ winner · 23,356v · 638L · 513sh · 2.2% · @iamaayushswamy
  https://www.instagram.com/reel/DWe7Rs3ko1F/
  > "B-roll gets you views. Storytelling content gets you followers. High-value carousels with how-tos, guides,"
- · mid · 19,331v · 684L · 151sh · 0.78% · @sam.gaudet
  https://www.instagram.com/reel/DYzijI0yl3t/
  > "The last thing you wanna do is build a personal brand by accident. If"
- · mid · 16,813v · 531L · 98sh · 0.58% · @sam.gaudet
  https://www.instagram.com/reel/DV_QOJNkm_d/
  > "I'm going to share a little dark brand psychology with you guys that you"
- · mid · 16,286v · 675L · 135sh · 0.83% · @sam.gaudet
  https://www.instagram.com/reel/DVvyy4HEkrK/
  > "Repurposing content is probably the worst advice that you could ever listen to on"
- · mid · 15,956v · 392L · 63sh · 0.39% · @sam.gaudet
  https://www.instagram.com/reel/DXHd1BbSX0k/
  > "If you want results like this, you have to be controversial in your content."
- · mid · 15,735v · 584L · 55sh · 0.35% · @sam.gaudet
  https://www.instagram.com/reel/DXZZc3VyqYK/
  > "I think a lot of people skip to building a personal brand without doing"
- · mid · 15,686v · 395L · 69sh · 0.44% · @sam.gaudet
  https://www.instagram.com/reel/DXb-VVYS44W/
  > "content manager. I know that's the next role I need to hire. What does"
- · mid · 11,792v · 243L · 27sh · 0.23% · @sam.gaudet
  https://www.instagram.com/reel/DV6H82TkuQ9/
  > "There's only one of these three videos that's actually considered viral. And the reason"
- · mid · 11,541v · 378L · 44sh · 0.38% · @sam.gaudet
  https://www.instagram.com/reel/DYpSEHqyGTw/
  > "Not all views are created equal. A view on your YouTube video could be"
- · mid · 11,042v · 158L · 14sh · 0.13% · @realskytan
  https://www.instagram.com/reel/DX2UXXuiLnG/
  > "Let me show you the power of a really good text book, which is"
- · mid · 10,221v · 335L · 36sh · 0.35% · @sam.gaudet
  https://www.instagram.com/reel/DVydFDFktCY/
  > "Let me put you on some game that nobody else in the content industry"
- · mid · 9,951v · 249L · 42sh · 0.42% · @sam.gaudet
  https://www.instagram.com/reel/DWUjIPJEmfE/
  > "something that a lot of people do wrong when they're trying to go broad"
- · mid · 8,895v · 166L · 81sh · 0.91% · @alinamerkelcoach
  https://www.instagram.com/reel/DXkQJgMNAbo/
  > "Expert want 1 million views. Expert get 200 views. Expert sad. Expert spend four"
- · mid · 8,738v · 124L · 32sh · 0.37% · @realskytan
  https://www.instagram.com/reel/DX_Bj5biSom/
  > "The most disgusting viral hooks of all time use a concept called power words."
- · mid · 8,722v · 209L · 59sh · 0.68% · @realskytan
  https://www.instagram.com/reel/DYofpCUC7Nr/
  > "In every era of social media, there's always one main way to go viral."
- · mid · 8,588v · 162L · 42sh · 0.49% · @realskytan
  https://www.instagram.com/reel/DX8Vn3PCnzm/
  > "Now, what if I told you generational runs on social media can actually be"
- ✅ winner · 8,462v · 239L · 71sh · 0.84% · @iamaayushswamy
  https://www.instagram.com/reel/DXt_FDFDL2O/
  > "This is how the algorithm works on social media. Once you learn the algorithm,"
- · mid · 7,238v · 134L · 16sh · 0.22% · @realskytan
  https://www.instagram.com/reel/DYaAxLSCsEp/
  > "Let's talk about the science of falling off. Falling off in itself isn't a"
- ✅ winner · 5,567v · 143L · 65sh · 1.17% · @iamaayushswamy
  https://www.instagram.com/reel/DY8FCQ7yfbZ/
  > "More cuts equals more engagement. And with the human attention span being this small,"
- ✅ winner · 4,486v · 31L · 25sh · 0.56% · @loganforsyth
  https://www.instagram.com/reel/DYYWUI7R8ap/
  > "Breaking news, and this is for if you have a podcast. Doing this for"
- ✅ winner · 3,280v · 31L · 3sh · 0.09% · @loganforsyth
  https://www.instagram.com/reel/DX0FVaSCz3O/
  > "Neon spends a million dollars a month on clippers. Wow. That's why you see"
- ✅ winner · 2,708v · 53L · 7sh · 0.26% · @loganforsyth
  https://www.instagram.com/reel/DXsTiw-ArFz/
  > "Eminem has said he writes every single day, verses that will never be on"
- ✅ winner · 2,563v · 58L · 72sh · 2.81% · @loganforsyth
  https://www.instagram.com/reel/DX5F2r4iXKf/
  > "This is how you protect yourself from AI in the future. Watch this. We"
- ✅ winner · 2,380v · 53L · 6sh · 0.25% · @iamaayushswamy
  https://www.instagram.com/reel/DZGuWFYJlwP/
  > "It took me 10 years to realize that even though my videos were super"
- ✅ winner · 2,244v · 12L · 14sh · 0.62% · @loganforsyth
  https://www.instagram.com/reel/DYbPyXENFHW/
  > "Back with another breaking news, YouTube Shorts is now at over 200 billion daily"
- ✅ winner · 2,024v · 16L · 3sh · 0.15% · @loganforsyth
  https://www.instagram.com/reel/DX8S7svtW8t/
  > "An article on X is going viral right now showing that the value of"
- ✅ winner · 2,023v · 34L · 5sh · 0.25% · @loganforsyth
  https://www.instagram.com/reel/DX-QHVrCWVZ/
  > "Picasso produced over 20,000 works in his lifetime. Almost all of them were average,"
- ✅ winner · 1,246v · 9L · 1sh · 0.08% · @loganforsyth
  https://www.instagram.com/reel/DXpc3w2gm3G/
  > "Serena Williams has an 80% win rate in Grand Slam finals. The bigger the"
- ✗ flop · 773v · 16L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DYnjd9uPQku/
  > "If I died and all my content was deleted, except for one video, I"
- · mid · 746v · 11L · 1sh · 0.13% · @iamaayushswamy
  https://www.instagram.com/reel/DZGvCqSJHTm/
  > "this is exactly why your views still look like this. The best videos perform"
- ✗ flop · 623v · 10L · 1sh · 0.16% · @sam.gaudet
  https://www.instagram.com/reel/DV7YLd5CdJK/
  > "I'm going to share a little dark brand psychology with you guys that you"
- · mid · 350v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX-2EytNbAG/
  > "This is the future of advertising. Watch this. I have been shocked by how"
- · mid · 312v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX8TCKYNrUl/
  > "the direction of the media economy is only going further and further in this"
- · mid · 265v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DZG2zvqsMlK/
  > "The easier your visuals communicate what you're saying, the less your viewer's brain needs"
- · mid · 237v · 0L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DZIO4KoMV1d/
  > "It took me 10 years to realize that even though my videos were super"
- · mid · 235v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX8THupNO0e/
  > "the direction of the media economy is only going further and further in this"
- · mid · 201v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWjwbxKDHFv/
  > "You should always, always, always think twice before taking someone else's advice. Way too"
- ✗ flop · 110v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWmL0CVDBtu/
  > "This is how the algorithm works on social media. Once you learn the algorithm,"
- ✗ flop · 84v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWj_H92jI57/
  > "Reels get views, carousels get engagement, stories get leads. Reels get shown to non-followers"
- ✗ flop · 64v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWhYwigjJ25/
  > "How Do I Generate Leads From My Social Media? Look, I know this is"
- ✗ flop · 24v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW4cQKtDGAk/
  > "This is how the algorithm works, and once you master it, you will know"
- ✗ flop · 9v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWCCanVDOMF/
  > "More cuts equals more engagement, and with the human attention span being this small,"
- ✗ flop · 8v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWZptnqDEDI/
  > "Here's a dark psychology secret that will help you grow a cult following and"
- ✗ flop · 6v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWZcVb2jBK_/
  > "Here's how to get paid to exist without actually having to go viral. And"
- ✗ flop · 4v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWRr2XOjHZe/
  > "There are two types of shirts that fuck up your videos. A white shirt"
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWCRIcZDBkY/
  > "Posting schedule for 100k followers. Reels, 6 times per week. Carousels, 1-2 times per"
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW1jkMPDAy8/
  > "This is a marketing secret you shouldn't ignore, and this is exactly why McDonald's,"
- ✗ flop · 3v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX8TmJetRSt/
  > "It goes on to state that the future of media is clipping. An article"
- ✗ flop · 2v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX8Tc1jNufr/
  > "take advantage of the clip economy. An article on X is going viral right"

---

## 4. SPOKEN TAKE INTERVIEW RANT
**Tier:** A — solid, reliable  ·  **N=136 reels · 8 creators · 25% win · 19% flop**
**Engagement (median):** 1,616 views · 30 likes · 2 shares · 0.11% share-rate · 0.94× own-median

**HOW IT'S PACKAGED:** A first-person spoken-word monologue carrying the value as the expert's discursive take — either a podcast/interview clip answering a posed question with anecdote, or a self-driven rant/manifesto riffing on a broad belief or worldview. No on-screen steps, lists, or demos; the persuasive argument is the package.

**VERBAL SIGNALS (how they actually say it):**
- "What's the best investment you ever made?"
- "Is school still relevant / is it still worth it to"
- "Why are Gen Z kids so fragile?"
- "I think the world's gotten / here's the deal"
- "answer framed as 'I think...' with a personal story"
- "interviewer interjections (Holy shit, that's a big idea)"

**EVIDENCE** (136 reels, by views — real opening words quoted):
- ✅ winner · 164,312v · 1,781L · 978sh · 0.6% · @bhavinipanjwanii
  https://www.instagram.com/reel/DWLhh_NKwgE/
  > "Girl, what you doin' just to get to where you're goin'? Yeah, I see"
- ✅ winner · 159,085v · 3,647L · 1,337sh · 0.84% · @sam.gaudet
  https://www.instagram.com/reel/DWT8wEvgvmk/
  > "Is it still worth it to go to university? There's no correlation of going"
- ✅ winner · 158,108v · 2,320L · 428sh · 0.27% · @sam.gaudet
  https://www.instagram.com/reel/DWkQQxWkiXr/
  > "ChatGPT is dying a slow death. They're trying to keep up. They're trying to"
- ✅ winner · 156,928v · 1,562L · 227sh · 0.14% · @sam.gaudet
  https://www.instagram.com/reel/DXsI2HIDLys/
  > "What's the 50 to fix it rule? Anybody can make a decision to solve"
- ✅ winner · 147,239v · 2,650L · 410sh · 0.28% · @sam.gaudet
  https://www.instagram.com/reel/DY95GtnjoSh/
  > "Is Chad GPT good again? Yeah, Codex is actually really compelling. Image 2, pretty"
- ✅ winner · 139,770v · 1,779L · 251sh · 0.18% · @sam.gaudet
  https://www.instagram.com/reel/DY79fFqlGuI/
  > "What's the best investment you ever made in business? Definitely a coach. I have"
- ✅ winner · 122,176v · 2,390L · 929sh · 0.76% · @sam.gaudet
  https://www.instagram.com/reel/DYfpM3NChKQ/
  > "Is school relevant in 2030? No. Go to university to what? To memorize shit?"
- ✅ winner · 112,616v · 2,072L · 296sh · 0.26% · @sam.gaudet
  https://www.instagram.com/reel/DXP0E0ICisT/
  > "Why are Gen Z kids so fragile these days? I don't blame them. Over"
- ✅ winner · 90,231v · 1,482L · 287sh · 0.32% · @sam.gaudet
  https://www.instagram.com/reel/DWWhq1WgpTy/
  > "As an AI expert, what scares you the most about AI? There's like a"
- ✅ winner · 86,368v · 1,836L · 475sh · 0.55% · @sam.gaudet
  https://www.instagram.com/reel/DYPp13-jlol/
  > "Should you praise your kids? I don't celebrate a kid's win. I celebrate the"
- ✅ winner · 85,130v · 1,608L · 506sh · 0.59% · @sam.gaudet
  https://www.instagram.com/reel/DWpgupLDvzX/
  > "How do you start a business in 2026? Sell anything to a stranger. When"
- ✅ winner · 83,802v · 1,309L · 282sh · 0.34% · @sam.gaudet
  https://www.instagram.com/reel/DV_ZDCYAdH7/
  > "Do you think people could use AI instead of coaches in the future? AI"
- · mid · 77,833v · 1,393L · 895sh · 1.15% · @personalbrandlaunch
  https://www.instagram.com/reel/DXRbBwaBIUy/
  > "What's one small detail in a video that makes a huge difference? Putting your"
- ✅ winner · 75,694v · 2,838L · 518sh · 0.68% · @bhavinipanjwanii
  https://www.instagram.com/reel/DXNOfp2AMmI/
  > "Thanks for watching!"
- ✅ winner · 61,846v · 1,021L · 98sh · 0.16% · @sam.gaudet
  https://www.instagram.com/reel/DX9hWE_gBk_/
  > "Should business owners teach their team AI? Most business owners can't teach their team"
- · mid · 61,530v · 1,291L · 228sh · 0.37% · @personalbrandlaunch
  https://www.instagram.com/reel/DW1GftaDXN_/
  > "What do the top 1% do on social media? You know, I could give"
- · mid · 48,803v · 708L · 127sh · 0.26% · @personalbrandlaunch
  https://www.instagram.com/reel/DW_Zi2WPE-b/
  > "How do you think AI is going to affect content? Yeah, the idea in"
- ✅ winner · 44,822v · 839L · 192sh · 0.43% · @bhavinipanjwanii
  https://www.instagram.com/reel/DXD_Tuvj4Rr/
  > "Those innocent eyes That smile on your face Makes it easy To trust you"
- · mid · 43,657v · 453L · 121sh · 0.28% · @personalbrandlaunch
  https://www.instagram.com/reel/DXWk5d-j1eJ/
  > "How important are Instagram stories? And do you have any like advice for Instagram"
- ✗ flop · 29,845v · 426L · 12sh · 0.04% · @personalbrandlaunch
  https://www.instagram.com/reel/DZCt6ffOoq_/
  > "Hey guys, it's Saturday. I just finished filming some shorts. I have been up"
- · mid · 26,075v · 318L · 66sh · 0.25% · @realskytan
  https://www.instagram.com/reel/DYDiMXTvoNi/
  > "is when I see somebody wearing an Apple Watch and they post it after"
- · mid · 25,224v · 733L · 178sh · 0.71% · @sam.gaudet
  https://www.instagram.com/reel/DX7Yh9xvnQL/
  > "So I posted a video about the CEO of PayPal hiring a head of"
- · mid · 23,398v · 735L · 121sh · 0.52% · @sam.gaudet
  https://www.instagram.com/reel/DWEs5CzADMe/
  > "So the CEO of PayPal and other CEOs at other top companies are hiring"
- · mid · 21,018v · 739L · 272sh · 1.29% · @sam.gaudet
  https://www.instagram.com/reel/DV4GoimAcWv/
  > "Caleb Ralston, he's worked on Gary Vee's brand, the Hormozy's brands. He's famous for"
- · mid · 19,250v · 561L · 69sh · 0.36% · @sam.gaudet
  https://www.instagram.com/reel/DX2r5dvPz9y/
  > "On the other side of you building your personal brand, there will be 100%"
- · mid · 18,632v · 547L · 77sh · 0.41% · @sam.gaudet
  https://www.instagram.com/reel/DXUQV9BSPrB/
  > "50% of the videos that we shoot don't actually make it to the face"
- · mid · 17,848v · 657L · 30sh · 0.17% · @sam.gaudet
  https://www.instagram.com/reel/DVlqXtLEqrT/
  > "When I was 14 years old, my dad calls me into his office and"
- · mid · 17,736v · 137L · 59sh · 0.33% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYPI5mmAQwK/
  > "The way you walk, the way you understand me, the way you move, the"
- · mid · 15,185v · 257L · 30sh · 0.2% · @bhavinipanjwanii
  https://www.instagram.com/reel/DW538wIynhw/
  > "And I wonder if you even notice me and you got"
- · mid · 14,524v · 238L · 23sh · 0.16% · @bhavinipanjwanii
  https://www.instagram.com/reel/DWD67DiDHw-/
  > "Her face is a map of the world, is a map of the world"
- · mid · 14,228v · 148L · 16sh · 0.11% · @bhavinipanjwanii
  https://www.instagram.com/reel/DX1ZcXcgC1W/
  > "Don't hesitate Go put your records on Tell me your favorite song"
- ✅ winner · 13,513v · 195L · 13sh · 0.1% · @iamaayushswamy
  https://www.instagram.com/reel/DWm4T7QD3WB/
  > "So I've been struggling mentally for quite a while now and it's forced me"
- · mid · 13,411v · 277L · 12sh · 0.09% · @sam.gaudet
  https://www.instagram.com/reel/DW1kUBwOzLY/
  > "If someone listening is like, I really want my brand to cut through. What"
- · mid · 13,188v · 413L · 66sh · 0.5% · @bhavinipanjwanii
  https://www.instagram.com/reel/DWWvwfZjFRi/
  > "Although there's distance between us, there's no place I'd rather be Owe you some"
- · mid · 12,822v · 205L · 36sh · 0.28% · @bhavinipanjwanii
  https://www.instagram.com/reel/DW3FUTRjfKi/
  > "the next, video!!"
- · mid · 12,784v · 147L · 19sh · 0.15% · @bhavinipanjwanii
  https://www.instagram.com/reel/DXYjzPojOQK/
  > "Fuck anyone that's bringing you down Sweetheart, you're doing your thing right now Good"
- ✅ winner · 12,178v · 189L · 11sh · 0.09% · @iamaayushswamy
  https://www.instagram.com/reel/DXBCLTcDM55/
  > "I don't know who needs to hear this, but this whole yapping to the"
- · mid · 11,452v · 82L · 8sh · 0.07% · @alinamerkelcoach
  https://www.instagram.com/reel/DWWXJ4uujnN/
  > "you"
- · mid · 11,093v · 164L · 13sh · 0.12% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYopeY1KnIx/
  > "And you don't seem to understand"
- · mid · 9,086v · 135L · 6sh · 0.07% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYZrP_nMgCS/
  > "When the night has come and the land is dark"
- · mid · 9,015v · 0L · 0sh · 0.0% · @bhavinipanjwanii
  https://www.instagram.com/reel/DY6rFcWKJMO/
  > "["Teach Me Baby"]"
- · mid · 8,735v · 258L · 44sh · 0.5% · @alinamerkelcoach
  https://www.instagram.com/reel/DWFVAaJDf3M/
  > "www.youtube.com or www.youtube.com and www.youtube.com"
- · mid · 8,665v · 193L · 14sh · 0.16% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYB_qR9AcWi/
  > "♪ At last my love has come to me ♪"
- · mid · 7,812v · 168L · 9sh · 0.12% · @alinamerkelcoach
  https://www.instagram.com/reel/DXJwL4zN4bb/
  > "Bless you. ♪ The way my mind falls in love ♪"
- · mid · 7,404v · 72L · 8sh · 0.11% · @alinamerkelcoach
  https://www.instagram.com/reel/DXXUyaUNDT_/
  > "All right, let's go There's gonna be one less lonely girl One less lonely"
- · mid · 7,349v · 81L · 3sh · 0.04% · @realskytan
  https://www.instagram.com/reel/DX-1ZsvCzVR/
  > "You know that quote that goes like you sell because you're stuck at marketing"
- · mid · 6,379v · 232L · 25sh · 0.39% · @alinamerkelcoach
  https://www.instagram.com/reel/DWFVIoLjQuI/
  > "You"
- · mid · 6,116v · 56L · 18sh · 0.29% · @alinamerkelcoach
  https://www.instagram.com/reel/DWyyp2EtfBE/
  > "I'll be your blonde tonight, if that's what you like Cilantro and fishnets, if"
- · mid · 6,011v · 206L · 31sh · 0.52% · @alinamerkelcoach
  https://www.instagram.com/reel/DW84xp3twxO/
  > "Yeah, I'm trying things, you tried it too. How are you going to knock"
- · mid · 5,777v · 105L · 51sh · 0.88% · @alinamerkelcoach
  https://www.instagram.com/reel/DY0J9CntcZ6/
  > "🎶 Music Outro 🎶"
- ✅ winner · 5,717v · 100L · 81sh · 1.42% · @loganforsyth
  https://www.instagram.com/reel/DXxiPiFCd32/
  > "This is the future of advertising. Watch this. I have been shocked by how"
- ✅ winner · 5,298v · 98L · 44sh · 0.83% · @loganforsyth
  https://www.instagram.com/reel/DYBDbkfxJI-/
  > "The main reason I went was to ask about media and content and all"
- · mid · 5,102v · 236L · 12sh · 0.24% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1q4W-Da3a/
  > "Girl"
- · mid · 4,715v · 74L · 2sh · 0.04% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1XwjGDSVi/
  > "덤블링"
- ✅ winner · 4,460v · 113L · 2sh · 0.04% · @loganforsyth
  https://www.instagram.com/reel/DYK2Z52hHW1/
  > "Well, the reason I asked y'all to come to lunch is because I love"
- ✅ winner · 4,239v · 49L · 30sh · 0.71% · @loganforsyth
  https://www.instagram.com/reel/DZBs4xQR1Y6/
  > "He's saying I'm here with Mads Englund co-founder CEO roll out. No, what do"
- · mid · 4,103v · 107L · 6sh · 0.15% · @alinamerkelcoach
  https://www.instagram.com/reel/DYsdUmsNz32/
  > "24"
- ✗ flop · 2,603v · 33L · 20sh · 0.77% · @alinamerkelcoach
  https://www.instagram.com/reel/DWggyJqjV2N/
  > "Thanks for watching!"
- ✗ flop · 2,447v · 32L · 9sh · 0.37% · @alinamerkelcoach
  https://www.instagram.com/reel/DWZGthqDRZ_/
  > "I know you are tired, but remember the life you promised yourself."
- ✅ winner · 2,395v · 59L · 9sh · 0.38% · @loganforsyth
  https://www.instagram.com/reel/DXs1pQBjdJz/
  > "사랑해 사랑해 사랑해 사랑해 사랑해"
- ✅ winner · 2,258v · 34L · 25sh · 1.11% · @loganforsyth
  https://www.instagram.com/reel/DX2i6aLRj1f/
  > "You say that the new highest paid skill in today's world is content creation."
- ✗ flop · 2,140v · 22L · 2sh · 0.09% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1Xs2xDQvB/
  > "emphasizing 선수들에게 질문시킨 댕댕이에겐 올림픽에 대해 계속 많이 설명해야할 것!"
- ✅ winner · 2,088v · 26L · 2sh · 0.1% · @loganforsyth
  https://www.instagram.com/reel/DYf3oWWCaXX/
  > "Anyone else hate to eat food during the day? I really wish that there"
- ✗ flop · 1,970v · 49L · 4sh · 0.2% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1X1hsDaSw/
  > "귀여운 친구들��양 안녕"
- ✗ flop · 1,951v · 123L · 5sh · 0.26% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1qv1UDZ87/
  > "Oh, girl, it's..."
- ✅ winner · 1,751v · 39L · 7sh · 0.4% · @loganforsyth
  https://www.instagram.com/reel/DYVXVaISwVR/
  > "Claude co-work is getting so much hype and everyone's like the AI AI is"
- ✗ flop · 1,746v · 68L · 8sh · 0.46% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1qzoOjTH1/
  > "Oh, girl, it's..."
- ✗ flop · 1,625v · 13L · 2sh · 0.12% · @alinamerkelcoach
  https://www.instagram.com/reel/DY2nT9INmBz/
  > "자막제작 by UpTitle http://www.uptitle.co.kr"
- ✅ winner · 1,608v · 37L · 89sh · 5.53% · @loganforsyth
  https://www.instagram.com/reel/DYqCeGvikAj/
  > "John D. Rockefeller was one of the richest people in American history, and you"
- ✅ winner · 1,566v · 41L · 1sh · 0.06% · @loganforsyth
  https://www.instagram.com/reel/DXsyOKBjYyA/
  > "Yeah, yeah, yeah, yeah, yeah, yeah"
- ✅ winner · 1,450v · 43L · 2sh · 0.14% · @loganforsyth
  https://www.instagram.com/reel/DYiqYsJRQ5M/
  > "I truly don't understand people who don't wanna have kids. I had my first"
- ✅ winner · 1,428v · 22L · 1sh · 0.07% · @loganforsyth
  https://www.instagram.com/reel/DYnwe1NRMgq/
  > "We recently made a larger multi six-figure investment into coaching and advisory with the"
- ✅ winner · 1,344v · 29L · 1sh · 0.07% · @loganforsyth
  https://www.instagram.com/reel/DX78hOAx7Q7/
  > "Picasso produced over 20,000 works in his lifetime. Almost all of them were average,"
- ✅ winner · 1,276v · 26L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXqXpmUjfnG/
  > "♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪"
- ✅ winner · 1,237v · 32L · 1sh · 0.08% · @loganforsyth
  https://www.instagram.com/reel/DXx7TFsN5AO/
  > "이 영상은 유료광고를 포함하고 있습니다."
- ✅ winner · 1,232v · 20L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX2BQcyxhAL/
  > "Love, you can go back to being friends with me"
- ✗ flop · 1,107v · 28L · 5sh · 0.45% · @alinamerkelcoach
  https://www.instagram.com/reel/DWZHqm-DYTx/
  > "I know you are tired, but remember the life you promised yourself."
- ✅ winner · 1,078v · 27L · 1sh · 0.09% · @loganforsyth
  https://www.instagram.com/reel/DYIa2AUy-JH/
  > "The real marketers know if I click on your URL and I don't see"
- ✗ flop · 970v · 29L · 2sh · 0.21% · @alinamerkelcoach
  https://www.instagram.com/reel/DWZGemDjT4T/
  > "I know you are tired, but remember the life you promised yourself."
- ✗ flop · 935v · 14L · 1sh · 0.11% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1Xp0-Da9F/
  > "우리estone 뮤직비디오 뽐내는 법 Seoul쪼미"
- · mid · 917v · 14L · 2sh · 0.22% · @loganforsyth
  https://www.instagram.com/reel/DYvuK6QuHuV/
  > "entrepreneur community can be toxic and so misguided at times. A lot of people"
- · mid · 874v · 20L · 3sh · 0.34% · @loganforsyth
  https://www.instagram.com/reel/DYsaSTUicZm/
  > "There is no type of person who I despise more than a victim. Those"
- ✗ flop · 853v · 14L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DWZHaYwDcQR/
  > "I know you are tired, but remember the life you promised yourself."
- ✗ flop · 713v · 3L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DYdHG6LyZ38/
  > "There's a specific type of content creator that AI is creating, and I think"
- · mid · 649v · 7L · 8sh · 1.23% · @loganforsyth
  https://www.instagram.com/reel/DX2BW9HRHFO/
  > "Love, you can go back to being friends with me"
- · mid · 632v · 10L · 1sh · 0.16% · @loganforsyth
  https://www.instagram.com/reel/DX2BKE9R0v6/
  > "Yeah, uh, I thought I'd be like, oh, baby, what you waiting for?"
- ✗ flop · 607v · 10L · 3sh · 0.49% · @sam.gaudet
  https://www.instagram.com/reel/DXZV0ylSiis/
  > "content manager. I know that's the next role I need to hire. What does"
- · mid · 600v · 12L · 2sh · 0.33% · @loganforsyth
  https://www.instagram.com/reel/DX78Q3Mxa5U/
  > "Picasso produced over 20,000 works in his lifetime. Almost all of them were average,"
- · mid · 585v · 20L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuLSNCEUuS/
  > "But I can see it's lost in the memory August slipped away into a"
- ✗ flop · 510v · 3L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1Xl-qjR9W/
  > "?? 뭐야?"
- ✗ flop · 444v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DYM6UeaSJEh/
  > "I felt inspired and I shot a video, and it didn't get any views"
- · mid · 419v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiSE88EZFC/
  > "Peace."
- · mid · 415v · 13L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXxm0Caiz9F/
  > "."
- · mid · 401v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiNLmQkWDV/
  > "Peace."
- · mid · 363v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuYGwLES8e/
  > "Yeah, uh, I thought I'd be like, oh, baby, what you waitin' for? Maybe"
- ✗ flop · 337v · 2L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1XZitjVOl/
  > "오프닝"
- · mid · 302v · 6L · 6sh · 1.99% · @loganforsyth
  https://www.instagram.com/reel/DXsucB6DQnw/
  > "you"
- · mid · 295v · 5L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuLJRvEVmB/
  > "But I can see it's lost in the memory August slipped away into a"
- · mid · 295v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiRdW1kR6Q/
  > "Peace."
- · mid · 294v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXugsGmAnmY/
  > "2017 I wanted everything that was a star at 23. I bought it all"
- · mid · 294v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXsyV3iDSBf/
  > "Yeah, yeah, yeah, yeah, yeah, yeah"
- ✗ flop · 289v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DWmUu6SyeU2/
  > "Look, I think I've been hiding something for you guys. And I wanted to"
- · mid · 284v · 5L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXx4OXCRtSg/
  > "이 영상은 유료광고를 포함하고 있습니다."
- · mid · 273v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuYA0PEV1K/
  > "Yeah, uh, I thought I'd be like, oh, baby, what you waitin' for? Maybe"
- · mid · 268v · 5L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXqHwFfEfPP/
  > "Thanks for watching and subscribe for more!"
- · mid · 260v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiNEoTEe_h/
  > "Peace."
- · mid · 255v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX50vEiNdbI/
  > "You're breaking all my limits And it hurts so good"
- · mid · 252v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiRRzpEVgF/
  > "Peace."
- · mid · 251v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX5013_tYQm/
  > "You're breaking all my limits And it hurts so good"
- · mid · 247v · 3L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX0WYmnxhDV/
  > "Yeah, uh, I try to act like, oh, baby, what you waitin' for?"
- · mid · 247v · 3L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiRYXzEX01/
  > "Peace."
- · mid · 241v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuh7C9gqXl/
  > "2017 I wanted everything that was a star at 23. I bought it all"
- · mid · 229v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX0WivrxqPR/
  > "Yeah, uh, I try to act like, oh, baby, what you waitin' for?"
- · mid · 223v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXxnAU9CIZB/
  > "."
- · mid · 212v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXugkn1At5H/
  > "2017 I wanted everything that was a star at 23. I bought it all"
- ✗ flop · 208v · 1L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1XgBTjU49/
  > "6월 1일 проблем 없다는 민지와 순위를 시작합니다 끝"
- · mid · 207v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXug380AtpT/
  > "2017 I wanted everything that was a star at 23. I bought it all"
- ✗ flop · 194v · 12L · 0sh · 0.0% · @devinjatho
  https://www.instagram.com/reel/DYPdLGBSCOF/
  > "Peanut butter jelly the long way. You can't restaurant use mint. So if you"
- · mid · 191v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuYRFjkTzB/
  > "Yeah, uh, I thought I'd be like, oh, baby, what you waitin' for? Maybe"
- ✗ flop · 190v · 3L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV1qrOnjVr1/
  > "Oh, girl, it's... BAD BAD BAD BAD"
- · mid · 188v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX0WchoxqjE/
  > "Yeah, uh, I try to act like, oh, baby, what you waitin' for?"
- · mid · 185v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXx4FoNxGFU/
  > "이 영상은 유료광고를 포함하고 있습니다."
- · mid · 182v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXx37TmR7xL/
  > "She just wants to be beautiful, she goes"
- · mid · 182v · 5L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXsuJ5tjeUo/
  > "you"
- · mid · 180v · 3L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX5woEZtc0T/
  > "you"
- · mid · 178v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXsur81DeAA/
  > "."
- · mid · 176v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXx6iBPt3z8/
  > "I sleep well I sleep well"
- · mid · 175v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXsukkPDV9F/
  > "."
- · mid · 170v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXuLZ7IkW9f/
  > "But I can see it's lost in the memory August slipped away into a"
- · mid · 164v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXsyIvHDeHQ/
  > "."
- ✗ flop · 145v · 2L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXxmpYzCb_q/
  > "."
- ✗ flop · 141v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXx6P7wNZTK/
  > "Thanks for watching!"
- ✗ flop · 130v · 1L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXpyFw0gsyw/
  > "3, 2, 1!"
- ✗ flop · 17v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX-2Y9etiiE/
  > "This is the future of advertising. Watch this. I have been shocked by how"
- ✗ flop · 3v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXiSMp8EYYf/
  > "Peace."
- ✗ flop · 2v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DXqYX37jQ3f/
  > "♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪ ♪♪"

---

## 5. COMPARISON JUXTAPOSITION
**Tier:** B — works, execution-dependent  ·  **N=55 reels · 7 creators · 21% win · 21% flop**
**Engagement (median):** 24,613 views · 438 likes · 134 shares · 0.43% share-rate · 0.98× own-median

**HOW IT'S PACKAGED:** Teaches by contrast — either pitting two named rivals against each other to name a winner/difference (A vs B, platform vs platform, tool vs tool) or showing graded paired exemplars side by side (bad/good/great, paid vs free, 100-view vs 1M-view, used-to-do vs now-do). The delivery is the parallel two-sided juxtaposition itself.

**VERBAL SIGNALS (how they actually say it):**
- "100 view hook vs 1 million view hook version"
- "this is a bad hook, this is a good hook, this is a great hook"
- "what's the difference between X and Y"
- "Video A or Video B? still A"
- "this one's paid, this one's free"
- "I used to do X (wrong), now I do Y (right)"

**EVIDENCE** (55 reels, by views — real opening words quoted):
- · mid · 217,927v · 4,914L · 2,166sh · 0.99% · @personalbrandlaunch
  https://www.instagram.com/reel/DWo_wr1l7t6/
  > "Yo, watch this. What? Same exact hook, different delivery. Sell me this pen. Sell"
- · mid · 184,153v · 2,827L · 1,830sh · 0.99% · @personalbrandlaunch
  https://www.instagram.com/reel/DWerTC9B5Jv/
  > "100 view hook, five steps to open a Roth IRA. 1 million view hook"
- · mid · 179,718v · 2,582L · 1,221sh · 0.68% · @personalbrandlaunch
  https://www.instagram.com/reel/DXUv41QBvkg/
  > "This is a bad hook. This is a good hook. This is a great"
- · mid · 176,447v · 3,967L · 2,994sh · 1.7% · @personalbrandlaunch
  https://www.instagram.com/reel/DWCCv6DGOo0/
  > "This one's payed. This one's free. This one's paid. This one's free. This one's"
- ✅ winner · 161,293v · 4,004L · 906sh · 0.56% · @sam.gaudet
  https://www.instagram.com/reel/DWe48IlCZMt/
  > "Why did you switch to Claude? Claude's the top dog. They have the best"
- · mid · 144,933v · 2,081L · 1,056sh · 0.73% · @personalbrandlaunch
  https://www.instagram.com/reel/DWj3P7xDws5/
  > "This is a bad hook. This is a good hook. This is a great"
- · mid · 131,914v · 2,001L · 786sh · 0.6% · @personalbrandlaunch
  https://www.instagram.com/reel/DVwDhiAjtPZ/
  > "Comparing videos about the same topic, but with an a hundred view hook. A"
- · mid · 116,995v · 2,467L · 1,557sh · 1.33% · @personalbrandlaunch
  https://www.instagram.com/reel/DV_BrTPjg2f/
  > "I don't script my videos, I freestyle. I write out a rough draft of"
- ✅ winner · 106,272v · 1,508L · 407sh · 0.38% · @sam.gaudet
  https://www.instagram.com/reel/DYafyKdlJ77/
  > "What's the difference between a manager and a leader? Manager's too insecure to f***ing"
- · mid · 103,795v · 1,625L · 659sh · 0.63% · @personalbrandlaunch
  https://www.instagram.com/reel/DX2OYPWkiiD/
  > "If two people posted a video and both got a million views, but one"
- · mid · 81,905v · 1,168L · 417sh · 0.51% · @personalbrandlaunch
  https://www.instagram.com/reel/DYKEsaFgch8/
  > "Both our videos got one million views, but mine only got a hundred followers,"
- · mid · 79,071v · 1,388L · 332sh · 0.42% · @personalbrandlaunch
  https://www.instagram.com/reel/DWgg2u_FEzQ/
  > "Same exact hook, but different delivery. Selling to the poor versus selling to the"
- · mid · 74,623v · 1,244L · 629sh · 0.84% · @personalbrandlaunch
  https://www.instagram.com/reel/DWRDxY1mr0J/
  > "I don't attach any audios when posting. I attach audios when posting my carousels"
- · mid · 72,571v · 1,236L · 463sh · 0.64% · @personalbrandlaunch
  https://www.instagram.com/reel/DXkMuXwhOOM/
  > "Hashtags or captions? Caption. Hashtags do nothing. Hooks or editing? Hooks. Idea or value?"
- · mid · 65,096v · 1,338L · 421sh · 0.65% · @personalbrandlaunch
  https://www.instagram.com/reel/DYHf7tAgfN1/
  > "A hundred view hook is niche and makes no one care. A one million"
- · mid · 62,577v · 862L · 304sh · 0.49% · @personalbrandlaunch
  https://www.instagram.com/reel/DVjlKwqFPxI/
  > "Two videos about the same topic and from the same creator, but which one"
- · mid · 62,215v · 777L · 226sh · 0.36% · @personalbrandlaunch
  https://www.instagram.com/reel/DYri5KqhSlp/
  > "Old and not really working anymore. New and definitely working right now. Old, not"
- · mid · 61,463v · 1,131L · 537sh · 0.87% · @personalbrandlaunch
  https://www.instagram.com/reel/DYzRNZ6PT5w/
  > "I focus on long and broad stories. I choose one story to focus on"
- · mid · 55,931v · 728L · 240sh · 0.43% · @personalbrandlaunch
  https://www.instagram.com/reel/DVyvfDdoHxZ/
  > "I recreate every trend. I create a mix of these three types of content."
- · mid · 53,314v · 762L · 189sh · 0.35% · @personalbrandlaunch
  https://www.instagram.com/reel/DWW9gYkjQH8/
  > "Can you define what you see as fluff in most content? When I think"
- · mid · 52,353v · 908L · 267sh · 0.51% · @personalbrandlaunch
  https://www.instagram.com/reel/DWg_VubGexk/
  > "If you look at an audio B-roll video versus a talking form video, you"
- · mid · 49,650v · 566L · 134sh · 0.27% · @personalbrandlaunch
  https://www.instagram.com/reel/DVlz--mEXwU/
  > "Which video do you think got more views? This one or this one? If"
- · mid · 42,837v · 607L · 153sh · 0.36% · @personalbrandlaunch
  https://www.instagram.com/reel/DW13E7gDOvT/
  > "There are two types of winners I'm seeing on social media right now. Winner"
- · mid · 41,818v · 720L · 130sh · 0.31% · @personalbrandlaunch
  https://www.instagram.com/reel/DV0ugXbETya/
  > "Okay, but is it easier to build a faceless brand or a personal brand"
- · mid · 39,010v · 424L · 105sh · 0.27% · @personalbrandlaunch
  https://www.instagram.com/reel/DVyJuo1DnXG/
  > "100 view video, one million view video. 100 view video, one million view video."
- ✅ winner · 37,966v · 415L · 479sh · 1.26% · @alinamerkelcoach
  https://www.instagram.com/reel/DYnZcy1Ntsv/
  > "First seconds of your reel to get a thousand views. Todd here with Location"
- ✅ winner · 28,087v · 873L · 254sh · 0.9% · @iamaayushswamy
  https://www.instagram.com/reel/DXacxAyCalY/
  > "Posting three times a day versus posting three times a week. Which one's gonna"
- · mid · 24,613v · 799L · 171sh · 0.69% · @sam.gaudet
  https://www.instagram.com/reel/DYZ3i_DyPAk/
  > "It used to be company brands, now it's founder brands. It used to be"
- · mid · 22,497v · 742L · 154sh · 0.68% · @sam.gaudet
  https://www.instagram.com/reel/DWBsSODkswf/
  > "Six things you should never say in content. Never say and, say but or"
- ✅ winner · 21,662v · 288L · 61sh · 0.28% · @alinamerkelcoach
  https://www.instagram.com/reel/DW_jxv2tD9b/
  > "This is how my video looks without camera light. This is how my video"
- · mid · 16,983v · 364L · 81sh · 0.48% · @realskytan
  https://www.instagram.com/reel/DYoeeRSiKS7/
  > "Zoom scrolling for content ideas is terrible for your personal brand. Doing a daily"
- · mid · 15,797v · 380L · 87sh · 0.55% · @sam.gaudet
  https://www.instagram.com/reel/DWRfA6fSrWo/
  > "For research, it used to be Reddit, now it's Sandcastle's AI. For scripting, it"
- · mid · 15,541v · 438L · 42sh · 0.27% · @sam.gaudet
  https://www.instagram.com/reel/DYKrxCOyZZI/
  > "I felt inspired, and I shot a video, and it didn't get any views,"
- · mid · 14,321v · 240L · 112sh · 0.78% · @alinamerkelcoach
  https://www.instagram.com/reel/DX-AIjgt8QF/
  > "First seconds of your reel to get a thousand views. If you eat like"
- ✅ winner · 12,502v · 286L · 59sh · 0.47% · @iamaayushswamy
  https://www.instagram.com/reel/DXnIw_SDOVG/
  > "100 view creator versus 1 million view creator. Here are the three top marketing"
- ✅ winner · 12,342v · 141L · 12sh · 0.1% · @iamaayushswamy
  https://www.instagram.com/reel/DYDtneEJuwP/
  > "If I go from filming cinematically to yapping in my car, now if I"
- · mid · 12,171v · 180L · 73sh · 0.6% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYMTpkxqMtw/
  > "Focus on aesthetics, focus on attention, post professional polished videos, make it raw, real"
- ✅ winner · 12,065v · 346L · 140sh · 1.16% · @iamaayushswamy
  https://www.instagram.com/reel/DWg87PlDAQ1/
  > "Having no script or using ChatGPT to write your scripts is bad. Writing a"
- ✅ winner · 11,214v · 143L · 6sh · 0.05% · @iamaayushswamy
  https://www.instagram.com/reel/DYGTyiUM45l/
  > "If I swap out my camera for my phone, and then I turn off"
- ✅ winner · 11,095v · 197L · 46sh · 0.41% · @iamaayushswamy
  https://www.instagram.com/reel/DYBRwsEMf_I/
  > "Posting three times per day versus posting three times a week, which is actually"
- ✅ winner · 8,788v · 200L · 66sh · 0.75% · @iamaayushswamy
  https://www.instagram.com/reel/DXMwNryjPOa/
  > "Stories versus Reels. Which one is going to be better for you to make"
- · mid · 6,790v · 113L · 9sh · 0.13% · @realskytan
  https://www.instagram.com/reel/DY3ckAti9Ws/
  > "analyzing viral videos to see if it's over or under a million views. Let's"
- ✗ flop · 1,421v · 16L · 1sh · 0.07% · @sam.gaudet
  https://www.instagram.com/reel/DXPjJ95yRGh/
  > "Topic or thumbnail? Topic, easy. Apps or analytics? Analytics for sure. Gear or formats?"
- ✅ winner · 1,261v · 15L · 3sh · 0.24% · @iamaayushswamy
  https://www.instagram.com/reel/DYBQ_-vsAtI/
  > "Posting three times per day versus posting three times a week, which is actually"
- ✗ flop · 929v · 8L · 2sh · 0.22% · @sam.gaudet
  https://www.instagram.com/reel/DYWGP3-ySYN/
  > "It used to be company brands, now it's founder brands. It used to be"
- ✗ flop · 525v · 5L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DZG9s2pymG6/
  > "What to focus on when building a personal brand. Hooks or thumbnails? Hooks. Hooks"
- ✗ flop · 101v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWHL1qJjDz6/
  > "Having no script or using chat GPT to write your scripts is bad. Writing"
- ✗ flop · 51v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWWo0lDDE8_/
  > "If you wanna sell to some poor people, focus on speed so fast results,"
- ✗ flop · 23v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWmh5dDDJB3/
  > "This video gets views. Reincarnated, I'm a stargazer, life goes on, I need all"
- ✗ flop · 14v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW4IAGxjEuf/
  > "100 View Creator vs. 1,000,000 View Creator Here are the 3 top marketing books"
- ✗ flop · 4v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWrkiqEDLn7/
  > "Hashtags. SEO keywords. Post all content formats. Stick to one to two formats. B-roll"
- ✗ flop · 3v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWCdfd6jNUQ/
  > "B-roll gets you views. Storytelling content gets you followers. High-value carousels with how-tos, guides,"
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWrPQxLDDSY/
  > "100 view creator versus 1 million view creator. Do you want to lose fat"
- ✗ flop · 3v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX-uEWnxWh4/
  > "This is no longer a conspiracy. Official data shows that platforms are now rewarding"
- ✗ flop · 0v · 0L · 0sh · 0% · @loganforsyth
  https://www.instagram.com/reel/DX-uO7-RvXc/
  > "This is no longer a conspiracy. Official data shows that platforms are now rewarding"

---

## 6. HYPOTHETICAL RESET BLUEPRINT
**Tier:** S — PROVEN (consistent winner)  ·  **N=14 reels · 4 creators · 50% win · 14% flop**
**Engagement (median):** 11,766 views · 307 likes · 111 shares · 0.94% share-rate · 3.83× own-median

**HOW IT'S PACKAGED:** Value framed as a first-person counterfactual — 'if I had to start over / hit goal X from scratch, here's exactly what I'd do' — then delivered as conditional-mood ordered moves toward an ambitious end state. The 'if I were starting / if I had to' framing licensing an idealized roadmap is the signature.

**VERBAL SIGNALS (how they actually say it):**
- "If I had to go from zero to a million"
- "if I wanted to / if I had to start over"
- "here's exactly what I'd do"
- "Step one I would... Step two I would"
- "if I only had X minutes/days"
- "if I had to implement this from scratch, this is exactly how"

**EVIDENCE** (14 reels, by views — real opening words quoted):
- ✅ winner · 2,215,348v · 60,402L · 42,270sh · 1.91% · @sam.gaudet
  https://www.instagram.com/reel/DV3n5CvEjNQ/
  > "If I wanted to go from zero to a million dollars using AI, what"
- ✅ winner · 427,550v · 10,647L · 9,587sh · 2.24% · @personalbrandlaunch
  https://www.instagram.com/reel/DWUYjHal4XN/
  > "If you had to go from zero to a million followers in six months,"
- · mid · 111,427v · 2,856L · 1,685sh · 1.51% · @personalbrandlaunch
  https://www.instagram.com/reel/DXEjuFijUm_/
  > "If I had to implement AI into my content workflow from scratch, this is"
- · mid · 30,420v · 1,111L · 303sh · 1.0% · @sam.gaudet
  https://www.instagram.com/reel/DXEzbv0Sije/
  > "So as you guys know, I don't do consulting, but if you hired me"
- ✅ winner · 16,591v · 432L · 234sh · 1.41% · @iamaayushswamy
  https://www.instagram.com/reel/DWMmcrtAW9K/
  > "Not to flex, but I'm pretty fucking good at social media. And if I"
- ✅ winner · 13,751v · 414L · 179sh · 1.3% · @iamaayushswamy
  https://www.instagram.com/reel/DYf-dKgsCNm/
  > "If I wanted to reach 10K followers in the next 30 days, these are"
- ✅ winner · 12,155v · 295L · 141sh · 1.16% · @iamaayushswamy
  https://www.instagram.com/reel/DXYEvOJjJDi/
  > "If I wanted to reach 10k followers in the next 30 days, these are"
- · mid · 11,378v · 140L · 30sh · 0.26% · @realskytan
  https://www.instagram.com/reel/DX9sWa4iCmu/
  > "I'm a millionaire now. Instant credibility. But if I had to start from zero,"
- · mid · 10,438v · 319L · 82sh · 0.79% · @sam.gaudet
  https://www.instagram.com/reel/DZDBd_bhj6z/
  > "So as you guys know, I don't do consulting, but if I had to"
- ✅ winner · 6,054v · 123L · 32sh · 0.53% · @iamaayushswamy
  https://www.instagram.com/reel/DYxVBtbJV8B/
  > "If you need to sign a new client in the next 24 hours, this"
- ✅ winner · 5,597v · 143L · 28sh · 0.5% · @iamaayushswamy
  https://www.instagram.com/reel/DYlYzc2sLZz/
  > "If I wanted to reach 10K followers in the next 30 days, these are"
- ✗ flop · 1,145v · 15L · 10sh · 0.87% · @sam.gaudet
  https://www.instagram.com/reel/DZA2laVSjoQ/
  > "So as you guys know, I don't do consulting, but if I had to"
- · mid · 303v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DX5YgmPJSEq/
  > "As you can see, I'm not new to going viral, but here's three keys"
- ✗ flop · 18v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWFEkXPjBx6/
  > "Not to flex, but I'm pretty fucking good at social media. And if I"

---

## 7. TOOLKIT SWIPE FILE HANDOUT
**Tier:** C — over-used / high flop  ·  **N=32 reels · 5 creators · 25% win · 40% flop**
**Engagement (median):** 10,408 views · 244 likes · 91 shares · 0.85% share-rate · 1.39× own-median

**HOW IT'S PACKAGED:** Delivers a curated roster of copyable assets — named tools mapped to tasks, or plug-and-play templates/hooks/scripts the viewer can steal verbatim. The deliverable is the kit itself (tool-to-job pairings or template-then-example pairs), often capped with a comment-to-get-the-list CTA.

**VERBAL SIGNALS (how they actually say it):**
- "seven figure content toolkit"
- "use these for research, use these for scripting"
- "for writing Claude, for business advice Acquisition AI"
- "steal these five viral hooks"
- "the quickest way to X is by Y -> concrete example"
- "I use [tool] to find viral outliers"

**EVIDENCE** (32 reels, by views — real opening words quoted):
- · mid · 198,684v · 4,848L · 5,154sh · 2.59% · @personalbrandlaunch
  https://www.instagram.com/reel/DWrj3gUDwb-/
  > "I scroll for hours to find ideas. I use sandcastles.ai to find viral outlier"
- · mid · 195,312v · 5,100L · 3,353sh · 1.72% · @personalbrandlaunch
  https://www.instagram.com/reel/DYj0imohYWv/
  > "I ask AI to write me viral hooks. I have AI find viral outlier"
- · mid · 178,738v · 5,081L · 3,621sh · 2.03% · @personalbrandlaunch
  https://www.instagram.com/reel/DWToQzSCVl2/
  > "seven figure content toolkit. Use these for research. Use these for scripting. Use these"
- · mid · 110,975v · 3,033L · 1,291sh · 1.16% · @personalbrandlaunch
  https://www.instagram.com/reel/DWbWZ8xBfJ3/
  > "for writing and scripting. Claude, probably because it sounds mostly human. But I would"
- · mid · 108,574v · 2,757L · 1,606sh · 1.48% · @personalbrandlaunch
  https://www.instagram.com/reel/DX7X-AsiAZ1/
  > "Can you teach me a hundred viral hooks in 60 seconds? Ready, set, go."
- · mid · 40,612v · 1,179L · 430sh · 1.06% · @sam.gaudet
  https://www.instagram.com/reel/DVtPZaUEpSj/
  > "Editing videos. CapCut with AI captions. B-roll creation. Cling AI. Project management. Notion AI,"
- ✅ winner · 31,186v · 485L · 800sh · 2.57% · @alinamerkelcoach
  https://www.instagram.com/reel/DY8LM_NtVoF/
  > "10 hooks that always work. The fastest way to result is not what you"
- · mid · 29,175v · 861L · 283sh · 0.97% · @sam.gaudet
  https://www.instagram.com/reel/DYPbJ8JSkpH/
  > "Editing videos. CapCut with AI captions. B-roll creation. Cling AI. Project management. Notion AI,"
- ✅ winner · 26,109v · 367L · 580sh · 2.22% · @alinamerkelcoach
  https://www.instagram.com/reel/DY-n_p9tdTm/
  > "Don't ask ChargePT to give you content ideas. Instead, use this prompt. Please do"
- · mid · 21,203v · 540L · 156sh · 0.74% · @sam.gaudet
  https://www.instagram.com/reel/DWWhX5Hgdzs/
  > "Never ever post content until you've used these five AI tools. For writing, use"
- · mid · 20,334v · 533L · 98sh · 0.48% · @sam.gaudet
  https://www.instagram.com/reel/DWmSYEGyLr8/
  > "If you're asking AI to make you viral videos, you're never gonna actually get"
- · mid · 17,703v · 335L · 383sh · 2.16% · @alinamerkelcoach
  https://www.instagram.com/reel/DWglY97jdzT/
  > "Don't ask ChargePT to give you content ideas. Instead, use this prompt. Please do"
- · mid · 15,015v · 342L · 68sh · 0.45% · @sam.gaudet
  https://www.instagram.com/reel/DYw8gWxS0fJ/
  > "If you're using ChatGPT to come up with content ideas, you'll probably sound like"
- ✅ winner · 11,070v · 343L · 193sh · 1.74% · @iamaayushswamy
  https://www.instagram.com/reel/DW97ZtfgTeC/
  > "Here's how to turn one shitty idea into 7 viral hooks for your next"
- ✅ winner · 11,035v · 265L · 129sh · 1.17% · @iamaayushswamy
  https://www.instagram.com/reel/DWVI0l9DMEh/
  > "Why the fuck is it so hard to write a good hook? Well, good"
- ✅ winner · 10,612v · 224L · 152sh · 1.43% · @iamaayushswamy
  https://www.instagram.com/reel/DWw6T2LEinM/
  > "Steal these five viral hooks. X is great, but it's really dangerous. Buying a"
- ✗ flop · 10,205v · 304L · 186sh · 1.82% · @devinjatho
  https://www.instagram.com/reel/DWL9BwjEri4/
  > "These right here are the top five hooks to go viral in March, starting"
- ✅ winner · 8,536v · 179L · 85sh · 1.0% · @iamaayushswamy
  https://www.instagram.com/reel/DXhz-VoDLQp/
  > "Creators won't stop using these five bottle hooks because they're getting millions of views."
- ✅ winner · 5,798v · 83L · 25sh · 0.43% · @iamaayushswamy
  https://www.instagram.com/reel/DX2b1pDyAcx/
  > "Steely's five viral hooks. I have a X for ya. I have a townhome"
- ✗ flop · 3,869v · 76L · 56sh · 1.45% · @devinjatho
  https://www.instagram.com/reel/DWL9NzlEuXy/
  > "If you wanna go viral this month, then steal these five viral hooks for"
- ✗ flop · 2,605v · 24L · 10sh · 0.38% · @sam.gaudet
  https://www.instagram.com/reel/DWOoVwxSsQU/
  > "For research, it used to be Reddit, now it's Sandcastle's AI. For scripting, it"
- ✅ winner · 1,900v · 18L · 13sh · 0.68% · @iamaayushswamy
  https://www.instagram.com/reel/DWmbpDrjLGF/
  > "You are ruining your content if your background music doesn't match your video. Steal"
- ✗ flop · 631v · 6L · 1sh · 0.16% · @sam.gaudet
  https://www.instagram.com/reel/DWSLiR6Bv1x/
  > "Never ever post content until you've used these five AI tools. For writing, use"
- ✗ flop · 160v · 0L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DVma7Wdj7G5/
  > "Editing videos. CapCut with AI captions. B-roll creation. Cling AI. Project management. Notion AI,"
- ✗ flop · 118v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWZVk7bjIef/
  > "Every time you get a new follower, send them this exact message to turn"
- ✗ flop · 10v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWzcsTxjA8I/
  > "Have you ever heard your recorded voice and absolutely hate it? And the truth"
- ✗ flop · 8v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWzL1CODLjx/
  > "five fitness creators who are crushing it on social media that you should be"
- ✗ flop · 6v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWZiuqSjCL1/
  > "Steal these five viral hooks. This looks dangerous, but it will blow your mind."
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWmFn4wDF-F/
  > "All of these viral videos have the same exact hook. What if I told"
- ✗ flop · 1v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWPPCyHjI6V/
  > "One of the biggest scams in content creation is crazy video editing. See, videos"
- ✗ flop · 1v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWrWNVojGMc/
  > "Steal these five viral hooks. You want to get rid of x, then stop"
- ✗ flop · 0v · 1L · 0sh · 0% · @iamaayushswamy
  https://www.instagram.com/reel/DWHac7qDAVd/
  > "Why the f**k is it so hard to write a good hook? Well, good"

---

## 8. ANNOTATED TEARDOWN DEMO
**Tier:** B — works, execution-dependent  ·  **N=46 reels · 8 creators · 19% win · 30% flop**
**Engagement (median):** 14,144 views · 215 likes · 43 shares · 0.33% share-rate · 1.01× own-median

**HOW IT'S PACKAGED:** Dissects existing on-screen content or screen real estate, alternating between showing a beat/zone and inserting an analytical label for why it works or where things go. Covers both line-by-line video teardowns (content fragment -> technique name) and spatial diagram demos (pointing at frame zones like the safe zone or hook placement). Teaches by annotated autopsy.

**VERBAL SIGNALS (how they actually say it):**
- "this creates an open loop / borrows interest"
- "that's a micro commitment"
- "negative power word combined with visual hook"
- "this is your safe zone, this is the area to avoid"
- "this is where the hook goes, this is where the caption goes"
- "let me break down why this video works"

**EVIDENCE** (46 reels, by views — real opening words quoted):
- ✅ winner · 768,857v · 16,343L · 18,682sh · 2.43% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYRa7qQqtSc/
  > "This is your safe zone, and this is the area you should avoid. This"
- ✅ winner · 311,153v · 5,650L · 5,881sh · 1.89% · @bhavinipanjwanii
  https://www.instagram.com/reel/DY4p39tskeY/
  > "This is your safe zone, and this is the area you should avoid. This"
- ✅ winner · 301,749v · 3,058L · 3,798sh · 1.26% · @alinamerkelcoach
  https://www.instagram.com/reel/DXPmVbwNZQm/
  > "this means your video sucks, this means you have a bad hook, this means"
- · mid · 72,264v · 1,500L · 763sh · 1.06% · @personalbrandlaunch
  https://www.instagram.com/reel/DWjFZjkkQTu/
  > "This hook structure is going very viral right now. Just check this out. It"
- · mid · 56,666v · 954L · 416sh · 0.73% · @personalbrandlaunch
  https://www.instagram.com/reel/DV8cxKQjaIn/
  > "This one hook structure has been going viral. It goes like this. If you"
- · mid · 50,712v · 860L · 173sh · 0.34% · @personalbrandlaunch
  https://www.instagram.com/reel/DXbukSOIOEk/
  > "OK, so I was on a podcast once and the host literally tested me"
- · mid · 45,188v · 638L · 119sh · 0.26% · @personalbrandlaunch
  https://www.instagram.com/reel/DWELtskgFH9/
  > "So this creator posted this video and it blew up. And because he's smart,"
- ✅ winner · 42,497v · 619L · 111sh · 0.26% · @realskytan
  https://www.instagram.com/reel/DV4UKFMiQFK/
  > "Textbook attracts her avatar. B-roll every half second timed to the beat. Shows progress,"
- ✅ winner · 39,505v · 576L · 301sh · 0.76% · @loganforsyth
  https://www.instagram.com/reel/DZD9z5TiDNw/
  > "I'm carving the Diamond District grounds with the first ever diamond knuckles and they're"
- ✅ winner · 38,266v · 555L · 107sh · 0.28% · @iamaayushswamy
  https://www.instagram.com/reel/DW7b_O1j_Vu/
  > "this is a visual hook this is a visual hook this is a visual"
- ✅ winner · 36,297v · 521L · 114sh · 0.31% · @realskytan
  https://www.instagram.com/reel/DV2RDB-kcFb/
  > "Uh, I need somebody to explain to me why I can eat bread in"
- · mid · 29,929v · 702L · 179sh · 0.6% · @sam.gaudet
  https://www.instagram.com/reel/DWouxBLyGKW/
  > "This means you have a bad hook. This means you have a bad payoff"
- · mid · 29,192v · 762L · 204sh · 0.7% · @sam.gaudet
  https://www.instagram.com/reel/DWtu-iJAHm6/
  > "This is your go zone, and this is your no zone. Your eye line"
- · mid · 28,666v · 488L · 210sh · 0.73% · @realskytan
  https://www.instagram.com/reel/DWW4iswAt1j/
  > "science leverages credibility shows that you need to be extreme leans closer to phone"
- · mid · 26,427v · 213L · 59sh · 0.22% · @realskytan
  https://www.instagram.com/reel/DWSBupZgiqM/
  > "So y'all better be taking notes because I'm about to give you the game"
- · mid · 24,546v · 258L · 78sh · 0.32% · @realskytan
  https://www.instagram.com/reel/DWcw6f8CYuZ/
  > "Good visual hook. What's actually in your Starbucks paper cup. It's a plastic cup."
- · mid · 21,162v · 579L · 84sh · 0.4% · @sam.gaudet
  https://www.instagram.com/reel/DWePGNjS21f/
  > "Did you know statistically? Curiosity hook, asking a question. Richest people in the world."
- · mid · 20,669v · 186L · 30sh · 0.15% · @realskytan
  https://www.instagram.com/reel/DYBGHm9ilSV/
  > "So you've seen the Mont Texture tool all over your feed, but what is"
- · mid · 17,089v · 471L · 82sh · 0.48% · @sam.gaudet
  https://www.instagram.com/reel/DW4Ny1oS9jf/
  > "The education system. Broad topic. As we know it today is done. Contrary intake."
- · mid · 16,336v · 403L · 41sh · 0.25% · @sam.gaudet
  https://www.instagram.com/reel/DYAC79fSbvn/
  > "I can tell how crappy it is. Swear word pattern interrupt. Company is. Topic"
- · mid · 15,314v · 194L · 17sh · 0.11% · @realskytan
  https://www.instagram.com/reel/DX8hw3li6df/
  > "Never go through the airport scanner. Humans have negative bias. You can always opt"
- · mid · 15,143v · 133L · 20sh · 0.13% · @realskytan
  https://www.instagram.com/reel/DZBucnniEtr/
  > "Sometimes when I look in the mirror, I'd feel both fat and small at"
- · mid · 14,698v · 427L · 34sh · 0.23% · @sam.gaudet
  https://www.instagram.com/reel/DXjwpHsS1pX/
  > "People are like what's more important your wife being happier kids being happy We"
- · mid · 13,590v · 200L · 88sh · 0.65% · @bhavinipanjwanii
  https://www.instagram.com/reel/DYmGqDfg1Va/
  > "This means your hook didn't hook. This means your content got overlooked. This means"
- · mid · 11,898v · 268L · 48sh · 0.4% · @realskytan
  https://www.instagram.com/reel/DYX_JqaCe5g/
  > "Brian Johnson should fire his marketing team so they can come work for me"
- · mid · 11,641v · 263L · 34sh · 0.29% · @sam.gaudet
  https://www.instagram.com/reel/DXPJs65yV_V/
  > "Have you noticed in ChatGPT? Curiosity hook asking a question plus using ChatGPT as"
- · mid · 11,201v · 218L · 45sh · 0.4% · @realskytan
  https://www.instagram.com/reel/DYA5WMyiNGN/
  > "I'm Hank and eight months ago, I quit my nine to five job to"
- · mid · 11,003v · 244L · 140sh · 1.27% · @alinamerkelcoach
  https://www.instagram.com/reel/DYVLRoltTmi/
  > "Never put your text here or down here. Do put your hook up here"
- · mid · 6,771v · 79L · 49sh · 0.72% · @alinamerkelcoach
  https://www.instagram.com/reel/DW3vIUSN7Ty/
  > "Avoid the edges and keep everything inside the safe zone. Keep your face well"
- ✅ winner · 6,259v · 112L · 38sh · 0.61% · @iamaayushswamy
  https://www.instagram.com/reel/DY97BtvMhF_/
  > "This is where you should be centered here, here, and here is where your"
- ✗ flop · 5,749v · 127L · 12sh · 0.21% · @devinjatho
  https://www.instagram.com/reel/DY4zuG5SZj8/
  > "Never transfer your home into your kid's name or leave it to them in"
- · mid · 4,684v · 116L · 28sh · 0.6% · @alinamerkelcoach
  https://www.instagram.com/reel/DV9KbBljS3W/
  > "Eyes slightly above center. Not too high, not too low. Avoid the edges and"
- ✗ flop · 3,541v · 56L · 30sh · 0.85% · @realskytan
  https://www.instagram.com/reel/DWo2hFFCb1y/
  > "Most people can't last 30 seconds in a sexual innuendo in a dead hang."
- ✗ flop · 3,074v · 58L · 35sh · 1.14% · @realskytan
  https://www.instagram.com/reel/DV4TjIwklJo/
  > "science leverages credibility shows that you need to be extreme leans closer to phone"
- ✗ flop · 2,680v · 49L · 36sh · 1.34% · @realskytan
  https://www.instagram.com/reel/DWpJYSfknZa/
  > "What? It's cool. Camera's off. Good pattern interrupt. Yeah, we're re- Oh man. Steel"
- ✗ flop · 1,421v · 28L · 1sh · 0.07% · @devinjatho
  https://www.instagram.com/reel/DY4z__1SZK9/
  > "Never transfer your home into your kid's name or leave it to them in"
- ✗ flop · 1,408v · 21L · 2sh · 0.14% · @sam.gaudet
  https://www.instagram.com/reel/DY6J8R6S3E9/
  > "People are like what's more important your wife being happier kids being happy We"
- ✗ flop · 1,238v · 23L · 3sh · 0.24% · @realskytan
  https://www.instagram.com/reel/DWo2_BriUPq/
  > "Neuroscience leverages a popular topic for a female audience, shows that the law of"
- ✅ winner · 812v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW4itZ-jJvp/
  > "This is where your face should be, this is where your captions should be,"
- ✗ flop · 741v · 3L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV8efrQjQ6S/
  > "Avoid the edges and keep everything inside the safe zone. Eyes slightly above center."
- ✗ flop · 680v · 5L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DX9tGKJSMed/
  > "I can tell how crappy it is. Swear word pattern interrupt. Company is. Topic"
- ✗ flop · 590v · 17L · 3sh · 0.51% · @realskytan
  https://www.instagram.com/reel/DYTx9wLCnKQ/
  > "Brian Johnson should fire his marketing team so they can come work for me"
- ✗ flop · 284v · 4L · 0sh · 0.0% · @devinjatho
  https://www.instagram.com/reel/DY4z8q8yOtR/
  > "Never transfer your home into your kid's name, or leave it to them in"
- ✗ flop · 17v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWzVhd0DA68/
  > "You are ruining your videos if you are not in the Insta safe zone."
- ✗ flop · 10v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWrqQevjJgS/
  > "If you dead hang for 30 seconds, this is a visual hook. Eggs, fruit,"
- ✗ flop · 4v · 0L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWo_zrXjFUi/
  > "How to Create Bulletproof Knees This video got 880,000 views, and I'm going to"

---

## 9. OFFER CTA PROMO
**Tier:** A — solid, reliable  ·  **N=18 reels · 5 creators · 27% win · 16% flop**
**Engagement (median):** 26,024 views · 912 likes · 446 shares · 1.33% share-rate · 1.42× own-median

**HOW IT'S PACKAGED:** The reel's primary architecture is a pitch — it exists mainly to drive a comment/DM/keyword action for a free resource, lead magnet, or service, with teaching reduced to a teaser. The give-to-get conversion IS the substance, distinct from reels that merely append a CTA to real content.

**VERBAL SIGNALS (how they actually say it):**
- "comment X and I'll send it to you"
- "comment SMM for more information"
- "DM me the word / comment ready and I'll send the prompt"
- "I made a free library / guide / prompt"
- "we will research, script, edit, and upload for you"
- "comment the word song and I'll send it"

**EVIDENCE** (18 reels, by views — real opening words quoted):
- ✅ winner · 1,720,374v · 37,444L · 44,125sh · 2.56% · @personalbrandlaunch
  https://www.instagram.com/reel/DWBm-iAlZb4/
  > "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Business Center is looking to grow and"
- ✅ winner · 509,959v · 22,863L · 10,748sh · 2.11% · @devinjatho
  https://www.instagram.com/reel/DYM77_bSI0J/
  > "These background songs go viral time and time again. Use them in your next"
- ✅ winner · 277,926v · 4,786L · 8,761sh · 3.15% · @alinamerkelcoach
  https://www.instagram.com/reel/DWq2mazNwlP/
  > "Instagram just dropped its own AI growth tool that big creators are already using"
- · mid · 164,307v · 2,754L · 2,371sh · 1.44% · @personalbrandlaunch
  https://www.instagram.com/reel/DYuHqwkBCYi/
  > "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Business owners looking to grow and sell"
- · mid · 107,890v · 1,547L · 1,047sh · 0.97% · @personalbrandlaunch
  https://www.instagram.com/reel/DW7AntnDyBg/
  > "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Follow for more social media marketing education."
- · mid · 101,623v · 1,629L · 499sh · 0.49% · @personalbrandlaunch
  https://www.instagram.com/reel/DYhP26ewTAQ/
  > "this is my video, and this is my script. This is my video, and"
- · mid · 85,721v · 1,565L · 449sh · 0.52% · @personalbrandlaunch
  https://www.instagram.com/reel/DWrDHg2jeyO/
  > "This is my video and this is my script for that video. This is"
- · mid · 30,468v · 1,306L · 746sh · 2.45% · @devinjatho
  https://www.instagram.com/reel/DX_96kVSAq_/
  > "These background songs go viral time and time again. Use them in your next"
- · mid · 27,318v · 929L · 366sh · 1.34% · @devinjatho
  https://www.instagram.com/reel/DYpZKuFyHfz/
  > "These background songs go viral time and time again. Use them in your next"
- ✅ winner · 24,730v · 387L · 443sh · 1.79% · @alinamerkelcoach
  https://www.instagram.com/reel/DZBB2tRtOK0/
  > "Instagram just dropped its own AI growth tool that big creators are already using"
- · mid · 24,667v · 895L · 491sh · 1.99% · @devinjatho
  https://www.instagram.com/reel/DX_-cwXyxh_/
  > "These background songs go viral time and time again. Use them in your next"
- · mid · 18,493v · 457L · 207sh · 1.12% · @sam.gaudet
  https://www.instagram.com/reel/DV1X9h1D5cM/
  > "www.marcoparet.com Learn more on our channel!"
- · mid · 18,250v · 318L · 204sh · 1.12% · @alinamerkelcoach
  https://www.instagram.com/reel/DYfa9KyNrEu/
  > "Here's a new AI Instagram growth tool verified by Meta that big creators are"
- ✅ winner · 17,898v · 455L · 377sh · 2.11% · @iamaayushswamy
  https://www.instagram.com/reel/DYpxb7ThGkP/
  > "What happens when you hire me as your content marketer? First, you'll be given"
- · mid · 15,984v · 205L · 106sh · 0.66% · @alinamerkelcoach
  https://www.instagram.com/reel/DX7X6EZtER-/
  > "How to edit videos in 10 seconds There's a tool that edits reels for"
- ✗ flop · 10,137v · 301L · 133sh · 1.31% · @devinjatho
  https://www.instagram.com/reel/DX_-oKyy4l_/
  > "These background songs go viral time and time again. Use them in your next"
- ✗ flop · 8v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWHhZGAjB9m/
  > "I've created three high-performing video templates that I usually charge my clients anywhere from"
- ✗ flop · 5v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWW4QNBjIo5/
  > "Everyone wants to get their first viral video, but where the fuck do you"

---

## 10. MYTH BUST DIRECTIVE
**Tier:** C — over-used / high flop  ·  **N=57 reels · 7 creators · 21% win · 40% flop**
**Engagement (median):** 6,868 views · 142 likes · 24 shares · 0.27% share-rate · 0.72× own-median

**HOW IT'S PACKAGED:** The payload is a correction or command: it either names a widely-held belief/common practice and overturns it with the 'real' truth ('everyone says X, actually Y'), or issues a blunt imperative rule ('stop doing X', 'never post until Y', 'you'll never go viral unless Z'). Low on step-detail — the value is the reversal or mandate itself.

**VERBAL SIGNALS (how they actually say it):**
- "everyone tells you X but no one shows you how"
- "most creators think X, actually Y"
- "stop using hooks like / never post until you fix"
- "you will never go viral if you don't"
- "delete your highlights if they look like this"
- "the dumb creators do X, the smart creators do Y"

**EVIDENCE** (57 reels, by views — real opening words quoted):
- ✅ winner · 2,153,990v · 52,627L · 7,941sh · 0.37% · @devinjatho
  https://www.instagram.com/reel/DY5rxTQSxLy/
  > "You will never go viral if you don't learn how to speak on camera."
- ✅ winner · 326,444v · 6,740L · 611sh · 0.19% · @devinjatho
  https://www.instagram.com/reel/DZD6ivySIP0/
  > "You will never go viral if you don't learn how to speak on camera."
- ✅ winner · 131,109v · 826L · 1,189sh · 0.91% · @alinamerkelcoach
  https://www.instagram.com/reel/DXci7n2tu8x/
  > "Delete your highlights if they look like this. Instead, create highlights that make people"
- ✅ winner · 128,764v · 1,794L · 305sh · 0.24% · @devinjatho
  https://www.instagram.com/reel/DZD6v0HyxSQ/
  > "You will never go viral if you don't learn how to speak on camera."
- ✅ winner · 121,455v · 2,555L · 317sh · 0.26% · @devinjatho
  https://www.instagram.com/reel/DZECbQvy7q7/
  > "You will never go viral if you don't learn how to speak on camera."
- · mid · 49,324v · 794L · 164sh · 0.33% · @personalbrandlaunch
  https://www.instagram.com/reel/DXHIGqYCUTl/
  > "Content yes or no. Let's go. Do hashtags matter? No, they're not gonna get"
- · mid · 48,627v · 952L · 636sh · 1.31% · @personalbrandlaunch
  https://www.instagram.com/reel/DX983Zok1cL/
  > "Stop creating content for your ideal customer if you actually want to grow on"
- · mid · 46,692v · 1,435L · 412sh · 0.88% · @sam.gaudet
  https://www.instagram.com/reel/DXMv2TQARog/
  > "Look, if you wanna get views and followers on social media and actually build"
- · mid · 34,797v · 1,093L · 144sh · 0.41% · @sam.gaudet
  https://www.instagram.com/reel/DYhg2_USZAH/
  > "All right, you guys asked for it. Five ways to ruin your personal brand."
- · mid · 24,591v · 678L · 181sh · 0.74% · @sam.gaudet
  https://www.instagram.com/reel/DWKKgF5hjN-/
  > "Post every single reel four times. If you posted a video 90 days ago"
- · mid · 23,031v · 914L · 117sh · 0.51% · @sam.gaudet
  https://www.instagram.com/reel/DYum_sESVsn/
  > "If I died and all my content was deleted, except for one video, I"
- ✅ winner · 21,572v · 487L · 131sh · 0.61% · @iamaayushswamy
  https://www.instagram.com/reel/DWr_zjugRc5/
  > "I'm about to get unfollowed for this, but fuck it. I'm going to tell"
- · mid · 21,173v · 633L · 231sh · 1.09% · @sam.gaudet
  https://www.instagram.com/reel/DY2KuOlyt4n/
  > "Post every single reel four times. If you posted a video 90 days ago"
- · mid · 21,049v · 747L · 133sh · 0.63% · @sam.gaudet
  https://www.instagram.com/reel/DXWxgglSpLP/
  > "your rich followers don't want to buy an outcome. They want to hear how"
- · mid · 18,975v · 602L · 63sh · 0.33% · @sam.gaudet
  https://www.instagram.com/reel/DYe3dHTSf-e/
  > "There's a specific type of content creator that AI is creating, and I think"
- · mid · 18,851v · 550L · 110sh · 0.58% · @sam.gaudet
  https://www.instagram.com/reel/DWT4cT0yMU7/
  > "Never, ever, ever think that a setting is going to help you go viral."
- · mid · 18,022v · 661L · 201sh · 1.12% · @sam.gaudet
  https://www.instagram.com/reel/DXrYxOKy5ol/
  > "If you wanna get views on social media, you're gonna have to start yapping"
- · mid · 15,604v · 540L · 97sh · 0.62% · @sam.gaudet
  https://www.instagram.com/reel/DYkCeOPyN3L/
  > "Stop saying hey guys in your content. Stop saying hey everyone. Stop saying hey"
- · mid · 14,951v · 393L · 108sh · 0.72% · @sam.gaudet
  https://www.instagram.com/reel/DY94zHGyMFk/
  > "Repurposing content is probably the worst piece of advice that you could ever follow"
- · mid · 14,927v · 572L · 174sh · 1.17% · @sam.gaudet
  https://www.instagram.com/reel/DW9R_anSXvI/
  > "Stop trying to come up with new content ideas and just repeat what actually"
- · mid · 14,112v · 445L · 24sh · 0.17% · @sam.gaudet
  https://www.instagram.com/reel/DYM6Oe4S0s3/
  > "Oh, Sam, the algorithm didn't like my videos. No, bro. The audience didn't like"
- · mid · 13,499v · 311L · 32sh · 0.24% · @sam.gaudet
  https://www.instagram.com/reel/DXJ26yvyPnv/
  > "If you're using chat GPT to write your video scripts, you're probably doing it"
- · mid · 12,480v · 400L · 57sh · 0.46% · @sam.gaudet
  https://www.instagram.com/reel/DWg4I45SpP_/
  > "Stop trying to build a personal brand and start doing cool shit and talking"
- · mid · 11,637v · 417L · 15sh · 0.13% · @sam.gaudet
  https://www.instagram.com/reel/DXhMPrCScQA/
  > "If you want to get more views and followers on social media, stop trying"
- · mid · 11,392v · 409L · 57sh · 0.5% · @sam.gaudet
  https://www.instagram.com/reel/DVqt_wkkuP3/
  > "Most creators don't run out of ideas, they run out of observations. The best"
- ✅ winner · 10,248v · 282L · 83sh · 0.81% · @iamaayushswamy
  https://www.instagram.com/reel/DYZiOoZMqsY/
  > "If you don't post at least two times per day, you will never, ever,"
- ✗ flop · 8,785v · 261L · 54sh · 0.61% · @devinjatho
  https://www.instagram.com/reel/DYx0HFvyITp/
  > "Stop using hooks in your videos like, here's my ultimate hack to steal my"
- ✗ flop · 7,370v · 251L · 20sh · 0.27% · @sam.gaudet
  https://www.instagram.com/reel/DY4or0eypyi/
  > "Most creators don't run out of ideas, they run out of observations. The best"
- · mid · 6,868v · 142L · 13sh · 0.19% · @realskytan
  https://www.instagram.com/reel/DYN4NIkC7mZ/
  > "Let me de-influence you from all the advice out there telling you to only"
- ✅ winner · 6,313v · 142L · 27sh · 0.43% · @iamaayushswamy
  https://www.instagram.com/reel/DY2ZslssZEs/
  > "I'm about to get unfollowed for this, but I'm going to tell you anyways"
- · mid · 5,991v · 102L · 39sh · 0.65% · @alinamerkelcoach
  https://www.instagram.com/reel/DXpm4hStmqp/
  > "Expert post every day. Expert get likes. Expert not make money. Expert sad. Expert"
- ✅ winner · 4,747v · 99L · 22sh · 0.46% · @iamaayushswamy
  https://www.instagram.com/reel/DYSX5EWsEEp/
  > "If you're constantly refreshing your feed the moment you post to see how many"
- ✅ winner · 3,798v · 61L · 40sh · 1.05% · @loganforsyth
  https://www.instagram.com/reel/DY3DMwSC2bi/
  > "The influencer era is officially dead. What I mean by that is the traditional"
- · mid · 3,382v · 37L · 12sh · 0.35% · @alinamerkelcoach
  https://www.instagram.com/reel/DWtcAevNcxn/
  > "If you're a coach, please stop selling $19-$50 low-ticket products if you don't want"
- ✗ flop · 2,015v · 14L · 2sh · 0.1% · @sam.gaudet
  https://www.instagram.com/reel/DXUvvIYvYZO/
  > "Hashtags are dead. They mattered in 2016, but they don't matter anymore We've gotten"
- ✗ flop · 1,547v · 29L · 5sh · 0.32% · @sam.gaudet
  https://www.instagram.com/reel/DYr8iWRSmhy/
  > "If I died and all my content was deleted, except for one video, I"
- ✅ winner · 1,421v · 34L · 3sh · 0.21% · @iamaayushswamy
  https://www.instagram.com/reel/DZG92YjMThI/
  > "It took me 10 years to realize that even though my videos were super"
- ✅ winner · 1,057v · 11L · 5sh · 0.47% · @loganforsyth
  https://www.instagram.com/reel/DYyTujQxhVm/
  > "Stop following this outdated content advice. There's two main pieces of content advice that"
- ✗ flop · 652v · 4L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DYqP9qZSGJm/
  > "Stop contrarian takes maxing. I've been seeing a lot of content creators online right"
- ✗ flop · 604v · 4L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DVnd9luEiMB/
  > "Most creators don't run out of ideas, they run out of observations. The best"
- ✗ flop · 524v · 3L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXXEI7CSCmw/
  > "I think a lot of people skip to building a personal brand without doing"
- ✗ flop · 516v · 1L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXWnsEgyEEV/
  > "your rich followers don't want to buy an outcome. They want to hear how"
- ✗ flop · 505v · 7L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DY796BqSbWN/
  > "Repurposing content is probably the worst piece of advice that you could ever follow"
- ✗ flop · 503v · 5L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXacSBtyrh6/
  > "I've grown my personal brand to over 40k followers without any fancy editing and"
- ✗ flop · 415v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DY92cA2S5tJ/
  > "Stop contrarian takes maxing. I've been seeing a lot of content creators online right"
- ✗ flop · 406v · 3L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXX-2EHPR3k/
  > "If you want to get more views and followers on social media, stop trying"
- ✗ flop · 283v · 1L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DWPGIrnyDv1/
  > "Never, ever, ever think that a setting is going to help you go viral."
- ✗ flop · 147v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DYDNJt1COsV/
  > "I made this mistake and brands everywhere are making this mistake and this is"
- ✗ flop · 139v · 1L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DV86OLWkhTG/
  > "Six things you should never say in content. Never say and, say but or"
- ✗ flop · 119v · 4L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DYDNQyICs9j/
  > "It's not what you say, it's how you say it. It's not about the"
- ✗ flop · 114v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DYDNAePidmt/
  > "It's not what you say, it's how you say it. It's not about the"
- ✗ flop · 92v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWCKMwODLqj/
  > "Stop using call to actions at the end of your videos like follow me"
- ✗ flop · 8v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWy9f4BDNqP/
  > "Never, ever, ever post those raw talking head videos like this. This is where"
- ✗ flop · 7v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW1pZ0LDDFm/
  > "Stop using call to actions at the end of your videos like follow me"
- ✗ flop · 4v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWwlqOyibnl/
  > "I'm about to get unfollowed for this, but fuck it. I'm going to tell"
- ✗ flop · 2v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW1wlAODISy/
  > "There are two types of shirts that will fuck up your videos. A white"
- ✗ flop · 2v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWoxQowDO-b/
  > "Never, ever, ever film content with your phone again. It'll look like dog shit."

---

## 11. CATEGORY TAXONOMY EXPLAINER
**Tier:** B — high reach, inconsistent (big hits + big flops)  ·  **N=47 reels · 5 creators · 14% win · 21% flop**
**Engagement (median):** 51,136 views · 1,005 likes · 437 shares · 0.98% share-rate · 1.0× own-median

**HOW IT'S PACKAGED:** Teaches by laying out a fixed classification — N named types/categories of a thing — and explaining each one's role, often mapping types to outcomes (views/followers/leads). The spine is 'there are X types of Y: type 1 is..., type 2 is...', a conceptual catalog rather than sequential actions or scored items.

**VERBAL SIGNALS (how they actually say it):**
- "There are five main types of content"
- "type number one is educational, number two storytelling"
- "TOFU / MOFU / BOFU"
- "six main types of educational posts"
- "these are the different types of viral sound effects"
- "recommended content types for this would be"

**EVIDENCE** (47 reels, by views — real opening words quoted):
- ✅ winner · 350,622v · 17,297L · 10,049sh · 2.87% · @personalbrandlaunch
  https://www.instagram.com/reel/DWOe5DnjLHF/
  > "These are the different types of viral sound effects that you can use in"
- ✅ winner · 304,477v · 10,628L · 8,870sh · 2.91% · @personalbrandlaunch
  https://www.instagram.com/reel/DVq-bkuAEPw/
  > "There are five main types of content that you should be posting. Oh my"
- · mid · 217,391v · 5,461L · 4,014sh · 1.85% · @personalbrandlaunch
  https://www.instagram.com/reel/DXui_NmjJyY/
  > "There are three types of content you should post. Tofu, top of funnel content."
- · mid · 157,196v · 3,914L · 3,121sh · 1.99% · @personalbrandlaunch
  https://www.instagram.com/reel/DW3rY49j1zy/
  > "What separates the business owners who blow up on social media from the ones"
- · mid · 142,243v · 5,161L · 2,947sh · 2.07% · @personalbrandlaunch
  https://www.instagram.com/reel/DWcGejSBMij/
  > "If you could only watch one video your entire life to know everything you"
- · mid · 136,403v · 3,947L · 2,562sh · 1.88% · @personalbrandlaunch
  https://www.instagram.com/reel/DVqbe2-jSF8/
  > "There are three types of content you should post. Tofu, top of funnel content,"
- · mid · 134,045v · 3,110L · 2,440sh · 1.82% · @personalbrandlaunch
  https://www.instagram.com/reel/DYE7J_YEzW5/
  > "Are you building a following? Or are you building a personal brand? There are"
- · mid · 113,323v · 2,548L · 1,529sh · 1.35% · @personalbrandlaunch
  https://www.instagram.com/reel/DWKE2OThq4g/
  > "I'm gonna pin my most viral videos. Wait, stop. What? This is the perfect"
- · mid · 108,127v · 2,737L · 1,969sh · 1.82% · @personalbrandlaunch
  https://www.instagram.com/reel/DYeqr1pNXid/
  > "Always remember, for educational posts, post common mistakes slash myths, step-by-step tutorials, comparisons, do"
- · mid · 105,217v · 2,428L · 1,895sh · 1.8% · @personalbrandlaunch
  https://www.instagram.com/reel/DWmbo4slSTq/
  > "All of these viral videos have the same exact structure. Remember, hoodie, messy bun."
- · mid · 90,748v · 2,235L · 1,053sh · 1.16% · @personalbrandlaunch
  https://www.instagram.com/reel/DXmxe9Jh9IE/
  > "Everybody has a niche on social media, but did you know that your niche"
- · mid · 86,706v · 2,440L · 2,622sh · 3.02% · @personalbrandlaunch
  https://www.instagram.com/reel/DXZ7EyPD_q9/
  > "These are the different types of viral sound effects that you can use in"
- · mid · 80,091v · 1,870L · 796sh · 0.99% · @personalbrandlaunch
  https://www.instagram.com/reel/DYPOkUPp6Vv/
  > "are all viral videos equal? Nope, there's a hierarchy. At the bottom, you have"
- · mid · 75,374v · 1,626L · 823sh · 1.09% · @personalbrandlaunch
  https://www.instagram.com/reel/DV_f2y3oMYa/
  > "Stop posting random content and start posting these structures instead. Number one, the hand"
- · mid · 74,025v · 1,220L · 683sh · 0.92% · @personalbrandlaunch
  https://www.instagram.com/reel/DVvlIBlDT6t/
  > "Tofu, MoFu, BoFu, ranking videos, storytelling videos about personal or business wins, losses, experiences,"
- · mid · 73,970v · 1,463L · 814sh · 1.1% · @personalbrandlaunch
  https://www.instagram.com/reel/DYCWMfeAaN-/
  > "Did you know that every viral video has seven different components? Number one, topic,"
- · mid · 71,940v · 1,416L · 754sh · 1.05% · @personalbrandlaunch
  https://www.instagram.com/reel/DY9kgjxhK_7/
  > "Remember, for yapping videos, use this visual hook, this visual hook, and this visual"
- · mid · 66,744v · 1,350L · 1,015sh · 1.52% · @personalbrandlaunch
  https://www.instagram.com/reel/DWuIEWdB38X/
  > "Educational Reels get trust, Storytelling Reels get followers, and Authority Reels get leads. Educational"
- · mid · 64,197v · 1,297L · 1,045sh · 1.63% · @personalbrandlaunch
  https://www.instagram.com/reel/DX4zL-kiRGz/
  > "There are four levels of awareness. You may be using the wrong one in"
- · mid · 64,053v · 1,577L · 661sh · 1.03% · @personalbrandlaunch
  https://www.instagram.com/reel/DV3uuU7BXxd/
  > "Use a low angle shot to build authority. Use an above angle shot for"
- · mid · 58,585v · 1,416L · 709sh · 1.21% · @personalbrandlaunch
  https://www.instagram.com/reel/DYMqbv1ONBD/
  > "Okay, this is the hierarchy of personal brands because trust me, they are not"
- · mid · 57,677v · 1,005L · 476sh · 0.83% · @personalbrandlaunch
  https://www.instagram.com/reel/DWL5kH_Bqeb/
  > "Educational Reels build trust. Storytelling Reels get followers. Authority Reels get leads. Educational Reels"
- · mid · 52,512v · 1,102L · 534sh · 1.02% · @personalbrandlaunch
  https://www.instagram.com/reel/DY4a9WWviWM/
  > "As a founder, there are two types of content you're gonna be posting if"
- · mid · 51,136v · 762L · 401sh · 0.78% · @personalbrandlaunch
  https://www.instagram.com/reel/DYIP5_Cj0ym/
  > "Everybody has a niche on social media, but did you know your niche falls"
- · mid · 49,375v · 955L · 437sh · 0.89% · @personalbrandlaunch
  https://www.instagram.com/reel/DX4DMYJnz3r/
  > "Okay, so how do you actually document what you're building on social media? Well,"
- · mid · 45,846v · 724L · 304sh · 0.66% · @personalbrandlaunch
  https://www.instagram.com/reel/DWv8vVjBRVy/
  > "If you're in a visual niche like this where people need to visually see"
- · mid · 44,040v · 746L · 328sh · 0.74% · @personalbrandlaunch
  https://www.instagram.com/reel/DV3TUQXhpuf/
  > "Did you know there are five different types of stories? Number one, personal stories."
- · mid · 43,905v · 721L · 243sh · 0.55% · @personalbrandlaunch
  https://www.instagram.com/reel/DWWNjebjP_3/
  > "Every video can be put into one of four quadrants. On the Y-axis, you"
- · mid · 31,821v · 1,365L · 241sh · 0.76% · @sam.gaudet
  https://www.instagram.com/reel/DYUtcX9ywxL/
  > "Social media will expose your friendships more than any other platform on this planet"
- ✗ flop · 27,881v · 369L · 194sh · 0.7% · @personalbrandlaunch
  https://www.instagram.com/reel/DZFS-IXhJXN/
  > "Remember, for visual niches, script videos in these structures, film videos in these formats."
- ✗ flop · 21,671v · 382L · 213sh · 0.98% · @personalbrandlaunch
  https://www.instagram.com/reel/DZH3ulkuuEc/
  > "This is a tutorial carousel. This is a right versus wrong or do versus"
- · mid · 17,436v · 497L · 56sh · 0.32% · @sam.gaudet
  https://www.instagram.com/reel/DVoWZKsEtyE/
  > "This is a curiosity hook. Is it possible to replace an entire SEO agency"
- ✅ winner · 16,936v · 265L · 151sh · 0.89% · @iamaayushswamy
  https://www.instagram.com/reel/DXqOPPvjGPo/
  > "Five content formats that will never fail. Overwrite comparison, important versus not important, cinematic"
- · mid · 14,463v · 321L · 242sh · 1.67% · @bhavinipanjwanii
  https://www.instagram.com/reel/DZE8h9QKlab/
  > "This is talking to the camera content. Do you want to know why some"
- ✅ winner · 10,628v · 122L · 33sh · 0.31% · @iamaayushswamy
  https://www.instagram.com/reel/DXZw7wAjNtN/
  > "Here are six topics you will get banned for talking about on social media"
- · mid · 9,747v · 271L · 13sh · 0.13% · @sam.gaudet
  https://www.instagram.com/reel/DWjWtNUg8_9/
  > "A lot of creators in the industry create personal brands that they actually hate"
- ✅ winner · 8,181v · 120L · 22sh · 0.27% · @iamaayushswamy
  https://www.instagram.com/reel/DXwqTopsnod/
  > "If you dead hang for 30 seconds, this is a visual hook. Eggs, fruit,"
- ✗ flop · 8,102v · 172L · 27sh · 0.33% · @sam.gaudet
  https://www.instagram.com/reel/DW4cKujD6C0/
  > "There is viral growth, where you get viral video, 30,000 followers. That's the kind"
- ✅ winner · 7,913v · 197L · 70sh · 0.88% · @iamaayushswamy
  https://www.instagram.com/reel/DWhs7plgTur/
  > "this video gets views reincarnated i was stargazing life goes on i need all"
- ✅ winner · 7,426v · 160L · 69sh · 0.93% · @iamaayushswamy
  https://www.instagram.com/reel/DXelK_aDqFX/
  > "If you need more views, followers, and reach, then you're at the bottom of"
- ✗ flop · 5,342v · 100L · 9sh · 0.17% · @realskytan
  https://www.instagram.com/reel/DY2SQvyCcTm/
  > "Let's talk about the most underrated part of building a personal brand. And it"
- ✗ flop · 271v · 2L · 0sh · 0.0% · @bhavinipanjwanii
  https://www.instagram.com/reel/DX3n4LEs5kM/
  > "Have you ever heard people saying, Day one of starting my own business. Day"
- ✗ flop · 153v · 0L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DVmsSneEqPl/
  > "This is a curiosity hook. Is it possible to replace an entire SEO agency"
- ✗ flop · 61v · 10L · 2sh · 3.28% · @iamaayushswamy
  https://www.instagram.com/reel/DWR5qPYDKkA/
  > "The difference between growing your following versus growing your personal brand is dictated by"
- ✗ flop · 17v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWg9TYPjOMR/
  > "This is the same piece of content, but from two different creators. What? Each"
- ✗ flop · 11v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWzEVdGDLQW/
  > "You are ruining your videos if you're not stealing what your competition is doing."
- ✗ flop · 4v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWoqoTTjAJc/
  > "There are five main types of content that you should be posting. Number one"

---

## 12. NUMBERED HOWTO TUTORIAL
**Tier:** C — over-used / high flop  ·  **N=121 reels · 8 creators · 18% win · 35% flop**
**Engagement (median):** 6,424 views · 110 likes · 39 shares · 0.59% share-rate · 0.85× own-median

**HOW IT'S PACKAGED:** A repeatable method or single tactic delivered as a concrete procedure the viewer can replicate — either an enumerated do-this-then-that list of steps/tips or one focused hack walked through start-to-finish. Distinguished from settings-walkthrough by not being in-app menu navigation, and from the reset-blueprint by having no counterfactual framing (just 'here's how').

**VERBAL SIGNALS (how they actually say it):**
- "Number one... Number two... Number three"
- "here's how / what you're going to do is"
- "all you have to do is"
- "the perfect formula for X"
- "explained in under 30 seconds"
- "the fastest way to double your views with no extra effort"

**EVIDENCE** (121 reels, by views — real opening words quoted):
- ✅ winner · 1,338,595v · 22,755L · 34,001sh · 2.54% · @alinamerkelcoach
  https://www.instagram.com/reel/DWTrZy8Oe_e/
  > "how to copy any video. Open CapCut as a free app, upload a video"
- ✅ winner · 521,470v · 17,244L · 17,942sh · 3.44% · @devinjatho
  https://www.instagram.com/reel/DVtNysZjc7I/
  > "Instagram just slapped their dick on the table with this new update. Because look,"
- ✅ winner · 220,761v · 5,907L · 4,666sh · 2.11% · @iamaayushswamy
  https://www.instagram.com/reel/DXPlUuDDNTk/
  > "This is the fastest way to double your views with no extra effort. Explained"
- · mid · 134,170v · 3,272L · 2,020sh · 1.51% · @personalbrandlaunch
  https://www.instagram.com/reel/DWyiV2IDwFN/
  > "What should people do after their first viral video? The dumb creators just do"
- · mid · 133,638v · 2,988L · 1,750sh · 1.31% · @personalbrandlaunch
  https://www.instagram.com/reel/DX9Sj-HO89h/
  > "How do you create a month worth of content ideas in 60 minutes? Step"
- · mid · 129,642v · 3,605L · 2,223sh · 1.71% · @personalbrandlaunch
  https://www.instagram.com/reel/DXAJmtDv3Er/
  > "I only have 45 minutes to plan an entire month of content. Okay, let's"
- · mid · 105,489v · 2,653L · 1,305sh · 1.24% · @personalbrandlaunch
  https://www.instagram.com/reel/DXO2pxSjHvx/
  > "Guys, viral yapping content is actually pretty pre-planned. So if you want your yaps"
- · mid · 104,830v · 2,703L · 362sh · 0.35% · @personalbrandlaunch
  https://www.instagram.com/reel/DY12vGYvi7J/
  > "Guys, I just learned my older audience does not know this. Sorry guys, I"
- · mid · 104,632v · 2,772L · 1,252sh · 1.2% · @personalbrandlaunch
  https://www.instagram.com/reel/DXcdyMxDEUJ/
  > "I just posted a new reel. Wait, really? Yep. Okay, you have to do"
- · mid · 104,005v · 2,030L · 571sh · 0.55% · @personalbrandlaunch
  https://www.instagram.com/reel/DVi1CaIDf2t/
  > "Why do creators always say follow MrBeast on Instagram? Then hit that follow button."
- · mid · 101,289v · 1,995L · 1,141sh · 1.13% · @personalbrandlaunch
  https://www.instagram.com/reel/DWR0KjUDxym/
  > "I do what's called the 5X rule. So I'm like, OK, if it gets"
- · mid · 84,528v · 1,638L · 679sh · 0.8% · @personalbrandlaunch
  https://www.instagram.com/reel/DWzRs7ZD1wi/
  > "What happens when you hire me as your social media manager? Step number one,"
- · mid · 83,836v · 1,943L · 1,495sh · 1.78% · @personalbrandlaunch
  https://www.instagram.com/reel/DWtX8PihOJ3/
  > "How to create a viral carousel in 60 seconds. Step number one, find your"
- · mid · 63,642v · 1,189L · 538sh · 0.85% · @personalbrandlaunch
  https://www.instagram.com/reel/DYmZtBsOZKF/
  > "Okay, so this slide deck format is really working for reals right now. Here's"
- · mid · 60,790v · 936L · 284sh · 0.47% · @personalbrandlaunch
  https://www.instagram.com/reel/DVlYjf3kRyG/
  > "This creator can make any video go viral, and so can this creator. Oh,"
- · mid · 58,140v · 1,077L · 512sh · 0.88% · @personalbrandlaunch
  https://www.instagram.com/reel/DX_xdW5DOeX/
  > "Here's how to turn one boring hook into four engaging ones. Now, there are"
- ✅ winner · 57,739v · 1,306L · 1,287sh · 2.23% · @sam.gaudet
  https://www.instagram.com/reel/DYCmHvXyEFp/
  > "Trial Reels aren't dead, you just don't understand how they work now. I've gotten"
- · mid · 47,732v · 688L · 222sh · 0.47% · @personalbrandlaunch
  https://www.instagram.com/reel/DX6n__8j7tZ/
  > "What is the 5X rule in content? Yeah, so that's basically what an outlier"
- · mid · 47,037v · 2,144L · 758sh · 1.61% · @sam.gaudet
  https://www.instagram.com/reel/DXAYIFxStd5/
  > "Content Maxing 101, post daily, ideally one to two times a day. Record weekly,"
- · mid · 46,088v · 1,231L · 582sh · 1.26% · @sam.gaudet
  https://www.instagram.com/reel/DXmXZTOyBE1/
  > "So ClogCode just started replacing low-level video editors. I'm gonna show you exactly how"
- ✅ winner · 43,506v · 876L · 1,167sh · 2.68% · @alinamerkelcoach
  https://www.instagram.com/reel/DXxRQ5stDeI/
  > "What's going viral this week? Carbohydrate good. Woman eat salad. Woman tired. Here's a"
- · mid · 42,903v · 741L · 217sh · 0.51% · @personalbrandlaunch
  https://www.instagram.com/reel/DXtwj_3Dk-2/
  > "10 things I learned from hitting one million followers. Research and find viral outlier"
- · mid · 42,356v · 581L · 144sh · 0.34% · @personalbrandlaunch
  https://www.instagram.com/reel/DWoOaGBDrEv/
  > "Did you notice when big creators go viral, they just recreate that video over"
- · mid · 41,704v · 625L · 169sh · 0.41% · @personalbrandlaunch
  https://www.instagram.com/reel/DXXVbRnkUN_/
  > "So if you get a video that performs well, there's actually two specific ways"
- · mid · 39,827v · 1,062L · 323sh · 0.81% · @sam.gaudet
  https://www.instagram.com/reel/DWzbFQwyYoJ/
  > "Most people make content backwards because they expect to get viral videos without having"
- · mid · 37,802v · 1,033L · 410sh · 1.08% · @sam.gaudet
  https://www.instagram.com/reel/DXCO8h3S16t/
  > "Cloud Code just started replacing editors and I'm gonna show you exactly how to"
- ✅ winner · 35,590v · 1,313L · 711sh · 2.0% · @realskytan
  https://www.instagram.com/reel/DYOLB7BCSC3/
  > "Let's plan your next 30 days worth of content in 30 minutes. It's called"
- · mid · 33,398v · 1,006L · 377sh · 1.13% · @sam.gaudet
  https://www.instagram.com/reel/DYSJgUWyHb1/
  > "I think I completely cracked yapmaxing, and I'm gonna share with you the exact"
- · mid · 31,356v · 1,153L · 365sh · 1.16% · @sam.gaudet
  https://www.instagram.com/reel/DWMLJTiS_iI/
  > "If you wanna get views on social media, you're gonna have to start yapping"
- · mid · 29,903v · 760L · 339sh · 1.13% · @sam.gaudet
  https://www.instagram.com/reel/DWOvlgzytMg/
  > "Yo, this trial reel hack should be illegal. I've helped Dan Martell get over"
- · mid · 29,562v · 809L · 491sh · 1.66% · @sam.gaudet
  https://www.instagram.com/reel/DVjGY5QEoBq/
  > "Can you actually replace your entire thumbnail designer team with one simple tool and"
- · mid · 25,275v · 795L · 241sh · 0.95% · @sam.gaudet
  https://www.instagram.com/reel/DWHCzK-gjMb/
  > "All right, let me put you on some game that nobody else in the"
- · mid · 23,253v · 869L · 241sh · 1.04% · @sam.gaudet
  https://www.instagram.com/reel/DYIQurZP7S3/
  > "I helped Dan Martell go from 100K followers to over 10 million across all"
- · mid · 22,364v · 575L · 188sh · 0.84% · @sam.gaudet
  https://www.instagram.com/reel/DYmnokAS6SR/
  > "This means you have a bad hook. This means you have a bad payoff"
- ✅ winner · 20,670v · 583L · 225sh · 1.09% · @iamaayushswamy
  https://www.instagram.com/reel/DW17e0_kuKx/
  > "How do you make fake comments like this? Well, double tap it real quick"
- · mid · 20,189v · 548L · 127sh · 0.63% · @sam.gaudet
  https://www.instagram.com/reel/DV09JnPEl_W/
  > "Is it possible to make viral videos in 2026 using AI? Yes, but there's"
- · mid · 18,982v · 612L · 248sh · 1.31% · @sam.gaudet
  https://www.instagram.com/reel/DXzaMRLyRoJ/
  > "Let me put you on some game that nobody else in the YouTube space"
- · mid · 15,633v · 467L · 142sh · 0.91% · @sam.gaudet
  https://www.instagram.com/reel/DX48bulyxJD/
  > "In 2026, if you make a video that performs really well on organic, just"
- · mid · 14,977v · 458L · 108sh · 0.72% · @sam.gaudet
  https://www.instagram.com/reel/DYFRifpyFe4/
  > "If you want your videos to perform on social media and stop guessing if"
- · mid · 14,949v · 312L · 87sh · 0.58% · @realskytan
  https://www.instagram.com/reel/DXziY8fi0B1/
  > "Good content isn't creative, good content is operationalized. The best creators aren't the best"
- ✅ winner · 13,884v · 240L · 139sh · 1.0% · @iamaayushswamy
  https://www.instagram.com/reel/DX8BEhcpF-J/
  > "If your views look like this or like this, your account isn't cooked, you're"
- · mid · 13,856v · 500L · 149sh · 1.08% · @sam.gaudet
  https://www.instagram.com/reel/DXo6HtbyMD8/
  > "All right, HookMaxi101, if you're posting content but nobody's watching, it's not because your"
- ✅ winner · 13,636v · 391L · 192sh · 1.41% · @iamaayushswamy
  https://www.instagram.com/reel/DYKvLOmPxzG/
  > "If your content looks like this, you're signaling low value. But if it looks"
- · mid · 13,172v · 251L · 96sh · 0.73% · @sam.gaudet
  https://www.instagram.com/reel/DZAxmlpylTk/
  > "This AI tool just started replacing low level designers and I'm gonna show you"
- · mid · 12,785v · 251L · 78sh · 0.61% · @bhavinipanjwanii
  https://www.instagram.com/reel/DXEOlIljY95/
  > "Have you ever heard people saying day one of starting my own business, day"
- · mid · 12,623v · 422L · 42sh · 0.33% · @sam.gaudet
  https://www.instagram.com/reel/DXuD-snEsmq/
  > "Good ideas fail on social media because they're explained before they're felt. Viewers need"
- ✅ winner · 12,498v · 189L · 69sh · 0.55% · @iamaayushswamy
  https://www.instagram.com/reel/DXrbnI9jLwG/
  > "Stop using profile pictures like this if you want your IG to look more"
- · mid · 12,258v · 167L · 89sh · 0.73% · @alinamerkelcoach
  https://www.instagram.com/reel/DXEw2lSNcQw/
  > "Let me show you how to change your lighting from this to this. I'll"
- ✅ winner · 11,765v · 362L · 87sh · 0.74% · @iamaayushswamy
  https://www.instagram.com/reel/DYDA9RmMvm4/
  > "One of the biggest scams in content creation is crazy video editing. See, videos"
- · mid · 11,615v · 265L · 93sh · 0.8% · @sam.gaudet
  https://www.instagram.com/reel/DZF7u70p4Is/
  > "Is it possible to make viral videos in 2026 using AI? Yes, but there's"
- ✅ winner · 10,296v · 253L · 111sh · 1.08% · @iamaayushswamy
  https://www.instagram.com/reel/DYn5N4UM80M/
  > "If your views look like this, or like this, your account isn't cooked. You're"
- · mid · 9,760v · 163L · 107sh · 1.1% · @alinamerkelcoach
  https://www.instagram.com/reel/DXr-j6QNOGi/
  > "Best hack if you're recording talking head reels. I used to spend 30 minutes"
- ✅ winner · 8,552v · 247L · 68sh · 0.8% · @iamaayushswamy
  https://www.instagram.com/reel/DXHlQGrjNfy/
  > "In order to make world-class content that gets you views and sales, you need"
- · mid · 8,550v · 127L · 28sh · 0.33% · @realskytan
  https://www.instagram.com/reel/DYaNKCHCtkr/
  > "Five things you need to do to go viral. Use formats, use visual hook,"
- ✅ winner · 7,972v · 207L · 102sh · 1.28% · @iamaayushswamy
  https://www.instagram.com/reel/DXpRq5zDENI/
  > "To post every day, you don't need to create every day. I've spent the"
- · mid · 7,084v · 87L · 42sh · 0.59% · @alinamerkelcoach
  https://www.instagram.com/reel/DWbcofQt3zw/
  > "Delete that video and post it again. If your video flopped, but you genuinely"
- ✅ winner · 6,813v · 188L · 39sh · 0.57% · @iamaayushswamy
  https://www.instagram.com/reel/DYQRlH4h_w8/
  > "If you don't change just one thing about your content, your Instagram will look"
- · mid · 6,610v · 120L · 59sh · 0.89% · @alinamerkelcoach
  https://www.instagram.com/reel/DYQP-nSNXtY/
  > "This trials hack got me 5,000 followers in one month. When you record a"
- · mid · 6,537v · 136L · 57sh · 0.87% · @alinamerkelcoach
  https://www.instagram.com/reel/DYiPxg4Nl3b/
  > "Three steps to batch record your B-roll so you always have content for reels."
- ✅ winner · 6,527v · 198L · 32sh · 0.49% · @iamaayushswamy
  https://www.instagram.com/reel/DXUrMBkiePr/
  > "10 things I've learned after generating over 500 million views, let's go. One, consistency"
- · mid · 6,424v · 122L · 13sh · 0.2% · @realskytan
  https://www.instagram.com/reel/DYXPjcLCFzX/
  > "If once upon a time you were pulling hundreds of thousands of views and"
- · mid · 5,894v · 98L · 65sh · 1.1% · @alinamerkelcoach
  https://www.instagram.com/reel/DWltiLvtK0A/
  > "This outfit is AI. Now you can record even in your pajamas and then"
- ✅ winner · 4,460v · 110L · 28sh · 0.63% · @iamaayushswamy
  https://www.instagram.com/reel/DY-X1Z7BxH9/
  > "Never in your fucking life wait for a client to send you a testimony"
- ✗ flop · 4,419v · 77L · 43sh · 0.97% · @devinjatho
  https://www.instagram.com/reel/DYqbCTtSK1g/
  > "If you post these three stories today, you will get to at least one"
- ✅ winner · 4,052v · 80L · 34sh · 0.84% · @iamaayushswamy
  https://www.instagram.com/reel/DY0fruQPC1y/
  > "I keep seeing fitness coaches making dog shit content, and as someone who has"
- ✗ flop · 3,888v · 66L · 44sh · 1.13% · @devinjatho
  https://www.instagram.com/reel/DYqbJoxyGdX/
  > "If you post these three stories today, you will get to at least one"
- · mid · 3,621v · 67L · 10sh · 0.28% · @alinamerkelcoach
  https://www.instagram.com/reel/DV4Ud8bjfiq/
  > "Don't stress about what to post today, just grab a video from three months"
- · mid · 3,413v · 49L · 9sh · 0.26% · @alinamerkelcoach
  https://www.instagram.com/reel/DWoXiW1NRNA/
  > "Reviewing my followers account on how to grow and make money from it. I"
- ✅ winner · 3,266v · 62L · 24sh · 0.73% · @iamaayushswamy
  https://www.instagram.com/reel/DY3HxYas7qm/
  > "Here are seven high IQ habits of a seven figure business owner that I"
- ✗ flop · 2,830v · 40L · 27sh · 0.95% · @alinamerkelcoach
  https://www.instagram.com/reel/DWgjd1AjUMr/
  > "You will never go viral if you continue using ChatGPT like this. Give me"
- ✗ flop · 2,078v · 50L · 21sh · 1.01% · @alinamerkelcoach
  https://www.instagram.com/reel/DWgjI-1DWWu/
  > "Don't ask ChargerPT to give you content ideas like this. Give me 10 content"
- ✗ flop · 1,965v · 22L · 15sh · 0.76% · @alinamerkelcoach
  https://www.instagram.com/reel/DWglHUWDRyQ/
  > "Stop using chatGPT like this if you want to go viral. Instead, use this"
- ✗ flop · 1,917v · 24L · 11sh · 0.57% · @devinjatho
  https://www.instagram.com/reel/DYqbUtqywxg/
  > "If you post these three stories today, you will get to at least one"
- ✗ flop · 1,765v · 13L · 3sh · 0.17% · @sam.gaudet
  https://www.instagram.com/reel/DWKxb6Ppyoh/
  > "If you wanna get views on social media, you're gonna have to start yapping"
- ✗ flop · 1,588v · 21L · 2sh · 0.13% · @devinjatho
  https://www.instagram.com/reel/DYrUHnYS39D/
  > "If you post these three stories TODAY, you will get to at least one"
- ✗ flop · 1,539v · 25L · 9sh · 0.58% · @sam.gaudet
  https://www.instagram.com/reel/DYfTQ5sy_Ts/
  > "All right, you guys asked for it. Five ways to ruin your personal brand."
- ✗ flop · 1,505v · 19L · 8sh · 0.53% · @sam.gaudet
  https://www.instagram.com/reel/DXAdkdSyugP/
  > "Cloud Code just started replacing editors and I'm gonna show you exactly how to"
- ✅ winner · 1,342v · 27L · 24sh · 1.79% · @iamaayushswamy
  https://www.instagram.com/reel/DYLvlz_M-nY/
  > "If your content looks like this, you're signaling low value. But if it looks"
- ✅ winner · 1,287v · 22L · 20sh · 1.55% · @iamaayushswamy
  https://www.instagram.com/reel/DX8A6bhJN3D/
  > "If your views look like this or like this, your account isn't cooked, you're"
- ✗ flop · 1,256v · 18L · 8sh · 0.64% · @sam.gaudet
  https://www.instagram.com/reel/DY3payYSujB/
  > "All right, let me put you on some game that nobody else in the"
- ✅ winner · 1,182v · 16L · 7sh · 0.59% · @iamaayushswamy
  https://www.instagram.com/reel/DYQ1u3es7_K/
  > "If you don't change just one thing about your content, your Instagram will look"
- ✗ flop · 976v · 14L · 13sh · 1.33% · @sam.gaudet
  https://www.instagram.com/reel/DX648gyyO_d/
  > "Trial Reels aren't dead, you just don't understand how they work now. I've gotten"
- · mid · 750v · 8L · 4sh · 0.53% · @iamaayushswamy
  https://www.instagram.com/reel/DX2ZoveSmuZ/
  > "You didn't go viral because you committed one of the seven deadly content sins."
- ✗ flop · 714v · 11L · 6sh · 0.84% · @sam.gaudet
  https://www.instagram.com/reel/DXk07wry_sj/
  > "Good ideas fail on social media because they're explained before they're felt. Viewers need"
- ✗ flop · 684v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXkeSkcyxnT/
  > "So ClogCode just started replacing low-level video editors. I'm gonna show you exactly how"
- ✗ flop · 654v · 6L · 1sh · 0.15% · @sam.gaudet
  https://www.instagram.com/reel/DV9BiqYEvum/
  > "So the CEO of PayPal and other CEOs at other top companies are hiring"
- ✗ flop · 584v · 11L · 3sh · 0.51% · @sam.gaudet
  https://www.instagram.com/reel/DYKuLnoyWjZ/
  > "I helped Dan Martell go from 100K followers to over 10 million across all"
- ✗ flop · 528v · 3L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DVrr_Hmj3uf/
  > "Is it possible to make viral videos in 2026 using AI? Yes, but there's"
- ✗ flop · 462v · 4L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DXnMcW7vvQa/
  > "All right, HookMaxi101, if you're posting content but nobody's watching, it's not because your"
- · mid · 444v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWHn2YbjL60/
  > "Posting schedule for $50k a month. Top of funnel reels $3-$4 per week. Middle"
- ✗ flop · 423v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DWMvDqVhwnB/
  > "Yo, this trial reel hack should be illegal. I've helped Dan Martell get over"
- ✗ flop · 419v · 1L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DYOXCeSyKYC/
  > "I think I completely cracked yapmaxing, and I'm gonna share with you the exact"
- ✗ flop · 395v · 5L · 0sh · 0.0% · @realskytan
  https://www.instagram.com/reel/DWW4GSOCVUI/
  > "What to say when contrasting a relationship between a professional lawyer and a casual"
- ✗ flop · 345v · 1L · 0sh · 0.0% · @alinamerkelcoach
  https://www.instagram.com/reel/DV4UQiKjX9i/
  > "Post your old videos again. Just take the exact same video you posted three"
- · mid · 329v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWE9-K3DNwn/
  > "The difference between a video that looks unique and professional versus one that blends"
- · mid · 227v · 5L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWZPChojJPh/
  > "Never should you ever record a video, get up, and then turn off the"
- · mid · 199v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWO6I-7DJf1/
  > "Hi, I'm Ayush, and I build personal brands for a living. In the last"
- · mid · 170v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW4WPlUDBnk/
  > "30,000 followers from one video. Here's how you can do it in five steps."
- · mid · 165v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWEwI6IDF5B/
  > "Here's how to stop fucking up your videos that are keeping you stuck in"
- · mid · 151v · 3L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWXIQgBjABQ/
  > "Trial Reels is dead. Instagram patched the go to trial reels because creators were"
- ✗ flop · 95v · 0L · 0sh · 0.0% · @loganforsyth
  https://www.instagram.com/reel/DX-uHqoxs2u/
  > "This is no longer a conspiracy. Official data shows that platforms are now rewarding"
- ✗ flop · 54v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWjoAvCDJVW/
  > "How do you make fake comments like this? Well, double tap it real quick"
- ✗ flop · 48v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWEokqMjCl_/
  > "Everyone tells you that you need a good hook, but no one tells you"
- ✗ flop · 46v · 3L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWhD3sfDG0n/
  > "Here's how to transform one shitty idea into seven viral hooks for your next"
- ✗ flop · 35v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWUKX3VjBn5/
  > "Here are five reasons why you need to start a brand new account. In"
- ✗ flop · 33v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWRlSPiDKGk/
  > "don't start posting any content until you've done this never ever post on instagram"
- ✗ flop · 15v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW4ObpaDNEs/
  > "If you find it hard to remember what to say on camera, never just"
- ✗ flop · 10v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWUg-vPjKui/
  > "It has never been easier than now to start your social media. So let"
- ✗ flop · 10v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWRzTWODDR0/
  > "2026 social media predictions you need to know. Here's what's actually changing and what"
- ✗ flop · 5v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWUY70gjF7e/
  > "If you hit record and suddenly sound nothing like yourself, it's because you're missing"
- ✗ flop · 5v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DW1_dWgjOnc/
  > "Doesn't make you a dick to steal other people's content? Well no, if you"
- ✗ flop · 5v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWj4DthDKe0/
  > "anyone can talk confidently on camera if they do this one thing. This was"
- ✗ flop · 4v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWUEfOLDKVj/
  > "If your videos are stuck under 10,000 views, it's because your videos aren't stupid"
- ✗ flop · 4v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWPH97GjNhB/
  > "If your brain freezes the second the camera turns on, it's because you simply"
- ✗ flop · 4v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWpIUQIDDiT/
  > "You notice when big creators get a viral video, they recreate that viral video"
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWW__Q_DPb2/
  > "There's a style of video that's blowing up right now, and I'm talking millions"
- ✗ flop · 2v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWUSmz0jNHH/
  > "Everyone tells you to use storytelling in your scripts, but no one knows how"
- ✗ flop · 2v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWE2nRSjJuT/
  > "creator, editor, strategist, and if you're wearing the hats by yourself, here's a shortcut"
- ✗ flop · 2v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWo4fEBjOxh/
  > "The only reason why you can't go viral is because you're not being a"
- ✗ flop · 1v · 2L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWPWhoajKw_/
  > "Would you trust me or me? I wouldn't trust the first guy. Here's the"
- ✗ flop · 0v · 1L · 0sh · 0% · @iamaayushswamy
  https://www.instagram.com/reel/DWCY9nCDAYR/
  > "If no one is engaging with your content, this is the part you're f***ing"

---

## 13. PERSONAL PROOF CASE STUDY
**Tier:** B — high reach, inconsistent (big hits + big flops)  ·  **N=43 reels · 6 creators · 9% win · 16% flop**
**Engagement (median):** 41,527 views · 651 likes · 49 shares · 0.15% share-rate · 0.97× own-median

**HOW IT'S PACKAGED:** A first-person narrative of a specific past experiment, struggle, or client result delivered as evidence — setup (I tried this / was stuck) -> turning point -> outcome and the transferable lesson. Value is carried by the before/after story arc and its receipts, not by a generic list or demo.

**VERBAL SIGNALS (how they actually say it):**
- "I tried X and here's what happened"
- "I finally cracked meta ads / I've never successfully done this before"
- "as soon as I added keywords my reels started"
- "before that I was stuck at"
- "I got this advice from Hermozi that worked"
- "wanted to report back from someone who's posted thousands of videos"

**EVIDENCE** (43 reels, by views — real opening words quoted):
- ✅ winner · 234,281v · 2,876L · 5,061sh · 2.16% · @alinamerkelcoach
  https://www.instagram.com/reel/DXfGjZQtIKE/
  > "My reels finally started getting views even in trials as soon as I added"
- · mid · 142,371v · 4,469L · 2,473sh · 1.74% · @personalbrandlaunch
  https://www.instagram.com/reel/DXonKuqoMip/
  > "So I've never successfully ran meta ads before in my life. I've tried a"
- · mid · 106,346v · 1,172L · 32sh · 0.03% · @personalbrandlaunch
  https://www.instagram.com/reel/DXwWQJ5PL8z/
  > "We just got woken up by the cops knocking on our door and ringing"
- · mid · 90,783v · 1,471L · 70sh · 0.08% · @personalbrandlaunch
  https://www.instagram.com/reel/DW81QAMDR4i/
  > "Good morning, guys. Happy Monday. It's 1.08 in the morning. And look what I"
- · mid · 90,648v · 1,832L · 266sh · 0.29% · @personalbrandlaunch
  https://www.instagram.com/reel/DX1eXi0EdF_/
  > "So how much money do I make from social media? Shout out Shelby, she"
- · mid · 80,738v · 1,169L · 46sh · 0.06% · @personalbrandlaunch
  https://www.instagram.com/reel/DYRzIXBttnE/
  > "Good morning guys. It's currently 12 43. Let's kick it So this is my"
- · mid · 79,666v · 1,015L · 49sh · 0.06% · @personalbrandlaunch
  https://www.instagram.com/reel/DXjcqSjB_wa/
  > "Morning guys, so it's 12 a.m. Time to grind. Guys, Ben's pressure washing. Can't"
- · mid · 77,053v · 1,188L · 59sh · 0.08% · @personalbrandlaunch
  https://www.instagram.com/reel/DWYyqj2F6EK/
  > "The question is, do I wear my natural hair more? I don't know. Help"
- · mid · 72,932v · 1,276L · 218sh · 0.3% · @personalbrandlaunch
  https://www.instagram.com/reel/DYUYk_WB9Gw/
  > "Okay, I'm gonna show you how easy it is to go viral. These are"
- · mid · 72,239v · 995L · 145sh · 0.2% · @personalbrandlaunch
  https://www.instagram.com/reel/DXy5nMnDF6q/
  > "What was one of the most challenging accounts to grow? We had a client"
- · mid · 71,796v · 997L · 236sh · 0.33% · @personalbrandlaunch
  https://www.instagram.com/reel/DXH8jxUlSGV/
  > "Tell me about some of your clients, what have been like some crazy success"
- · mid · 69,917v · 1,125L · 43sh · 0.06% · @personalbrandlaunch
  https://www.instagram.com/reel/DVoR_zZERdf/
  > "I'm going to start documenting my weekly life as a married 20-year-old who built"
- · mid · 59,822v · 708L · 22sh · 0.04% · @personalbrandlaunch
  https://www.instagram.com/reel/DXT_7RxBZX7/
  > "Good morning. You think there's just one cat doing teamwork with me? No. There's"
- · mid · 57,371v · 935L · 91sh · 0.16% · @personalbrandlaunch
  https://www.instagram.com/reel/DXB-TvYB6ZT/
  > "I just found this video from July 4th, 2022. I have been getting really"
- · mid · 52,921v · 962L · 255sh · 0.48% · @personalbrandlaunch
  https://www.instagram.com/reel/DXg4WDwkWkP/
  > "The first time I posted this video, I got 47,000 followers. The second time"
- · mid · 49,417v · 651L · 35sh · 0.07% · @personalbrandlaunch
  https://www.instagram.com/reel/DV6TgSohEMj/
  > "I'm going to start documenting my weekly life as a married 20-year-old who built"
- · mid · 45,594v · 712L · 91sh · 0.2% · @personalbrandlaunch
  https://www.instagram.com/reel/DXmBeuBBLN1/
  > "This video got my client Carl 67,000 followers. So we recreated it and kept"
- · mid · 45,282v · 503L · 40sh · 0.09% · @personalbrandlaunch
  https://www.instagram.com/reel/DYo-rXvvKVQ/
  > "I think, guys, it's 1.45 a.m. Airsy is working with me in a day."
- · mid · 45,108v · 695L · 247sh · 0.55% · @personalbrandlaunch
  https://www.instagram.com/reel/DYZhUANBb7Z/
  > "This is a viral script structure going around. Item politised it and did it"
- · mid · 43,649v · 603L · 22sh · 0.05% · @personalbrandlaunch
  https://www.instagram.com/reel/DW4cM9ejfl5/
  > "happy saturday good morning guys i'm gonna pray read the bible and then get"
- · mid · 43,639v · 493L · 66sh · 0.15% · @personalbrandlaunch
  https://www.instagram.com/reel/DXKdr7XjrGh/
  > "Has there been any other success story that stands out to you? Like someone"
- · mid · 41,527v · 513L · 20sh · 0.05% · @personalbrandlaunch
  https://www.instagram.com/reel/DWGwKzpjsMC/
  > "I'm going to start documenting my weekly life as Mary, 20 year old, who"
- · mid · 40,093v · 402L · 4sh · 0.01% · @personalbrandlaunch
  https://www.instagram.com/reel/DWlqPQRGLKy/
  > "Good morning. It's saturday time to rise and grind. All right guys. It is"
- · mid · 40,052v · 558L · 50sh · 0.12% · @personalbrandlaunch
  https://www.instagram.com/reel/DXrMnnjGN2D/
  > "Guys, I promised my team once I hit a million followers, I would make"
- ✗ flop · 32,017v · 351L · 44sh · 0.14% · @personalbrandlaunch
  https://www.instagram.com/reel/DZAJPDcBx3S/
  > "Sometimes I see these posting hack videos on my page, but there's like a"
- · mid · 30,339v · 1,339L · 56sh · 0.18% · @sam.gaudet
  https://www.instagram.com/reel/DW6pzs_S6vR/
  > "But this is day 140 of getting to 100,000 followers with just my iPhone"
- · mid · 24,152v · 760L · 196sh · 0.81% · @sam.gaudet
  https://www.instagram.com/reel/DYGDAhyhIlI/
  > "was sitting down with this person on MrBeast's team and I asked him, what"
- · mid · 23,546v · 1,155L · 17sh · 0.07% · @sam.gaudet
  https://www.instagram.com/reel/DYch6fTyJYk/
  > "When I was 14 years old, my dad called me into his office and"
- · mid · 21,250v · 791L · 102sh · 0.48% · @sam.gaudet
  https://www.instagram.com/reel/DWwP7E7Ac2L/
  > "I'm an introvert, I don't like being on camera. I like being behind it."
- · mid · 16,243v · 532L · 65sh · 0.4% · @sam.gaudet
  https://www.instagram.com/reel/DXeefwUym2j/
  > "I am on a journey to get to 100K followers with just my iPhone"
- · mid · 12,566v · 266L · 51sh · 0.41% · @realskytan
  https://www.instagram.com/reel/DX-cleFCK2B/
  > "I grew 100,000 followers in two weeks sitting right here and right there just"
- · mid · 11,812v · 449L · 45sh · 0.38% · @sam.gaudet
  https://www.instagram.com/reel/DWrC6JiSC5t/
  > "Look, I think I've been hiding something for you guys. And I wanted to"
- · mid · 11,665v · 195L · 28sh · 0.24% · @realskytan
  https://www.instagram.com/reel/DX7wiMRCwiq/
  > "What if you're accidentally too good at content? So at least he was averaging"
- ✅ winner · 10,896v · 189L · 200sh · 1.84% · @loganforsyth
  https://www.instagram.com/reel/DXkVG-jgn9B/
  > "An article on X is going viral right now showing that the value of"
- ✅ winner · 7,321v · 112L · 27sh · 0.37% · @iamaayushswamy
  https://www.instagram.com/reel/DYVuyGEJyl1/
  > "My client Alex gained over 150,000 followers in just 14 days with a single"
- ✅ winner · 7,009v · 198L · 100sh · 1.43% · @iamaayushswamy
  https://www.instagram.com/reel/DZDTweZJTa6/
  > "I used to think hashtags were completely dead until I figured out the one"
- ✗ flop · 1,458v · 20L · 4sh · 0.27% · @realskytan
  https://www.instagram.com/reel/DY272obprwo/
  > "I want to share some news with you. Did you know how you're sitting"
- ✗ flop · 745v · 9L · 1sh · 0.13% · @realskytan
  https://www.instagram.com/reel/DY27u2qJVNK/
  > "I have some news to share with you. Did you know how you're sitting"
- ✗ flop · 649v · 2L · 0sh · 0.0% · @sam.gaudet
  https://www.instagram.com/reel/DY_cGFSScM8/
  > "Although I think it's important to have a team eventually, I do think solo"
- · mid · 388v · 4L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWWv9evjL0N/
  > "These are the exact same video, but the second time it was posted, it"
- ✗ flop · 13v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWRfOVLjE09/
  > "Hi, I'm Ayush, and I build personal brands for a living. In the last"
- ✗ flop · 6v · 3L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWjhT9ojGzG/
  > "This video right here blew up with over 4 million views and made me"
- ✗ flop · 3v · 1L · 0sh · 0.0% · @iamaayushswamy
  https://www.instagram.com/reel/DWHS4S2jNCk/
  > "I used to think hashtags were completely dead until I figured out the one"

---

## 14. DIALOGUE GUESSING GAME
**Tier:** ⚠️ PROMISING (small N)  ·  **N=5 reels · 3 creators · 60% win · 0% flop**
**Engagement (median):** 165,746 views · 1,720 likes · 93 shares · 0.16% share-rate · 7.55× own-median

**HOW IT'S PACKAGED:** Value carried through a staged interactive rhythm: a two-voice scripted skit (curious sidekick + expert trading banter), or a gamified yes/no interrogation that probes attributes until a mystery answer (usually an AI tool) is revealed. The back-and-forth question-clue-reveal mechanic IS the packaging, distinct from a sincere interview.

**VERBAL SIGNALS (how they actually say it):**
- "Wait, stop. What? ... Okay, then what's next?"
- "Isn't that right, Barry?"
- "Do you talk to it? Does it create images? ... Grok. You got it."
- "Is it a large language model? No. ... Gemini."
- "yes/no rapid-fire clues ending in a name"
- "two-person teaching banter"

**EVIDENCE** (5 reels, by views — real opening words quoted):
- ✅ winner · 558,649v · 17,583L · 11,666sh · 2.09% · @personalbrandlaunch
  https://www.instagram.com/reel/DWE72LsIGQy/
  > "Which video do you think got more views? Video A or Video B? Um,"
- ✅ winner · 168,507v · 2,039L · 263sh · 0.16% · @sam.gaudet
  https://www.instagram.com/reel/DYpS9k-Dz6B/
  > "Do you talk to it? You could. Does it create images? Yes. Is it"
- ✅ winner · 165,746v · 1,720L · 93sh · 0.06% · @sam.gaudet
  https://www.instagram.com/reel/DYzmGKUiVzJ/
  > "Have I talked about this tool before? All the time. Kicked out of this"
- · mid · 50,836v · 559L · 37sh · 0.07% · @personalbrandlaunch
  https://www.instagram.com/reel/DXeTlE5DQlO/
  > "What year were you born? 2005, baby. Favorite hobby? I love to read. It's"
- · mid · 9,023v · 170L · 71sh · 0.79% · @alinamerkelcoach
  https://www.instagram.com/reel/DXCPdguN8zW/
  > "So when are you actually going to start? When I'm ready. What if starting"

---