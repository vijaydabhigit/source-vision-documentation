# source-vision-documentation — the home for all Source Vision docs & skills

This repo is the **single home** for everything that describes the Source Vision project. The Laravel code lives separately in the sibling `../source-vision/` repo.

## The rule

> **Always create documents in `documents/` and skills in `skills/` inside this repo — never inside the code repo.**

- New document (`.md`, generated `.docx`, notes, plans, meeting docs) → `documents/`.
- New skill → `skills/<skill-name>/SKILL.md`.
- Never add a `documentation/` folder or a `.claude/skills/` folder inside `../source-vision/`.

## Layout

```
source-vision-documentation/
├── README.md                     # index — read this first
├── CLAUDE.md                     # this file
├── documents/                    # ALL documents + their tooling
│   ├── 00–06 *.md (+ .docx copies)
│   ├── check-sources.sh          # drift check against the client's source files
│   ├── build-docs.sh             # regenerate the .docx copies from the .md
│   ├── session-start-check.sh    # SessionStart hook wrapper (wired from ../source-vision/.claude/settings.json)
│   ├── sources.sha256            # fingerprint baseline
│   └── tools/                    # md2html.py, fix-docx-tables.py
└── skills/                       # ALL skills
    ├── source-vision-design/
    └── source-vision-functionality/
```

## Working notes

- Commands (`documents/check-sources.sh`, `documents/build-docs.sh`) are meant to be run from this repo's root.
- The code repo's session-start hook points here at `../source-vision-documentation/documents/session-start-check.sh`; the script `cd`s into its own directory, so it always operates on this repo.
- The `.md` files are the source of truth. Never hand-edit a `.docx` — `documents/build-docs.sh` overwrites it.
- Keeping docs and skills in sync with the client's files: see `documents/04-Skill-Update-Rules.md`.
- These skills are **not** auto-loaded by Claude Code from here (they no longer sit in `../source-vision/.claude/skills/`). Load them explicitly, or wire them up, when working in the code repo.
