# Gate 3 — Run it like a real thing

<div class="gatecheck g3" markdown="1">
<span class="q">Are you here yet?</span>
You've gone live, ideally with Gate 2's nets under you, and you're still adding to it: real people lean on it, and keeping it alive is no longer the whole job. If the thought *"what happens to this if I step away?"* has started to nag, you're here. If it's a finished little thing you only tinker with, you can happily skip this gate.
</div>

**The fear this kills:** *"I'm chained to this thing — I can't change it calmly now that it's live, and I can't hand it off."*

Three skills, for shipping forever without being chained to it.

<p class="taphint">Tap a skill's name to open its own page; each has a short 20-second video.</p>

## [`/release-foundation`](skill-release-foundation.html) — run once: build your release calendar

Now that you can change your app safely, you stop shipping every feature the second it's done. You pick how often features go out (weekly / every 2 weeks / monthly), and it builds — and shows you — a calendar of which feature goes out on which date. A finished feature stays parked until its day. And the rule that ends the panic: a feature that isn't ready by its date just catches the next release. No all-nighter.

## [`/release`](skill-release.html) — run on each release date

Release day, seatbelts on: it takes the feature you parked, makes sure it still works with your live app, you watch the checks go green, and then, on your okay, it goes live. Plus a bookmark you can jump back to, and a plain note of what changed. If a check goes **red**, it stops cold and refuses to bless the version — that's the check doing its job.

## [`/handoff`](skill-handoff.html) — run when you step away

Writes down where everything lives: every account, who owns it, where each login is kept (never the password itself). Then it proves a stranger could run the app from the packet alone. You stop being the single point of failure, and it never locks you out.

<div class="cal stop" markdown="1">
<span class="lbl">When to stop</span>
Don't set up a release calendar (`/release-foundation`) or run release day (`/release`) unless your app is actually live to real strangers, meaning random people, not just you and a few friends. Until then, skip the schedule and keep shipping freely with **`/ship-change`**. (Both skills check this and will turn you around if it isn't time.)
</div>

[See **everything on one page** &rarr;](everything.html)
