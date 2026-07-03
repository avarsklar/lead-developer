#!/usr/bin/env python3
"""Build the multi-page 'Lead Developer Hardening Handbook' site.

Two kinds of pages:
  * MAIN pages (Start, the three gates, Everything) — sticky top nav + prev/next.
  * SKILL pages (one per skill) — same top nav (parent gate highlighted),
    a back-to-gate footer, and an embedded Remotion video.

Raw HTML/SVG in the markdown passes through. Usage:  python3 build.py
"""
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent
EXT = ["extra", "toc", "sane_lists"]
REPO_URL = "https://github.com/avarsklar/lead-developer-skills"

# (slug, nav-label, body-class, md-file)  -- the 5 top-nav pages
PAGES = [
    ("index",      "Start",       "start",      "index.md"),
    ("gate-1",     "Gate 1",      "gate1",      "gate-1.md"),
    ("gate-2",     "Gate 2",      "gate2",      "gate-2.md"),
    ("gate-3",     "Gate 3",      "gate3",      "gate-3.md"),
    ("everything", "Everything",  "everything", "everything.md"),
]

# (out-slug, gate-label, gate-href, body-class, nav-active-slug)  -- per-skill pages
SKILL_PAGES = [
    ("skill-readiness-check",    "Start",  "index.html",  "start", "index"),
    ("skill-safety-net",         "Gate 1", "gate-1.html", "gate1", "gate-1"),
    ("skill-ship-change",        "Gate 1", "gate-1.html", "gate1", "gate-1"),
    ("skill-qa-harness",         "Gate 2", "gate-2.html", "gate2", "gate-2"),
    ("skill-go-live-check",      "Gate 2", "gate-2.html", "gate2", "gate-2"),
    ("skill-emergency-plan",     "Gate 2", "gate-2.html", "gate2", "gate-2"),
    ("skill-release-foundation", "Gate 3", "gate-3.html", "gate3", "gate-3"),
    ("skill-release",            "Gate 3", "gate-3.html", "gate3", "gate-3"),
    ("skill-handoff",            "Gate 3", "gate-3.html", "gate3", "gate-3"),
]

CSS = """
:root{--ink:#222;--muted:#666;--line:#e0e0e0;--g1:#5a9367;--g2:#c98a2b;--g3:#4a6fa5}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--ink);line-height:1.62;margin:0;padding:0;background:#fff}
main{max-width:720px;margin:0 auto;padding:6px 24px 60px}
.topnav{position:sticky;top:0;background:rgba(255,255,255,.93);backdrop-filter:saturate(180%) blur(8px);-webkit-backdrop-filter:saturate(180%) blur(8px);border-bottom:1px solid var(--line);text-align:center;padding:11px 12px;font-size:14px;z-index:10}
.topnav a{color:#555;text-decoration:none;margin:0 2px;padding:5px 9px;border-radius:6px;display:inline-block}
.topnav a:hover{background:#f3f3f3}
.topnav a.here{color:#111;font-weight:700;background:#eee}
.topnav a.get{color:#4a6fa5;font-weight:700}
.topnav a.get:hover{background:#eef2f8}
.topnav .sep{color:#cfcfcf}
h1{font-size:28px;line-height:1.2;border-bottom:2px solid #333;padding-bottom:9px;margin:26px 0 16px}
.gate1 h1{border-color:var(--g1)} .gate2 h1{border-color:var(--g2)} .gate3 h1{border-color:var(--g3)}
h2{font-size:20px;margin-top:30px}
h2 code{background:transparent;padding:0;font-size:1em;font-weight:700}
h2 a{text-decoration:none;border-bottom:2px solid rgba(0,0,0,.16);padding-bottom:1px;color:inherit}
h2 a:hover{border-bottom-color:currentColor}
.gate1 h2 a{color:var(--g1)} .gate2 h2 a{color:var(--g2)} .gate3 h2 a{color:var(--g3)}
.start h2 a{color:#444}
.lead{font-size:17px;color:#444}
.kicker{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:800;color:#4a6fa5;margin:20px 0 -8px}
.taphint{font-size:13.5px;color:#8a8a8a;background:#f7f7f7;border:1px solid #eee;border-radius:8px;padding:9px 13px;margin:4px 0 6px}
code{background:#f4f4f4;padding:2px 6px;border-radius:3px;font-size:.92em;font-family:"SF Mono",Menlo,monospace}
a{color:#4a6fa5}
table{border-collapse:collapse;margin:18px 0;width:100%;font-size:13.5px}
th,td{border:1px solid #ccc;padding:8px 11px;text-align:left;vertical-align:top}
th{background:#f0f0f0}
td a{font-weight:600;text-decoration:none}
td a:hover{text-decoration:underline}
ul,ol{padding-left:22px}
li{margin:5px 0}
strong{color:#000}
em{color:#666}
svg{max-width:100%;height:auto;display:block;margin:6px auto}
video{width:100%;border-radius:11px;border:1px solid #e6e6e6;background:#fafafa;display:block;margin:14px 0 6px}
figure.fig{margin:22px 0}
figure.fig figcaption{font-size:13px;color:#8a8a8a;text-align:center;margin-top:8px;font-style:italic}
.cal{border-left:4px solid #ccc;background:#fafafa;padding:12px 18px;margin:20px 0;border-radius:0 6px 6px 0;font-size:15px}
.cal .lbl{display:block;font-size:11px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;margin-bottom:6px}
.cal p{margin:6px 0}
.cal.do{border-left-color:var(--g1);background:#f1f7f2}.cal.do .lbl{color:#39623f}
.cal.plain{border-left-color:#6b86b3;background:#f2f5fa}.cal.plain .lbl{color:#3f5780}
.cal.reality{border-left-color:var(--g2);background:#fbf5ec}.cal.reality .lbl{color:#8f6011}
.cal.stop{border-left-color:#b5483d;background:#f9ece9}.cal.stop .lbl{color:#9a382c}
.gatecheck{border:2px solid #ccc;border-radius:11px;padding:18px 20px;margin:14px 0 26px;background:#fbfbfb}
.gatecheck .q{display:block;font-size:13px;letter-spacing:.05em;text-transform:uppercase;font-weight:800;margin-bottom:9px}
.gatecheck p{margin:8px 0}
.gatecheck.g1{border-color:var(--g1);background:#f4faf5}.gatecheck.g1 .q{color:#39623f}
.gatecheck.g2{border-color:var(--g2);background:#fdf7ee}.gatecheck.g2 .q{color:#8f6011}
.gatecheck.g3{border-color:var(--g3);background:#f4f7fc}.gatecheck.g3 .q{color:#33486b}
.pagenav{margin-top:46px;padding-top:16px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:12px;font-size:15px}
.pagenav a{color:#4a6fa5;text-decoration:none;font-weight:600}
.pagenav .spacer{flex:1}
@media (max-width:520px){main{padding:6px 16px 48px}.topnav a{padding:5px 7px}h1{font-size:24px}}
"""

TEMPLATE = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>{title} — Lead Developer Hardening Handbook</title><style>{css}</style></head>'
            '<body class="{bodyclass}">{nav}<main>{body}{footer}</main></body></html>')


def nav(active):
    parts = []
    for i, (slug, label, _, _) in enumerate(PAGES):
        if i:
            parts.append('<span class="sep">·</span>')
        here = ' class="here"' if slug == active else ''
        parts.append(f'<a href="{slug}.html"{here}>{label}</a>')
    parts.append('<span class="sep">·</span>')
    parts.append(f'<a href="{REPO_URL}" class="get" target="_blank" rel="noopener">Get the skills ↗</a>')
    return '<nav class="topnav">' + ''.join(parts) + '</nav>'


def main_footer(cur):
    idx = next(i for i, p in enumerate(PAGES) if p[0] == cur)
    left = (f'<a href="{PAGES[idx-1][0]}.html">&larr; {PAGES[idx-1][1]}</a>'
            if idx > 0 else '<span></span>')
    right = (f'<a href="{PAGES[idx+1][0]}.html">{PAGES[idx+1][1]} &rarr;</a>'
             if idx < len(PAGES) - 1 else '<span></span>')
    return f'<div class="pagenav">{left}<span class="spacer"></span>{right}</div>'


def skill_footer(gate_label, gate_href):
    left = f'<a href="{gate_href}">&larr; Back to {gate_label}</a>'
    right = '<a href="everything.html">Everything &rarr;</a>'
    return f'<div class="pagenav">{left}<span class="spacer"></span>{right}</div>'


def render(md_file):
    return markdown.markdown((ROOT / md_file).read_text(encoding="utf-8"), extensions=EXT)


def build():
    for slug, label, bodyclass, md in PAGES:
        html = TEMPLATE.format(title=label, css=CSS, bodyclass=bodyclass,
                               nav=nav(slug), body=render(md), footer=main_footer(slug))
        (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
        print("built", slug + ".html")

    for out, gate_label, gate_href, bodyclass, nav_active in SKILL_PAGES:
        md = f"{out}.md"
        if not (ROOT / md).exists():
            print("  skip", out, "(no md)")
            continue
        # title from the skill slug
        title = "/" + out.replace("skill-", "")
        html = TEMPLATE.format(title=title, css=CSS, bodyclass=bodyclass,
                               nav=nav(nav_active), body=render(md),
                               footer=skill_footer(gate_label, gate_href))
        (ROOT / f"{out}.html").write_text(html, encoding="utf-8")
        print("built", out + ".html")


if __name__ == "__main__":
    build()
