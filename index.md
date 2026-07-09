<p class="kicker">Lead Developer Hardening Handbook</p>

# Scared to touch your own app?

<p class="lead">You built something real with AI. It works. People use it — maybe pay for it. And now you're scared to change a single thing, because you might break it.</p>

That fear is normal. It's what crossing from *making something work once* into *running something real* feels like, and nobody handed you the map for that part.

I created an app for fun for my college campus, but quickly became scared of it when strangers' data and money transactions became real. I didn't know how to secure the site, how to change things, or what steps to take next.

This is the map. It's short on purpose.

<div class="cal do" markdown="1">
<span class="lbl">Start here</span>
Not sure where you stand? Open your app's folder in Claude Code and run **[`/readiness-check`](skill-readiness-check.html)** — five minutes, four shrug-friendly questions, and it only looks; it never changes anything. It tells you which gate you're at and your next move. Don't have the skills yet? [Grab them first](#get); it takes about two minutes.
</div>

## The one big idea

Every fear you have about your app has a name, and every named fear has a smallest possible fix — not a course, not a rebuild, not a computer-science degree. You add one safety net at a time, and only when you actually feel the fear it removes.

Safety here is measured in **gates**: levels of how much net is under you. A gate answers one question: *how protected are you if something goes wrong?*

## Two things people confuse

There are two completely separate things, and your anxiety lives on the one nobody talks about:

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
<figcaption>Your anxiety lives on the vertical axis. The dangerous corner is lots of people on something fragile. That's exactly what happens when you build something good with AI, fast.</figcaption>
</figure>

## The trick that makes this safe to do with AI

A naive prompt — *"AI, fix my checkout"* — behaves like an eager junior, and being scared of that is correct. The whole approach here is to wrap the same AI in the rails a careful senior would never skip:

<figure class="fig">
<svg viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <text x="175" y="28" text-anchor="middle" font-size="13.5" font-weight="700" fill="#a23b2e">The eager junior</text>
  <text x="505" y="28" text-anchor="middle" font-size="13.5" font-weight="700" fill="#39623f">The careful senior (same AI, on rails)</text>
  <line x1="340" y1="44" x2="340" y2="368" stroke="#e6e6e6" stroke-width="1"/>
  <defs><marker id="d" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#999"/></marker></defs>
  <rect x="55" y="48" width="240" height="36" rx="6" fill="#fff" stroke="#ddd"/><text x="175" y="71" text-anchor="middle" font-size="12" fill="#444">&#8220;AI, fix my checkout&#8221;</text>
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
<figcaption>Same AI, same prompt. The only difference is the procedure around it.</figcaption>
</figure>

You don't become a developer. You become the person who gives the okay. You're already qualified for that, because you know what your app is supposed to do and you can look and tell if it's doing it.

## The whole climb

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
  <text x="92" y="130" font-size="15" font-weight="700" fill="#33486b">Gate 3 &#8212; Run it like a real thing</text>
  <text x="92" y="150" font-size="12.5" fill="#555">kills &#8220;I'm chained to it &#8212; can't change it calmly or hand it off&#8221;</text>
  <text x="92" y="172" font-size="11.5" fill="#7a7a7a">/release-foundation &#183; /release &#183; /handoff</text>
  <rect x="70" y="200" width="590" height="86" rx="8" fill="#fbf5ec" stroke="#ecdcc2"/>
  <rect x="70" y="200" width="7" height="86" rx="3" fill="#c98a2b"/>
  <text x="92" y="226" font-size="15" font-weight="700" fill="#8f6011">Gate 2 &#8212; Safe for real strangers</text>
  <text x="92" y="246" font-size="12.5" fill="#555">kills &#8220;it'll break with real people/money on it and I won't even know&#8221;</text>
  <text x="92" y="268" font-size="11.5" fill="#7a7a7a">/qa-harness &#183; /go-live-check &#183; /emergency-plan</text>
  <rect x="70" y="296" width="590" height="86" rx="8" fill="#f1f7f2" stroke="#cfe4d3"/>
  <rect x="70" y="296" width="7" height="86" rx="3" fill="#5a9367"/>
  <text x="92" y="322" font-size="15" font-weight="700" fill="#39623f">Gate 1 &#8212; Stop being scared to touch it</text>
  <text x="92" y="342" font-size="12.5" fill="#555">kills &#8220;if I touch it, I'll break it or lose my work&#8221;</text>
  <text x="92" y="364" font-size="11.5" fill="#7a7a7a">/safety-net &#183; /ship-change</text>
  <rect x="70" y="392" width="590" height="80" rx="8" fill="#f6f6f6" stroke="#dcdcdc"/>
  <rect x="70" y="392" width="7" height="80" rx="3" fill="#9aa0a6"/>
  <text x="92" y="418" font-size="15" font-weight="700" fill="#555">Gate 0 &#8212; Just shipped</text>
  <text x="92" y="438" font-size="12.5" fill="#666">it works. that's real. no nets yet &#8212; where everyone begins</text>
  <text x="92" y="460" font-size="11.5" fill="#9a9a9a">the front door &#8212; /readiness-check &#8212; tells you which gate you're at</text>
</svg>
<figcaption>Four gates, and the horizon above them. Most people need Gate 1 and stop there. You climb higher only when a higher gate's fear becomes <em>yours</em> — never to collect the whole set.</figcaption>
</figure>

## Where to go from here

Once `/readiness-check` tells you your gate, read that gate's page; each one starts by helping you check *are you even here yet?*

[**Gate 1 — Stop being scared to touch it**](gate-1.html) · [**Gate 2 — Safe for real strangers**](gate-2.html) · [**Gate 3 — Run it like a real thing**](gate-3.html)

Or see [**everything on one page**](everything.html).

## Who made this

I am a college student collaborating with two Rice University professors. I run these skills to build and maintain my own apps — including [Bucknell Refit](https://bucknellrefit.com), a campus marketplace students use to buy and sell, with real money moving through it. This isn't theory for me: it's the exact procedure I use to change a live app without breaking it. You can find me on [LinkedIn](https://www.linkedin.com/in/ava-sklar-06851a2a2) or email me at [avarsklar@gmail.com](mailto:avarsklar@gmail.com).

<div class="cal plain" markdown="1" id="get">
<span class="lbl">Get the skills</span>
The nine skills are free, and they run in **Claude Code**, the same kind of AI you already build with, pointed at the folder your app lives in. **[Get them on GitHub ↗](https://github.com/avarsklar/lead-developer-skills)**: click the green **Code** button, choose **Download ZIP** (no account needed), and follow the short install steps in the README. Then run `/readiness-check`.
</div>
