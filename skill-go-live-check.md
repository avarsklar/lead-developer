<p class="kicker">Gate 2 · prove the nets</p>

# `/go-live-check`

<p class="lead">Proves your safety nets actually catch real failures — before you let strangers and real money in.</p>

<video controls preload="metadata" playsinline>
<source src="videos/go-live-check.mp4" type="video/mp4">
Your browser can't play this. <a href="videos/go-live-check.mp4">Download the video</a>.
</video>

**The fear it kills:** *"It'll break and I won't even know — I'll find out from an angry email."*

## What it does

- Sets up the nets: an error alert, an "is it down?" alert, a check that your database isn't readable by strangers, a check that strangers can't get into accounts that aren't theirs, checks that the money moved matches what was ordered, and proof that the emails your app sends (receipts, password resets) actually arrive.
- Makes each one fail on purpose, so you see the net catch it: the alert landing on your phone, the stranger's read getting blocked, the test email arriving in your inbox.
- Renders a blunt **go / no-go**.

The first time I ran this check on one of my apps, it failed. The alert system I thought I had was actually doing nothing. It looked set up, but when the check broke the app on purpose, no alert ever came. If I had launched like that, I would have found out about problems from users instead of alerts.

## When to run it

Before you launch to the public or push for growth; figure 30–45 minutes the first time, shorter on re-runs. Then every few months after: a monitor you set up in March can be quietly dead by June.

## When to stop or skip

A **no-go** doesn't lock you out; it means "not yet." Whatever failed is your next job: fix it, then re-run.

## What you need first

[`/safety-net`](skill-safety-net.html). The money and sign-in checks also lean on [`/ship-change`](skill-ship-change.html)'s private copy.

## What's next

**[`/emergency-plan`](skill-emergency-plan.html)**: your calm plan for the night something breaks anyway. That's the last piece of Gate 2.
