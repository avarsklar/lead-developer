# Positioning — Lead Developer ("Scared to touch your own app?")

*Confirmed with Ava 2026-07-03. Every launch piece inherits this page. Nothing downstream may claim anything not on the proof ledger (§8).*

## 1. The one reader (named like a real person)

Someone building something real with AI — a marketplace, a club tool, a small SaaS — who has crossed (or is about to cross) from *making it work* into *people actually using it*. The sharpest version, and the moment every headline aims at: **the day changing their own app starts to feel like defusing a bomb.** They build in Lovable, Bolt, Replit, Cursor, or Claude Code. They are not a professional developer and don't want to become one.

**NOT for:** professional developers already comfortable with git, tests, and CI (they'll say "just learn git" — let them); people idly prototyping with no intention of real users.

**Naming rule:** name the SITUATION, never the person. "Scared to touch your own app" lets people self-select by the fear. Use the phrase "vibe coder" only inside communities that use it about themselves (r/vibecoding); never in headlines — by mid-2026 the label splits rooms.

## 2. The sharp pain (a scene, in their words)

It's a Tuesday night. A user messages that something's broken. You paste "fix it" into the AI and pray, because there's no practice copy, no test, no way back if it makes things worse. You've been putting off every improvement for three weeks because the last time you asked the AI to change something, it quietly broke something else. The app works — that's the problem. It works, people use it, and you're the only thing standing between it and disaster, with no map for this part.

## 3. What it is (one plain sentence)

**Lead Developer is a free kit of nine plain-English skills that turn the AI you already build with into a careful senior developer for the app you're scared to touch.**

Honest asterisk that travels with it everywhere: *the kit runs in Claude Code, which needs a paid Claude plan (~$20/month — still less than 10 minutes of a $200/hour cleanup developer). The handbook, the readiness quiz, and the downloadable cards are free forever, whatever tool you build with.*

## 4. The wedge (why this, not the obvious alternative)

**Today they use:** raw prompting ("AI, fix my checkout") and hope — or paralysis (touching nothing). The real competitor is *doing nothing*.

**The one reason to switch:** every safety net in this kit is **proven, not configured**. A backup that's "on" in a dashboard, an error monitor that's "set up" — those are promises. This kit makes a safe failure happen and has you *watch the net catch it* before it counts as done.

**Honest limit — it's worse if:** you don't use Claude Code (the ideas still apply; the automation doesn't). Validated on common web stacks (Next.js / Supabase / Vercel-style); phone apps aren't covered. Built and maintained by one person, with a dated "last verified" stamp so you can see it's alive.

## 5. Why now

A real trigger, all checkable: the first big wave of AI-built apps crossed into production with strangers and money on them, and the disasters are now public — Replit's agent deleting a production database (July 2025), Lovable's RLS exposure (CVE-2025-48757). Thousands of builders got the first half of the map (build it) and nobody handed them the second half (run it).

## 6. The surprising specific

**The first time I rehearsed my own emergency plan, the drill caught a real bug in my own rollback script — the "way back" I'd been trusting for weeks would have failed on the exact night I needed it.** (Refit, 2026-06-29 — receipts: the rollback.sh fix commit.)

Backup specific: my own launch-readiness check failed my own app — the error monitor showed "on" in every dashboard, but when we threw a test error on purpose, nothing arrived. Verdict: NO-GO. I wrote the check. (Club Ralley, 2026-06-30.)

## 7. The one memorable message

> **A safety net isn't real until you've watched it catch something. Proven, not configured.**

**Two registers — audit every asset for which one it uses:**
- **Dev register** (Hacker News, Simon Willison, newsletters): "break your app on purpose and prove your backups actually work."
- **Builder register** (r/vibecoding, handbook, short videos, creator collabs): "we stage a fake failure on a private practice copy — **your real app is never touched** — and you watch the safety net catch it." A person scared to touch their app bounces off "break your app"; the safety must live inside the sentence.

## 8. Proof on hand (the honesty guardrail)

**Real, existing — may be claimed:**
- Live handbook site: https://avarsklar.github.io/lead-developer/ (visuals + a short video per skill)
- Public repo: https://github.com/avarsklar/lead-developer-skills — 9 skills, plain-English, dependency-free markdown
- The rollback-script bug caught by the /emergency-plan drill on Refit (2026-06-29), fixed and re-proven
- The Club Ralley NO-GO: /go-live-check caught a silently dead error monitor in production, plus two broken pages (2026-06-30)
- Ava built Refit (Bucknell campus marketplace) with AI and was the scared builder herself
- A 64-agent adversarial review of the kit itself (43 findings, being applied) — the kit gets the same treatment it gives apps

**Do NOT claim:** user counts, installs, stars, testimonials, "trusted by," any statistic without a linkable source, how any competitor's product works internally (say "a scanner can tell you a policy exists; only a drill tells you it holds" — never characterize Lovable's scanner).

---

## Appendix A — Channel routing (and why)

**Project type:** open source kit + free guide hybrid. "Popular" (Ava, 2026-07-03) = real people using it (primary), GitHub visibility, career credibility.

**The two-tier rule (the structural answer to the Claude Code constraint):**
- **The HANDBOOK is the tool-agnostic top of funnel, promoted everywhere.** Lovable/Bolt/Replit/Cursor audiences get the ideas — restore points, proof-by-drill, break-glass cards, the readiness quiz — with an honest "the kit needs Claude Code; here's the method in your tool" page. The handbook is the canonical link in every builder-facing venue.
- **The SKILLS are promoted directly only in Claude-native venues** (r/ClaudeCode, r/ClaudeAI, the plugin directory, awesome-lists), where "runs in Claude Code" needs no apology.

**Primary venue:** two-wave launch — Wave A for credibility (Show HN + one amplifier email; metric = links and citations), Wave B for actual users (r/vibecoding + creator pitches + short video; metric = reported runs and quiz completions). *Fact behind the choice: HN reaches developers who don't have this fear; the fear lives in builder communities — but HN/directory credibility is what makes a scared stranger trust a free tool enough to point their app at it.*

**Secondary:** Anthropic community plugin directory (submission page verified live 2026-07-03: platform.claude.com/plugins/submit) and awesome-claude-code-class lists — the compounding, no-audience-required channels.

**Deliberately skipping:** Product Hunt as a bet (one afternoon for the badge/backlink only — 2026 PH sends curious browsers, not scared builders); paid anything (ads, placement agencies); broadcast X threads from a zero-follower account (X is for replies under big accounts, not broadcasting).

## Appendix B — Release sequence

1. Prep gate first (repo spike-proof; see Promotion Game Plan.md Phase 0) — nothing is posted anywhere before the gate is green.
2. Publish the essay on the handbook site (the durable anchor).
3. LinkedIn post (career-credibility lane) — same week, not the same hour.
4. Show HN on a weekday morning when Ava has 3–4 clear hours to answer every comment (timing is a weak preference; presence is the binding constraint). Pre-written maker comment ready as the first reply.
5. Wave B community posts roll out over the following days — each written fresh for its room, never pasted.
6. Cover emails (amplifier + creators) go out with the essay link, off the critical path — zero replies is the base case, any reply is upside.

**Never fire all pieces into the same feed in the same hour.**

## Appendix C — Standing rules for all promotion

- **No statistic appears in public copy without a linkable source.** (The kit's pitch is "proven, not asserted" — the marketing must survive its own standard.)
- **Every venue's rules are treated as expired until re-checked the week of use** (self-promo policies, submission forms, subreddit norms — monitors rot; so do channel facts).
- **Every war story ships with receipts** (commit diff, transcript, screenshot) and in **two cuts** — dev register and plain-language register.
- The handbook intro and war-story lines are **Ava's own words** before anything ships (standing editorial rule).
