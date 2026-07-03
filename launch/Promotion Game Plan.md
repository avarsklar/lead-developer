# Promotion Game Plan — Lead Developer

*Drafted 2026-07-03 from a multi-agent research pass (7 researchers on open-source promotion history, the Claude Code ecosystem, and where AI builders congregate; 1 synthesis; 3 adversarial critics whose fixes are folded in). Companion files: positioning.md (the message), launch-kit.html (the three launch pieces, ready to edit and ship).*

---

## The one-line strategy

**Prep until the repo can survive attention, plant the free compounding channels, then fire one two-wave launch — one wave for credibility (developers), one for actual users (scared builders) — and keep a small weekly engine running that a full course load can't kill.**

---

## What the history of projects like this actually says

Three patterns repeat across every comparable project that got big, and they're the skeleton of this plan:

1. **The closest analogue to your kit already proved the path.** Superpowers — Jesse Vincent's Claude Code skills kit — launched October 2025 as a personal blog post about *using* it (not a product page), timed to an Anthropic platform moment. Simon Willison covered it the next day, it hit Hacker News, and acceptance into Anthropic's plugin directory turned a 27k-star project into a 200k-star one. (Both source posts verified live 2026-07-03.) The repeatable mechanics: **personal narrative, platform timing, one respected amplifier, official directory distribution.** You can't schedule the amplifier; you can absolutely do the other three.

2. **Guides spread differently than tools.** Free handbook-style projects (roadmap.sh, The Odin Project, freeCodeCamp) win because reading costs nothing — no install, no trust, no runtime. Their growth came from one instantly-shareable artifact (a picture, a quiz, a list), one ignition post, then years of being *the default answer* people paste into help threads. Your handbook is that kind of asset; your kit is not — which is why they get different treatment below.

3. **The failure mode is almost never the launch — it's what's true when the launch hits.** Launch attention is a ~48-hour pulse and doesn't come back. Projects die at the install step, or from launching once and going silent, or from the maintainer measuring stars (which are bookmarks, not users) and burning out. Every "do not" at the bottom of this plan is a documented grave.

---

## The two decisions that shape everything

**The two-tier rule (how we handle "kit needs Claude Code" honestly).** Most scared builders live on Lovable/Bolt/Replit and can't run the kit today. So: the **handbook is the tool-agnostic top of funnel, promoted everywhere** — it's the canonical link in every builder-facing venue. The **kit is promoted directly only in Claude-native venues** where the prerequisite needs no apology. And the paid prerequisite is disclosed up front, everywhere: *"the kit needs Claude Code (paid plan, ~$20/mo — less than 10 minutes of a $200/hr cleanup developer); the handbook, quiz, and cards are free forever."* Say it before a commenter says it for you.

**Two registers of the one message.** "Proven, not configured" is the message everywhere, but:
- **Dev venues:** "break your app on purpose and prove your backups actually work."
- **Builder venues:** "we stage a fake failure on a **private practice copy — your real app is never touched** — and you watch the net catch it."
A person who is literally scared to touch their app will bounce off "break your app." Audit every asset for register.

---

## What success means (written down before anything posts)

Stars are bookmarks. The metric is **scared builders actually helped**, measured by the only instruments we can build (the skills have no telemetry, on purpose):

- **Kit tier:** reported `/readiness-check` runs — via a "Share your gate" GitHub Discussions category / issue template that the skills' closing message points to, plus "what gate did you land at?" replies on posts. Log it as *reported runs, knowing true runs are higher*.
- **Handbook tier:** quiz completions, emergency-card and go/no-go checklist downloads, "I applied this in Lovable/Bolt" replies. Without this, the biggest audience segment is invisible to us.
- **A good launch = 5–10 confirmed runs and ONE third-party "it caught something in MY app" story.** That's genuinely enough to fuel the next three months. The median Show HN gets 2 points; a dead post means *different angle later*, not failure. Write this paragraph somewhere you'll reread in October.

---

## Phase 0 — Make it spike-proof (≈3 weeks, realistically 35–45 hours total)

*Nothing is posted anywhere until this gate is green, because fixes shipped on day 3 land after the audience has left. The launch date is set by this checklist, not the calendar: "the first good week AFTER the gate is green."*

**The gate (exit criteria):**
1. **One-command install.** Package the kit as a Claude Code plugin (`.claude-plugin/marketplace.json`, `claude plugin validate` passing) so installing is typed inside Claude Code — no git, no symlinks. **Pick ONE canonical skill invocation** (plugin install may namespace skills as `/lead-developer:readiness-check` while the handbook and all 9 videos say `/readiness-check`) and sweep every doc to match; add a visible "if `/readiness-check` does nothing, type…" callout to the README, handbook header, and video captions (captions are editable; re-records aren't). ~6–9 hrs.
2. **README rebuilt as a landing page for a scared non-developer.** One line above the fold → a ~30-second GIF of the signature moment (the drill catching the *real* rollback.sh bug) → honest prerequisites box (Claude Code, paid) → install → "start here: `/readiness-check`" → handbook link → maintenance promise with a dated **"last verified against Claude Code vX on DATE"** stamp. ~4 hrs.
3. **Video pipeline session (once).** 3–4 hrs to build a repeatable recording setup — fixed terminal theme, big font, QuickTime/OBS preset, one free editor — so the README GIF and every future clip come off the same assembly line instead of being a fresh struggle.
4. **The shareable artifacts.** The 3-gates/9-skills map as one standalone self-explaining image (the kind of picture that IS the share, roadmap.sh-style); the emergency card and go/no-go checklist as downloadable PDFs; a 1280×640 GitHub social-preview card; all ~20 relevant repo topics. ~4 hrs.
5. **Handbook front door for the 95% who'll never install.** Complete value in one scroll *before* Claude Code is mentioned; the 4-question readiness quiz as an interactive widget with a shareable result ("I'm at Gate 1 — no tested undo"); a 15-minute illustrated **bridge page: "get your Lovable/Bolt/Replit app into Claude Code"** (many of those users CAN use the kit via GitHub sync — without this page the two-tier split writes them off). ~5–6 hrs.
6. **Receipts assembled.** For each war story: the rollback.sh fix commit/diff, the Club Ralley go-live-check transcript + dead-monitor screenshot, canonical public links for the Replit incident and the Lovable CVE. "Proven, not asserted" applies to the marketing. ~2 hrs.
7. **Eat your own cooking, publicly provable.** Run `/go-live-check` on the handbook site and repo (no 404s, no dead links); apply the 3 HIGH findings from your own adversarial review. The student angle draws extra scrutiny — any broken link becomes the comment thread. ~4–6 hrs. *(The pending Refit runs of `/release` and `/handoff` are real working sessions — do them if July allows, but they are NOT launch blockers; the two existing war stories carry the launch.)*
8. **The measurement instrument.** "Share your gate" Discussions category + issue template; skills' closing messages point to it. ~1 hr.
9. **Essay + pieces finalized in your own words.** The ✍️ spots in launch-kit.html rewritten by you; two war stories in both registers (dev cut + plain-language cut — "my app's alarm said it was on; we set off a test fire and no alarm rang"). ~4–6 hrs.
10. **Cold-read test, honestly labeled.** One genuinely non-technical person, starting from true zero (no Claude Code installed), on a screen-share where you never touch the keyboard. Book the person NOW — it's July and everyone's dispersed. Every stuck point is a Phase-0 bug. ~2 hrs. *(This is a usability test, not a stealth demo — if they can't retell the war story afterward, rewrite the plain cut.)*

**Two decisions to make this week:**
- **Domain:** ~$12/yr for a real domain now (redirect github.io to it), *before* any backlinks are planted — moving later breaks every link this plan earns. This is the one exception to the no-budget rule. Otherwise strike every "owned domain" assumption.
- **Your real July hours:** this phase assumes ~12–15 hrs/week for 3 weeks. If summer obligations make that fiction, stretch Phase 0 — never compress the gate.

---

## Phase 1 — Seed (overlaps Phase 0's tail → early August, ~3–5 hrs/week)

**Starts day 1 (no gate needed):**
- **The Reddit clock.** Genuinely answer "my AI-built app broke / am I safe to launch / how do I back this up" threads — **no links unless directly asked**. Home community: **r/vibecoding** (where the fear actually lives), secondary: r/ClaudeCode (where the prerequisite lives). This 9:1 participation history is the longest-lead item in the plan, it protects your best channel from a self-promo ban, and it's how you become the person others cite. ~1–2 hrs/week. *(Re-check each sub's current self-promo rules the week you first post a link — norms rot.)*

**Behind the repo-ready gate (items 1–8 above green):**
- **Anthropic community plugin directory** — submission page verified live (platform.claude.com/plugins/submit; directory at claude.com/plugins). Submit the day validation passes; review latency is unknown, so the launch copy must work with the raw GitHub link, and the directory page upgrades it whenever it lands. Fallback if rejected: awesome-lists become the primary directory play. ~2 hrs.
- **Awesome-list submissions:** awesome-claude-code (verified live) + the claude-skills lists — check each repo's CONTRIBUTING for issue-vs-PR etiquette that week. Judged on the resource, not the person; permanent discovery traffic. ~3 hrs one afternoon.
- **Anthropic community lanes:** their community-showcase channels and any student program — verify the current names/queues (10 minutes) before spending hours; a kit that makes Claude Code safe for non-developers expands *their* market, and Anthropic demonstrably features community maintainers. ~2 hrs.
- **Seed users: 5–8 people at ~1 hour each,** recruited from the Claude-native communities you're already active in (they have the tool and are reachable in July — classmates are a fall channel, campus is empty). Watch their install, fix what they trip on, and **capture exact quotes + written permission at the time** — these are launch week's third-party stories. If you have zero by August 10, launch anyway on your own two receipts; they're strong.
- **Plant the first three fear pages now** (so they're indexed before launch, and so launch posts have moment-of-fear pages to deep-link): "I'm scared to touch my AI-built app," "is my AI-built app safe to launch," "how do I back up an app I built with AI." Expect them to work as *the link people paste in replies and the page AI assistants cite* — not as a Google-traffic machine; check Search Console after three pages before writing more.
- **Pre-seed a dozen small labeled issues** ("add a Lovable-specific handbook page," "translate the emergency card") so launch-day arrivals have something to grab in the first 48 hours — that's how a spike becomes contributors.

---

## Phase 2 — The launch spike (one week you choose: first week of August, or the week after Labor Day — NEVER move-in week; ~15–20 hrs that week)

*Pick the week by looking at your actual calendar — the launch needs you present, and mid-late August at Bucknell is the busiest week of your year. Gate: Phase 0 green + at least two receipts packaged. Block the 48-hour window like an exam.*

**Wave A — credibility (metric: links and citations, not users):**
- **Day 0:** essay live on the handbook site: *"My own launch check failed my own app. Good."* The honest-NO-GO story is the highest-trust asset genre there is (disaster/postmortem stories consistently outperform product announcements).
- **Day 1, a weekday morning with 3–4 clear hours:** **Show HN.** Title leads with the behavior, not the stack: *"Show HN: Break your app on purpose to prove your backups actually work"* — Claude Code disclosed in the first line of the pre-written maker comment (HN punishes hidden dependencies harder than stated ones; "AI skills" in a title is a saturated, fatigued genre in 2026). Submit the **runnable repo**, not the handbook (reading material is off-topic for Show HN). Answer every comment. Timing folklore is stale and contested — your availability is the binding constraint.
- **Same week, off the critical path (~2 hrs, zero replies is the base case):** the cover email to Simon Willison with the essay — he documented-ly links to substantive work from unknowns in exactly this category; expected value is a durable citation and a few hundred qualified visitors, with a small chance of cascade. LinkedIn post (career lane). Newsletter submissions re-verified that week before sending.
- **If the Show HN dies at 2 points:** normal (that's the median). Weeks later: one repost with a different angle (the war story, not the kit), or a polite note to hn@ycombinator.com for the second-chance pool. Never delete-and-repost.

**Wave B — actual users (metric: reported runs, quiz completions, gate replies):**
- **r/vibecoding post written with the same care as the Show HN** — story-first, fear-named, builder register, plain-cut war story, ask: "take the 4-question check, tell me your gate." Then r/ClaudeCode (kit direct, dev register ok), r/SideProject the following week. Never the same text twice.
- **Creator pitches as a first-class lane, not a sub-bullet:** 10–15 researched vibe-coding YouTubers/creators, each offered a packaged, filmable segment — *"run the go-live check live on an audience-submitted app; the drama of a live NO-GO is your episode."* Plus **one owned YouTube video** (the drill catching the rollback bug, ~5 min) that every Reddit answer and fear page can embed — YouTube is where this audience actually learns, and it was missing from every draft of this plan until a critic caught it.
- **Short vertical clips as an experiment, not a commitment:** 4–6 TikTok/Reels/Shorts during launch month ("POV: you're scared to touch the app you built with AI"), vertical-native with big captions, only if the Phase-0 pipeline gets a clip under ~90 minutes. Keep the lane only if it produces any measurable traffic. X is for replies under big vibe-coding accounts, not broadcasting.
- **Spike-conversion duty:** for 48 hours answer every issue/comment fast, point arrivals at the pre-seeded issues, ask every commenter for their gate.

---

## Phase 3 — The evergreen engine (September onward, honestly ~4–6 hrs/week)

*Launch-once-then-silence is the default death. The engine is deliberately small — and it degrades gracefully instead of collapsing.*

- **Weekly, ONE artifact** (not three): the same story rotates formats across weeks — week 1 a short handbook essay, week 2 a clip of it, week 3 a tailored Reddit telling. Manage it on your own `/release-foundation` calendar — which is itself a story: *"I promote this kit on the release schedule the kit taught me."*
- **Weekly, 30–60 min:** keep answering scared-builder threads in r/vibecoding (+ a monthly check-in on the tool subreddits — r/lovable, r/cursor, r/replit — where the disasters get posted publicly). The end state: other people answer with your link.
- **The "just launched" sweep (20 min/week):** find people posting "I just launched my first AI-built app!" on r/SideProject and X, and offer the downloadable go/no-go checklist — the artifact, not the repo link. That's the before-the-break fear moment, and it's the exact moment `/go-live-check` exists for.
- **Monthly:** re-verify the kit against current Claude Code and update the "last verified" stamp; run one real drill on Refit (each run writes next month's content for free); one outreach shot (podcast pitch — the student-builds-her-own-lead-developer arc is a complete indie-podcast episode; or a "best Claude Code skills" roundup author; or one creator DM).
- **Event-driven, from templates:** pre-write 2–3 newsjack skeletons now ("here's the 15-minute check that would have caught this — in YOUR app") so when the next vibe-coding disaster trends, posting is a 45-minute edit. When schedule permits; skip without guilt otherwise.
- **Quarterly flagship (semester-project sized):** the data post, done ethically — **"I ran a free readiness check on the first 25 volunteer AI-built apps; here's what I found."** Opt-in volunteers recruited from the communities (which doubles as the seed-user pipeline). Never probe strangers' apps uninvited, and never write the headline number before the data exists. Also: a "Spring 2027 edition" handbook re-release with new war stories is a legitimate second launch.
- **Minimum viable week (pre-authorized for exams):** 30 minutes of Reddit answering, nothing else. Falling back to it is the plan *working*. Mark midterm and finals weeks as MVWs on the calendar now.

---

## Do not do (each one is a documented grave)

- **Don't post anything before the Phase-0 gate is green** — attention doesn't come back.
- **Don't measure stars or treat a 2-point Show HN as a verdict** — the median Show HN gets 2 points; stars are bookmarks.
- **Don't ask friends/classmates to upvote anything** — HN's vote-ring detection flags it and booster comments get flamed.
- **Don't delete-and-repost a failed HN submission** — detected and penalized; use the sanctioned second chance.
- **Don't drop links from a cold Reddit account** — bans are account-wide and would burn your best channel.
- **Don't say "vibe coder" in headlines** — the label splits rooms in 2026; name the fear, not the person.
- **Don't market it as "9 Claude Code skills"** — saturated genre; one program, one front door: `/readiness-check`.
- **Don't bet on Product Hunt** — one afternoon for the badge/backlink, zero prep hours.
- **Don't submit the handbook to Show HN** — reading material is off-topic; the runnable repo is the submission.
- **Don't pay for anything** — no ads, no placement agencies, no promoted posts.
- **Don't promise features in launch-week comment threads** beyond the published maintenance scope.
- **Don't put any statistic in public copy without a linkable source** — your pitch is "proven, not asserted"; the marketing must survive its own standard.
- **Don't characterize how competitors' products work internally** — "a scanner can tell you a policy exists; only a drill tells you it holds" makes the point without a falsifiable claim.

## Standing rule the whole plan runs on

**Every channel fact in this plan is treated as expired until re-checked the week of use** — submission forms, subreddit rules, newsletter addresses, program names. (Verified live on 2026-07-03: the Superpowers/Willison case-study links, platform.claude.com/plugins/submit, claude.com/plugins, awesome-claude-code, anthropics/skills. Console.dev's pages have moved — re-find before emailing.) This is your own "monitors rot" philosophy, applied to marketing.

## Honest risks

- **Anthropic ships an official hardening pack** (they already ship `/security-review`). Defense: get inside the wave (directory listing), and keep the durable moat — the plain-English pedagogy, the emotional job, the war stories — on your own domain. The method is yours even if the category commoditizes.
- **The Claude-native audience may skew technical** — the scared-non-technical person may be rarer in r/ClaudeCode than member counts suggest. The seed-user round is the test: track how every real target user found you, and rebalance toward the handbook tier if that's what the data says.
- **Amplifiers are invitable, not forceable.** Willison, creators, Anthropic features — all upside, none load-bearing. The plan works at zero replies.
- **You are one full-time student.** The engine is capped, the MVW exists, and quarterly flagships are semester-sized on purpose. Exceeding the cap is how solo maintainers burn out — and a stale *safety* tool actively misleads scared people. The dated "last verified" stamp is the honest contract.
