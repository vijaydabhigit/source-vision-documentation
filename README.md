# Source Vision — Documentation

This folder holds our understanding of the Source Vision project, written from the client's own files.

**Read in this order:**

| # | File | What it is | Word copy |
|---|---|---|---|
| **0** | [00-MVP-and-Full-System-Scope.md](documents/00-MVP-and-Full-System-Scope.md) | **THE MAIN DOCUMENT — plan from this one.** Three sections: what the MVP covers, the scope of the full system, and the questions. Written in plain language with no source references. `(From GRS)` marks anything reused from the old GRS system | [.docx](documents/00-MVP-and-Full-System-Scope.docx) |
| 1 | [01-Requirement-Understanding.md](documents/01-Requirement-Understanding.md) | **Start here.** The full requirement in simple English. Every fact has a source mark showing which client file it came from | [.docx](documents/01-Requirement-Understanding.docx) |
| 2 | [02-Open-Questions.md](documents/02-Open-Questions.md) | 13 questions for the client. **Q1–Q6 are blocking** | [.docx](documents/02-Open-Questions.docx) |
| 3 | [03-Change-Log.md](documents/03-Change-Log.md) | History of every change to these documents and to the skills | — |
| 4 | [04-Skill-Update-Rules.md](documents/04-Skill-Update-Rules.md) | The 7 rules that keep the skills up to date | — |
| 5 | [05-Client-Discussion-Module-Functionality.md](documents/05-Client-Discussion-Module-Functionality.md) | **Meeting document (v2.0).** Companion to the Execution Plan and decisions register: modules and submodules by wave with detailed functionality, all 13 GRS modules mapped, content for the team's 2 questions, and the 4 genuinely new items | [.docx](documents/05-Client-Discussion-Module-Functionality.docx) |
| 6 | [06-MVP-Build-Approach.md](documents/06-MVP-Build-Approach.md) | **Technical decision record.** Why the MVP is built on the latest stack in "demo mode" — no database, no auth, one demo-data file — and what that supersedes in Execution Plan v1.0 | — |

### Word (.docx) versions — for sending to the client

Documents 00, 01, 02 and 05 also exist as `.docx` files with real Word headings and tables, so they can be shared, printed or commented on.

```bash
bash documents/build-docs.sh          # regenerate the .docx files from the .md
bash documents/build-docs.sh --check  # warn if a .docx is older than its .md
```

The build also fixes what LibreOffice gets wrong on its own: every table is set to **full page width** with proportional columns, real cell padding, a navy header band that runs edge to edge, light row separators, and a header row that **repeats when a long table breaks across pages**. Page margins are squared to 2 cm all round.

> The `.md` files are the **source of truth**. Never edit a `.docx` by hand — the next build overwrites it. Run `documents/build-docs.sh` after changing either markdown file. The session-start hook also warns when a `.docx` has gone stale.

---

## Before you write any code

```bash
bash documents/check-sources.sh
```

This compares the client's document folder against a saved fingerprint of 105 files.

- `OK` → documentation and skills match the client's files. Continue.
- `DRIFT DETECTED` → **stop.** A client file changed. Update the documents and skills first — see [04-Skill-Update-Rules.md](documents/04-Skill-Update-Rules.md).

This also runs **automatically** at the start of every Claude Code session, via a `SessionStart` hook in `../source-vision/.claude/settings.json`. It stays silent when everything is in sync and warns only when a client file has changed.

---

## The two skills

Coding rules live in skills so they load automatically when relevant:

| Skill | Covers |
|---|---|
| [source-vision-design](skills/source-vision-design/SKILL.md) | Colours, Space Grotesk typography and type scale, buttons and states, logo rules, layout and component patterns, chart/status colours |
| [source-vision-functionality](skills/source-vision-functionality/SKILL.md) | Three portals, Services vs Packages vs Plans, the 6 campaign statuses, screen requirements, roles, dummy-data rules, the embedded reporting iframe, GRS-derived logic |

Both skills begin with the same **Step 0**: run `documents/check-sources.sh` and stop if it reports drift.

---

## Source marks used in every document

| Mark | Meaning |
|---|---|
| `[PB §n]` | Project Brief – Source Vision MVP - 140726.docx, section n |
| `[DH §n]` | Source Vision – Development Handover.docx, section n |
| `[QP-n]` | Source_Vision_Quick_Feedback_Pitch.pptx, slide n |
| `[IMG:name]` | A design mockup image |
| `[GRS §n]` | **OTHER PROJECT** — GRS-Online-Module-Overview.docx, module n. Reference only, not a confirmed requirement |
| `[TEAM]` | Our own decision or assumption. **Not** from the client. Needs approval |

**Rule:** a statement with no source mark is not trusted. See Rule 3 in [04-Skill-Update-Rules.md](documents/04-Skill-Update-Rules.md).

---

## The two things to remember about this project

1. **"Demo first. Product later."** `[PB §2]` — this is a sales demo built to raise the resale value of a business asset `[PB §1]`, not a finished SaaS product. Test every task with: *does this help a buyer understand the value faster?* `[PB §2]`
2. **Dummy data only.** `[PB Rule 4]` — no real customer, consumer, financial, email or login data, and no real third-party brand names.

---

## Client source files

Location: `/var/www/html/source-vision-test/Documentation/`

```
Documentation/
├── GRS-Online-Module-Overview.docx          ← other project, reference only
├── 7-Aug/drive-download-.../                ← earlier snapshot (same content as 11-Aug)
└── 11-Aug/drive-download-.../               ← current
    ├── 01_Administration/                   (empty)
    ├── 02_Project briefings & understanding/
    │   ├── Project Brief – Source Vision MVP - 140726.docx
    │   ├── Source Vision – Development Handover.docx
    │   └── Source_Vision_Quick_Feedback_Pitch.pptx
    ├── 03_Design & Templates/
    │   ├── Part_2/                          (7 newer screens)
    │   ├── Source_Vision_Images/            (6 screens + 8 package artboards)
    │   ├── Visual Identity/                 (palette, logo, Space Grotesk font)
    │   └── Dashboard_Screenrecording/       (29 MB .mov — not reviewed yet, Q7)
    ├── 04_Web & Technology/                 (empty)
    ├── 05_Reports/                          (empty)
    └── 99_Archive/                          (empty)
```

Override the watched folder with `SV_DOC_ROOT=/other/path bash documents/check-sources.sh`.
