<p class="kicker">Gate 3 · each release date</p>

# `/release`

<p class="lead">Release day — seatbelts on. Puts your parked feature live, proven and bookmarked.</p>

<video controls preload="metadata" playsinline>
<source src="videos/release.mp4" type="video/mp4">
Your browser can't play this. <a href="videos/release.mp4">Download the video</a>.
</video>

**The fear it kills:** *"I want to announce a feature for a date and actually have it ready — not pull an all-nighter or ship something that quietly broke."*

## What it does

- Catches your parked feature up to your live app.
- You watch your safety checks go green: proof nothing important broke.
- On your okay, it flips the feature on. This is the real go-live, because the feature stayed parked until now.
- Saves a bookmark you can jump back to, and writes the plain what-changed notes.

If a check goes **red**, it stops cold and refuses to bless the version — that's the seatbelt winning.

## When to run it

On each release date, or whenever a parked feature is ready.

## When to stop or skip

Stop if your app isn't live to real strangers yet: there's nothing to "release" to; just ship it with [`/ship-change`](skill-ship-change.html). A red check stops the release until you fix it.

## What you need first

[`/safety-net`](skill-safety-net.html), [`/qa-harness`](skill-qa-harness.html) (the checks *are* the seatbelts), and [`/ship-change`](skill-ship-change.html).

## What's next

**[`/handoff`](skill-handoff.html)**: when you want someone else (or future-you) to be able to run it without you.
