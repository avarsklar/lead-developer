<!-- DRAFT for Ava to make her own. Per your standing rule, the personal lines
(marked ✍️) must end up in YOUR words before this ships — rewrite them the way
you'd say them out loud. The facts and structure are ready; the voice is yours.
Publish on the handbook site as the launch anchor. ~1,100 words, ~6 min read. -->

# My own launch check failed my own app. Good.

In June I ran a launch-readiness check on an app I help run. It failed. Here's the part that matters: I wrote the check.

The app is Club Ralley, and by every dashboard it was fine. Error monitoring: on. Password reset: built. The kind of green lights that let you sleep. Then the check did the one thing dashboards never do — it stopped *reading* the settings and started *testing* them. We threw a fake error on purpose, the kind a real user would cause, and watched for the alarm.

Nothing arrived.

The error monitor — configured, installed, showing "active" in its own dashboard — had been silently doing nothing in production. If a real user had hit a real bug, no one would have known. Not that night, not that week. The check's verdict was blunt: NO-GO. Fix the nets, then launch.

I want to tell you why that failing grade was the best result I got all month, and why I think the thing that produced it matters to a lot of people right now.

## The wall nobody warns you about

Two years ago I couldn't have built a real app. Then AI made it possible, and I did — a campus marketplace called Refit, for buying and selling at my college. It worked. Real people used it.

<!-- ✍️ AVA: 2–3 sentences here, in your own words — the specific week you realized you were scared to touch Refit. What you were trying to change, what you were afraid would happen, what you did instead (nothing?). This is the paragraph strangers will quote. -->

And that's the wall: the moment your AI-built thing stops being a project and starts being something people depend on, every change becomes a gamble. You type "fix my checkout" into the AI and pray, because there's no practice copy, no test, no way back if it makes things worse. The fear isn't silly. It's the correct response to running something real with no net under it.

You've seen where that goes when it goes badly. Last July, an AI coding agent at Replit deleted a company's production database during a code freeze. Lovable — a tool specifically for non-developers — shipped a vulnerability (CVE-2025-48757) that left users' app data readable by strangers. These made the news because they were dramatic. The undramatic version happens every day: someone's app breaks, they don't find out for a week, and they quietly conclude they were never qualified to run it.

They were qualified. They were just missing the second half of the map. AI handed a generation of people the first half — *how to build it* — and nobody handed them the part professional developers spend years absorbing: how to change something safely, how to know when it breaks, how to get back to a version that worked.

## What a careful senior developer actually does

Here's the thing I learned building my way out of my own fear: every practice a senior developer adds to a project exists to kill one specific fear. A restore point kills "I'll lose everything." A practice copy kills "I'll break it live." A tested backup kills "the data is gone." None of it requires you to become a developer. It requires a procedure — and the judgment to hold the procedure — which is exactly what you can encode.

So I encoded it. **Lead Developer** is a free, open-source kit of nine plain-English skills that turn the AI you already build with into a careful senior developer for your own app. You run one command — `/readiness-check` — and it tells you which safety net you're missing and the single next move. Not a forty-item checklist. One net at a time, only when you actually feel the fear it removes.

One idea holds the whole kit together, and it's the idea that failed Club Ralley's launch: **a safety net isn't real until you've watched it catch something. Proven, not configured.**

Every kit skill ends the same way — not with settings saved, but with a staged failure. On a private practice copy (your real app is never touched), we make the bad thing happen on purpose: throw the error, break the page, restore the backup. Then you watch, with your own eyes, whether the net catches it. A scanner can tell you a policy exists. Only a drill tells you it holds.

## The drill that caught my own rollback script

The clearest proof I have is what happened when I pointed the kit at my own app.

The emergency-plan skill includes a fire drill: deliberately break a practice copy of your app, then use your own documented "way back" to recover it — so the night something really breaks, you're following a rehearsed path instead of improvising at 2 a.m.

I ran the drill on Refit. The rollback script — the thing whose entire job is saving me on the worst night — **had a bug**. It had been sitting there for weeks, looking exactly like safety. If I'd skipped the drill and trusted the script, it would have failed at the precise moment I needed it, with my app down and me panicking.

The drill caught it in a rehearsal, where it cost nothing. We fixed it, re-ran the drill, watched the recovery actually work. That's the whole philosophy in one story: I didn't *believe* my safety net was real. I watched it fail, fixed it, and then watched it hold.

## What this is not

Honesty is the only marketing budget I have, so: the kit runs in Claude Code, which needs a paid Claude plan — about $20 a month, which is real money, though it's also less than ten minutes of a cleanup developer's time. If you build in Lovable, Bolt, Replit, or Cursor, the free handbook teaches the same method for your tool, and there's a path to bring your app into Claude Code if you want the automation. The skills are validated on common web stacks; phone apps aren't covered yet. And it's maintained by one person — me — which is why the repo carries a dated "last verified" stamp instead of a promise to be a team I'm not.

The handbook — the plain-language guide to all of it, with pictures and a short video per skill — is free forever, whatever you build with.

<!-- ✍️ AVA: optional 2–3 sentences — why you, why this, what you want for the person reading. Your words only. -->

## Where to start

If any of this is your fear, start with the five-minute version: open the [handbook](https://avarsklar.github.io/lead-developer/) and take the four-question readiness check — it tells you which gate your app is at and the one next move. Nothing to install, nothing touched.

A safety net you've never watched catch something isn't a net. It's a hope. Go find out which one you have.

<!--
Receipts to link before publishing (assemble these in Phase 0):
- rollback.sh bug: the fix commit / diff in the Refit repo
- Club Ralley NO-GO: the go-live-check transcript excerpt + screenshot of the dead monitor
- Replit incident + CVE-2025-48757: link to public coverage (both are documented; find canonical links)
-->
