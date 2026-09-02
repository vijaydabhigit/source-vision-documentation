# MVP Build Approach — Technical Decision Record

**Date:** 12 August 2026
**Decided by:** Development team, on the instruction *"keep with latest version and create MVP with the best approach that you can decide"*
**Status:** Decided. Supersedes the Phase 1 technology in NexusLink Execution Plan v1.0 §3.1.
**Target:** Wave 1 — nine screens, demo live Tuesday 1 September 2026

---

## 1. The decision in one line

> Build the demo on the **installed latest stack — Laravel 13.25 + Inertia 3 + Vue 3.5 + Tailwind 4 + Vite 8 — running in "demo mode": no database, no migrations, no models, no real authentication. Every figure on every screen comes from one shared demo-data file.**

This keeps the speed profile the Execution Plan wanted from static HTML, while producing code that **is** the Phase 2 target rather than something that must be converted into it.

---

## 2. What changed, and why

Execution Plan v1.0 §3.1 specified static HTML for Phase 1, with Laravel 11 + Vue 3 as a separately quoted Phase 2 (§3.2, §13). The instruction now is to use the latest stack and build the MVP directly.

The Plan's reasoning for static HTML was sound and is worth restating, because this decision has to satisfy the same goals:

| Plan's goal for Phase 1 §3.1 | How this approach still meets it |
|---|---|
| "No backend, no database" | No database, no migrations, no models, no auth tables. Nothing to provision |
| "One shared demo-data file drives every figure on every screen, so no two screens can contradict each other" | Kept exactly — a single PHP data file is the only source of figures |
| "Forms and toggles are visual. Numbers are fixed" | Kept — forms post nowhere in Wave 1 |
| "Late design and copy changes cost minutes instead of migrations" | Kept — copy and figures live in the data file and page components, not in a schema |
| "Folder and component structure mirrors the future Blade/Vue component tree" | **Improved** — they *are* Vue components. No mapping step |
| "Every colour, font, radius and spacing value is a CSS custom property… the same token sheet drives Phase 2" | Kept — Tailwind 4 `@theme` tokens compile to CSS custom properties |
| "The demo-data file is written in the shape of future database records" | Kept — array shapes mirror future tables, so they convert to seeders and factories |

### Why this is better than static HTML, given the instruction

1. **No Phase 2 rewrite at all.** The Plan's own framing was that Phase 1 is "engineered to become Phase 2". This removes the conversion step entirely.
2. **Component reuse cuts the repetitive work.** Wave 1's nine screens are dense with repeated patterns: 8 KPI cards, 5 plan cards, 8 package cards, 8 service tiles, data tables, status chips, two mega-menus, a navy sidebar. Written once as Vue components, each additional use is nearly free. In static HTML each is a copied block.
3. **Live white-label re-theming becomes trivial.** The Plan ranks this first among optional enhancements (§9) and calls it *"the single sentence the entire asset is sold on"*. With `@theme` custom properties plus Vue reactivity, changing the colour fields re-skins the platform live — a few lines, not a rebuild.
4. **Cross-screen consistency is structural, not a review step.** The Plan's risk register lists "two screens contradict each other" as a top risk, mitigated by a Stage 5 reconciliation pass. Here every screen reads the same file, so the contradiction cannot occur.

---

## 3. What "demo mode" means precisely

| Layer | Decision | Reason |
|---|---|---|
| **Database** | **None.** No migrations, no models, no Eloquent | Nothing in Wave 1 persists. PHP 8.5 here also has no `pdo_sqlite` |
| **Demo data** | One file, `config/demo.php`, holding customers, plans, packages, services, campaigns, leads, newsletters, activity and every KPI. Array shapes mirror future tables | The Plan's single-source-of-truth requirement; converts straight to seeders in Phase 2 |
| **Auth** | No users table, no passwords. The login screen is real UI that posts nowhere. A **demo role switcher** holds the current role in the session | `[PB §7.1]` asks for an optional demo role selector. Plan §13: buyers are walked through, never given hands-on logins |
| **Session / cache / queue** | `file` / `file` / `sync` — already configured | No database dependency |
| **Design tokens** | Tailwind 4 `@theme` block in `resources/css/app.css`, self-hosted Space Grotesk | This *is* the token sheet Blue Virtue must approve at Gate M1 |
| **Pages** | One Inertia page component per screen in `resources/js/pages/` | Matches the installed Inertia 3 auto-resolution |
| **Routes** | All Wave 1 routes stubbed to on-brand empty pages **first** | The Plan's Stage 2 "clickable shell" — the walkthrough never dead-ends |
| **Forms** | Visual only. Optionally a success state, listed as a very-low-effort enhancement in §9 | Plan §3.1 |
| **Responsive** | Mobile-first Tailwind, three tiers | Standing design Rule B |
| **Hosting** | Needs PHP hosting rather than a static host. Register item S7 already defaults to NexusLink hosting | Compatible with the existing default |

---

## 4. Build order — the Plan's stages, unchanged

The technology changed; the sequence and the gates did not.

| Stage | Dates | Work | Gate |
|---|---|---|---|
| 0 | 12–14 Aug | Decisions locked (26-item register) | G0 |
| 1 | 17–18 Aug | Tokens in `@theme`, Space Grotesk, shared component library, `config/demo.php` | M1 — Blue Virtue approves the token sheet |
| 2 | 18–19 Aug | Clickable shell: public header with both mega-menus, customer chrome, navy admin sidebar, development portal sidebar, demo role switcher, every Wave 1 route stubbed | M2 — full walkthrough navigable |
| 3 | 19–24 Aug | Customer layer: Homepage, Login, Customer Dashboard (7 blocks), Marketing Services catalogue, Marketing Packages (8 cards), Marketing Plans (5 tiers) | M3 — Blue Virtue reviews |
| 4 | 24–27 Aug | Admin + Development layers: Admin Dashboard, Development Portal overview, White-Label configuration | M4 — Wave 1 complete |
| 5 | 27–28 Aug | Content and figure reconciliation, replace the real company logos, English copy pass | Asset owner approves figures |
| 6 | 28 Aug | Optional enhancements, live white-label re-theming first | Cut first if anything slipped |
| 7 | 28–31 Aug | Responsive pass, cross-browser, link audit, deploy behind HTTP basic auth, four documents | M5 — demo live |
| 8 | 31 Aug – 1 Sep | Dry run, defect fix, handover | M6 — Acquire-ready |

### Component library to build in Stage 1

`Button` (primary blue / commercial orange / secondary / text) · `Card` · `KpiCard` (icon, label, value, delta, sparkline) · `StatusChip` · `DataTable` (chips + pagination) · `ServiceTile` · `PlanCard` · `PackageCard` · `InclusionList` · `MegaMenu` · `Sidebar` · `SectionEyebrow` · `BrandedBand` · `LineChart` · `DonutChart` · `ProgressBar` · `NotificationRow` · `EmptyState`

Charts: load the `dataviz` skill, then map its palette onto the brand tokens.

---

## 5. Risks I am accepting, stated plainly

| Risk | Assessment |
|---|---|
| **A build step now exists** (Vite). A plain static host is no longer enough | Low. S7's default is already NexusLink hosting on its own infrastructure |
| **The 124–170 h estimate was for static HTML** | The component-reuse gain and the removed conversion step roughly offset the framework overhead — but I am **not** claiming this closes the capacity gap. **Item S2 (one developer, two developers, or a later date) is unchanged and still needs an answer.** With one developer the arithmetic in Plan §4.2 still applies |
| **Execution Plan v1.0 §3.1, §3.2 and §13 are now wrong** on Phase 1 technology and on the Laravel version | The client holds that document. It must be reissued or corrected before they rely on it — see the note in document 05 |
| **Laravel 13 vs the documented Laravel 11 Phase 2 target** | Laravel 13 requires PHP ^8.3; the Plan assumed PHP 8.2+. Any Phase 2 hosting spec written against PHP 8.2 needs updating |
| **More moving parts than raw HTML** | Mitigated by no database, no auth and no API layer. The setup is done and verified: build passes, tests pass, Inertia renders |

---

## 6. What is already in place

Verified working in this repository:

- Laravel 13.25.0 on PHP 8.5.9, Inertia 3.3.1 server-side, `@inertiajs/vue3` 3.6.1, Vue 3.5.41, Vite 8.2.1, Tailwind 4.3.3
- `HandleInertiaRequests` and `AddLinkHeadersForPreloadedAssets` registered
- Inertia page resolution from `resources/js/pages/`, verified end to end (page object renders with correct props; a bad asset version returns 409)
- `npm run build` passes, code-splitting works; `php artisan test` passes
- No database configured — session, cache and queue on `file`/`file`/`sync`

### Still to do before Stage 1 can start
1. Replace the skeleton's Instrument Sans with **self-hosted Space Grotesk** from the client's font files
2. Add the brand tokens to `@theme` and publish the token sheet for Blue Virtue's approval (Gate M1)
3. Write `config/demo.php`
4. Build the component library above

---

## 7. Related documents

- [05-Client-Discussion-Module-Functionality.md](05-Client-Discussion-Module-Functionality.md) — module and submodule detail, GRS mapping, and the client-facing note about this change
- [01-Requirement-Understanding.md](01-Requirement-Understanding.md) — the underlying requirement
- `skills/source-vision-functionality/SKILL.md` — build rules
- `skills/source-vision-design/SKILL.md` — design rules
- Client folder `12-Aug/` — Execution Plan v1.0, Open Decisions register, Roadmap one-pager
