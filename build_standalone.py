#!/usr/bin/env python3
"""Build ONE self-contained handbook HTML you can send or drop on a portfolio.

Linearizes all the handbook pages into a single scrollable page, rewrites the
cross-page links (skill-x.html -> #skill-x) into in-page anchors, and embeds the
9 videos as base64 data URIs so the file works with nothing else beside it — no
folder, no repo, no server. Output: ../Lead-Developer-Hardening-Handbook.html

Usage:  python3 build_standalone.py
"""
import base64
import re
from pathlib import Path
import markdown
from build import CSS  # reuse the site's stylesheet

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "Lead-Developer-Hardening-Handbook.html"
EXT = ["extra", "sane_lists"]  # no "toc" -> avoids duplicate header ids across pages

# (md file, section id, gate class) — in reading order
ORDER = [
    ("index.md",                     "index",                 "start"),
    ("skill-readiness-check.md",     "skill-readiness-check", "start"),
    ("gate-1.md",                    "gate-1",                "gate1"),
    ("skill-safety-net.md",          "skill-safety-net",      "gate1"),
    ("skill-ship-change.md",         "skill-ship-change",     "gate1"),
    ("gate-2.md",                    "gate-2",                "gate2"),
    ("skill-qa-harness.md",          "skill-qa-harness",      "gate2"),
    ("skill-go-live-check.md",       "skill-go-live-check",   "gate2"),
    ("skill-emergency-plan.md",      "skill-emergency-plan",  "gate2"),
    ("gate-3.md",                    "gate-3",                "gate3"),
    ("skill-release-foundation.md",  "skill-release-foundation", "gate3"),
    ("skill-release.md",             "skill-release",         "gate3"),
    ("skill-handoff.md",             "skill-handoff",         "gate3"),
    ("everything.md",                "everything",            "everything"),
]

_video_cache = {}
def embed_videos(html):
    def repl(m):
        name = m.group(1)
        if name not in _video_cache:
            p = ROOT / "videos" / f"{name}.mp4"
            if not p.exists():
                return m.group(0)  # leave as-is if missing
            b64 = base64.b64encode(p.read_bytes()).decode("ascii")
            _video_cache[name] = f"data:video/mp4;base64,{b64}"
        return f'src="{_video_cache[name]}"'
    return re.sub(r'src="videos/([\w-]+)\.mp4"', repl, html)

def rewrite_links(html):
    # skill-safety-net.html(#x) -> #skill-safety-net ; index.html -> #index ; etc.
    return re.sub(r'href="([\w-]+)\.html(?:#[\w-]+)?"', r'href="#\1"', html)

EXTRA_CSS = """
section.hb{border-top:1px solid #ededed;padding-top:8px;margin-top:8px}
section.hb:first-of-type{border-top:none}
.hbnav a.get{color:#4a6fa5;font-weight:700}
"""

def nav():
    items = [("index","Start"),("gate-1","Gate 1"),("gate-2","Gate 2"),
             ("gate-3","Gate 3"),("everything","Everything")]
    parts = []
    for i,(slug,label) in enumerate(items):
        if i: parts.append('<span class="sep">·</span>')
        parts.append(f'<a href="#{slug}">{label}</a>')
    parts.append('<span class="sep">·</span>')
    parts.append('<a href="https://github.com/avarsklar/lead-developer-skills" '
                 'class="get" target="_blank" rel="noopener">Get the skills ↗</a>')
    return '<nav class="topnav hbnav">' + ''.join(parts) + '</nav>'

def build():
    sections = []
    for md, sid, cls in ORDER:
        raw = (ROOT / md).read_text(encoding="utf-8")
        body = markdown.markdown(raw, extensions=EXT)
        body = rewrite_links(embed_videos(body))
        sections.append(f'<section id="{sid}" class="hb {cls}">{body}</section>')
    doc = (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Lead Developer Hardening Handbook</title>'
        f'<style>{CSS}{EXTRA_CSS}</style></head><body class="start">'
        f'{nav()}<main>' + "\n".join(sections) + '</main></body></html>'
    )
    OUT.write_text(doc, encoding="utf-8")
    mb = OUT.stat().st_size / 1_000_000
    print(f"built {OUT.name}  ({mb:.1f} MB, {len(_video_cache)} videos embedded)")

if __name__ == "__main__":
    build()
