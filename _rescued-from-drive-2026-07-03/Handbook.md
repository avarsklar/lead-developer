<style>
.cal { border-left: 4px solid #ccc; background: #fafafa; padding: 12px 18px; margin: 20px 0; border-radius: 0 6px 6px 0; font-size: 15px; }
.cal .lbl { display:block; font-size: 11px; letter-spacing: .09em; text-transform: uppercase; font-weight: 700; margin-bottom: 6px; }
.cal p { margin: 6px 0; }
.cal.do { border-left-color:#5a9367; background:#f1f7f2; } .cal.do .lbl { color:#39623f; }
.cal.plain { border-left-color:#6b86b3; background:#f2f5fa; } .cal.plain .lbl { color:#3f5780; }
.cal.reality { border-left-color:#c98a2b; background:#fbf5ec; } .cal.reality .lbl { color:#8f6011; }
.cal.stop { border-left-color:#b5483d; background:#f9ece9; } .cal.stop .lbl { color:#9a382c; }
figure.fig { margin: 28px 0; }
figure.fig figcaption { font-size: 13px; color:#8a8a8a; text-align:center; margin-top: 10px; font-style: italic; }
svg { max-width: 100%; height: auto; display:block; }
@media print { .cal, figure.fig, svg { page-break-inside: avoid; } }
</style>

# Scared to Touch It: A Builder's Field Guide From "It Works" to "It's Real"

*You built something real with AI. Here's how to stop being afraid of it — one named fear, one small fix at a time.*

## The feeling you walked in with

You used AI to build something. It works. People are using it — maybe paying for it. And somewhere along the way you noticed a feeling you didn't expect: you're scared to touch your own product.

You don't say it out loud, because it sounds a little absurd. You made this thing. It runs. People rely on it. And yet every time you think about changing the button, fixing the copy, improving the page everyone complains about, a quiet voice says *don't — you'll break it.* So you leave it alone. You work around it. You tell yourself you'll deal with it later.

Here is the first thing to know, before anything else: that fear is not a character flaw. It is not a sign you're a fraud, or in over your head, or that you should have learned to code "properly" first. It's a signal. It means you've arrived somewhere most "build with AI" content never mentions — the gap between making something work once and running something real.

Professional developers have a whole vocabulary for that gap. They have names for every fear you're feeling and a standard practice for each one. You don't have those names yet — not because you're behind, but because you got here a different way. You built something real without spending years watching live apps break and learning, one disaster at a time, what would have stopped it. You skipped the disasters. That's a good thing. It just means nobody handed you the map.

This is the map.

Here's the only promise it makes, and it makes it on every page: every fear you have about your app has a name. And every named fear has a smallest possible thing — not a course, not a rebuild, not a computer science degree — that makes it go away. We'll take them one at a time. You'll never have to do all of it at once. You'll finish each part more in control than you started, never measured, never graded.

So take a breath. The fear means you built something worth being careful with. Let's make it safe to touch.

<div class="cal do" markdown="1">
<span class="lbl">If you'd rather just begin</span>
You don't have to read all of this first. Open your project and run **`/readiness-check`** — about five minutes, four easy questions, and it hands you the single next move. The rest of this is the *why*, and it'll keep.
</div>

## Two separate things, and the corner nobody warns you about

When people talk about a product "growing up," they usually mean one thing: more users. That's a real axis — one stick you can measure a product by. But it's not the one keeping you up at night.

There's a second, independent axis, and it's the one your anxiety actually lives on: **how hardened is it?** Can you trust it? Can you change it without breaking it? Can you walk away from it for a weekend without dreading what you'll come back to?

These two axes are independent. That's the whole insight. How many people use your app and how solid it is underneath have nothing to do with each other. You can have a handful of users on something rock-solid, or a thousand users on something held together with tape.

Picture it as four corners:

<figure class="fig">
<svg viewBox="0 0 680 470" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <rect x="92" y="58" width="264" height="182" fill="#f3f6f4"/>
  <rect x="356" y="58" width="264" height="182" fill="#eef3ec"/>
  <rect x="92" y="240" width="264" height="182" fill="#f7f7f6"/>
  <rect x="356" y="240" width="264" height="182" fill="#f9eae6"/>
  <line x1="92" y1="58" x2="92" y2="422" stroke="#bbb" stroke-width="1.5"/>
  <line x1="92" y1="422" x2="620" y2="422" stroke="#bbb" stroke-width="1.5"/>
  <line x1="356" y1="58" x2="356" y2="422" stroke="#ddd" stroke-width="1" stroke-dasharray="4 4"/>
  <line x1="92" y1="240" x2="620" y2="240" stroke="#ddd" stroke-width="1" stroke-dasharray="4 4"/>
  <line x1="92" y1="422" x2="636" y2="422" stroke="#666" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="92" y1="422" x2="92" y2="44" stroke="#666" stroke-width="1.5" marker-end="url(#ar)"/>
  <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#666"/></marker></defs>
  <text x="360" y="452" text-anchor="middle" font-size="13" fill="#555" font-weight="600">How many people use it  &#8594;</text>
  <text x="74" y="240" text-anchor="middle" font-size="13" fill="#555" font-weight="600" transform="rotate(-90 74 240)">How solid is it underneath  &#8593;</text>
  <text x="150" y="438" font-size="11" fill="#999">few</text>
  <text x="585" y="438" font-size="11" fill="#999">many</text>
  <text x="106" y="86" font-size="13" font-weight="700" fill="#3a3a3a">Few &#183; solid</text>
  <text x="106" y="106" font-size="12" fill="#555">A boring, safe</text>
  <text x="106" y="122" font-size="12" fill="#555">little app. Fine.</text>
  <text x="370" y="86" font-size="13" font-weight="700" fill="#2f5d3a">Many &#183; solid</text>
  <text x="370" y="106" font-size="12" fill="#436b4c">A real company.</text>
  <text x="370" y="122" font-size="12" fill="#436b4c">The goal. &#9733;</text>
  <text x="106" y="268" font-size="13" font-weight="700" fill="#3a3a3a">Few &#183; fragile</text>
  <text x="106" y="288" font-size="12" fill="#555">A weekend</text>
  <text x="106" y="304" font-size="12" fill="#555">project. No rush.</text>
  <text x="370" y="268" font-size="13" font-weight="700" fill="#a23b2e">Many &#183; fragile</text>
  <text x="370" y="288" font-size="12" fill="#a23b2e" font-weight="600">THE DANGER ZONE &#8212;</text>
  <text x="370" y="304" font-size="12" fill="#a23b2e">real people on something</text>
  <text x="370" y="320" font-size="12" fill="#a23b2e">that could fall over,</text>
  <text x="370" y="336" font-size="12" fill="#a23b2e">no one watching.</text>
</svg>
<figcaption>Two independent axes. Your anxiety lives on the vertical one — but the world only ever talks about the horizontal one.</figcaption>
</figure>

That last corner is the danger zone. It is not a failure or an embarrassment. It is the *normal* path for an app that found traction faster than its safety nets — which is exactly what happens when you build something good with AI, fast. You're probably reading this for one of two reasons. Either you're already in that corner and need to climb out without losing what works. Or you're on the on-ramp — about to relaunch, about to push for users — and some instinct told you to harden *before* the traffic arrives rather than after something breaks.

Both instincts are right, and this map serves both. Because hardening before the traffic is just the same climb, done early — while it's calm, instead of during an emergency. You harden on the on-ramp, before the crowd, not after the crash.

## Every safety practice kills one specific fear

Here's the reframe that makes the whole climb teachable, and it's worth slowing down for.

Every single discipline a senior developer adds to an app exists to kill one specific, nameable fear. Not because it's "best practice." Not because it's virtuous. Because there's a particular 2 a.m. thought it makes go away. Senior developers don't usually say it this way — to them the practices are just habits — but underneath every habit is a fear it was built to bury.

You already have the fears. You feel them sharply. What you're missing is only the other half of each pair: the practice that removes it.

We name them in pairs — the fear first, in your own words, then the smallest responsible thing that kills it. Never a practice for its own sake; only ever one that buries a fear you can already feel.

The fears come in three groups. Don't try to hold all three at once — you'll only need the one you're standing in. But it helps to see the shape of the whole climb before we start, so here it is, top to bottom:

**"If I touch it, I'll break it, or lose my work."** This is the one you walked in with. The fix isn't "go learn the tools." It's three small things: a saved working version you can return to with one move, so any change is undoable. A private practice copy of your app — your own copy where you try changes before anyone else sees them. And a backup you've actually restored from once, with your own eyes, because a backup you've never restored from is not really a backup. When this is in place, every change becomes reversible. You can finally improve the thing without praying.

**"It'll break and a customer will lose money or data — or get stranded when it's down — and I won't even know."** This fear shows up the moment real strangers are transacting on your app, or simply depending on it being up. The fix: something watching that tells you the instant something breaks, before the angry email. A written list of the paths through your app that must never break — for a marketplace, *log in, list an item, buy, pay, confirm* — turned into checks that run on their own. And a guarantee that no transaction can silently vanish. When this is in place, real people can transact and you'll find out the moment something's off, instead of hearing it from them first.

**"I'm chained to this thing. I can't change it safely now that it's live, and I can't hand it off."** This is the fear most builders never even get the words for. The fix is a release calendar — you stop shipping every new feature the second it's done, and instead line them up on dates, so a finished feature waits its turn instead of owning your night before a deadline — plus a record of what changed and when, written-down instructions so someone other than you could keep it running, and a rule that sorts a break you fix right now from a new feature that rides the schedule. When this is in place, you ship your tenth change as calmly as your first — and you could walk away.

<div class="cal plain" markdown="1">
<span class="lbl">In plain words — what's a "gate"?</span>
A **gate** is just a *level of safety* — how much of a net is under you. It is not a grade, a size, or a measure of success. You climb gates in order, and you don't skip one, because each gate's net rests on the one below it. That's the only thing the word means in this book.
</div>

Notice what this is *not*: a forty-item checklist you grind through all at once. That would just produce a different paralysis — the exact one this book exists to end. You add one net at a time, and only when you actually feel the fear it kills. Hardening everything up front is its own mistake; you'd spend a month building defenses for a flood that isn't coming. The discipline here is almost the opposite of "be thorough." It's: add the single smallest net that removes the fear you have *right now*. Then move faster, without the rest.

We'll come back to each of these in turn, slowly, with the actual moves. For now you just need the shape: three fears, three nets, climbed in order.

## The three gates

Those three groups of fears have names. Developers would call them gates. A gate here is a **level of safety** — that's all. It says nothing about whether you're "successful." It only says how much of a net is under you.

There's a starting line before the first gate — call it Gate 0. It's simply where every just-shipped app begins, the moment after it works for the first time. It is not a grade. It is not a zero you should be ashamed of. It's the trailhead. Everyone starts there, including every app every senior engineer has ever built. You are not behind for being there. You're just at the beginning of a path that, until now, nobody drew for you.

Here is the whole ladder, bottom to top:

<figure class="fig">
<svg viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <line x1="40" y1="500" x2="40" y2="30" stroke="#bbb" stroke-width="1.5" marker-end="url(#up)"/>
  <defs><marker id="up" markerWidth="10" markerHeight="10" refX="3" refY="2" orient="auto"><path d="M0,7 L3,0 L6,7 Z" fill="#bbb"/></marker></defs>
  <text x="32" y="270" text-anchor="middle" font-size="11" fill="#999" transform="rotate(-90 32 270)">climb in order &#8212; don't skip</text>
  <rect x="70" y="36" width="590" height="58" rx="8" fill="#fbfbfb" stroke="#e2e2e2" stroke-dasharray="5 4"/>
  <text x="92" y="62" font-size="14" font-weight="700" fill="#bdbdbd">Scale</text>
  <text x="92" y="80" font-size="12" fill="#c4c4c4">many thousands of users, many hands &#8212; the horizon, not where you are</text>
  <rect x="70" y="104" width="590" height="86" rx="8" fill="#f3f6fb" stroke="#cdd9ec"/>
  <rect x="70" y="104" width="7" height="86" rx="3" fill="#4a6fa5"/>
  <text x="92" y="130" font-size="15" font-weight="700" fill="#33486b">Gate 3 &#8212; Release-managed</text>
  <text x="92" y="150" font-size="12.5" fill="#555">kills &#8220;I'm chained to it &#8212; can't change it safely or hand it off&#8221;</text>
  <text x="92" y="172" font-size="11.5" fill="#7a7a7a">/release-foundation &#183; /release &#183; /handoff</text>
  <rect x="70" y="200" width="590" height="86" rx="8" fill="#fbf5ec" stroke="#ecdcc2"/>
  <rect x="70" y="200" width="7" height="86" rx="3" fill="#c98a2b"/>
  <text x="92" y="226" font-size="15" font-weight="700" fill="#8f6011">Gate 2 &#8212; Go-live</text>
  <text x="92" y="246" font-size="12.5" fill="#555">kills &#8220;it'll break with real people/money on it and I won't even know&#8221;</text>
  <text x="92" y="268" font-size="11.5" fill="#7a7a7a">/qa-harness &#183; /go-live-check &#183; /emergency-plan</text>
  <rect x="70" y="296" width="590" height="86" rx="8" fill="#f1f7f2" stroke="#cfe4d3"/>
  <rect x="70" y="296" width="7" height="86" rx="3" fill="#5a9367"/>
  <text x="92" y="322" font-size="15" font-weight="700" fill="#39623f">Gate 1 &#8212; Robust prototype</text>
  <text x="92" y="342" font-size="12.5" fill="#555">kills &#8220;if I touch it, I'll break it or lose my work&#8221;</text>
  <text x="92" y="364" font-size="11.5" fill="#7a7a7a">/safety-net &#183; /ship-change</text>
  <rect x="70" y="392" width="590" height="80" rx="8" fill="#f6f6f6" stroke="#dcdcdc"/>
  <rect x="70" y="392" width="7" height="80" rx="3" fill="#9aa0a6"/>
  <text x="92" y="418" font-size="15" font-weight="700" fill="#555">Gate 0 &#8212; Just shipped</text>
  <text x="92" y="438" font-size="12.5" fill="#666">it works. that's real. no nets yet &#8212; the starting line everyone begins at</text>
  <text x="92" y="460" font-size="11.5" fill="#9a9a9a">the front door &#8212; /readiness-check &#8212; tells you which gate you're at</text>
</svg>
<figcaption>The whole climb. Most builders need Gate 1 and stop there. You climb higher only when a higher gate's fear becomes actually yours.</figcaption>
</figure>

**Gate 0 — Just shipped.** It works. That's the achievement, and it's real. No nets yet. The starting line.

**Gate 1 — Robust prototype.** Kills "if I touch it, I'll break it or lose my work." You have a saved version to return to, a private copy to try things on, and a backup you've actually restored. Now you can change things without fear.

**Gate 2 — Go-live.** Kills "it'll break and a customer will lose money or data — or get stranded when it's down — and I won't even know." Something is watching, your must-not-break paths are checked automatically, and no transaction can vanish. Now strangers can transact, and people can depend on it, safely.

**Gate 3 — Release-managed.** Kills "I'm chained to this — I can't change it safely or hand it off." A release calendar for new features, written-down operations, and clear support boundaries. This is the gate where you'd finally ship forever without being chained to it, and someone else could take it over.

Above Gate 3 is Scale — the world of many thousands of users, many hands, serious infrastructure. We name it only as the horizon. It's not where you are, and pretending otherwise would just hand you anxiety you don't need.

A word about Gate 3, because it changed recently and honesty matters more than tidiness: when this guide was first written, the Gate-3 tools were still being built, and it said so. **They're built now** — `/release-foundation`, `/release`, and `/handoff` — and you'll meet all of them below. The whole road, front door to handoff, exists. What's *still* coming are a couple of questions that aren't really skills at all — what this will cost you to run, and whether you should become a real business — and this guide still names those as horizon rather than pretending they're answered.

## What forces the floor, and what you only get to park

Now, the question you're actually asking: *which gate do I need to be at?* You don't get to answer that purely by how you feel about it. Part of it is forced on you, and part of it is yours to choose. Getting this distinction right is what keeps you both safe and sane.

**Exposure sets the floor.** Three things, and any one of them on its own drags your required level up to at least Gate 2 — no matter how small your app feels, no matter how few users you have today:

- **Real money flows through it.** Someone can pay, or get paid, or get charged.
- **Other people's data flows through it.** You hold information that belongs to someone who isn't you — accounts, messages, details they'd hate to see leaked.
- **Other people genuinely depend on it being up.** This is the easy one to miss. An app with no payments and no logins at all can still strand a thousand people who were counting on it. "Free" and "no accounts" does not mean "low stakes."

If any one of those is true, the floor is Gate 2. Full stop. And notice what *isn't* on that list: how small you are. "It's just a side project," "I barely have any users," "it's basically a hobby" — none of those lower the floor. Exposure is about what's at stake when it breaks, not how often it's used.

**Intent only parks the ceiling.** Here's the part that's yours. What you *want* — "I'm keeping this small, I'm not chasing growth, I just want it to work for the few people who use it" — is a real and valid choice. But it can only do one thing: set Gate 3 aside, *for now*. You can say "I don't need the full shipping-rhythm-and-handoff machinery yet," and that's fine. But it's reversible — you've parked it until your plans change, not deleted it. And intent can never reach down and lower the floor that exposure set. You don't get to say "I'll keep it small, so I don't need to worry about losing a customer's money." The money is flowing. The floor stands.

<div class="cal plain" markdown="1">
<span class="lbl">The one-sentence version</span>
**Exposure** (money / other people's data / people depending on uptime) sets your *floor*, and you can't opt out of it. **Intent** (how big you want to get) only decides whether Gate 3 is *now* or *parked for later*. Let exposure tell you your floor; climb to it one net at a time.
</div>

## Ship the atom

Before we open the toolbox, one principle that governs how you use all of it, because it's the difference between this map calming you down and this map becoming a new source of dread.

You will be tempted, having now seen the whole ladder, to go do all of it. Don't. Seeing the whole climb at once is the one thing that can turn this map from something that calms you into a new kind of dread — a backlog you feel behind on. It isn't one. The ladder is a menu you pull from when a fear arrives, not a checklist you owe.

Instead: **ship the atom.** Just the one net for the fear in front of you — then go move faster, without the rest, until the product itself tells you it's time for the next one, by handing you the next fear, specifically, in your own gut.

This is the spirit behind a handful of plain principles worth keeping in your pocket as you climb:

- **Buy boring infrastructure before exotic tools.** The dull, proven, widely-used option is almost always the right one for where you are. Save your attention for your product.
- **If you can't rebuild it from scratch in a day, it's too complex for your stage.** Complexity is a cost you pay forever.
- **Every tool you add is a tool you must maintain.** A new thing in the stack is a new thing that can break.
- **When in doubt, do the thing you can undo.** Reversible moves are cheap. Irreversible ones deserve a pause.

One net at a time. That's not you being timid. That's the actual discipline.

## Why you can climb this at all — the AI thesis

There's an honest objection sitting underneath everything so far, and it deserves a straight answer: *"This is exactly the stuff I don't know how to do. And doing it with AI feels like a leap of faith."*

It does. And here's why it feels that way, named precisely.

When you type a naive prompt — *"AI, improve my checkout page"* — what you get back behaves like an eager junior developer. It opens up your actual live code, makes the change directly, and hopes it worked. No saved version first. No check that the important thing still works. No private copy to look at before real users hit it. Just a change, straight into the thing people are using, and a cheerful "done!" That genuinely *is* a leap of faith. Your instinct to be scared of it is correct.

But the AI doesn't have to behave like that junior. The entire trick — the heart of this whole approach — is to wrap the AI in the discipline a senior engineer would never skip, and never let it skip a step.

<figure class="fig">
<svg viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <text x="175" y="28" text-anchor="middle" font-size="13.5" font-weight="700" fill="#a23b2e">The eager junior</text>
  <text x="505" y="28" text-anchor="middle" font-size="13.5" font-weight="700" fill="#39623f">The careful senior (same AI, on rails)</text>
  <line x1="340" y1="44" x2="340" y2="368" stroke="#e6e6e6" stroke-width="1"/>
  <defs><marker id="d" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#999"/></marker></defs>
  <rect x="55" y="48" width="240" height="36" rx="6" fill="#fff" stroke="#ddd"/><text x="175" y="71" text-anchor="middle" font-size="12" fill="#444">&#8220;AI, improve my checkout&#8221;</text>
  <line x1="175" y1="86" x2="175" y2="104" stroke="#999" marker-end="url(#d)"/>
  <rect x="55" y="106" width="240" height="40" rx="6" fill="#f9eae6" stroke="#e3b8af"/><text x="175" y="131" text-anchor="middle" font-size="12" fill="#a23b2e">edits your LIVE app directly</text>
  <line x1="175" y1="148" x2="175" y2="166" stroke="#999" marker-end="url(#d)"/>
  <rect x="55" y="168" width="240" height="40" rx="6" fill="#f9eae6" stroke="#e3b8af"/><text x="175" y="193" text-anchor="middle" font-size="12" fill="#a23b2e">&#8220;done!&#8221; &#8212; hope it worked</text>
  <text x="175" y="250" text-anchor="middle" font-size="12" fill="#888">No copy. No check. No way back.</text>
  <text x="175" y="270" text-anchor="middle" font-size="12.5" font-weight="700" fill="#a23b2e">= a leap of faith</text>
  <rect x="385" y="48" width="240" height="30" rx="6" fill="#fff" stroke="#ddd"/><text x="505" y="68" text-anchor="middle" font-size="11.5" fill="#444">set your live app aside, untouched</text>
  <line x1="505" y1="80" x2="505" y2="92" stroke="#999" marker-end="url(#d)"/>
  <rect x="385" y="94" width="240" height="30" rx="6" fill="#f1f7f2" stroke="#cfe4d3"/><text x="505" y="114" text-anchor="middle" font-size="11.5" fill="#39623f">try it on a private copy</text>
  <line x1="505" y1="126" x2="505" y2="138" stroke="#999" marker-end="url(#d)"/>
  <rect x="385" y="140" width="240" height="30" rx="6" fill="#f1f7f2" stroke="#cfe4d3"/><text x="505" y="160" text-anchor="middle" font-size="11.5" fill="#39623f">check the must-not-break flows</text>
  <line x1="505" y1="172" x2="505" y2="184" stroke="#999" marker-end="url(#d)"/>
  <rect x="385" y="186" width="240" height="30" rx="6" fill="#eef3ec" stroke="#bcd2b8"/><text x="505" y="206" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2f5d3a">YOU look &#8212; with your own eyes</text>
  <line x1="505" y1="218" x2="505" y2="230" stroke="#999" marker-end="url(#d)"/>
  <rect x="385" y="232" width="240" height="30" rx="6" fill="#eef3ec" stroke="#bcd2b8"/><text x="505" y="252" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2f5d3a">your okay &#8594; it goes live</text>
  <text x="505" y="296" text-anchor="middle" font-size="12" fill="#888">A one-move way back stays ready the whole time.</text>
  <text x="505" y="316" text-anchor="middle" font-size="12.5" font-weight="700" fill="#39623f">= a guided procedure with rails</text>
</svg>
<figcaption>Same AI, same prompt. The only difference is the procedure wrapped around it — and that difference is the whole product.</figcaption>
</figure>

The AI does the typing. The procedure enforces the discipline. *You* approve the gates. That's the whole move, and it's what converts "leap of faith" into "guided procedure with safety rails."

That is the product this book is wrapped around. A "virtual lead developer" is nothing more exotic than that procedure, encoded — so the AI acts like a careful senior engineer instead of an eager junior, and the parts that need judgment pause and wait for *your* yes. You don't become a developer. You become the person who approves the gates. That role, it turns out, is one you're entirely qualified for: you know what your app is supposed to do, and you can look at it and tell whether it's doing it. That's the whole job at each gate.

<div class="cal reality" markdown="1">
<span class="lbl">Reality check — "proven" means you watched it</span>
Across this entire system, you don't confirm that a safety net *exists*. You watch it *catch something*. A backup you've never restored from is not a backup. A monitor you've never seen fire is a guess. So whenever this book says a net is "proven," it means one exact thing: a safe, on-purpose failure was made to happen, and **you** watched the net catch it with your own eyes. You are the witness — not the AI. That's what makes the calm real instead of borrowed.
</div>

## The road — every tool, in the order you'd use them

Everything above is the *why*. Here's the *how* — the actual set of tools, in the actual order you'd use them. Each one is a skill you run with the AI. Each does one job. The order is not optional, because each one needs the ground the last one laid.

**The front door — `/readiness-check`.** You don't have to figure out which gate you're at on your own. This is the diagnostic, and it's where everyone starts. You answer four shrug-friendly questions — the kind you can answer even if you're not sure — and it reads through your app's code itself. About five minutes. Then it hands you back two things and only two things: which gate you're at, and the single next move to make. Not a score. Not a grade. A named gate is friendlier and more useful than a number, because it points somewhere. It never fixes anything and never prescribes a specific repair — it diagnoses and it routes. It's the calmest possible front door.

Then the road forks by gate.

**Gate 1, run once — `/safety-net`.** This is the one-time setup that kills "if I touch it, I'll break it or lose my work." When it's done you have four things, each proven, not just switched on: a clean saved version you can return to in one move; your *secrets* — the passwords and access codes your app uses to reach other services, like a payment company or a database — pulled out of the code and actually replaced with brand-new ones, so the old ones sitting exposed are now dead and useless (and only the ones that truly need it, because some of these codes are public by design, and the skill leaves those alone); automated backups; and — the un-skippable part — a restore you watched work, where a real backup was put back and you saw the data come through intact. After this, you cannot lose your work and you cannot lose your data.

**Gate 1, run every time — `/ship-change`.** This is the loop. You run it every single time you change anything, however small — a button color, a typo, a whole feature, doesn't matter. It's the AI thesis made real: set live aside, make the change, preview it on a private practice copy, eyeball it against your must-not-break list, publish only on your okay — with a fresh one-move way back every time. And its very first run quietly stands up the private practice copy `/safety-net` left for it, so by the end of your first change you have the full Gate 1 setup and you've already used it once.

That's Gate 1. For most builders that's the whole emergency, handled. If your exposure sets the floor at Gate 2 — money, other people's data, or people depending on you being up — there are three more.

**Gate 2 — `/qa-harness`.** This turns each plain-English must-not-break flow you named in `/ship-change` into an automatic check — and proves it. You watch it get built, then watch the AI break that flow on purpose, on a throwaway copy, so you see the check go red, then watch it put the flow back. After that the check runs by itself, *inside your change loop*, every time. You never touch test code; you name the flow and witness it get proven. *"The buy button charges a card"* stops being something you click through by hand and hope, and becomes a check that goes red the instant it stops working.

**Gate 2 — `/go-live-check`.** This is the launch-readiness audit, and it's blunt on purpose: a clear go or no-go before you push for real strangers and real money. It proves most go-live nets the same honest way — by making each one fail and watching it catch the failure, with the alert landing on *your* phone or inbox: error monitoring, an uptime alert, a security pass (including the wide-open-database check that catches the most common quiet disaster), transaction integrity, an email that actually arrives. (The one exception is the legal floor — terms and a privacy policy that are present and honest about what you collect — which it checks by reading, not by breaking: a floor, not a lawyer.) It's built to be re-run, because monitors rot — a net that worked in March can quietly stop working by June.

**Gate 2 — `/emergency-plan`.** The calmest tool in the kit: the plan for the night something breaks anyway, so you're not improvising at 2 a.m. It runs in two parts, and says so up front. **Part 1** (15–20 minutes, touches nothing live) writes a one-page emergency card you keep on every device, phone included — *is it just me or everyone? how do I get back to working? what do I tell my users? who do I call?* — and puts your panicking-at-2-a.m. AI on a tested leash so it stays a careful reader, not an improviser making things worse. **Part 2** (recommended now, bookable for later) makes the plan *proven* instead of merely written: it rehearses the undo for real, builds an in-app banner to tell your users, and wires the "your app is down" alarm to your phone. It needs `/safety-net` first — a *tested* way back is a hard requirement. This is the last rung of the go-live gate.

Then Gate 3 — the tools for shipping forever without being chained to it. **These exist now too.**

**Gate 3, run once — `/release-foundation`.** The "driving lesson." You run it once, and it installs a release *schedule* for your new features. The headline is a calendar: you pick how often you put features out (every week / 2 weeks / month), and it builds you a **Future Releases chart** — a plain plan of which feature goes out on which date — and *shows it to you*, laid out by date, so you can read your own plan at a glance and move things around. The big idea, in plain words: now that you can change your app safely, you're a bigger operation, so you stop shipping every feature the second it's done — you put it in a *holding pen* and release it on a date. It also teaches the one rule that ends the panic: if a feature isn't ready by its date, it just catches the next release — no all-nighter.

**Gate 3, on each release date — `/release`.** Release day, seatbelts on. It takes the feature you parked, catches it up to your live app, re-runs your automated checks (`/qa-harness`) and has you watch them go green, then — on your okay — flips the feature on. *This* is the real go-live moment, because the feature was held until now. Then it saves a known-good bookmark you can jump back to, and writes the plain what-changed notes. If a check goes **red**, it stops cold and refuses to bless the version — that's the seatbelt winning, not failing.

**Gate 3, when you step away — `/handoff`.** The capstone. It turns *you-are-the-documentation* into an asset someone else (or future-you) could run without ever calling you. The centerpiece is the accounts inventory — every service, who owns it, *where* the login lives (never the password itself), and which lapses are time-bombs. It writes a first-day guide for a brand-new operator, then *proves* the packet by cold-read: a memory-less reader runs one real task from it alone, and every stuck point becomes a hole patched until the packet carries someone who knows nothing. Peace-of-mind is the default — it touches nothing live and never locks you out. The clean-break "I'm handing this to a real person now" transfer is a separate door that opens only when you say so.

<div class="cal stop" markdown="1">
<span class="lbl">When to stop — the two release tools are for live apps only</span>
Don't set up a release schedule (`/release-foundation`) or run release day (`/release`) unless your app is **actually live to real strangers** — random people you don't know, not just you and a few friends testing. A holding pen and a calendar solve a problem you only *have* once real people depend on what you put out. If it isn't public yet, you don't need a schedule: just keep shipping freely with **`/ship-change`** whenever you want. (About to launch? Run `/go-live-check` first — that's the gate that comes before a release rhythm.) Both skills now ask this up front and turn you around warmly if it isn't time yet.
</div>

## The whole map — when to run each, and when to stop

If you remember nothing else, remember this picture and the table under it. The picture is the road. The table is the "when do I use this, and when do I leave it alone."

<figure class="fig">
<svg viewBox="0 0 680 560" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <defs>
    <marker id="dn" markerWidth="10" markerHeight="10" refX="4" refY="6" orient="auto"><path d="M1,1 L7,1 L4,7 Z" fill="#aaa"/></marker>
    <marker id="rt" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#9bbf9f"/></marker>
    <marker id="rb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#9fb0d0"/></marker>
  </defs>
  <rect x="120" y="18" width="440" height="48" rx="8" fill="#f4f5f6" stroke="#cfcfcf"/>
  <text x="340" y="40" text-anchor="middle" font-size="13.5" font-weight="700" fill="#444">START HERE &#8212; /readiness-check</text>
  <text x="340" y="57" text-anchor="middle" font-size="11.5" fill="#777">tells you your gate &amp; the one next move</text>
  <line x1="340" y1="68" x2="340" y2="88" stroke="#aaa" stroke-width="1.5" marker-end="url(#dn)"/>
  <rect x="40" y="90" width="600" height="96" rx="9" fill="#f5faf6" stroke="#cfe4d3"/>
  <text x="58" y="114" font-size="13.5" font-weight="700" fill="#39623f">GATE 1 &#183; for everyone</text>
  <rect x="58" y="126" width="240" height="48" rx="7" fill="#fff" stroke="#bcd2b8"/>
  <text x="178" y="146" text-anchor="middle" font-size="12.5" font-weight="600" fill="#2f5d3a">/safety-net</text>
  <text x="178" y="164" text-anchor="middle" font-size="11" fill="#7a8f7d">once &#183; the floor you can't fall through</text>
  <line x1="300" y1="150" x2="336" y2="150" stroke="#9bbf9f" stroke-width="1.5" marker-end="url(#rt)"/>
  <rect x="340" y="126" width="282" height="48" rx="7" fill="#fff" stroke="#bcd2b8"/>
  <text x="481" y="146" text-anchor="middle" font-size="12.5" font-weight="600" fill="#2f5d3a">/ship-change</text>
  <text x="481" y="164" text-anchor="middle" font-size="11" fill="#7a8f7d">every single change, forever</text>
  <line x1="340" y1="188" x2="340" y2="206" stroke="#aaa" stroke-width="1.5" marker-end="url(#dn)"/>
  <rect x="40" y="208" width="600" height="110" rx="9" fill="#fcf6ee" stroke="#ecdcc2"/>
  <text x="58" y="232" font-size="13.5" font-weight="700" fill="#8f6011">GATE 2 &#183; if strangers, money, or data depend on it</text>
  <rect x="58" y="244" width="180" height="56" rx="7" fill="#fff" stroke="#e3cda1"/>
  <text x="148" y="266" text-anchor="middle" font-size="12" font-weight="600" fill="#8f6011">/qa-harness</text>
  <text x="148" y="284" text-anchor="middle" font-size="10.5" fill="#a98a52">set up your checks</text>
  <rect x="250" y="244" width="180" height="56" rx="7" fill="#fff" stroke="#e3cda1"/>
  <text x="340" y="266" text-anchor="middle" font-size="12" font-weight="600" fill="#8f6011">/go-live-check</text>
  <text x="340" y="284" text-anchor="middle" font-size="10.5" fill="#a98a52">prove the nets &#183; re-run</text>
  <rect x="442" y="244" width="180" height="56" rx="7" fill="#fff" stroke="#e3cda1"/>
  <text x="532" y="266" text-anchor="middle" font-size="12" font-weight="600" fill="#8f6011">/emergency-plan</text>
  <text x="532" y="284" text-anchor="middle" font-size="10.5" fill="#a98a52">the 2 a.m. plan</text>
  <line x1="340" y1="320" x2="340" y2="338" stroke="#aaa" stroke-width="1.5" marker-end="url(#dn)"/>
  <rect x="40" y="340" width="600" height="150" rx="9" fill="#f4f7fc" stroke="#cdd9ec"/>
  <text x="58" y="364" font-size="13.5" font-weight="700" fill="#33486b">GATE 3 &#183; if you're growing it (and it's live to strangers)</text>
  <rect x="58" y="376" width="240" height="50" rx="7" fill="#fff" stroke="#bcc9e3"/>
  <text x="178" y="396" text-anchor="middle" font-size="12.5" font-weight="600" fill="#33486b">/release-foundation</text>
  <text x="178" y="414" text-anchor="middle" font-size="11" fill="#7d88a5">once &#183; builds your calendar</text>
  <line x1="300" y1="401" x2="336" y2="401" stroke="#9fb0d0" stroke-width="1.5" marker-end="url(#rb)"/>
  <rect x="340" y="376" width="282" height="50" rx="7" fill="#fff" stroke="#bcc9e3"/>
  <text x="481" y="396" text-anchor="middle" font-size="12.5" font-weight="600" fill="#33486b">/release</text>
  <text x="481" y="414" text-anchor="middle" font-size="11" fill="#7d88a5">each release date</text>
  <rect x="58" y="434" width="564" height="44" rx="7" fill="#fff" stroke="#bcc9e3"/>
  <text x="340" y="455" text-anchor="middle" font-size="12.5" font-weight="600" fill="#33486b">/handoff</text>
  <text x="340" y="471" text-anchor="middle" font-size="11" fill="#7d88a5">when you step away &#8212; so you're never the single point of failure</text>
  <text x="340" y="516" text-anchor="middle" font-size="12" fill="#999">Most builders live at Gate 1. You climb only when a gate's fear is actually yours &#8212;</text>
  <text x="340" y="534" text-anchor="middle" font-size="12" fill="#999">never to collect the whole set.</text>
</svg>
<figcaption>The road, front door to handoff. Every arrow is "this needs the one before it." You walk it, you don't sprint it.</figcaption>
</figure>

There's one more picture worth carrying, because once you're at Gate 3 the most common confusion is *"where does this kind of work even go?"* Work splits into three lanes — and that split is exactly why there are separate tools:

<figure class="fig">
<svg viewBox="0 0 680 290" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <rect x="20" y="20" width="640" height="76" rx="9" fill="#fbf1ef" stroke="#e9cdc6"/>
  <rect x="20" y="20" width="6" height="76" rx="3" fill="#b5483d"/>
  <text x="44" y="48" font-size="13" font-weight="700" fill="#9a382c">Something's broken</text>
  <text x="44" y="68" font-size="11.5" fill="#9a6a62">can't buy, can't log in, it's down, an annoying bug</text>
  <text x="44" y="85" font-size="11" fill="#b5847c">&#9655;&#9655;&#9655; out now &#8212; never waits for a date</text>
  <rect x="430" y="38" width="210" height="40" rx="7" fill="#fff" stroke="#e3b8af"/>
  <text x="535" y="63" text-anchor="middle" font-size="12.5" font-weight="600" fill="#9a382c">/ship-change</text>
  <rect x="20" y="106" width="640" height="76" rx="9" fill="#f4f7fc" stroke="#cdd9ec"/>
  <rect x="20" y="106" width="6" height="76" rx="3" fill="#4a6fa5"/>
  <text x="44" y="134" font-size="13" font-weight="700" fill="#33486b">A brand-new feature</text>
  <text x="44" y="154" font-size="11.5" fill="#5e6e8c">a new thing you're adding for your users</text>
  <text x="44" y="171" font-size="11" fill="#8190ab">&#9655; rides a date &#8212; held in the pen until release day</text>
  <rect x="396" y="124" width="244" height="40" rx="7" fill="#fff" stroke="#bcc9e3"/>
  <text x="518" y="143" text-anchor="middle" font-size="11.5" font-weight="600" fill="#33486b">/release-foundation sets it up</text>
  <text x="518" y="158" text-anchor="middle" font-size="11" fill="#7d88a5">/release puts it out</text>
  <rect x="20" y="192" width="640" height="76" rx="9" fill="#f0f0f1" stroke="#d3d3d6"/>
  <rect x="20" y="192" width="6" height="76" rx="3" fill="#3a3f4a"/>
  <text x="44" y="220" font-size="13" font-weight="700" fill="#2f333c">A real emergency</text>
  <text x="44" y="240" font-size="11.5" fill="#5a5f68">2 a.m. &#8220;it's down,&#8221; a security hole, data at risk</text>
  <text x="44" y="257" font-size="11" fill="#7a7f88">&#9655;&#9655;&#9655;&#9655; fastest lane &#8212; break glass</text>
  <rect x="430" y="210" width="210" height="40" rx="7" fill="#fff" stroke="#c4c4c8"/>
  <text x="535" y="235" text-anchor="middle" font-size="12.5" font-weight="600" fill="#2f333c">/emergency-plan</text>
</svg>
<figcaption>Three lanes, three speeds. Reaching Gate 3 means you've earned the right to run it like a real company: features wait on a schedule, fixes don't, emergencies break glass.</figcaption>
</figure>

And here's the same thing as a table you can scan — what each tool is for, when you run it, and the part people forget: **when to leave it alone.**

| Skill | What it's for (plain) | Run it… | When to stop / skip | Needs first |
|---|---|---|---|---|
| **/readiness-check** | Tells you your gate and the one next move | First — and any time you're unsure where you stand | It only points; it never fixes. Re-run later to see progress | — |
| **/safety-net** | A floor you can't fall through: restore point, secrets cleaned up, backups that really restore | Once, before your first real change | One-time — don't redo finished steps; a plain static site skips backups (its history *is* the backup) | — |
| **/ship-change** | The everyday safe-change loop: private copy first, live only on your okay | **Every single time** you change anything, however small | Never "too small" to use, and never skipped — it's the loop you live in | /safety-net |
| **/qa-harness** | Turns a must-not-break flow into a check proven to go red | When you want "how do I know nothing broke" handled | Set up per flow; re-prove a check only when that flow changes. Not for phone apps yet (browser-only) | /ship-change |
| **/go-live-check** | Proves your nets catch real failures before strangers / money arrive | Before you launch to the public or push for growth | Re-run every few months (monitors rot). A FAIL means "not yet" — fix, then re-run | /safety-net |
| **/emergency-plan** | The 2 a.m. break-glass card, a proven way back, and an alarm | When you're about to depend on uptime, or scared of the night it breaks | Skip if nobody depends on it being up yet. Re-check every few months | /safety-net |
| **/release-foundation** | Once: your release calendar + holding pen + the fix-now-vs-feature sorter (and it shows you the calendar) | Once, when you're growing and putting new features out to real users | **Stop if it's not live to real strangers**, or if it's a finished personal thing you just tinker with | /safety-net, /ship-change |
| **/release** | Release day: put a parked feature live, seatbelts on, bookmark + notes | On each release date, or when a parked feature is ready | **Stop if it's not live to real strangers.** A red check stops it cold — that's it working | /safety-net, /qa-harness, /ship-change |
| **/handoff** | Prove someone else could run it without you — so you're not the single point of failure | When stepping away, or just for peace of mind | The clean-break "real handover" stays shut unless you say "I'm handing this to a real person now." Refresh every few months | the whole ladder behind it |

## What runs on its own, and what taps you on the shoulder

You asked a sharp question: *which of these run on a schedule?* The honest answer has two halves, and keeping them apart is the whole point — because for a non-developer, "scheduled" can mean two very different things, and confusing them is how people end up either anxious or over-reminded.

<figure class="fig">
<svg viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <rect x="20" y="20" width="310" height="180" rx="10" fill="#f1f7f2" stroke="#cfe4d3"/>
  <circle cx="175" cy="70" r="26" fill="#fff" stroke="#5a9367" stroke-width="2"/>
  <rect x="162" y="60" width="9" height="9" rx="2" fill="#5a9367"/><rect x="179" y="60" width="9" height="9" rx="2" fill="#5a9367"/>
  <rect x="164" y="80" width="22" height="4" rx="2" fill="#5a9367"/>
  <line x1="175" y1="44" x2="175" y2="34" stroke="#5a9367" stroke-width="2"/><circle cx="175" cy="32" r="3" fill="#5a9367"/>
  <text x="175" y="124" text-anchor="middle" font-size="13.5" font-weight="700" fill="#39623f">Runs on its own</text>
  <text x="175" y="146" text-anchor="middle" font-size="11.5" fill="#5b7d62">set it up once &#8212;</text>
  <text x="175" y="163" text-anchor="middle" font-size="11.5" fill="#5b7d62">then it works while you sleep,</text>
  <text x="175" y="180" text-anchor="middle" font-size="11.5" fill="#5b7d62">no human needed</text>
  <rect x="350" y="20" width="310" height="180" rx="10" fill="#fbf5ec" stroke="#ecdcc2"/>
  <circle cx="505" cy="70" r="26" fill="#fff" stroke="#c98a2b" stroke-width="2"/>
  <circle cx="505" cy="70" r="16" fill="none" stroke="#c98a2b" stroke-width="2"/>
  <line x1="505" y1="70" x2="505" y2="59" stroke="#c98a2b" stroke-width="2"/><line x1="505" y1="70" x2="513" y2="70" stroke="#c98a2b" stroke-width="2"/>
  <path d="M527 52 l9 -6 M529 60 l10 -2" stroke="#c98a2b" stroke-width="2" fill="none"/>
  <text x="505" y="124" text-anchor="middle" font-size="13.5" font-weight="700" fill="#8f6011">Taps you on the shoulder</text>
  <text x="505" y="146" text-anchor="middle" font-size="11.5" fill="#9a7636">a reminder shows up &#8212;</text>
  <text x="505" y="163" text-anchor="middle" font-size="11.5" fill="#9a7636">YOU run a short skill</text>
  <text x="505" y="180" text-anchor="middle" font-size="11.5" fill="#9a7636">(15&#8211;30 min), then you're done</text>
</svg>
<figcaption>Two kinds of "scheduled." The left runs without you. The right is a nudge that brings <em>you</em> back to do a short, human job.</figcaption>
</figure>

**Half one — set up once, then it runs by itself (you do nothing).** These aren't really "skills on a schedule"; they're automatic background jobs that certain skills *install* for you. Once they're on, they run with no one watching:

| What runs by itself | Installed by |
|---|---|
| Nightly backups of your data | **/safety-net** |
| A secret-leak guard that checks every save and blocks a leak | **/safety-net** |
| Your must-not-break checks — run automatically on **every change** | **/qa-harness** (they fire inside the `/ship-change` loop) |
| "Something errored" alert → your phone or inbox | **/go-live-check** |
| "Your app is down" alert → your phone | **/go-live-check** + **/emergency-plan** — *one shared alarm,* coordinated, not two |
| A quiet "time-bomb" watch for renewals/expiries (domain, card, free-tier caps) that stays silent until something's about to bite | **/handoff** |

**Half two — a reminder taps you to come run something (15–30 min, you do it).** *These* are the ones that genuinely "run on a schedule" in the everyday sense — but what's scheduled is a **nudge to a human**, not an action. Each is wired through the kit's reminder mechanism (`/schedule`) when you set the skill up, and each one *only* prompts you; it never changes your app by itself:

| The reminder | Brings you back to run | Owned by |
|---|---|---|
| "It's release day — here's what's parked" | **/release** (you take the look, you give the okay) | /release-foundation sets it; /release re-anchors it |
| "Monitors rot — re-run your go-live check" (every few months) | **/go-live-check** | /go-live-check |
| "Re-check your emergency card" (every few months) | **/emergency-plan** | /emergency-plan |
| "Refresh your handoff packet" (every few months) | **/handoff** | /handoff |

**And the rest you run only when you need them — never on a clock:** `/readiness-check` (whenever you're unsure), `/ship-change` (every time you change something), `/safety-net` and `/release-foundation` (one-time setups), and `/emergency-plan` *in an actual emergency* (its card and alarm are standing, but you reach for the plan when the night comes).

<div class="cal plain" markdown="1">
<span class="lbl">The shortest answer to "which run on a schedule?"</span>
**Release day** is the one human ceremony that lives on a recurring calendar. **/go-live-check, /emergency-plan, and /handoff** each set a gentle few-months reminder to *re-run* themselves, because nets rot. Everything *automatic* (backups, the secret guard, your checks, the error/uptime alarms, the renewal watch) is set up once by a skill and then runs without you. No skill ever pushes a change to your live app on a timer — a human always approves the moments that matter.
</div>

## What isn't on the map yet — and why that's the point

A map you can trust is one that's honest about where the trail runs out. The nine skills above are all built and real. Here, plainly, are the questions this kit *doesn't* answer yet — named, not buried, because answering them badly would be worse than marking them clearly.

**"What will all this cost me to run?"** A fair question, and one worth asking before you lean on any of it. But cost is the one place a confident answer is dangerous: any number a tool hands you reads like a promise, and the day the bill comes in different, it spends the trust everything else depends on. So this book names no prices, no "free until," no ceilings. Cost gets its own dedicated tool later, grounded in your actual setup and real pricing — not a guess dressed up as a fact.

**"Will what I built hold up where I'm trying to take it?"** Sometimes the very foundation an app stands on — the plan it's hosted on, the database it started with — has a ceiling a real growth push will eventually meet. That's true and worth knowing early. But naming a specific breaking point ("it falls over at exactly this much traffic") is the same can't-stand-behind-it trap as quoting a cost. So if it comes up, it's a directional heads-up, never a number — and, like cost, it's headed for its own tool.

**"If real money and real strangers are involved, am I personally on the hook?"** The moment your app takes real money and real people depend on it, a non-technical question arrives: should this stop being "a project" and become a real business, so that if something goes wrong it doesn't land on you personally? It's the legal twin of the go-live gate, and most builders hit it with no vocabulary for it. It's real, it's coming as its own plain-English explainer, and it won't be legal advice — just orientation.

And two smaller, honest gaps in the tools themselves. First: there's no skill yet for the **admin dashboard** every builder eventually wants — the back-office view of *who signed up, what's selling, what's stuck* — though it's wanted and on the way. Second: the automatic-checks skill (`/qa-harness`) drives a real web browser, so for now it fits **web apps**; if what you built is a phone app, that particular protection isn't there yet, and the map says so plainly rather than pretend a browser check covers a phone.

None of this is in a footnote. It's here, named, because the method is the same at every level: tell you the truth about what's solid and what isn't, and never let "looks handled" stand in for "is handled."

## Where you actually are

Let's go back to where you started, because the whole point is to answer it in full.

You walked in scared to touch your own app. Under that one feeling were three fears about the app itself — and beneath all of them, a fourth doubt about the method. Each has an answer now.

*I'll break it or lose my work* — you'll have a saved version you can return to in one move, and a private copy to try everything on first.

*It'll fail with real people on it and I won't know* — when you're exposed enough to need it, you'll have nets you've personally watched catch a failure, and you'll find out the moment it happens, not from an angry customer.

*I'll be chained to this thing forever* — there's a real release rhythm, a written-down operation, and a proven handoff packet, so you ship your tenth change as calmly as your first and could hand the whole thing to someone else tomorrow.

And the doubt underneath all three — *doing this with AI is a leap of faith* — isn't true anymore either. It's a guided procedure: the AI does the typing, you approve each step, and a way back stays ready the whole time.

And the small scope you're at right now is not "stuck." It's correctly sized for today. You parked what deserves parking and you're climbing only what your actual exposure demands. That's not falling short of some bigger thing. That's doing it right.

<div class="cal do" markdown="1">
<span class="lbl">Your whole assignment</span>
There's only one thing left to do, and it's small. Open your project and run **`/readiness-check`**. Five minutes, four easy questions, and it tells you the one gate you're at and the one move that comes next. Not the ladder. Not the nine skills. Just the front door.
</div>

If you built something real with AI and you're scared to touch it, you're not behind. You're exactly where the map begins.
