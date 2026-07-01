# Gate 2 — Safe for real strangers

<div class="gatecheck g2" markdown="1">
<span class="q">Are you here yet?</span>
Check the list. If **any one** is true, you're here — no matter how small your app feels:

- **Real money** flows through it — someone can pay, get paid, or get charged.
- **Other people's data** lives in it — accounts, messages, things they'd hate to see leaked.
- **People genuinely depend on it being up** — even with no payments and no logins, being down can strand people who were counting on you.

"It's just a side project / I barely have any users / it's basically a hobby" does **not** lower this. What's at stake when it breaks sets the floor — not how busy it is.
</div>

**The fear this kills:** *"It'll break with real people on it — someone loses money or data, or gets stranded — and I won't even know."*

Three tools. They need Gate 1 underneath them first.

<p class="taphint">Tap a skill's name to open its own page — each has a short 20-second video.</p>

## [`/qa-harness`](skill-qa-harness.html) — set up your safety checks

Turns each must-not-break flow you care about (*log in, list an item, buy, pay…*) into a check that's been **proven to go red** when it breaks. You watch it break on purpose once, then it runs by itself on every change. *"The buy button charges a card"* stops being something you click through by hand and hope.

## [`/go-live-check`](skill-go-live-check.html) — the launch-readiness audit

A blunt **go / no-go** before you let strangers and real money in. It stands up the nets — an error alert, an "is it down?" alert, a wide-open-database check, transaction checks, an email that actually arrives — and **makes each one fire so you see it catch the failure** on your own phone. Re-run it every few months, because monitors quietly rot.

## [`/emergency-plan`](skill-emergency-plan.html) — the 2 a.m. plan

A one-page card you keep on your phone for the night something breaks: *is it just me or everyone? how do I get back to working? what do I tell my users? who do I call?* — plus a way back you've **watched work**, and an alarm wired to your phone. So you're never improvising in a panic, and the AI you reach for at 2 a.m. stays a careful reader instead of making it worse.

[Next: **Gate 3 — run it like a real thing** &rarr;](gate-3.html)
