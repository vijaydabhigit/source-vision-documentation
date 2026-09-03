# Scope Review & Decisions — September 2026

**Date:** 2 September 2026
**Purpose:** Single record of the August–September 2026 scope-review sequence, what is now **finalised (locked)**, and what is still **open**. This document is the authority for the scope/naming/wave changes; the two skills and the code-repo `CLAUDE.md` are written from it.

## Source marks used in this document

| Mark | Meaning |
|---|---|
| `[MVP-v1]` | Phase 1 — MVP Demo Module List **v1.0**, 12 Aug 2026 (sent to client) — `sources/…MVP_Module_List_v1_12Aug2026.pdf` |
| `[OV-v1]` | Phase 1 & Phase 2 Module Overview **v1.0**, 12 Aug 2026 (sent to client) — `sources/…Overview_v1_12Aug2026.pdf` |
| `[BV-SR]` | **Blue Virtue Scope Review & Alignment Notes, 31 Aug 2026** (client feedback) — `sources/…Scope_Review_Alignment_Notes_BlueVirtue_31Aug2026.docx` |
| `[DLOG]` | SourceVision Decision Log v1, 1 Sep 2026 (NexusLink internal) — `pm-pack/SourceVision_Decision_Log_v1.xlsx` |
| `[BIBLE]` | SourceVision Project Bible v1, 1 Sep 2026 (NexusLink internal PM handover) — `pm-pack/SourceVision_Project_Bible_v1.docx` |
| `[MVP-v2]` | Phase 1 — MVP Demo Module List **v2.0**, 2 Sep 2026 (sent to client today) — `sources/…MVP_Module_List_v2_02Sep2026.pdf` |
| `[OV-v2]` | Phase 1 & Phase 2 Module Overview **v2.0**, 2 Sep 2026 (sent to client today) — `sources/…Overview_v2_02Sep2026.pdf` |

Earlier marks (`[PB]`, `[DH]`, `[QP-n]`, `[IMG:x]`, `[GRS]`, `[TEAM]`) are defined in [01-Requirement-Understanding.md](01-Requirement-Understanding.md#how-to-read-the-source-marks).

---

## 1. The sequence (what happened, in order)

1. **12 Aug 2026 — sent to client.** NexusLink shared the Phase 1 MVP Module List v1.0 `[MVP-v1]` and the Phase 1 & Phase 2 Module Overview v1.0 `[OV-v1]`. Phase 1 = 24 screens in three waves; Wave 1 = 9 committed screens led by **Public Homepage**; "Developer view" was one of the demo areas; Phase 2 = 24 modules presented as a build.
2. **31 Aug 2026 — client feedback.** Blue Virtue returned the **Scope Review & Alignment Notes** `[BV-SR]`. Phase 1 **direction approved, subject to Wave 1 re-prioritisation**; Phase 2 **accepted as a working framework only** — not an approved build. Specific refinements requested (see §2).
3. **1 Sep 2026 — internal PM pack (prepared by Claude for the PM).** The **Decision Log v1** `[DLOG]` (25 locked + 16 open decisions + IP register) and the **Project Bible v1** `[BIBLE]` (full PM handover) were produced to start execution.
4. **2 Sep 2026 (today) — sent to client.** NexusLink shared the revised **MVP Module List v2.0** `[MVP-v2]` and **Module Overview v2.0** `[OV-v2]`, applying the Blue Virtue feedback.

---

## 2. What Blue Virtue asked for (31 Aug) `[BV-SR]`

- **Phase 1:** prioritise the buyer demo **story**, not the screen count — a buyer must understand the full commercial loop in ~10 minutes. Move **Campaign Request Flow, Scratch Game / Lead Generation and Campaign Reporting into Wave 1** (demo depth). Public Homepage may stay but is less important.
- **Role naming:** replace **"Developer view"** with **Platform Owner / Platform Settings**. The three demo areas read as **Customer Portal · Admin Portal · Platform Settings**.
- **Packages / plans / pricing:** treat as **example monetisation models**, configurable by the platform owner — not fixed Source Vision commercial terms.
- **Phase 2:** present as **"Proposed Full Platform / Future Product Architecture"**, not a committed build. Module-level estimates only **after** scope approval. Specific module changes: GRS Data Migration → **Generic Data Import & Migration Tools** (no GRS data assumed); **Reporting** kept as a layer but assess Blue Virtue's existing dashboard technology before building a custom analytics engine; **AI Campaign Assistant** and **Print Portal** → roadmap/optional; **Integrations Layer** split into core / optional third-party / API; **Content Library** = simple asset organisation (legacy GRS folder module excluded); **Multi-tenancy / white-label** = strategic foundation; **Email & Newsletter Engine** = later design (document provider model, sending domains, volume tiers, deliverability, variable email costs, tenant economics before Phase 2 approval); **Laravel + Vue** accepted subject to portability/documentation/transferability.
- **IP governance:** start a **Development & IP Register** from the first implementation work; new development must **not** imply any ownership %, licence or revenue share. No Source Vision scope assumes GRS customers/data/technology/IP transfer unless confirmed in writing.
- **Infrastructure:** Phase 1 demo may use the **Blue Virtue VPS**, **source-vision.com** with **Cloudflare** DNS — **MVP infrastructure only**, not a production hosting decision.

---

## 3. FINALISED / LOCKED decisions

These are agreed and now govern the build. IDs match the Decision Log `[DLOG]`. Apply them everywhere.

### 3.1 From the 31 Aug scope review (client-authoritative) `[BV-SR]` `[MVP-v2]` `[OV-v2]`

| ID | Locked decision | Impact |
|---|---|---|
| **L13** | **Wave 1 must tell the full 10-minute commercial story:** Login → Customer → Services/Plans → Request → Campaign/Lead Gen → Results → Admin → White-label | Sets Wave 1 order and content |
| **L14** | **Campaign Request Flow, Scratch Game / Lead Gen and Campaign Reporting are Wave 1** (demo depth), pulled forward from Wave 2 | Wave 1 grows to 12 screens |
| **L15** | **Public Homepage deprioritised** within Wave 1 — completed after the storyline screens; trim first if capacity is tight | Homepage no longer the Wave 1 lead screen |
| **L16** | **"Developer view / Development Portal" renamed "Platform Settings" (Platform Owner).** Three portals = **Customer Portal · Admin Portal · Platform Settings** | Rename in every doc, mockup and menu label |
| **L17** | **Plan/package pricing shown = example monetisation model, configurable by the platform owner** | Add a small "example configuration" label wherever pricing appears in the demo |
| **L18** | Phase 2 "GRS Data Migration" → **"Generic Data Import & Migration Tools"** — no GRS data assumed | Phase 2 Module Overview v2 wording |
| **L19** | Phase 2 = **"Proposed Full Platform / Future Product Architecture"** — framework only, not a committed build | **No Phase 2 effort/cost figures in any client-facing doc** until the framework is signed |
| **L20** | **AI Campaign Assistant + Print Portal = ROADMAP only** in Phase 2 | Out of core Phase 2 list; show as future modules only |
| **L21** | **Integrations Layer split** into: Core Integrations / Optional Third-Party Integrations / API Framework | Not one implementation effort |
| **L22** | **Content Library = simple asset organisation**; legacy GRS folder module **excluded** | Reword so it does not read as a GRS carry-over |
| **L23** | **Multi-tenancy / white-label = strategic priority** of Phase 2 (top of the Phase 2 list) | Shared codebase, tenant separation, custom domains, branding, roles, data separation |
| **L24** | **Phase 1 hosting = Blue Virtue VPS; demo domain = source-vision.com on Cloudflare; MVP infra only** | Not a production hosting commitment. Answers old Q13 |
| **L25** | **Development & IP Register maintained from day 1** of implementation | Log every new component. Entries imply no ownership/revenue position |

### 3.2 Carried from 11–12 Aug (still locked) `[DLOG]` `[BIBLE]`

| ID | Locked decision |
|---|---|
| **L2** | **Dummy data only** in Phase 1 — no real data of any kind; forms do not submit |
| **L3** | **English** throughout Phase 1 (Newsletter Overview may show Dutch GRS screenshots as heritage) |
| **L4** | **EUR (€)** throughout — no USD/GBP/INR |
| **L5** | **Brand system locked** by the Blue Virtue Development Handover — navy `#192A4B` / blue `#001FFA` / orange `#FD5104`, Space Grotesk, logo assets |
| **L6** | **Campaign Reporting Dashboard built natively** for the demo — the Meneer Online iframe is **rejected** (Dutch UI, live analytics, off-brand, breaks the dummy-data rule). *(This resolves the earlier "reporting = build neither" conflict, register S6.)* Phase 2 reporting is re-assessed against Blue Virtue's dashboard tech — see O9 |
| **L8** | **Single-DB multi-tenancy with CSS-custom-property re-theming** (Phase 2 architecture direction) |
| **L9** | **eMagazine WITHDRAWN — build nowhere** (dashboard, service selection, packages, reporting) |
| **L11** | Homepage hero stat = **"~100,000 employees using Source Vision platforms worldwide"** (not "users") |
| **L12** | Homepage trusted-by row uses **placeholder logos**, not real third-party brands |

---

## 4. OPEN decisions (not yet finalised)

IDs match the Decision Log `[DLOG]`. Do not guess these — build what is unblocked and leave a `// TODO O<n>` marker.

| ID | Open item | Owner | Priority |
|---|---|---|---|
| **O1** | Franchise Plan pricing: **€999** (Plans page) vs **€1,049** (Upgrade page) — reconcile. Default **€999** | Blue Virtue | High |
| **O2** | Custom Campaign Support: **€299** standalone vs **€99** add-on — reconcile | Blue Virtue | High |
| **O3** | Admin plan vocabulary (Basic/Standard/Pro) does not match the 5 customer plan names | Blue Virtue | Medium |
| **O5** | Buttons: **Space Grotesk** (mockups) vs **Inter** (handover text). Default Space Grotesk | Blue Virtue | High |
| **O6/O7/O8** | Exact light-grey tokens, border colour, radius, spacing scale · navy gradient stops · icon library (Heroicons / Lucide / Blue Virtue set) | Blue Virtue / PM | Medium |
| **O9** | **Blue Virtue dashboard technology** — reference/demo/docs, so we assess reuse **before quoting Phase 2 reporting** | Blue Virtue | High |
| **O10** | **Capacity option A / B / C** for the September build | Blue Virtue + Vijay | **CRITICAL — before build kick-off** |
| **O11** | **One-page MVP-phase working agreement** (NexusLink drafts, Blue Virtue counter-signs) | Vijay | **CRITICAL — before build kick-off** |
| **O12** | VPS access + source-vision.com Cloudflare credentials handover | Blue Virtue | High |
| **O13** | Software sales professional — do they need specific screens / materials / metrics? | Blue Virtue | Low |
| **O14** | Who owns demo storyline, demo script, Acquire listing copy? | Blue Virtue | Medium |
| **O16** | Buyer walkthrough format — guided recording, live walk-through, or both? | Blue Virtue | Low |

---

## 5. ⚠ CONFLICT TO RESOLVE — Phase 1 build approach (static HTML vs Laravel demo-mode)

There are **two different statements** of how Phase 1 is built. This must be reconciled before build kick-off; it is **not silently decided here**.

- **PM pack (Decision Log L1 + Project Bible §23) `[DLOG]` `[BIBLE]`:** Phase 1 = **static HTML + CSS + vanilla JavaScript, no framework, no backend, no database** ("Vijay explicit: 'make it html only for now'"). IP-register paths use `source-vision-mvp/…/*.html`.
- **Code repo + [06-MVP-Build-Approach.md](06-MVP-Build-Approach.md) + `source-vision-functionality` skill:** Phase 1 = **Laravel 13 + Inertia 3 + Vue 3 + Tailwind 4 in "demo mode"** — no database, no auth, one `config/demo.php` data file. This document explicitly **supersedes** the static-HTML plan.

Both deliver the same "no real data" demo, but on different technology, and the actual `source-vision` codebase is the Laravel version.

**Recommendation (needs Vijay's written confirmation):** keep **Laravel 13 demo-mode** (it is the working code and the reasoned supersession) and correct the Decision Log L1 / Project Bible §23 wording to match. Recorded as **open** until confirmed.

---

## 6. Answers this sequence gives to earlier open questions

- **Q1 (admin menu):** use the newer `Part_2` menu (Dashboard, Customers, Campaigns, Subscriptions, Leads, Requests, Content Library, User Management, Reports, Settings) — confirmed by the Wave 1 acceptance criteria `[BIBLE]`.
- **Q2 (public website in scope):** yes — Public Homepage stays in Wave 1 but is **deprioritised** (L15).
- **Q4 (final Wave 1 list):** the 12-screen storyline order in `[MVP-v2]` is the answer; eMagazine excluded (L9).
- **Q13 (demo hosting):** Blue Virtue VPS + source-vision.com + Cloudflare, MVP infra only (L24).
- Still open: Q5/Q6 pricing & font (O1, O2, O5), and the new O3, O6–O16 above.
