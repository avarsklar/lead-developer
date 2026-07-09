<p class="kicker">Gate 1 · run once</p>

# `/safety-net`

<p class="lead">A floor you can't fall through. Run once, before your first real change.</p>

<video controls preload="metadata" playsinline>
<source src="videos/safety-net.mp4" type="video/mp4">
Your browser can't play this. <a href="videos/safety-net.mp4">Download the video</a>.
</video>

**The fear it kills:** *"If I touch it, I'll lose my work or my data."*

## What it does

- A saved version of your app you can return to in one move.
- Your secret keys pulled out of the code and replaced with brand-new ones. (When an AI builds an app it often pastes keys straight into the code, where anyone who ever sees that code can use them. Replacing them makes the exposed ones dead and useless.)
- The rare exception handled too — a key you can't just swap for a new one, or personal info like a name or student ID committed by accident — gets scrubbed out of your project's history instead, only with your okay and after a full backup.
- A safe home for those keys: a password manager, so your logins live in one locked place instead of scattered in your head or a notes file.
- A guard on the door that blocks any save containing a secret, so one can't slip back into your code later.
- Automatic nightly backups of your data.
- A restore you watch work with your own eyes — because a backup you've never restored from isn't really a backup.

After this, no single mistake can wipe you out: every version of your code is saved, your data backs up on its own, and you've watched a restore actually work.

## When to run it

Once per project, before your first real change goes live. About 20–30 minutes for a simple app, closer to an hour if you have a real database to back up and restore-test.

## When to stop or skip

It's a one-time setup: don't re-walk finished steps. An app that stores nothing (no accounts, no orders, just pages people read) can skip the backup steps; the saved versions are the backup.

## What you need first

Nothing. This is the floor everything else rests on.

## What's next

**[`/ship-change`](skill-ship-change.html)**: make your first change the safe way. That completes Gate 1, and it's the loop you'll live in from here on.
