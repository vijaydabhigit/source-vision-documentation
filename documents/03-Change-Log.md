# Documentation & Skill Change Log

Every change to the understanding document or to the two skills is recorded here.
Rule: never delete an old requirement silently — always record what it was **before** and what it is **now** (see [04-Skill-Update-Rules.md](04-Skill-Update-Rules.md), Rule 6).

---

## 2026-08-12 — Version 1.0 — First version

**Trigger:** Client provided the 11-Aug ZIP folder and the GRS Online module overview.

**Source files read:**

| File | Result |
|---|---|
| `11-Aug/.../Project Brief – Source Vision MVP - 140726.docx` | Read fully (18 sections) |
| `11-Aug/.../Source Vision – Development Handover.docx` | Read fully (6 sections) |
| `11-Aug/.../Source_Vision_Quick_Feedback_Pitch.pptx` | Read fully (10 slides + speaker notes) |
| `GRS-Online-Module-Overview.docx` | Read fully (13 modules) — **other project** |
| 14 design screens + 3 of 8 package artboards | Viewed |
| `logoSource VIsion Report.txt`, Space Grotesk font folder | Read |

**Created:**
- `01-Requirement-Understanding.md` — main understanding document, simple English, every fact source-marked
- `02-Open-Questions.md` — 13 questions (Q1–Q6 blocking)
- `03-Change-Log.md` — this file
- `04-Skill-Update-Rules.md` — 7 rules for keeping skills current
- `check-sources.sh` — drift detector (tested: change / add / delete all detected)
- `sources.sha256` — baseline of 105 client files
- `session-start-check.sh` + `.claude/settings.json` `SessionStart` hook — runs the drift check automatically at the start of every session (tested: silent when in sync, warns on drift, silent when folder unreachable)
- `CLAUDE.md` — project rules, always in context
- `01-Requirement-Understanding.docx` + `02-Open-Questions.docx` — Word versions for the client (real Word headings and tables: 16 and 2 tables respectively)
- `build-docs.sh` + `tools/md2html.py` — regenerates the `.docx` from the `.md` (tested: full rebuild, and `--check` correctly flags a stale `.docx`)
- `skills/source-vision-design/SKILL.md` — v1.0
- `skills/source-vision-functionality/SKILL.md` — v1.0

**Findings recorded (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | 7-Aug vs 11-Aug ZIP | Assumed 11-Aug had new content | Verified byte-by-byte: same 50 files. Only the 2 `.docx` differ, and their **text is identical** (save metadata only). Nothing new was added between 7 and 11 August |
| 2 | Franchise Plan price | — | Conflict found: €999 `[IMG:Marketing_Plans]` vs €1,049 `[IMG:Upgrade ur plan]`. Not resolved → Q5 |
| 3 | Add-on vs standalone pricing | — | Google Advertising €549 standalone vs €79 add-on; Custom Campaign Support €299 vs €99. Not resolved → Q5 |
| 4 | Font for buttons | — | Conflict found: `[DH §2]` says Space Grotesk but its button line says "Inter"; white-label mockup also shows Inter. Assumption `[TEAM]`: Space Grotesk → Q6 |
| 5 | Admin sidebar | — | Two different versions exist. Assumption `[TEAM]`: newer `Part_2` version wins, because it contains Content Library as requested in `[QP-7]` → Q1 |
| 6 | Toggle vs request/status | Mockups show ON/OFF toggles | Pitch feedback `[QP-7]` overrides mockups → build request/status with the 6 statuses from `[PB §7.5]` → Q3 |
| 7 | Service count | Brief lists 10 services incl. eMagazine + Print portal `[PB §7.3]` | Design menu shows only 8 `[IMG:MENU_...]`. eMagazine and Print portal missing → Q4 |
| 8 | Screen numbering | — | Brief has no screen number 9; list jumps 8 → 10 `[PB §7]` → Q4 |
| 9 | Reporting dashboard | Assumed we build it | We do **not** build it. External partner Meneer Online hosts it; we embed an iframe, no backend/database needed `[PB §10]` |
| 10 | Homepage trust logos | — | Mockup uses real companies (Cisco, Morgan Stanley, BNY, Moderna, Uber) as "Trusted by leading companies" `[IMG:Homepage_Soruce_Vision]`. Breaks Rule 4 dummy-data-only `[PB Rule 4]` and implies false endorsement. Marked **do not build** → Q11 |
| 11 | White-label mockup colours | — | `#2563EB` / `#0F172A` / `#10B981` shown there are **sample form values**, not the brand palette. Brand palette stays `#192A4B` / `#001FFA` / `#FD5104` `[DH §1]` |
| 12 | Timeline | Brief assumed ~200 hours over 1.5 months `[PB §3]` | Today is 12 Aug 2026, target is beginning of September ≈ 3 weeks ≈ 90 hours. Raised as a risk → Q10 |
| 13 | Empty ZIP folders | — | `01_Administration`, `04_Web & Technology`, `05_Reports`, `99_Archive` contain no files |
| 14 | GRS relationship | Unclear how GRS relates | GRS is a **separate older project**. Source Vision is built "from the existing value of the GRS Mailsystem and the GRS Marketing System" `[PB §Main Objective]`. All 13 GRS modules mapped to Source Vision screens in section 13 of the understanding document, each marked `[GRS]` |
| 15 | GRS known weakness | — | GRS Marketingmiddelen has a data-loss-on-save problem `[GRS §6]`. Recorded as "do not copy this" |

**Still open:** 13 questions in [02-Open-Questions.md](02-Open-Questions.md). Q1–Q6 block completion of the package, plan and admin screens.

**Not reviewed yet:** `Customer_Dashboard.mov` (29 MB, no video tool on this machine), 5 of 8 package artboards, `Gradient_Image.jpg`, `logoSource VIsion.ai`, and `Source_Vision_Understanding_and_Technology_Brief.docx` (not in the given scope → Q9).

---

## 2026-08-12 — Version 1.1 — Three standing design rules added

**Trigger:** Client instruction — "All design must be responsive and modern and must follow the Blue Virtue instruction/guide."

**Changes (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | Design authority | `[PB §2]` recorded that Blue Virtue owns design, but it was not stated as a working rule | **Rule A**: Blue Virtue's instruction/guide is the highest authority on any visual or UX question — above the mockups and above our own preference. We must **never invent design**; an unspecified visual detail is marked `[TEAM]` and raised as a question, not decided quietly |
| 2 | Responsive | Design skill §7 only noted that `[DH §2]` names three type tiers | **Rule B**: responsive is mandatory on every screen. §7 rewritten with breakpoints, a per-component reflow table (9 patterns), and 7 hard rules (no sideways page scroll, ≥ 44 px touch targets, no fixed widths, nothing important hidden on mobile, etc.) |
| 3 | Modern | `[DH §5]` gave a prose direction only | **Rule C**: modern is now checkable — a do/not-this table in §5 (surfaces, padding, radii, shadows, icons, transitions, chips, loading) plus required hover / focus / pressed / empty / loading / error states |
| 4 | Conflict priority (Rule 5 in the update rules) | One flat list, highest = latest client answer | Split by question type first: **design → Blue Virtue**, **scope → client**, **technical → us** `[PB §2]`. Then the existing order applies within that |
| 5 | Responsive design gap | Not previously noticed | **All 17 supplied mockups are desktop only** (measured: 1671×941 to 5792×4344 px). `[DH §2]` gives tablet/mobile font sizes but no layouts. Since we must not invent design, this needs Blue Virtue input → new **Q14**, marked blocking |
| 6 | Breakpoint values | Not defined anywhere | Proposed `[TEAM]`: mobile < 768 px, tablet 768–1023 px, desktop ≥ 1024 px. Needs Blue Virtue confirmation → Q14 |

**Files updated:** `01-Requirement-Understanding.md` (new section 8.0 + section 3 role note), `02-Open-Questions.md` (Q14 added, blocking list now Q1–Q6 + Q14), `04-Skill-Update-Rules.md` (Rule 5 rewritten), `CLAUDE.md` (rules renumbered, 3 new rules at the top), `skills/source-vision-design/SKILL.md` (v1.0 → v1.1).

**Skills updated:** design (functionality skill unchanged — these are visual rules)
**Questions closed:** none
**New questions:** Q14 (blocking)

---

## 2026-08-12 — Version 1.2 — Client discussion document created

**Trigger:** Client-side request — prepare one document for today's meeting covering module/submodule functionality, checked against the GRS documents, with content for the team's 2 questions plus our own doubts.

**Created:** `05-Client-Discussion-Module-Functionality.md` (+ `.docx`, 35 tables). Added to `build-docs.sh`.

**Contents:**

| Part | What it covers |
|---|---|
| A | The 2 questions from `Documentation/document`, with prepared content |
| B | 21 module groups + 10 legacy modules, 113 submodule rows, each with detailed functionality, source mark, GRS reference and a status mark |
| C | All 13 GRS modules mapped to Source Vision, with a reuse tick-box each, plus the 5 patterns we most want to reuse |
| D | 7 blocking questions + 15 new doubts + 5 recommendations |
| E | Decision sheet: 7 blocking decisions, 5 items for Blue Virtue, 7 items from others |

**New findings recorded (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | Design coverage | Not measured | **Only ~6 of 15 brief screens have a design.** Missing: Login (mandatory), Service Selection (mandatory), Campaign Request, Newsletter, Scratch Game, Landing Page, Account Management, Service/Package Management → item BV-4 |
| 2 | Design source file | Not asked | We have a Word document + flat images, **no Figma/Sketch/XD**. Exact spacing and state colours have to be measured from screenshots → item BV-2 |
| 3 | Design freeze | Not asked | `[DH §6]` says design may still change; with ~3 weeks left this is the biggest risk to the date → item BV-3 |
| 4 | Team's question 2 | Unread | Found in `Documentation/document`: *"For front website, we have to think for"* — the sentence is **incomplete**. Prepared content for the likely intent (8 considerations) and asked for the rest → item X-7 |
| 5 | Team's question 1 | Unread | *"Will the design be provided by Blue Virtue?"* — answered from `[PB §2]`, plus the 4 gaps that make a plain "yes" insufficient |
| 6 | Scale of undecided work | Unknown | **39 of 113 submodule rows need a client decision**; 21 depend on confirming GRS reuse; 10 legacy admin modules hinge on Q1 alone |
| 7 | 15 new doubts | — | Recorded as D-01 to D-15, including: is the Scratch Game playable, are landing pages real, does white-label actually re-theme the platform, what is in the Content Library, what are all 16 modules, monthly or yearly billing |

**Skills updated:** none — this is a client-facing discussion document, not a build rule. Any decision taken in the meeting must then flow through Rule 2 of `04-Skill-Update-Rules.md`.
**Questions closed:** none
**New questions:** D-01 to D-15 (recorded in document 05, to be promoted into `02-Open-Questions.md` as they are answered or escalated)

---

## 2026-08-12 — Version 1.3 — Four NexusLink documents found; stack decided; document 05 reconciled

**Trigger:** `check-sources.sh` reported drift. The client folder had **moved** to `~/Documents/Projects/Source Vision` and contained a new `12-Aug/` folder with four NexusLink documents dated 12 Aug 2026.

**Folder move:** all 105 previously-baselined files verified present and unchanged by hash. Nothing lost. `check-sources.sh` default path updated.

**New sources read:** `Source_Vision_MVP_Execution_Plan.pdf` (24 pp, v1.0) · `Source_Vision_Open_Decisions_and_Blockers.pdf` (9 pp, 26 items) · `Source_Vision_MVP_Roadmap_OnePager.pdf` (2 pp). **Not read:** `Source_Vision_MVP_Summary.pdf` (4 pp) — appears to condense the Execution Plan.

These are authored by **NexusLink (Vijay Dabhi)** and were already issued to Blue Virtue, answers due **Fri 14 Aug 2026**.

**Changes (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | **Build model** | Laravel 13 + Inertia 3 + Vue 3.5 installed with no stated model | **Decided by the user:** keep the latest stack and build in **"demo mode"** — no database, no migrations, no models, no auth; one `config/demo.php` drives every figure. **Supersedes Execution Plan §3.1** (static HTML Phase 1) and **§3.2/§13** (Laravel 11 / PHP 8.2 Phase 2). Recorded in new document `06-MVP-Build-Approach.md` |
| 2 | **Campaign Reporting** | Functionality skill said "embedded, do NOT build" per `[PB §10]` | **Conflict recorded, build neither.** `[EP §11.2]` + item **S6** recommend a native English build with the Meneer Online iframe as a roadmap item. Pending client answer |
| 3 | **Toggles vs request/status** | Skill said replace all toggles per `[QP-7]` | **Too absolute.** Item **D5**: toggles stay on the commercial cards ("what I have"); request/status chips on the dashboard services grid ("what I asked for") |
| 4 | **Screen scope** | 15 brief screens, priority unknown, my Q4 open | **Wave 1 = nine protected screens**, Wave 2 = seven, Wave 3 = eleven `[EP §6]`. Anything else is a roadmap entry in the Development Portal |
| 5 | **eMagazine** | My Q4 asked whether to include it | **Withdrawn** — item **C4**. Roadmap service only |
| 6 | **Admin menu (my Q1)** | Assumption: the newer `Part_2` sidebar | **Confirmed** by item **S5** — Campaign Planning Tool, Email Marketing and CMS Management are dropped from the interface and become roadmap modules |
| 7 | **Font (my Q6)** | Assumption: Space Grotesk | **Confirmed** by item **D1** — Inter is a leftover |
| 8 | **Franchise price (my Q5)** | Conflict, unresolved | **C1** — adopt €999 and correct the Upgrade screen. **C2** — the €299 package vs €99 add-on gap is intentional bundled pricing |
| 9 | **Public website (my Q2)** | Scope unknown | **In scope:** Public Homepage is Wave 1 screen 2; Service Landing Page template ×8 is Wave 2 |
| 10 | **Homepage logos and stats (my Q11)** | Our recommendation | **Matched** by **C5** (neutral placeholders in Stage 5) and **C6** (illustrative, not audited) |
| 11 | **Taxonomy** | Our reading of Services/Packages/Plans | **Confirmed** by **C3** — and the admin dummy data must be rewritten to the five customer-facing plan names |
| 12 | **Packages price range** | Only €299 and €549 measured from artboards | Actual range is **€129–€849 across 8 cards** `[EP §6.1]`. We have measured only 3 of 8 → new item **NEW-1** |
| 13 | **GRS system access** | Not known | ⚠ **X4** — the GRS Mailsystem at `grsonline.nl` is outdated but **still live and still collecting real email addresses**. Strictly read-only; screenshots only after real recipient data is removed |
| 14 | **Timeline** | Our risk note about ~3 weeks | Quantified by `[EP §4.2]`: Wave 1 needs **124–170 h** against **66–78 h** available with one developer. Capacity item **S2** unchanged by the stack decision |
| 15 | **Document 05** | Standalone meeting document with its own Q1–Q14 | **Rewritten as a companion (v2.0):** restructured around Wave 1/2/3, uses the existing register IDs, and reduced to **four genuinely new items** (NEW-1 to NEW-4). Its own question set was removed to avoid putting two registers in front of one client |
| 16 | **Doubts D-01…D-15 from v1** | 15 open doubts | **11 resolved** by the new documents (scratch game = overview only, landing pages = overview only, white-label re-theming = enhancement S4, monthly billing, static suggestion content, no analytics accounts needed, no password reset, segment naming via C3, in-app notifications only, English only, custom reports painted). **4 remain** as NEW-1 to NEW-4 |

**Files created:** `06-MVP-Build-Approach.md`
**Files rewritten:** `05-Client-Discussion-Module-Functionality.md` (v1 → v2.0)
**Files updated:** `check-sources.sh` (new root path), `CLAUDE.md`, `skills/source-vision-functionality/SKILL.md`, `03-Change-Log.md`

**Skills updated:** functionality (build model, wave structure, reporting conflict, D5 nuance, X4 warning). Design skill unchanged — no design rule changed.

**Still open:** the 26 register items (due Fri 14 Aug) plus NEW-1 to NEW-4. **Action required outside this repository:** Execution Plan v1.0 §3.1, §3.2 and §13 are now out of date on technology and should be reissued before the client relies on them.

---

## 2026-08-13 — Version 1.3 — Front website MVP: Stage 1 foundation + the public homepage

**Trigger:** Instruction to start the MVP for the front website. `check-sources.sh` reported **OK** (109 files match) before any work began.

**Source files read:** `Homepage_Soruce_Vision.png`, `Menu_Source Vision_Frontend.jpg`, `Visual Identity/Gradient_Image.jpg`, `Logo_Source Vision/*`, `Space_Grotesk_Font/*`

**What was built.** Stage 1 of the build approach (tokens, font, component library, demo data) plus Stage 2's public shell and the Wave 1 Public Homepage.

| # | Item | Before | Now |
|---|---|---|---|
| 1 | **Typeface** | Laravel skeleton's Instrument Sans, loaded from Bunny CDN | **Space Grotesk self-hosted** from the client's own font files; the Bunny plugin is removed from `vite.config.js` `[DH §2]` |
| 2 | **Design tokens** | None | Full brand token sheet in the Tailwind 4 `@theme` block — navy, blue, orange, neutrals, status families, radii, soft shadows. **This is the sheet Blue Virtue approves at Gate M1** |
| 3 | **Demo data** | None | `config/demo.php` — brand, 8 services, 5 plans, the 6 canonical statuses, and every homepage label and figure. No component holds a figure `[DH §6]` |
| 4 | **Route names → URLs** | n/a | `App\Support\DemoContent` resolves route names stored in config into hrefs, so components never hardcode a path and an unbuilt route degrades to `#` instead of throwing |
| 5 | **Components** | None | `SvButton` (5 variants incl. commercial orange and a non-orange destructive), `SvCard`, `SvIcon`, `SvLogo`, `SectionEyebrow`, `FeatureCard`, `TextLink`, `PublicHeader` (both mega-menus + mobile drawer), `PublicFooter`, `PublicLayout` |
| 6 | **Public homepage** | Laravel welcome page | All five mockup sections built, mobile-first, verified at 390 / 820 / 1440 px |
| 7 | **Route shell** | One route (`/`) | 13 public routes, every one answering with a real page or an **on-brand stub** — Gate M2's no-dead-ends rule |
| 8 | **Real company logos** | Cisco, Morgan Stanley, BNY, Moderna, Uber in the mockup | Replaced with the invented companies used in the dashboards, per **C5**. A test now fails if any of the five reappears `[PB Rule 4]` |
| 9 | **Homepage statistics** | Read as real claims | Kept as **C6** allows, with a visible demo notice beside them and in the footer |
| 10 | **Logo assets** | ~24% empty canvas, rendering the logo far too small in a 72 px header | Web copies use a trimmed `viewBox` keeping ~10% of glyph height as clear space. **No path changed** — not distorted, not recoloured `[DH §4]` → Q15 |
| 11 | **Tests** | One skeleton test | `FrontWebsiteTest` — homepage content, every nav link resolves, all 8 service pages, unknown service 404s, no real brand appears, and figures provably come from config. **8 tests pass** |

**Decisions taken under Rule A** (nearest documented rule, marked `[TEAM]`, question raised — never quietly decided):

| Gap | Decision | Question |
|---|---|---|
| No footer design supplied | Built from navy + white logo `[DH §4]` and the admin footer line | Q15 |
| No hero or insights photography supplied | Used the **approved navy-gradient panel** `[DH §4]`, reproduced in CSS rather than shipping the 30,184 px source JPEG | Q15 |
| Logo canvas padding | Trimmed `viewBox` only | Q15 |
| Google / TikTok brand marks as service icons | Neutral outline icons in the same line style | Q16 |
| Uppercase eyebrows vs `[DH §2]` sentence case | Followed the mockup; copy stored in sentence case so it flips in one line | Q17 |
| Nav label "Marketing" vs "Marketing Services" | Used "Marketing Services" — the written menu file wins over the mockup | existing conflict, design skill §8 |

**Skills updated:** none — no design or functional **rule** changed, only rules applied.
**Questions closed:** Q2 (public website is in scope), Q11 (applied C5 and C6 on the built page).
**New questions:** Q15, Q16, Q17.
**Still open and now urgent for this layer:** **Q14** — Blue Virtue has supplied no tablet or mobile layouts. The homepage reflow follows our documented reflow table and needs their approval.

---

## 2026-08-13 — Version 1.4 — Wave 1 complete: all nine protected screens

**Trigger:** Instruction to complete the rest of the MVP. `check-sources.sh` reported **OK** (109 files) before work began.

**Source files read this round:** `Part_2/Marketing_Plans.png`, `Part_2/Admin_Dshboard.png`, `Part_2/White_Label_Portal.png`, `Part_2/Customer_Dasboard.png`, `Part_2/Customer Dashboard.png`, `Source_Vision_Images/Packages/Artboard 2–9.jpg`

### The nine Wave 1 screens are now built

| # | Screen | Built as | Source |
|---|---|---|---|
| 1 | Login + demo role switcher | `Auth/Login` | `[PB §7.1]` — **no mockup exists**, see Q20 |
| 2 | Public Homepage | `Public/Home` | `[IMG:Homepage_Soruce_Vision]` |
| 3 | Customer Dashboard | `Customer/Dashboard` — all seven numbered blocks | `[PB §7.2]` `[IMG:Customer_Dasboard]` |
| 4 | Marketing Services catalogue | `Customer/Services` | `[PB §7.3]` — **no mockup exists**, see Q20 |
| 5 | Marketing Packages | `Customer/Packages` — 8 cards, €129–€849 | `[IMG:Packages/Artboard 2–9]` |
| 6 | Marketing Plans | `Customer/Plans` — 5 tiers, 3 + 2 layout | `[IMG:Marketing_Plans]` |
| 7 | Admin Dashboard | `Admin/Dashboard` | `[PB §7.11]` `[IMG:Part_2/Admin_Dshboard]` |
| 8 | Development / Settings Portal | `Dev/Overview` | `[PB §7.15]` `[IMG:Part_2/White_Label_Portal]` |
| 9 | White-Label configuration | `Dev/WhiteLabel` | `[PB §7.14]` `[IMG:Part_2/White_Label_Portal]` |

**Changes (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | **Package prices** | Only 3 of 8 measured — open item **NEW-1** | All 8 artboards measured: €129 · €179 · €249 · €299 · €334 · €549 · €549 · €849. Range matches `[EP §6.1]` exactly. **NEW-1 is closed** |
| 2 | **Admin dummy data** | Mockup used Enterprise / Professional / Basic plan names | Rewritten to the five confirmed plan names, as register item **C3** requires. A test now fails if any other name appears |
| 3 | **Franchise price** | Conflict €999 vs €1,049 | **€999**, per item **C1**. Asserted in a test |
| 4 | **Campaign statuses** | Mockups print "Active", not one of the six | Mapped to **In progress**; no seventh status invented. A test walks every campaign status and fails on an unknown one. New question **Q19** |
| 5 | **Service state chips** | Ambiguous whether these are campaign statuses | Modelled as a separate four-value vocabulary (Active / Requested / Completed / Available), per item **D5**. The six campaign statuses stay reserved |
| 6 | **Toggles** | Ambiguous after `[QP-7]` | Kept on Marketing Packages and Marketing Plans cards; request/status chips on the dashboard services grid. Item **D5** applied exactly |
| 7 | **Chart palette** | None | Five-hue categorical set validated with the `dataviz` validator — passes lightness band, chroma floor, CVD separation, normal-vision floor and contrast. Brand blue was too dark for a series slot, so chart-1 is its nearest passing step |
| 8 | **Charts** | None | `Sparkline`, `AreaChart` (crosshair + tooltip), `DonutChart` (legend always present, 2px segment gaps). No chart library added |
| 9 | **Demo role switcher** | Not built | `POST /demo/role` puts the role in the session and lands on that portal's home. No users table, no password `[PB §7.1]` |
| 10 | **Reporting dashboard** | Unbuilt | Still unbuilt **in both forms**, and now says so on screen. A test asserts no `<iframe>` renders. Item **S6** remains open |
| 11 | **Routes** | 13 | 34, every one resolving. A test walks every named GET route and fails on any non-200 |
| 12 | **Tests** | 8 | **22**, all passing |

### New evidence for the reporting conflict (item S6)

`03_Design & Templates/Part_2/Customer Dashboard.png` — the **newest** design file, dated 5 Aug — is not a Source Vision screen at all. It is the **Meneer Online analytics dashboard**: Dutch labels (`Gespendeerd budget`, `Kosten per conversie`, `Top Campagnes`), a `Dashboards` sidebar of its own, and **"Data niet beschikbaar"** in nine of its twelve widgets.

This independently confirms three of the four objections in Execution Plan §11.2: the dashboard **is** in Dutch, it **does** show "Data niet beschikbaar" without connected accounts, and it is off-brand. It also explains the brief's ambiguity — the file is literally named "Customer Dashboard", which is why the iframe instruction sits under that heading.

It does **not** settle the question, because `[PB §10]` is still a written client requirement. **S6 still needs the client's answer.**

### Decisions taken under Rule A (nearest documented rule, marked `[TEAM]`, question raised)

| Gap | Decision | Question |
|---|---|---|
| Login screen has no design | Navy-gradient panel + white logo `[DH §4]`, white form card | Q20 |
| Services catalogue has no design | Reused the homepage feature-card treatment | Q20 |
| Mockup chips say "Active" | Written brief wins → "In progress" | Q19 |
| "You're on our top plan" on the wrong plan | Copy kept verbatim, not corrected | Q18 |
| Brand blue unreadable on navy | Added one lighter step of the same hue for dark chrome only (5.9:1) | — |
| Demo customer identity | Lumina Studio, not the mockup's "Acme Co.", so the dashboard and the admin customer table cannot contradict each other | — |

**Skills updated:** none — no design or functional **rule** changed, only rules applied.
**Questions closed:** none new closed. **Register item closed:** **NEW-1** (all 8 package prices measured).
**New questions:** Q18, Q19, Q20.
**Still open and now urgent:** **Q14** (no tablet/mobile designs exist — nine screens now depend on our own reflow rules), **Q19**, **Q20**, and register item **S6**.

---

## 2026-09-02 — Version 1.5 — Blue Virtue Scope Review applied; Wave 1 re-prioritised; reporting resolved

**Trigger:** A four-step document sequence was provided: (1) v1 client docs sent 12 Aug, (2) **Blue Virtue Scope Review & Alignment Notes, 31 Aug 2026** (client feedback), (3) the internal PM pack (Decision Log v1 + Project Bible v1, 1 Sep), (4) the **v2 client docs sent today, 2 Sep**. All read in full.

**Source files added to the repo:**

| File | Location |
|---|---|
| MVP Module List v1 (12 Aug) · Module Overview v1 (12 Aug) | `documents/sources/…_v1_12Aug2026.pdf` |
| Blue Virtue Scope Review & Alignment Notes (31 Aug) | `documents/sources/…Scope_Review_Alignment_Notes_BlueVirtue_31Aug2026.docx` |
| MVP Module List v2 (2 Sep) · Module Overview v2 (2 Sep) | `documents/sources/…_v2_02Sep2026.pdf` |
| Decision Log v1 · Project Bible v1 (internal PM pack) | `documents/pm-pack/` |

**Created:** `07-Scope-Review-and-Decisions-Sep-2026.md` — the consolidated record of the sequence, the locked decisions (L1–L25), the open decisions (O1–O16) and the build-approach conflict.

**Changes (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | **Wave 1 order** | Nine screens led by Public Homepage `[EP §6]` | **Twelve-screen 10-minute buyer storyline** (L13): Login → Customer → Services/Plans → Request → Scratch/Lead Gen → Reporting → Admin → White-label + Platform Settings. Campaign Request Flow, Scratch Game and Reporting **pulled forward into Wave 1** at demo depth (L14); **Public Homepage deprioritised** within Wave 1 (L15) `[BV-SR]` `[MVP-v2]` |
| 2 | **Third portal name** | "Settings / Development Portal" (a.k.a. "Developer view") | **Platform Settings** (Platform Owner). Three portals = Customer · Admin · Platform Settings (L16). Renamed in the functionality skill, design skill and `CLAUDE.md` |
| 3 | **Campaign Reporting** | Conflict, "build neither" (item S6) | **RESOLVED (L6): build natively, on-brand, dummy data, Wave 1, demo depth.** Meneer Online iframe **rejected**. Phase 2 reporting is a "Reporting Layer" — assess Blue Virtue's dashboard tech first (O9) `[BV-SR]` `[OV-v2]` |
| 4 | **Pricing framing** | Prices treated as the model | **Example monetisation model, configurable by the platform owner** (L17). Show an "example configuration" label wherever pricing appears |
| 5 | **Phase 2 positioning** | Presented as a 24-module build | **"Proposed Full Platform / Future Product Architecture" — framework only** (L19). No effort/cost figures client-facing until signed. Multi-tenancy/white-label moved to the top (L23); Integrations split into core/optional/API (L21); AI Assistant + Print Portal → roadmap (L20); GRS Data Migration → "Generic Data Import & Migration Tools" (L18); Content Library = simple asset organisation, legacy GRS folder excluded (L22) `[OV-v2]` |
| 6 | **IP governance** | Not a standing rule | **Development & IP Register maintained from day 1** (L25); no GRS data/IP assumed unless confirmed in writing `[BV-SR]` |
| 7 | **Demo hosting (Q13)** | Open | **Answered:** Blue Virtue VPS + source-vision.com on Cloudflare — MVP infra only (L24) |
| 8 | **Admin menu (Q1)** | Assumption: newer `Part_2` menu | **Answered/confirmed** by the Wave 1 acceptance criteria in the Project Bible |
| 9 | **Franchise / Custom Support pricing** | Skill said "intentional" (C1/C2) | Re-opened per the Decision Log: **O1** (€999 vs €1,049) and **O2** (€299 vs €99) are **awaiting the client**. Default to €999 / seed Plans-page values and leave `// TODO` markers |
| 10 | ⚠ **Phase 1 build approach** | Repo built on Laravel 13 demo-mode (`06-MVP-Build-Approach.md`) | **Conflict flagged:** the Decision Log (L1) and Project Bible (§23) say Phase 1 = **static HTML, no framework**. The repo + `06-MVP-Build-Approach.md` say **Laravel 13 demo-mode**. Recommendation: keep Laravel demo-mode and correct the PM pack. **Needs Vijay's written confirmation** — recorded as open in doc 07 §5 |

**Skills updated:** functionality (v1.1 — wave order, portal name, reporting resolution, pricing framing, IP register, checklist), design (reporting responsive rule + pricing label). `CLAUDE.md` (rule 10 rewritten; rules 14–17 added).
**Questions closed:** Q1, Q4, Q13.
**New open items:** O1–O16 (see doc 07) + the static-HTML-vs-Laravel build-approach conflict.

---

## 2026-09-02 — Version 1.6 — MVP build updated to the revised Wave 1 (3 new screens + renames)

**Trigger:** Instruction to update the MVP design to the new features, on the existing Laravel demo-mode codebase (build-approach question answered: keep Laravel demo-mode). `check-sources.sh` returned MISSING SOURCE FOLDER (client folder not on this machine — exit 3, proceed).

**Built / changed (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | **Campaign Reporting** | `/reports` was a "Decision pending" stub; a test asserted it stayed unbuilt | **Built natively:** `Customer/Reporting.vue` — 6 stat tiles, cross-channel trend (AreaChart), leads-by-channel donut, META/Google/Website stat groups, top-3 campaigns table. New `reporting` data block, `DemoController@reports`, route → controller. Figures consistent with the dashboard (leads 428, open 42.6%). No iframe. [L6] [L14] |
| 2 | **Campaign Request Flow** | Wave 2 stub | **Built** (`Customer/RequestFlow.vue`): interactive 4-step wizard (type → goal → briefing → submit) with visual success state, plus the six-status pipeline and recent requests. New `request_flow` data, `DemoController@requestFlow`, `/campaign-requests/new` → controller. [L14] |
| 3 | **Scratch Game / Lead Gen** | No screen existed | **Built** (`Customer/ScratchGame.vue`): 4 summary tiles, games table (participants/emails/capture/status), prize setup. New `scratch_game` data, `DemoController@scratchGame`, new route `/lead-generation`. [L14] |
| 4 | **Third portal name** | "Settings / Development Portal", demo role "Developer" | **Platform Settings** (Platform Owner) across `config/demo.php`, `DemoController`, `AdminLayout.vue`, `Dev/Overview.vue`, `Dev/WhiteLabel.vue`, and the role switcher label. [L16] |
| 5 | **Pricing framing** | Plain prices | **"Example configuration"** label on Marketing Plans and Marketing Packages, from a new `pricing_note` data value. [L17] |
| 6 | **Dashboard links** | — | Customer Dashboard lead panel now links to the reporting and lead-generation screens, so the storyline is clickable end to end |
| 7 | **Tests** | Asserted reporting stays unbuilt | Rewritten: reporting built natively (no iframe), the 3 pulled-forward screens render, third portal named Platform Settings, and the six-status guard now also covers the new screens |

**Wave 1 is now 12 storyline screens, all reachable and clickable.**

**Skills updated:** none — these are rule *applications*, not rule changes (rules were updated in Version 1.5). **Verification:** `npm run build` passes (all pages compile); PHP/Composer are not available in this environment, so `php artisan test` must be run locally — the feature tests were updated to match.

---

<!--
Template for the next entry — copy this block:

## YYYY-MM-DD — Version X.Y — <short title>

**Trigger:** <new client file / answered question / drift reported by check-sources.sh>

**Source files read:** <list>

**Changes (was → now):**

| # | Item | Before | Now |
|---|---|---|---|
| 1 | | | |

**Skills updated:** design / functionality / both / none
**Questions closed:** Qn, Qn
**New questions:** Qn
-->
