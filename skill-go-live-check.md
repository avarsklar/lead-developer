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

<!-- ✍️ AVA (3 of 4): 2 sentences here, first person — the first time you ran this on a real app, the error monitor looked set up but was silently catching nothing in production; the check made it fail, nothing arrived, and the verdict was NO-GO. Say it your way. It's the strongest proof on this page. -->

## When to run it

Before you launch to the public or push for growth; figure 30–45 minutes the first time, shorter on re-runs. Then every few months after: a monitor you set up in March can be quietly dead by June.

## When to stop or skip

A **no-go** doesn't lock you out; it means "not yet." Whatever failed is your next job: fix it, then re-run.

## What you need first

[`/safety-net`](skill-safety-net.html). The money and sign-in checks also lean on [`/ship-change`](skill-ship-change.html)'s private copy.

## What's next

**[`/emergency-plan`](skill-emergency-plan.html)**: your calm plan for the night something breaks anyway. That's the last piece of Gate 2.
