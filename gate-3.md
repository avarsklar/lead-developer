# Gate 3 — Run it like a real thing (and hand it off)

<div class="gatecheck g3" markdown="1">
<span class="q">Are you here yet?</span>
You've gone live (Gate 2 is behind you), and your app has turned into **a real, ongoing thing** — not a toy anymore. You're **adding to it over time**, real people lean on it, and it needs *managing*, not just keeping alive.

You're here if you're **growing it** and it's become a genuine operation that needs help running — or if the thought *"what happens to this if I step away?"* has started to nag. If it's still a finished little thing you only tinker with, you can happily skip this gate.
</div>

**The fear this kills:** *"I'm chained to this thing — I can't change it calmly now that it's live, and I can't hand it off."*

Three tools — for shipping forever without being chained to it.

<p class="taphint">Tap a skill's name to open its own page — each has a short 20-second video.</p>

## [`/release-foundation`](skill-release-foundation.html) — run once: build your release calendar

Now that you can change your app safely, you stop shipping every new feature the second it's done. You pick how often you put features out (weekly / every 2 weeks / monthly), and it builds — and **shows you** — a calendar of which feature goes out on which date. A finished feature waits in a *holding pen* until its day. The rule that ends the panic: if a feature isn't ready by its date, it just catches the next one. No all-nighter.

## [`/release`](skill-release.html) — run on each release date

Release day, seatbelts on: it takes the feature you parked, makes sure it still works with your live app, you **watch the checks go green**, and then — on your okay — it goes live. Plus a bookmark you can jump back to, and a plain note of what changed. If a check goes **red**, it stops cold and refuses to bless the version — that's the seatbelt winning, not failing.

## [`/handoff`](skill-handoff.html) — run when you step away

Writes down where everything lives — every account, who owns it, **where** each login is (never the password itself) — so someone else, or future-you, could keep it running without ever calling you. Then it **proves** the packet by having a memory-less reader run one real task from it alone, patching every gap until it carries someone who knows nothing. You stop being the single point of failure. It touches nothing live and never locks you out.

<div class="cal stop" markdown="1">
<span class="lbl">When to stop</span>
Don't set up a release calendar (`/release-foundation`) or run release day (`/release`) unless your app is **actually live to real strangers** — random people, not just you and a few friends testing. A holding pen and a calendar solve a problem you only *have* once real people depend on what you put out. If it isn't public yet, skip the schedule and just keep shipping freely with **`/ship-change`**. Both tools now check this and turn you around warmly if it isn't time.
</div>

[See **everything on one page** &rarr;](everything.html)
