# `/qa-harness`

<p class="lead">Turns "I hope nothing broke" into a check that's been proven to catch a break.</p>

<video controls preload="metadata" playsinline>
<source src="videos/qa-harness.mp4" type="video/mp4">
Your browser can't play this. <a href="videos/qa-harness.mp4">Download the video</a>.
</video>

**The fear it kills:** *"How do I know nothing broke? A green checkmark feels like proof, but it might be lying to me."*

## What it does

- You name a flow that must never break — *log in, buy, pay…* — in plain English.
- The AI breaks it on purpose, once, so you watch the check go **red**.
- After that, the check runs by itself on every change, inside your `/ship-change` loop. The AI writes and maintains the test code; you name the flow and watch the proof.

## When to run it

When you're tired of clicking through your app by hand after every change, or you're hardening for real traffic. Plan a real sit-down session the first time: most flows take a few minutes each, but the buy-button/checkout flow is honest work and takes about an hour on its own. Re-runs are short.

## When to stop or skip

Set up per flow; re-prove a check only when that flow itself changes. It drives a real web browser, so it fits web apps; phone apps aren't covered yet.

## What you need first

[`/ship-change`](skill-ship-change.html), which provides your must-not-break list and the private copy the checks run on.

## What's next

**[`/go-live-check`](skill-go-live-check.html)**: prove your nets actually catch real failures before you let strangers in.
