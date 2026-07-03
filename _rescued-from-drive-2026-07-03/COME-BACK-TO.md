# Come back to this — Scared to Touch It

*Parked on 2026-07-01. Current state is good and shippable; these are the "later" items.*

## Publishing — ✅ DONE (live 2026-07-01)
- The guide is **live at https://avarsklar.github.io/lead-developer/** (repo `avarsklar/lead-developer`, GitHub Pages). Works on phone, videos included.
- The skills kit is public at https://github.com/avarsklar/lead-developer-skills
- To update the live site later: edit in `handbook-site/`, run `python3 build.py`, then `git -C handbook-site add -A && git -C handbook-site commit -m "update" && git -C handbook-site push`.

## Voiceover (the main "come back" item)
- Videos currently use the neural voice **Amy** (fine, warm). To change it:
  - Open **`handbook-site/voice-compare.html`** in a real browser, listen, and pick a different voice (Clara / Lessac / Ryan), OR
  - **Record your own** — recipe + the 9 scripts are on that page. Drop the clips in a folder and Claude re-syncs + re-renders.
  - For studio quality, an ElevenLabs / OpenAI TTS key would beat all the local voices.

## Smaller polish (offered, not done)
- A "make it leaner" trim pass on the long single-file `Handbook.md` (the site superseded it; could retire the old PDF).
- Fold the live-to-strangers gate wording into `Skills.md` + the Game Plan for consistency (only the skills + site have it now).
- The "everything" page could also carry the full long-form text if you'd rather it be a true catch-all.

## Known limits (by design, named in the guide)
- No cost tool, no scaling-ceiling tool, no LLC/liability explainer, no admin-dashboard skill, no phone-app testing yet.
