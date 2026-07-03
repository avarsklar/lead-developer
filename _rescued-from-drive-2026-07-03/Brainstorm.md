# Brainstorm

Raw notes for the Lead Developer project — gaps in my own experience, fears I still carry, and what the product should actually do for someone like me.

---

## What I wish I knew

- I needed to **plan before building**.
- I didn't know to have **"interns"** (a new chat for every task).
- **Where to store all of the API keys.**
- **What backend, frontend, error management system to use.**
- **Where to get a domain.**
- **How much will everything cost.**
- **How to use trees on git.**
- **How to make changes on a separate version before implementing.**
- **Terms and conditions.**
- **Transferring the project to another person.**
- **When do I need to use auth.**
- **How to organize all of my notes and MD files.**

---

## Fears

- **Scammers.**
- **Hacking.**
- **Good enough to publish.**
- **Will traffic break it.**
- **How to hide people's special info.**
- **How to know payments are secure.**
- **How do I make changes without breaking.**
- **Cost.**
- **When should a company become an LLC?** When does what I built stop being "a project" and need to become a real legal business to protect me personally — and am I on the hook if something goes wrong once real money and real strangers are involved? The legal twin of the go-live gate; likely its own later explainer/skill.

---

## What the project should do

- **Make a prototype without publishing.**
- **Making an admin dashboard with useful info.**
- **Finding all bugs** (broken buttons, links, etc).
- **Setting up a good to-do list.**
- **Creates skills.**

---

## Notes & Learnings

*Things I've worked out as we go. Each one started as a question on the lists above and got pinned down here.*

### What is a "stack"?

The set of technologies an app is built on. Four parts:

- **Frontend** — what users see in their browser (React, Next.js, Vue, Svelte, plain HTML, etc.)
- **Backend** — the server logic that runs when users do things (Node.js, Python, Ruby, or "serverless" — meaning your host runs little functions on demand)
- **Database** — where user data lives (Supabase, Firebase, Postgres, MongoDB, etc.)
- **Hosting** — where it's deployed so the world can reach it (Vercel, Netlify, Cloudflare, AWS, etc.)

A vibe coder often doesn't know what their stack is — they let Cursor / Lovable / Replit / v0 pick for them. That's the audience the skills have to serve.

**Design rule for all Lead Developer skills:** never assume the stack. The only safe assumption is **git** (and even that, a skill can set up if it's missing). Every skill should start by asking — or inspecting the repo — to figure out what the user is actually on, then translate each generic action into the specific clicks/commands for their stack.

### Copy of prod vs. sanitized clone (staging databases)

When you spin up a staging copy of your app, what data does it use?

- **Copy of prod** — an exact duplicate of your live database. Real users, real emails, real payments. If staging leaks, real people's data is exposed.
- **Sanitized clone** — same copy, but a script runs over it that replaces sensitive fields with fake versions. Real email `ava@bucknell.edu` → fake `user_47@example.com`. Real names, addresses, card numbers → all replaced. The **shape** of the data is real (same volume, same patterns, so tests are realistic) but the **content** is fake (so a leak is harmless).

Lead Developer's default for staging is **sanitized clone**.
