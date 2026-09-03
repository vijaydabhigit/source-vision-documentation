# Skill Update Rules

**Purpose:** keep the two Source Vision skills and this documentation always matching the client's latest files.
**Problem this solves:** the client says clearly that features, workflows, labels, pricing and content **may change** during the project `[DH §6]`. If our skills keep old rules, we build the wrong thing.

---

## The rule in one line

> **No Source Vision work starts before `check-sources.sh` says OK. If it reports drift, the documentation and skills are updated first — before any code.**

---

## What is tracked

| Item | Path |
|---|---|
| Client source folder (watched) | `/var/www/html/source-vision-test/Documentation` (all files, all sub-folders) |
| Fingerprint baseline | `sources.sha256` |
| Checker script | `check-sources.sh` |
| Automatic session hook | `session-start-check.sh`, wired in `../../source-vision/.claude/settings.json` |
| Main understanding document | `01-Requirement-Understanding.md` (+ generated `.docx`) |
| Open questions | `02-Open-Questions.md` (+ generated `.docx`) |
| **Scope-review decision record** | `07-Scope-Review-and-Decisions-Sep-2026.md` — locked (L1–L25) + open (O1–O16) decisions |
| Client-facing source docs | `sources/` — MVP/Overview v1 & v2 PDFs, Blue Virtue Scope Review 31 Aug |
| Internal PM pack | `pm-pack/` — Decision Log v1 (`.xlsx`), Project Bible v1 (`.docx`) |
| Word build script | `build-docs.sh` (+ `tools/md2html.py`) |
| Change log | `03-Change-Log.md` |
| Design skill | `../skills/source-vision-design/SKILL.md` |
| Functionality skill | `../skills/source-vision-functionality/SKILL.md` |

The client-file baseline currently covers **105 files**. Change the watched folder with `SV_DOC_ROOT=/other/path`.

> **Standing rule since 31 Aug 2026 (L25):** maintain the **Development & IP Register** (the `pm-pack` Decision Log's "IP Register" sheet) from day 1 — log every new Source Vision component (component · origin · developer · source/dependency · repo/location · status). Entries imply **no** ownership or revenue position. No GRS lists, templates, customer/consumer data, source code or IP may be reused unless confirmed **in writing**.

---

## RULE 1 — Check before you work (every time)

At the start of any Source Vision task — design, functionality, or documentation:

```bash
bash check-sources.sh
```

| Result | Exit code | What to do |
|---|---|---|
| `OK` | 0 | Continue working |
| `DRIFT DETECTED` | 1 | **Stop.** Go to Rule 2 |
| `NO BASELINE` | 2 | Run `--update` once, then continue |
| `MISSING SOURCE FOLDER` | 3 | Ask where the client documents are. Do not guess |

Both skills repeat this as their **Step 0**, so it is enforced no matter which skill is loaded.

### It also runs automatically

A `SessionStart` hook in `../../source-vision/.claude/settings.json` runs `session-start-check.sh` at the beginning of every Claude Code session, so the check happens even if a person forgets.

| Situation | Behaviour |
|---|---|
| Sources in sync | Silent. No noise at session start |
| Sources changed | Prints a warning to the user **and** injects the required update steps into Claude's context |
| Client folder not reachable | Silent (exit code 3). Not a requirement change, so it does not nag |

The hook always exits 0 — it reports, it never blocks a session.

> The hook was added after this session started. Claude Code only watches settings files that existed when the session began, so it may not fire until you open `/hooks` once or restart Claude Code. After that it runs every session automatically.

---

## RULE 2 — When drift is found, update in this exact order

Never reverse this order. The document is the single source of truth that the skills are written from.

```
1. READ      the changed / new client file
2. UPDATE    01-Requirement-Understanding.md   ← facts + source marks
3. UPDATE    02-Open-Questions.md              ← new conflicts or answered questions
4. UPDATE    ../skills/source-vision-design/SKILL.md    ← only if design/visual rules changed
5. UPDATE    ../skills/source-vision-functionality/SKILL.md ← only if behaviour/scope changed
6. LOG       03-Change-Log.md                  ← one row, what and why
7. REBUILD   bash build-docs.sh                ← regenerate the .docx for the client
8. ACCEPT    bash check-sources.sh --update
9. THEN      write code
```

### About the .docx files

`01-Requirement-Understanding.docx` and `02-Open-Questions.docx` are **generated copies** for sharing with the client. The `.md` files are the source of truth.

- **Never edit a `.docx` by hand** — the next build overwrites it.
- After changing either `.md`, run `bash build-docs.sh`.
- `bash build-docs.sh --check` reports (and exits 1) if a `.docx` is older than its `.md`. The session-start hook runs this check too.

### Which skill do I update?

| The change is about... | Update this skill |
|---|---|
| Colour, font, size, spacing, button, logo, layout, component look | `source-vision-design` |
| Screen list, scope, price, status, role, workflow, module, data, integration | `source-vision-functionality` |
| Both (e.g. a new screen with new visual rules) | Both |
| Only who does what, dates, deliverables | Neither — document only |

---

## RULE 3 — Every fact needs a source mark

Any new line added to the document or a skill must carry a source mark: `[PB §n]`, `[DH §n]`, `[QP-n]`, `[IMG:file]`, `[GRS §n]`, or `[TEAM]`.

- Use `[TEAM]` when it is **our** decision or assumption, not the client's word. Never present a `[TEAM]` assumption as a client requirement.
- Anything from `[GRS]` must additionally be marked as coming from the **other project** and must not be treated as a confirmed Source Vision requirement.

A line with no source mark must be deleted or given one.

---

## RULE 4 — When a client answer arrives

Answers to the open questions are requirement changes too.

1. Write the answer in the tracking table in `02-Open-Questions.md` and set Status to `Answered`.
2. Find every place the old assumption was used. Search for the question id:
   ```bash
   grep -rn "Q5"  skills/
   ```
3. Replace the `[TEAM]` assumption with the confirmed fact, and change the mark to the real source.
4. Remove the matching row from the "Known conflicts" table in the design skill, or the "never guess" table in the functionality skill.
5. Search the codebase for TODO markers left for that question and fix them:
   ```bash
   grep -rn "TODO Q" app/ resources/ database/ routes/
   ```
6. Log it in `03-Change-Log.md`.

---

## RULE 5 — Conflict priority

First decide **what kind of question it is**, because design and scope have different owners `[PB §2]`:

| Question is about... | Owner | Highest authority |
|---|---|---|
| Colour, type, spacing, layout, component look, UX structure, branding | **Blue Virtue** | Blue Virtue's latest written instruction / guide |
| Scope, priority, screens, pricing, features, dates, commercial logic | **Client (Sonny / project owner)** | Their latest written answer |
| Technical structure, backend logic, roles, implementation | **Us (Nexuslink)** | Our decision, recorded as `[TEAM]` |

Then, within that, follow this order (highest wins):

```
1. Latest written instruction from the owner of that question
     - design  -> Blue Virtue        [PB §2 assigns design direction to them]
     - scope   -> the client
2. Quick Feedback Pitch feedback slide   [QP-7]      ← the client correcting the mockups
3. Project Brief  [PB]  /  Development Handover  [DH] ← written specifications
4. Design mockups [IMG]                              ← "references, not specifications" [DH §6]
5. GRS Online project  [GRS]                          ← other project, reference only
6. Our own assumption [TEAM]                          ← lowest
```

> **Never invent design.** If Blue Virtue has not specified something visual, do not decide it quietly. Use the nearest documented rule, mark it `[TEAM]`, and add a question. This is Rule A in the design skill.

Record every conflict you find in `02-Open-Questions.md` instead of silently choosing one side.

**Worked example:** the mockups show ON/OFF toggles on plan cards `[IMG:Marketing_Plans]`, but the pitch feedback says *"Replace simple switches with request/status logic"* `[QP-7]`. Level 2 beats level 4, so we build request/status — and we still record it as Q3 for confirmation.

---

## RULE 6 — Never delete history

Do not overwrite an old requirement silently. In `03-Change-Log.md`, always record what the rule was **before** and what it is **now**. If the client reverses a decision later, we need to know what changed and when.

---

## RULE 7 — New file types

If a new client file cannot be read with the tools on this machine, do not guess its content. Add it to the "Not yet reviewed" table in `01-Requirement-Understanding.md` and raise a question.

Currently available on this machine: `python3`, `unzip`, `libreoffice`, PHP with GD.
**Not** available: `pandoc`, `python-docx`, `python-pptx`, ImageMagick, `ffmpeg`.

Helpers already written for this project (in the session scratchpad, re-create if needed):
- `.docx` / `.pptx` → text: a Python OOXML extractor (zip + XML, no dependencies)
- Large image → viewable size: a PHP GD downscaler

Video files (`.mov`) cannot be read at all right now — this is why the dashboard screen recording is still unreviewed (Q7).

---

## Quick command reference

```bash
bash check-sources.sh            # check for drift        (run this first, always)
bash check-sources.sh --update    # accept current state as baseline
bash check-sources.sh --list      # show all tracked files + hashes

grep -rn "\[TEAM\]"  skills/   # every unconfirmed assumption
grep -rn "TODO Q" app/ resources/ database/ routes/  # code waiting on a client answer
```
