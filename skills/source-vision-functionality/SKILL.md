---
name: source-vision-functionality
description: Source Vision functional and business rules — the three portals (Customer, Admin, Platform Settings), the Services vs Packages vs Plans model, campaign request statuses, screen-by-screen requirements, user roles, dummy-data rules, the natively-built campaign reporting dashboard, and which logic is reused from the older GRS Online project. Use this skill whenever building or reviewing routes, controllers, models, migrations, seeders, Inertia pages, permissions, workflows, statuses or business logic for Source Vision, and whenever deciding whether a feature belongs in the September MVP or the roadmap.
---

# Source Vision — Functionality & Business Rules

Authoritative functional rules for the Source Vision demo platform.

Source marks: `[PB §n]` = Project Brief section n, `[QP-n]` = pitch slide n, `[DH]` = Development Handover, `[IMG:x]` = design mockup, `[GRS §n]` = **other project** GRS Online module n, `[TEAM]` = our decision.
Full detail: [01-Requirement-Understanding.md](../../documents/01-Requirement-Understanding.md)

---

## THE BUILD MODEL — decided 12 Aug 2026

Build the demo on the **installed latest stack, in "demo mode"**:

**Laravel 13.25 + Inertia 3 + Vue 3.5 + Tailwind 4 + Vite 8 — with no database, no migrations, no models and no real authentication.** Every figure comes from one shared demo-data file, `config/demo.php`.

This **supersedes** Execution Plan v1.0 §3.1 (which specified static HTML for Phase 1) and §3.2/§13 (which named Laravel 11 / PHP 8.2 as a separate Phase 2). Full reasoning and risks: [06-MVP-Build-Approach.md](../../documents/06-MVP-Build-Approach.md)

| Rule | Detail |
|---|---|
| **No database** | No migrations, no models, no Eloquent. Session, cache and queue stay on `file`/`file`/`sync` |
| **One data source** | `config/demo.php` holds every customer, plan, package, service, campaign, lead and KPI. Array shapes mirror future tables so they convert to seeders in Phase 2. **No figure is ever written into a component** |
| **No auth** | No users table, no passwords. The login screen is real UI that posts nowhere. A **demo role switcher** keeps the current role in the session |
| **Forms are visual** | They post nowhere. A success state is an approved low-cost enhancement `[EP §9]` |
| **Components, not copies** | Wave 1 repeats heavily — 8 KPI cards, 5 plan cards, 8 package cards, 8 service tiles, tables, chips, 2 mega-menus, navy sidebar. Build each once |
| **Shell first** | Stub every Wave 1 route to an on-brand empty page before filling any of them, so the walkthrough never dead-ends (Stage 2 / Gate M2) |
| **Tokens** | Brand values live in the Tailwind 4 `@theme` block — this *is* the token sheet Blue Virtue approves at Gate M1 |

The stage sequence, gates and milestone dates from the Execution Plan are **unchanged**: build starts Mon 17 Aug, design cut-off Wed 20 Aug, demo live Tue 1 Sep.

### Wave structure — build in this order

> **REVISED 31 Aug 2026 after the Blue Virtue Scope Review `[BV-SR]` `[MVP-v2]`.** Wave 1 is now ordered as the **10-minute buyer demo storyline**, and three screens (Campaign Request Flow, Scratch Game / Lead Gen, Campaign Reporting) were **pulled forward from Wave 2 into Wave 1** at demo depth. Full record: [07-Scope-Review-and-Decisions-Sep-2026.md](../../documents/07-Scope-Review-and-Decisions-Sep-2026.md).

- **Wave 1 (protected, live 1 Sep) — twelve screens, in demo storyline order:**
  1. Login & demo role switcher →
  2. Customer Dashboard →
  3. Services Catalogue · Marketing Packages (8 cards) · Marketing Plans (5 tiers, €199–€1,299) →
  4. **Campaign Request Flow** *(moved forward — demo depth)* →
  5. **Scratch Game / Lead Generation** *(moved forward — demo depth)* →
  6. **Campaign Reporting Dashboard** *(moved forward — demo depth, built natively — see §8)* →
  7. Admin Dashboard →
  8. White-Label Configuration · **Platform Settings** →
  - Public Homepage — **kept in Wave 1 but deprioritised**; complete it after the storyline screens; trim first if capacity is tight `[BV-SR]`
- **Wave 2 (after the demo build):** Landing Page/Lead-Gen Overview · Notifications panel · Service Landing Page template ×8 · Upgrade Your Plan
- **Wave 3 (as time allows):** Newsletter Overview · Admin Customers · Admin Subscriptions & Plans/Pricing · Admin Requests · Admin Leads · Admin Campaigns · User Management + role matrix · Content Library · Contact · My Account · remaining Platform Settings sub-screens

Anything not on these lists is a **roadmap entry shown inside Platform Settings**, not a build item.

Other positions set by the plan and the decisions register that override earlier assumptions in this skill:

| Item | Position |
|---|---|
| **S1** | Wave 1 is a protected **twelve-screen** storyline list (revised 31 Aug) — see the Wave structure above and §7 |
| **C3** | Taxonomy confirmed: **Services / Packages / Plans**. Use the five customer-facing plan names everywhere and rewrite the admin dummy data to match |
| **C4** | **eMagazine is withdrawn** (L9) — it appears nowhere in Wave 1; record it as a roadmap service |
| **L17** | **Pricing shown = example monetisation model, configurable by the platform owner** (Blue Virtue, 31 Aug). Show a small "example configuration" label wherever plan/package pricing appears |
| **C1 / O1 / O2** | Default Franchise plan = **€999** (correct the Upgrade screen). Franchise €999 vs €1,049 (O1) and Custom Campaign Support €299 vs €99 (O2) remain **open** in the Decision Log — seed the €999/Plans-page values and leave a `// TODO O1`/`// TODO O2` marker |
| **D1 / O5** | Default **Space Grotesk everywhere**, including buttons; the "Inter" reference is a leftover. Confirmation still open (O5) |
| **D5** | Toggles stay on commercial cards; request/status chips on the dashboard services grid — see §6 |
| **S5** | Campaign Planning Tool, Email Marketing and CMS Management are **dropped from the interface** and become roadmap modules in Platform Settings |
| **S6 / L6** | Reporting dashboard — **RESOLVED: build natively at demo depth, in Wave 1**. The Meneer Online iframe is rejected — see §8 |
| **X4** | The GRS Mailsystem at `grsonline.nl` is **still live and still collecting real email addresses**. Treat as **read-only**. Reference screenshots only, and only after real recipient data is removed |

Decisions are due **Fri 14 Aug 2026**; unanswered items proceed on the NexusLink default. Build starts **Mon 17 Aug**; design cut-off **Wed 20 Aug**; demo live **Tue 1 Sep**.

---

## STEP 0 — Always do this first (mandatory)

```bash
bash documents/check-sources.sh
```

`OK` → continue. `CHANGED` / `NEW` / `MISSING` → **stop**, update this skill per [04-Skill-Update-Rules.md](../../documents/04-Skill-Update-Rules.md), then continue.

Also check [02-Open-Questions.md](../../documents/02-Open-Questions.md) before starting a screen. Six questions are **blocking** (Q1–Q6). If your task depends on one, build what is unblocked and flag the rest.

---

## 1. The one rule that governs every decision

This is a **sales demo to increase the resale value of a business asset**, not a production SaaS. `[PB §1]` `[PB §Main Objective]`

> **"Demo first. Product later."** `[PB §2]` `[QP-1]`

Test every task against: **"Does this help a buyer understand the value of Source Vision faster?"**
Yes → MVP. No → roadmap. `[PB §2]`

### The client's 5 rules `[PB §16]`
1. **Demo First** — not a complete SaaS product yet.
2. **Sales Value First** — every feature must explain value to a buyer.
3. **Avoid Scope Creep** — too complex → roadmap.
4. **Dummy Data Only** — no real customer, consumer, financial, email or login data. **Never** seed real personal data or real third-party brand names.
5. **Keep It Simple** — a clear simple demo beats a complex unfinished product.

### Engineering consequences `[TEAM]`
- Prefer a believable read-only screen over a half-working write flow.
- Every number on screen comes from a **seeder**, never hardcoded in a component.
- Keep prices, plan names, service names and labels in config/DB — the client warns all of this may change `[DH §6]`.
- Do not build multi-tenancy, invoicing, or real payment/AI integrations. They are explicitly out of scope `[PB §5]`.

---

## 2. Not in the September MVP `[PB §5]`

Full SaaS architecture · full multi-tenant backend · full invoicing · complete API integrations · complete Print.com integration · full AI functionality · complete rebuild of existing systems · advanced CRM integrations · full marketplace.

Show these as **roadmap items** in **Platform Settings** instead. `[PB §5]` `[PB §7.15]`

---

## 3. Three portals `[PB §4]` `[QP-5]`

| Portal | Audience | Sells the idea that... | Contains `[QP-5]` |
|---|---|---|---|
| **Customer Portal** | End customer (e.g. a shop) | customers can easily understand and buy marketing services | Dashboard, service selection, campaign requests, reports, leads |
| **Admin Portal** | The buyer's staff (agency/franchise HQ) | one company can manage many customers and services centrally | Accounts, subscriptions, campaign activity, service requests |
| **Platform Settings** (Platform Owner) | Buyer's technical owner | the platform can be fully rebranded and extended | White-label setup, logo/colours, modules, roles, integrations |

> **Naming — LOCKED 31 Aug 2026 (L16) `[BV-SR]`.** The third portal is **Platform Settings** (persona: **Platform Owner**). Do **not** call it "Developer view", "Development Portal" or "Dev Portal" anywhere — Blue Virtue explicitly renamed it. The three portals are **Customer Portal · Admin Portal · Platform Settings**.

Login should offer an **optional role switch for demo purposes** so a presenter can jump between portals quickly. `[PB §7.1]`

---

## 4. The demo narrative — build to support this flow `[QP-6]`

```
Create customer account → Select plan or package → Request marketing service
      → Launch campaign → Generate leads → Report results
```

Commercial logic: **platform access + recurring service packages + campaign add-ons.** `[QP-6]`
Any screen that does not serve a step in this flow is lower priority. `[TEAM]`

---

## 5. Services vs Packages vs Plans (core domain model)

The client flagged this as unclear and asked us to fix it: *"Clarify Plans vs Packages vs Services"* `[QP-7]`.
Current model `[TEAM]`, derived from the mockups — **subject to Q5**:

### 5.1 Service — the atomic unit
Eight services in the design menu `[IMG:MENU_Marketing Serivices _ Plans _ PACKAGES]`:
`Newsletter` · `Scratch Game` · `Product Promotion Email` · `Landing Page` · `Custom Campaign Support` · `Social Media Advertising` · `Google Advertising` · `TikTok Ads`

The brief additionally lists **eMagazine** and **Print portal (Coming soon)** `[PB §7.3]` — both **missing** from the design menu. Open — Q4.

### 5.2 Package — one service sold standalone, with its own price
One card per service: price/month, "Included services" bullet list, optional add-ons with NO/YES toggles, `Get Started`, monthly subscription total. `[IMG:Packages/Artboard 2, 9]`
Examples: Custom Campaign Support €299/mo, Google Advertising €549/mo.

### 5.3 Plan — a bundle/tier of several services
| Plan | €/month | Services |
|---|---|---|
| Starter | 199 | 2 |
| Growth | 349 | 3 |
| Full Service | 699 | 7 |
| Franchise | 999 (conflict: 1,049) | 7 |
| Agency | 1,299 | 8 |

Source `[IMG:Marketing_Plans]`; same five names in `[PB §7.4]`.
Each plan shows included services, optional add-ons with prices, upgrade option, active/inactive state. `[PB §7.4]`

### 5.4 Data model implication `[TEAM]`
```
Service (8+)
  ├── sold standalone as Package     → own price
  └── bundled into Plan (5 tiers)    → plan price
Add-on = Service attached to an active Plan/Package at a lower price
```
Model `services`, `plans`, `packages` and a pivot carrying `price` + `is_addon`, so the same service can hold different prices in different contexts. Do not duplicate service rows per price.

### 5.5 Pricing conflicts — never guess
| Item | Price A | Price B |
|---|---|---|
| Franchise Plan | €999 `[IMG:Marketing_Plans]` | €1,049 `[IMG:Upgrade ur plan]` |
| Google Advertising | €549 standalone `[IMG:Packages/Artboard 9]` | €79 add-on `[IMG:Marketing_Plans]` |
| Custom Campaign Support | €299 standalone `[IMG:Packages/Artboard 2]` | €99 add-on `[IMG:Marketing_Plans]` |

Seed the values from the **Marketing Plans** page and leave a `// TODO Q5` comment. `[TEAM]`
Currency is **EUR (€)** throughout; admin shows "All amounts in EUR". `[IMG:Part_2/Admin_Dshboard]`

---

## 6. Request + status logic (NOT simple toggles)

Client feedback said: *"Replace simple switches with request/status logic"* `[QP-7]`.

> **Refined position — NexusLink register item D5 (12 Aug 2026).** This is **not** a blanket replacement. The agreed split is:
> - **Keep the ON/OFF and ACTIVE/INACTIVE toggles on the commercial cards** (Marketing Packages, Marketing Plans) — there they read as *"what I have"*.
> - **Use request / status chips on the dashboard services grid** — there they read as *"what I have asked for"*.
>
> Owner: Blue Virtue, due Fri 14 Aug 2026. An earlier version of this skill said to remove all toggles; that was too absolute.

### The 6 canonical statuses `[PB §7.5]`
Use exactly these names, in this order:

1. `New request`
2. `In progress`
3. `Waiting for input`
4. `Waiting for approval`
5. `Scheduled`
6. `Completed`

Define once as a PHP enum and reuse everywhere. Never invent a seventh status without asking. `[TEAM]`

### Campaign request flow `[PB §7.5]`
`Choose campaign type → Choose campaign goal → Add briefing/remarks → Upload files or images → Submit request`

A simplified 4-step public version also exists for marketing pages: `Select service → Share brief → Approve delivery → Track results`. `[IMG:Part_2/Campaign customer journey]`

---

## 7. Screens

Brief states screens **1–4 are mandatory**; the rest are undecided `[PB §7]`. There is **no screen 9** in the brief (numbering jumps 8 → 10).

| # | Screen | Priority | Key requirement | Source |
|---|---|---|---|---|
| 1 | Login | **Mandatory** | Logo, SaaS look, login, optional demo role switch | `[PB §7.1]` |
| 2 | Customer Dashboard | **Mandatory** | 7 numbered blocks, see §7.1 | `[PB §7.2]` `[IMG:Dashboard]` |
| 3 | Service Selection | **Mandatory** | All services incl. "Print portal – Coming soon" | `[PB §7.3]` |
| 4 | Package / Subscription Builder | **Mandatory** | Visualises the revenue model | `[PB §7.4]` |
| 5 | Campaign Request Flow | High | 5 steps + the 6 statuses | `[PB §7.5]` |
| 6 | Newsletter Overview | Medium | Planned/sent/draft, stats, approval status | `[PB §7.6]` |
| 7 | Scratch Game Overview | High | Key differentiator; participants, emails collected, prize, conversion | `[PB §7.7]` |
| 8 | Landing Page / Lead Gen | Medium | 5 page examples, views/signups/conversion/leads | `[PB §7.8]` |
| 10 | Campaign Reporting | **Wave 1 (demo depth)** | **Build natively — iframe rejected (L6).** See §8 | `[PB §7.10]` `[BIBLE]` |
| 11 | Admin Dashboard | **Wave 1** | KPIs + tables, see §7.2 | `[PB §7.11]` `[IMG:Part_2/Admin_Dshboard]` |
| 12 | Account Management | High | 10 fields, 5 actions | `[PB §7.12]` |
| 13 | Service / Package Management | Medium | Admin CRUD for services/packages | `[PB §7.13]` |
| 14 | White-Label Settings | **Critical for sales story** | See §9 | `[PB §7.14]` `[IMG:Part_2/White_Label_Portal]` |
| 15 | **Platform Settings** (was "Development / Settings") | **Wave 1** | Modules, integrations, system status, roadmap — Platform Owner view (L16) | `[PB §7.15]` |
| — | Notifications "Action Required" | Medium | Design-only screen, see §7.3 | `[IMG:Notifcations_Action quired]` |
| — | Public website / homepage | **Scope unclear — Q2** | Design-only | `[IMG:Homepage_Soruce_Vision]` |

### 7.1 Customer Dashboard — the 7 blocks
Brief and mockup agree exactly; the mockup even numbers them. `[PB §7.2]` `[IMG:Dashboard]`

1. **Active Marketing Package** — plan name, started date, renews date, "7 of 10 services used" progress bar (70%), `View package details`
2. **Available Services** — 8 service icons in a grid + `Request a service`
3. **Current Campaigns** — thumbnail, name, type, status chip, date range, `See all`
4. **Lead Generation Results** — total leads (428) split From Ads / From Landing Pages / From Newsletter, line chart, period filter
5. **Latest Newsletter Performance** — email preview, Open Rate 42.6%, Click Rate 12.3%, Conversions 28, each with delta
6. **Suggested Opportunity** — "Recommended" chip, pitch text, CTA button
7. **Recent Activity** — timestamped feed, `View all activity`

Customer top nav: `Dashboard` · `Marketing Services` ▾ · `My Packages` ▾ · `Content Library` · `Contact` · orange `Subscribe` · user menu. `[IMG:MENU_Marketing Serivices _ Plans _ PACKAGES]`
`My Packages` ▾ → `Marketing Packages`, `Marketing Plans`. `[IMG:MENU_...]`

### 7.2 Admin Dashboard
Brief blocks: total accounts, active subscriptions, open campaign requests, planned campaigns, MRR indicator, top performing services, accounts needing attention, recent activity. `[PB §7.11]`
Mockup (newer): KPIs Total Customers 348 / Active Campaigns 56 / Qualified Leads 1,286 / MRR €148,750, each with "% vs last week" + sparkline; then Recent Customers table, Subscriptions & Requests Overview, Recurring Revenue Overview donut by plan, Campaign Performance table, Lead & Request Pipeline. `[IMG:Part_2/Admin_Dshboard]`

**Two different admin sidebars exist** — use the newer `Part_2` structure (Dashboard, Customers, Campaigns, Subscriptions, Leads, Requests, Content Library, User Management, Reports, Settings). Open — Q1. `[TEAM]`

### 7.3 Notifications — "Action Required"
Panel from the bell icon: title, "4 items need your attention", `Mark all as read`, close. Each row = coloured icon + title + description + status chip (`Approval needed` / `Missing content` / `Deadline soon`) + action button (`Review` / `Upload` / `View`). Footer `View all actions →`. `[IMG:Notifcations_Action quired]`
This pairs naturally with the request/status logic in §6. `[TEAM]`

---

## 8. Campaign Reporting — RESOLVED: build natively, Wave 1, demo depth

> ✅ **DECISION LOCKED (register L6). The Meneer Online iframe is rejected.** Build the **Campaign Reporting Dashboard natively, on-brand, in English, with dummy data** — and it is now a **Wave 1** screen (pulled forward on 31 Aug, L14). Full record: [07-Scope-Review-and-Decisions-Sep-2026.md](../../documents/07-Scope-Review-and-Decisions-Sep-2026.md).
>
> **Why the iframe was rejected:** the Meneer Online dashboard is in Dutch, pulls **live** analytics (which breaks the dummy-data-only rule `[PB Rule 4]`), shows "Data niet beschikbaar" without connected accounts, and is off-brand. A native screen with consistent dummy numbers demos better and stays on-brand.

### What to build (Wave 1, demo depth) `[BIBLE]`
One dashboard page. Cross-channel results with internally-consistent dummy numbers: emails sent, open rate, click rate, leads generated, scratch participants, landing-page signups, best-performing campaigns (top 3), plus META / Google / website stats as separate stat tiles. Static charts — no live data, no real analytics accounts.

### Phase 2 note — do NOT quote a custom analytics engine yet
For the **future platform**, reporting is a **"Reporting Layer"**, and Blue Virtue has existing dashboard technology through its network. Their tech must be **assessed for reuse/integration before any custom analytics build is scoped or quoted** (open item **O9**). `[BV-SR]` `[OV-v2]`

### Historical reference — the original brief instruction (now superseded for the demo)
The brief `[PB §10]` originally asked to embed the Meneer Online dashboard via iframe (blank page, no header/footer, Source Vision colours, Ruben maintains it). That is retained only as background; the demo does **not** embed it. The old ambiguity about which screen the iframe belonged to is now moot. A 29 MB screen recording (`Dashboard_Screenrecording/Customer_Dashboard.mov`) remains unreviewed (Q7).

---

## 9. White-label configuration `[PB §7.14]` `[IMG:Part_2/White_Label_Portal]`

Brief fields: platform name, logo, brand colours, custom domain, email sender name, login page branding, module activation, language settings.

Mockup adds: favicon; primary/secondary/accent colour pickers; font family; header style (3 presets); login page style (4 presets); domain management with SSL state per domain; modules as on/off switches tagged **Core** or **Add-on**; roles with user counts; integrations with connection state; system status panel.

> The colour values shown there (`#2563EB`, `#0F172A`, `#10B981`) and font "Inter" are **sample values inside the form**, not the Source Vision brand palette. Do not copy them into the theme. `[TEAM]`

### Integration states to display `[PB §7.15]` `[IMG:Part_2/White_Label_Portal]`
`SendGrid` Active/Connected · `Google Analytics` Active/Connected · `Print.com API` Roadmap/In Progress · `Stripe` Connected · `HubSpot` Disabled · `CRM integration` Roadmap · `AI Campaign Assistant` Roadmap · `Payment integration` Roadmap

These are **display states only** — no real integration is built for the MVP. `[PB §5]` `[TEAM]`

---

## 10. Roles `[IMG:Part_2/White_Label_Portal]`

| Role | Access |
|---|---|
| System Administrator | Full access |
| Marketing Manager | Marketing & reports |
| Content Manager | Content & campaigns |
| Client | Limited access |
| Developer | System & settings |

Deliverable 10 is a **user role / access matrix** `[PB §17]` — build this list into it.

---

## 11. Dummy data rules `[PB Rule 4]`

**Only invented data.** No real customer, consumer, financial, email or login data.

Use the fake companies already in the mockups: `NovaWave` · `Lumina Studio` · `Vertex Labs` · `BrightPath Co.` · `Northpeak Digital` · `Orion Works` · `Maple & Co.` · `Elevate Partners` · `Green & Co.` `[IMG:Part_2/Admin_Dshboard]` `[IMG:Dashboard]`

Statuses seen: `Active` `Trial` `Past Due` `Subscribed`. Segments: `Enterprise` `Growth` `SMB`, and account types `Business account` / `Agency account`. `[IMG:Part_2/Admin_Dshboard]` `[IMG:Back-End Menu]`

Reference volumes for seeders: 348 customers, 312 active subscriptions, 56 active campaigns, 1,286 qualified leads, MRR €148,750, 23 pending requests, 34 renewals this month. `[IMG:Part_2/Admin_Dshboard]`

> **Never** seed real third-party brand names as customers or endorsements. The homepage mockup uses Cisco, Morgan Stanley, BNY, Moderna and Uber under "Trusted by leading companies" `[IMG:Homepage_Soruce_Vision]` — this breaks Rule 4 and implies false endorsement. Do not implement it; see Q11. `[TEAM]`

---

## 12. Reusable logic from the GRS Online project

> **These come from a DIFFERENT project** — `[GRS]` = `Documentation/GRS-Online-Module-Overview.docx`, the GRS Online garden-centre platform. Source Vision is built "from the existing value of the GRS Mailsystem and the GRS Marketing System" `[PB §Main Objective]`, so its proven logic is useful reference — but **nothing here is a Source Vision requirement until the client confirms it.**

### 12.1 Patterns worth copying
| Pattern | How it works in GRS | Apply to |
|---|---|---|
| **Autosave every change** | Each package toggle saves immediately, so nothing is lost mid-selection `[GRS §2]` | Package/Plan selection (Screen 4) |
| **Confirm → PDF → email** | Final confirm locks the selection, generates a PDF summary, emails it to admin `[GRS §2]` `[GRS §3]` | Package/Plan confirm, campaign request submit |
| **Auto-approve on timeout** | Ad content the customer never answers is auto-approved after two weeks, so work never stalls `[GRS §8]` | Campaign approval (`Waiting for approval`) |
| **Submit → email, don't provision** | Scratch-card opt-in emails admin instead of creating a live subscription `[GRS §7]` | Ideal demo shortcut for any "buy" action |
| **Auto-calculated total + recommended package** | Running totals and a suggested package based on the customer's own data `[GRS §3]` | Plan/package screens, "Suggested Opportunity" block |
| **Magic login link** | Personalised password-free login link per recipient, embedded in the email `[GRS §11]` | Explains `Generate Login` in `[IMG:Back-End Menu]` |
| **Draft vs finalized state** | Registration tracked as draft or finalized, reportable across years `[GRS §3]` `[GRS §12]` | Subscriptions / Registrations reporting |

### 12.2 GRS module → Source Vision screen map
| GRS module | Source Vision equivalent |
|---|---|
| 1. Manage Garden Center — master customer record, bulk spreadsheet import, resend login link `[GRS §1]` | Screen 12 Account Management `[PB §7.12]` — nearly the same field list |
| 2. Page 2 Subscription — package selection, autosave, confirm, PDF, renewal `[GRS §2]` | Screen 4 Package/Subscription Builder `[PB §7.4]` |
| 3. Page 1 Folders — per-item config, totals, recommendation `[GRS §3]` | Plan/package configuration UX |
| 4–6. CMS Management / Content Pages / Marketingmiddelen `[GRS §4-6]` | `CMS Management` + `Content Library` in `[IMG:Back-End Menu]` |
| 7. Separate Registration — scratch-card opt-in page `[GRS §7]` | Screen 7 Scratch Game `[PB §7.7]` |
| 8. Ad Content — review/comment/approve/reject workflow, auto-approve after 2 weeks `[GRS §8]` | §6 request/status logic + Notifications `[QP-7]` |
| 9. Planning Tool — quarterly campaign calendar, change requests, Excel import `[GRS §9]` | `Campaign Planning Tool` `[IMG:Back-End Menu]`, "Planned campaigns" `[PB §7.11]` |
| 10. Statistics — admin uploads per-channel data yearly `[GRS §10]` | Screen 10 Reporting — **but Source Vision pulls live via API, not manual upload** `[PB §10]`. Different approach |
| 11. Email Marketing — template library + assigned batches with content snapshot `[GRS §11]` | `Email Marketing` / `Email Templates` `[IMG:Back-End Menu]` `[IMG:Part_2/White_Label_Portal]` |
| 12. Subscribers Overview — cross-year registration report, Excel/CSV export, re-download PDF `[GRS §12]` | `Registrations` `[IMG:Back-End Menu]`, "Active subscriptions" `[PB §7.11]` |
| 13. Admin Dashboard — 4 counters + 3 mini reports `[GRS §13]` | Screen 11 Admin Dashboard `[PB §7.11]` |

### 12.3 What NOT to copy
The GRS document records that the single most important goal for its Marketingmiddelen module today is to **stop content being accidentally destroyed on save** `[GRS §6]` — i.e. GRS has a known data-loss bug.
If we reuse GRS logic, we must not reuse this weakness. Always write save logic that cannot wipe existing content. `[TEAM]`

---

## 13. Deliverables due by beginning of September `[PB §17]`

Development: working demo environment · Customer Portal · Admin Portal · Platform Settings (Platform Owner)
Documentation: technical overview · user role/access matrix · roadmap overview · feature overview for buyers
Sales (owner to confirm — Q8): demo storyline · product demo script · updated Acquire listing copy · screenshot set

---

## 14. Functionality checklist before finishing any task

- [ ] `check-sources.sh` reported OK
- [ ] Task passes the "helps a buyer understand value faster?" test `[PB §2]`
- [ ] Nothing built from the out-of-scope list `[PB §5]`
- [ ] All data is dummy; no real brands or personal data `[PB Rule 4]`
- [ ] Prices/labels/names come from config or seeder, never hardcoded `[DH §6]`
- [ ] Statuses use exactly the 6 canonical names `[PB §7.5]`
- [ ] Request/status logic used instead of a bare toggle `[QP-7]`
- [ ] Reporting screen is **built natively** with dummy data — the Meneer iframe is rejected (L6)
- [ ] Third portal is called **Platform Settings**, never "Developer/Development" (L16)
- [ ] Plan/package pricing carries the "example configuration" label (L17)
- [ ] Every new component logged in the Development & IP Register (L25)
- [ ] Anything derived from `[GRS]` is marked as such and flagged for confirmation
- [ ] New ambiguity added to [02-Open-Questions.md](../../documents/02-Open-Questions.md)

---

## 15. Maintaining this skill

Trigger to update: `check-sources.sh` reports drift, OR a client answer arrives, OR new files are delivered.
Procedure: [04-Skill-Update-Rules.md](../../documents/04-Skill-Update-Rules.md)

| Version | Date | Based on | Change |
|---|---|---|---|
| 1.0 | 2026-08-12 | 11-Aug ZIP snapshot + GRS overview | First version. Built from `[PB]`, `[QP]`, `[DH]`, `[GRS]` and 17 design images |
| 1.1 | 2026-09-02 | Blue Virtue Scope Review 31 Aug `[BV-SR]` + MVP/Overview v2 `[MVP-v2]` `[OV-v2]` + Decision Log/Bible | Wave 1 re-ordered to the 10-min storyline; Campaign Request, Scratch Game and Reporting pulled into Wave 1; "Development/Settings Portal" → **Platform Settings**; Campaign Reporting **built natively** (Meneer iframe rejected, L6); pricing framed as example monetisation (L17); Development & IP Register from day 1 (L25). See [07-Scope-Review-and-Decisions-Sep-2026.md](../../documents/07-Scope-Review-and-Decisions-Sep-2026.md) |
