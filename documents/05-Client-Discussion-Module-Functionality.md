# Source Vision — Module & Functionality Companion

**Version:** 2.0 (reconciled) · **Date:** 12 August 2026
**Prepared by:** Development team (NexusLink)
**Status:** Ready for the discussion meeting

> ### What this document is, and what it is not
>
> This is a **companion** to the two documents already issued to Blue Virtue on 12 August 2026:
> **Execution Plan v1.0** (24 pages) and **Open Decisions & Blockers** (26 items, answers due Friday 14 August).
>
> Those two documents own the **plan, the dates, the capacity options and the decisions register**. This document does not repeat them and does not invent a second set of question numbers.
>
> What this document adds is the one thing they do not carry: **submodule-level functionality detail**, and **where each piece of functionality comes from in the older GRS Online system**.
>
> Every open item below is referenced by its **existing register ID** (S1–S8, C1–C8, D1–D5, X1–X5). Only four genuinely new items are raised, and they are marked **NEW**.

---

## How to read the tables

| Mark | Meaning |
|---|---|
| **[C]** | **Confirmed** — written in a client document, or settled by the Execution Plan |
| **[A]** | **Assumption** — our reading. Needs your OK |
| **[D:id]** | **Decision needed** — already in the register under that ID |
| **[G]** | **From GRS Online** — the older project. Confirm reuse in Part D |
| **NEW** | Not in the register. Raised here for the first time |

**Source marks:** `[PB §n]` Project Brief · `[DH §n]` Development Handover · `[QP-n]` Pitch slide · `[IMG:x]` design screen · `[GRS §n]` **GRS Online Module Overview (other project)** · `[EP §n]` Execution Plan v1.0 · `[REG id]` Open Decisions register · `[TEAM]` our own view.

---

# PART A — Your two questions

## A1. "Will the design be provided by Blue Virtue?"

**Yes, and it is contractual in the brief.** `[PB §2]` assigns Blue Virtue "the design direction, visual styling, UX structure, branding, interface look & feel, and sales presentation layer", and every screen in §7 of the brief is marked *"Point of action: Design by Blue Virtue"*. `[EP §2.2]` restates the same split.

It is also now a standing project rule on our side: **we follow Blue Virtue's guide and never invent design.** Where something visual is unspecified we use the nearest documented rule, mark it as an assumption and ask.

**What they have already supplied:** the Development Handover (colours, typography, buttons, logo, direction), 17 screen designs, the design feedback slide `[QP-7]`, and the brand assets including the Space Grotesk font files.

**Four gaps remain, and all four are already in the register:**

| Gap | Detail | Register ID |
|---|---|---|
| **Un-drawn screens** | Roughly half of Wave 1 and Wave 2 has no mockup. In Wave 1 specifically, **Login has no design** and **Marketing Services catalogue has no design**, and **White-Label configuration is only partly designed** `[EP §6.1]` | **D4** — design cut-off proposed Wed 20 Aug |
| **Missing token values** | The light-grey steps, border colour, corner radius and spacing scale are not published anywhere in the handover | **D2** — we extract them and publish a token sheet for approval within 24 hours |
| **Navy gradient** | Supplied only as a flattened image, not as colour stops | **D3** — we sample it from the image and confirm on the token sheet |
| **Design freeze** | The handover itself says features, labels, pricing and behaviour may still change `[DH §6]` | **D4** — after the cut-off, later design becomes a change request |

**One question we would still add** `[TEAM]`: is there a **Figma or other source design file**? We currently have a Word document and flat images, so exact spacing and state colours have to be measured from screenshots. A source file would remove that guesswork and speed up Stage 1.

---

## A2. "For front website, we have to think for …"

> **This question is incomplete in your notes file** (`document`) — the sentence stops at "we have to think for". Please complete it and we will extend this section. Below is what we believe you meant, together with what the Execution Plan has already settled.

### Already settled

| Point | Position |
|---|---|
| **Is the public site in scope?** | **Yes.** "Public Homepage" is **Wave 1, screen 2** — one of the nine protected screens `[EP §6.1]` |
| **How much of it?** | The homepage only in Wave 1. The **Service Landing Page template (×8)** is **Wave 2** `[EP §6.2]` |
| **Why it matters** | `[EP §8]` step 1: the homepage is "the first ten seconds. It must read as a funded product" |
| **Real company logos** | Replaced with neutral placeholders in Stage 5 unless written permission exists | **C5** |
| **Invented statistics** | Kept as illustrative demo copy, noted internally as placeholders, not audited figures | **C6** |
| **Content editable by the client?** | **No CMS in Phase 1.** Content lives in the page components and the demo-data file. GRS solved this with a CMS Management module `[GRS §4]` `[GRS §5]`; that is a Phase 2 or roadmap conversation |
| **Language** | **English only** `[EP §13]` |
| **Hosting / protection** | NexusLink hosts; HTTP basic authentication from the first deployment so the demo is not indexable before the Acquire relisting | **S7, S8** |

### Still worth deciding

| # | Point | Our recommendation |
|---|---|---|
| 1 | **Does the public site get white-labelled too?** If a buyer rebrands the platform, does the marketing site rebrand with it? This affects whether the homepage reads its brand from the token layer or has content baked in | Build the homepage reading the **same tokens** as the portal, so it re-skins with the platform. Costs almost nothing now and strengthens the white-label story |
| 2 | **Contact and "Request Support" destinations.** The public pages have working-looking buttons | Show a **success state** and send nothing. `[EP §9]` lists form success states as a very-low-effort enhancement, and GRS used exactly this submit-to-email-only pattern `[GRS §7]` |
| 3 | **SEO / meta tags** | Not needed for a password-protected demo. Roadmap |
| 4 | **Cookie / privacy notice** | Not needed while the demo is behind basic auth. Becomes real if the site is ever made public |

---

# PART B — A change to the delivery model you should know about

`[EP §3.1]` specified **static HTML** for Phase 1, with Laravel and Vue as a separately quoted Phase 2 `[EP §3.2]` `[EP §13]`.

**That has changed by instruction.** The demo will now be built directly on the current stack — **Laravel 13.25, Inertia 3, Vue 3.5, Tailwind 4, Vite 8** — running in "demo mode": **no database, no migrations, no models and no real authentication**, with every figure coming from one shared demo-data file.

### Why this still meets the Plan's intent

| The Plan wanted | Still true |
|---|---|
| No backend, no database | No database, no migrations, no models, no auth tables |
| One shared demo-data file so no two screens contradict each other | Kept — and now structural rather than a review step |
| Forms and toggles visual, numbers fixed | Kept |
| Late design and copy changes cost minutes | Kept |
| Structure that mirrors the future component tree | **Improved** — they *are* the future components |
| One token sheet driving both phases | Kept — Tailwind `@theme` compiles to CSS custom properties |

The stage sequence, the gates and the milestone dates are **unchanged**.

### What this changes for you

1. **Nothing is thrown away.** Phase 1 is now literally Phase 2's code, so the conversion step disappears.
2. **Live white-label re-theming gets cheaper** — the enhancement `[EP §9]` ranks first and calls "the single sentence the entire asset is sold on".
3. **Hosting needs PHP**, not a static host. Register default **S7** already has NexusLink hosting, so nothing changes in practice.
4. **Execution Plan v1.0 §3.1, §3.2 and §13 are now out of date**, and so is the Laravel 11 / PHP 8.2 Phase 2 target — it is Laravel 13 / PHP 8.3+. **That document should be reissued before the client relies on it.**
5. **This does not close the capacity gap.** `[EP §4.2]` puts Wave 1 at 124–170 hours against 66–78 available with one developer. **Item S2 still needs an answer.**

Full reasoning: [06-MVP-Build-Approach.md](06-MVP-Build-Approach.md)

---

# PART C — Modules and submodules, by wave

Structured to match `[EP §6]`. Please confirm the Wave 1 list under **S1**.

---

## WAVE 1 — the protected commitment · nine screens · live 1 September

### W1-1 · Login + demo role switcher — Entry layer · **no design** `[EP §6.1]`

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| Login screen | Branded page: logo, professional SaaS framing, email and password fields, login button. Posts nowhere in Phase 1 | `[PB §7.1]` | — | **[C]** Needs design — **D4** |
| Demo role switcher | Switch between Customer / Admin / Developer with no separate logins, so a presenter moves through the walkthrough quickly. Role held in the session | `[PB §7.1]` `[EP §8]` | — | **[C]** |
| Password reset | Not required — the login is non-functional and buyers never get hands-on logins `[EP §13]` | — | — | **[C]** Resolved |
| Generated login link | Password-free magic link per recipient. Appears as "Generate Login" in the older admin menu | `[IMG:Back-End Menu]` | `[GRS §11]` | **[G]** Wave 3 at the earliest |

### W1-2 · Public Homepage — Marketing layer · designed

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| Hero | "Everything you need to market smarter and grow faster", subtext, "Explore our packages" and "How it works" actions, stacked image cards with a ~100,000 figure overlay | `[IMG:Homepage_Soruce_Vision]` | — | **[C]** |
| Trusted-by row | Currently Cisco, Morgan Stanley, BNY, Moderna, Uber | `[IMG:Homepage_Soruce_Vision]` | — | **[D:C5]** Replace with neutral placeholders |
| Feature grid | 6 cards: Email & Newsletter, Scratch Game, Marketing Plans, Marketing Packages, Landing Pages, Campaign Support | `[IMG:Homepage_Soruce_Vision]` | — | **[C]** |
| Insight band | Dark branded band: "Make smarter decisions with real-time insights", 2.4M+ campaigns, 8.7K+ businesses, 98% satisfaction | `[IMG:Homepage_Soruce_Vision]` | — | **[D:C6]** Illustrative only |
| Closing CTA | "Start building better marketing today", "Explore our packages" + "Contact sales" | `[IMG:Homepage_Soruce_Vision]` | — | **[C]** |
| Public header | Logo, both mega-menus, orange Subscribe, user menu | `[IMG:Menu_Source Vision_Frontend]` | — | **[C]** Built in Stage 2 |

### W1-3 · Customer Dashboard — the key screen · designed

Seven numbered blocks; brief and design agree exactly `[PB §7.2]` `[IMG:Dashboard]`.

| # | Submodule | Functionality in detail | GRS | Status |
|---|---|---|---|---|
| 1 | Active Marketing Package | Plan name ("Growth Plan"), started date, renews date, usage bar "7 of 10 services used — 70%", "View package details" | — | **[C]** |
| 2 | Available Services | Grid of 8 service tiles, "See all", blue "Request a service" | `[GRS §2]` | **[C]** Request/status chips here — **D5** |
| 3 | Current Campaigns | Thumbnail, name, type, status chip (Active / Scheduled / Completed), date range, "See all" | `[GRS §9]` | **[C]** |
| 4 | Lead Generation Results | 428 total leads, split From Ads / From Landing Pages / From Newsletter, trend line chart, period filter, "+24% vs last month" | — | **[C]** |
| 5 | Latest Newsletter Performance | Preview image, Open Rate 42.6%, Click Rate 12.3%, Conversions 28, deltas, "See full report" | `[GRS §11]` | **[C]** |
| 6 | Suggested Opportunity | "Recommended" chip, headline, body, "Launch Google Ads Campaign". **Fixed content in Phase 1** | `[GRS §3]` | **[C]** Resolved — static |
| 7 | Recent Activity | Timestamped feed, "View all activity" | — | **[C]** |

### W1-4 · Marketing Services catalogue — **no design** `[EP §6.1]`

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| The 8 services | Newsletter · Scratch Game · Product Promotion Email · Landing Page · Custom Campaign Support · Social Media Advertising · Google Advertising · TikTok Ads | `[IMG:MENU_...]` | — | **[C]** |
| Catalogue behaviour | Presentation only, **no price** — the catalogue answers "what can this platform do?" | `[EP §2.4]` `[EP §6.1]` | `[GRS §2]` | **[C]** |
| eMagazine | **Withdrawn.** Struck through everywhere in the brief; no package card, no menu entry. Recorded as a roadmap service | `[EP §11.2]` | `[GRS §10]` | **[D:C4]** Confirm withdrawal |
| Print portal | Show as "Coming soon" | `[PB §7.3]` | — | **[C]** |
| Service detail pages | 8 landing pages, hero + benefits + 4-step process + request CTA | `[IMG:Campaign customer journey]` | `[GRS §6]` | **[C]** **Wave 2** |

### W1-5 · Marketing Packages — 8 cards, €129–€849/month · designed

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| Package card | Per single service: "Price per month from €x", "Included services" list, optional add-ons with NO/YES toggles, "Get Started", monthly subscription total | `[IMG:Packages/Artboard 2..9]` | `[GRS §2]` | **[C]** |
| ON/OFF state | **Toggles stay here** — on a commercial card they read as "what I have" | `[EP]` | `[GRS §2]` | **[D:D5]** |
| All 8 card prices | Newsletter €129 · Product Promotion Email €179 · Landing Page €249 · Custom Campaign Support €299 · Scratch Game €334 · Social Media Advertising €549 · Google Advertising €549 · TikTok Advertising €849. Range matches the €129–€849 in `[EP §6.1]` exactly | all 8 artboards read | — | **[C]** **NEW-1 now closed** — all eight read from the artboards. Full inclusion lists in document 00 §1.1 |
| Card content issues | Newsletter add-ons are garden-centre specific ("pet newsletter", "barbecue newsletter"); Scratch Game includes printed POS material and mixes yearly counts with a monthly price; Social Media and Google are both €549; reporting cadence differs across the three ad packages | all 8 artboards read | `[GRS]` legacy wording | **NEW-5** See document 00 questions 36–41 |
| Autosave each change | Every toggle saves immediately so nothing is lost mid-selection | — | `[GRS §2]` | **[G]** Phase 2 — no persistence in Phase 1 |
| Confirm → PDF → email | Final confirm locks the selection, generates a PDF summary, emails admin | — | `[GRS §2]` `[GRS §3]` | **[G]** Phase 2. Strong demo moment |
| Running total | Live recalculation as add-ons toggle | — | `[GRS §3]` | **[C]** `[EP §9]` enhancement, low effort |

### W1-6 · Marketing Plans — 5 tiers, €199–€1,299/month · designed

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| The 5 tiers | Starter €199 · Growth €349 · Full Service €699 · Franchise €999 · Agency €1,299 | `[IMG:Marketing_Plans]` `[PB §7.4]` | `[GRS §2]` | **[C]** |
| Franchise price conflict | €999 on Marketing Plans, €1,049 on Upgrade | `[IMG:*]` | — | **[D:C1]** Adopt €999, correct the Upgrade screen |
| Plan card | Navy hero, uppercase plan name, description, price, inclusion list, priced add-ons, upgrade note, ACTIVE/INACTIVE | `[IMG:Marketing_Plans]` | — | **[C]** |
| Add-on pricing | Add-ons cheaper than the standalone package — Google Ads €79 vs €549; Custom Campaign Support €99 vs €299 | `[IMG:*]` | — | **[D:C2]** Intentional bundling discount |
| Taxonomy | **Services / Packages / Plans** — three words, used consistently. Five customer-facing plan names everywhere; admin dummy data rewritten to match | `[QP-7]` `[EP §2.4]` | — | **[D:C3]** Critical — touches 5 screens |
| Upgrade Your Plan | Current plan banner + 4 upgrade cards + "billed monthly, cancel anytime" | `[IMG:Upgrade ur plan]` | — | **[C]** **Wave 2** |

### W1-7 · Admin Dashboard — designed

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| KPI cards | Total Customers 348 · Active Campaigns 56 · Qualified Leads 1,286 · MRR €148,750 — each with "% vs last week" and a sparkline | `[IMG:Part_2/Admin_Dshboard]` | `[GRS §13]` 4 counters | **[C]** |
| Recent Customers | Company, Segment, Subscription, Status, Last Activity, Renewal Date, row menu, pagination | `[IMG:Part_2/Admin_Dshboard]` | `[GRS §13]` | **[C]** |
| Subscriptions & Requests | Active Subscriptions 312 · Pending Requests 23 · New Today 18 · Renewals This Month 34 · System Status | `[IMG:Part_2/Admin_Dshboard]` | — | **[C]** |
| Recurring Revenue | Donut of MRR by plan with amounts and percentages | `[IMG:Part_2/Admin_Dshboard]` | `[GRS §13]` | **[C]** |
| Campaign Performance | Campaign, Client, Status, Leads, Revenue | `[IMG:Part_2/Admin_Dshboard]` | — | **[C]** |
| Lead & Request Pipeline | Available / Requested / Active / Completed with count and value | `[IMG:Part_2/Admin_Dshboard]` | — | **[C]** |
| Segment naming | Admin shows Enterprise / Growth / Professional / Basic / Trial; customer side shows the five plan names | `[IMG:*]` | — | **[D:C3]** Rewrite admin data to the five names |
| Admin sidebar | Dashboard · Customers · Campaigns · Subscriptions · Leads · Requests · Content Library · User Management · Reports · Settings | `[IMG:Part_2/Admin_Dshboard]` | — | **[C]** Older GRS-style menu dropped — **S5** |

### W1-8 · Development / Settings Portal overview — designed

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| Active vs future modules | What is owned today against what is on the roadmap | `[PB §7.15]` | — | **[C]** |
| Integration status | SendGrid Connected · Google Analytics Connected · Print.com In Progress · Stripe Connected · HubSpot Disabled; plus CRM, AI Campaign Assistant, Payment as Roadmap | `[PB §7.15]` `[IMG:White_Label_Portal]` | — | **[C]** Display only `[PB §5]` |
| Email delivery status | Delivery health indicator | `[PB §7.15]` | `[GRS §11]` | **[C]** |
| System status | System Health, PHP version, Database, Server, Environment, Last Backup | `[IMG:White_Label_Portal]` | — | **[C]** Static values in Phase 1 |
| Roadmap overview | Everything cut from Wave 1 appears here as a roadmap entry, including Campaign Planning Tool, Email Marketing and CMS Management | `[EP §2.4]` | `[GRS §4]` `[GRS §9]` `[GRS §11]` | **[D:S5]** |
| Module counter | "Active Modules 12 / 16" — only 5 are visible in the design | `[IMG:White_Label_Portal]` | — | **NEW-2** Please supply the full list of 16 |

### W1-9 · White-Label configuration — **partly designed** `[EP §6.1]`

The brief calls this "critical for the sales story" `[PB §7.14]`.

| Submodule | Functionality in detail | Source | GRS | Status |
|---|---|---|---|---|
| Brief's field list | Platform name, logo, brand colours, custom domain, email sender name, login page branding, module activation, language settings | `[PB §7.14]` | — | **[C]** |
| Logo + favicon upload | Both | `[IMG:White_Label_Portal]` | `[GRS §1]` | **[C]** |
| Colour pickers | Primary / Secondary / Accent with hex fields | `[IMG:White_Label_Portal]` | — | **[C]** |
| Font family | Interface font selector. The mockup shows "Inter" | `[IMG:White_Label_Portal]` | — | **[D:D1]** Space Grotesk is the answer; Inter is a leftover |
| Header style | 3 presets | `[IMG:White_Label_Portal]` | — | **[C]** |
| Login page style | 4 presets | `[IMG:White_Label_Portal]` | — | **[C]** |
| **Live re-theming** | Changing the colour fields re-skins the whole platform in front of the buyer | `[EP §9]` | — | **[D:S4]** Ranked **first** among enhancements. Cheap on our stack. **We recommend taking it** |
| Live preview panel | Preview of the branded result | `[EP Stage 4]` | — | **[C]** |
| Language settings | **English only in Phase 1** | `[EP §13]` | — | **[C]** Resolved |
| Domain management | Primary + additional domains, SSL state per domain, "Add New Domain". Design shows `app.sourcevision.com`, `sourcevision.com`, `staging.sourcevision.com` | `[IMG:White_Label_Portal]` | — | **[D:S7]** Are these the real domains? |

---

## WAVE 2 — 2–15 September · 40–55 h `[EP §6.2]`

| Screen | Key functionality | GRS | Status |
|---|---|---|---|
| **Campaign Request Flow + My Requests** | 5 steps: campaign type → goal → briefing → file upload → submit. **Six statuses, exactly these names:** New request · In progress · Waiting for input · Waiting for approval · Scheduled · Completed | `[GRS §8]` review/comment/approve workflow | **[C]** `[PB §7.5]` |
| **Campaign Reporting Dashboard** | Emails sent, open rate, click-through, leads, Scratch Game participants, landing page signups, best campaigns, META / Google / Website stats | `[GRS §10]` — but GRS uploaded data manually | **[D:S6]** **Conflict.** Brief says embed the Meneer Online iframe `[PB §10]`; `[EP §11.2]` recommends building it natively in English and roadmapping the iframe. **Not building either until this is answered** |
| **Notifications — Action Required** | Bell + red count. Panel: "4 items need your attention", "Mark all as read". Each row: coloured icon, title, description, status chip (Approval needed / Missing content / Deadline soon), action button (Review / Upload / View), "View all actions →" | `[GRS §8]` approval checkpoints | **[C]** Working panel is a very-low-effort enhancement `[EP §9]` |
| **Service Landing Page template (×8)** | Hero, description, benefits, 4-step process, request CTA — one per service | `[GRS §6]` | **[C]** |
| **Upgrade Your Plan** | Current plan banner, 4 upgrade cards, monthly billing note | — | **[C]** |
| **Scratch Game Overview** | Active campaigns, example campaign, participants, emails collected, prize setup, conversion rate, status. **Overview screen only — the game itself is not playable in the MVP** | `[GRS §7]` Krasactie, incl. the public opt-in page that emails admin | **[C]** Resolved — overview only |
| **Landing Page / Lead-Gen Overview** | 5 page examples; page views, signups, conversion rate, leads collected, connected campaign. **Overview screen only** | — | **[C]** Resolved — overview only |

---

## WAVE 3 — 16–30 September · 45–60 h `[EP §6.3]`

| Screen | Key functionality | GRS | Status |
|---|---|---|---|
| **Newsletter Overview** | Planned / sent / draft lists, approval status, send date, audience; stats: emails sent, open rate, click rate, unsubscribes, leads. Uses **cleaned GRS Mailsystem screenshots** as proof of the email heritage | `[GRS §11]` | **[C]** ⚠ See the GRS access warning below |
| **Admin Customers** | Company name, contact person, email, phone, website, logo, brand colours, selected services, subscription type, status. Create / edit / assign services / campaign history / activity | `[GRS §1]` near-identical fields, plus bulk spreadsheet import, activate-deactivate, resend login link | **[C]** + **[G]** |
| **Admin Subscriptions + Plans & Pricing** | Who registered for what and when, finalised vs draft. Service and package management: name, description, price, included-in-package, add-on, active/inactive | `[GRS §12]` cross-year report, Excel/CSV export, re-download PDF; `[GRS §2]` renewals | **[C]** + **[G]** |
| **Admin Requests** | All requests filtered by the six statuses; assign, progress, request input | `[GRS §8]` | **[C]** |
| — Request Types | Configure what kinds of request exist. Not described anywhere | — | **NEW-3** What are the request types? |
| **Admin Leads** | All leads, lead sources (ads / landing pages / newsletter / scratch game), pipeline stages | — | **[C]** |
| **Admin Campaigns** | Campaigns across all customers; prepare draft ad content; review customer feedback | `[GRS §8]` Excel upload of draft content, comment thread, **auto-approve after two weeks**; `[GRS §9]` quarterly calendar with budgets and change requests | **[C]** + **[G]** |
| **User Management + role matrix** | Users; roles: System Administrator (full) · Marketing Manager (marketing & reports) · Content Manager (content & campaigns) · Client (limited) · Developer (system & settings) | `[GRS §1]` | **[C]** Feeds the role/access matrix deliverable |
| **Content Library** | Requested in the menu `[QP-7]`, present in the newer designs — but **no design and no description of what is inside it** | `[GRS §6]` content, testimonials, packages info | **NEW-4** What goes in it? Downloads, campaign assets, brand files, past newsletters? |
| **Contact** | Page content and behaviour unspecified | `[GRS §5]` Contact page editor | **[C]** Success state, sends nothing |
| **My Account** | Profile area implied by the user menu | — | **[C]** |
| **Dev Portal sub-screens** | Domains · Modules · Roles · Integrations · Email Templates · System Status · Audit Logs · API & Webhooks | `[GRS §11]` template library | **[C]** Display only |

> ⚠ **Register item X4 — read carefully before anyone touches GRS.**
> The GRS Mailsystem at `grsonline.nl` is **outdated but still live, and still collecting real email addresses** through the scratch game and landing-page capture.
> **Treat it as strictly read-only. No changes of any kind.** Reference screenshots only, and only after all real recipient data has been removed. Phase 1 needs no access to either GRS system beyond screenshots.

---

# PART D — GRS Online reuse · confirm each

> **GRS Online is a different, older project** — a platform for garden centres. Source is `GRS-Online-Module-Overview.docx`, 13 modules. We studied it because the brief says Source Vision is built "from the existing value of the GRS Mailsystem and the GRS Marketing System" `[PB §Main Objective]`.
> **Nothing here is a Source Vision requirement until you confirm it.**

We checked **all 13 modules**.

| GRS module | What it does there | Where it lands here | Wave | Reuse? |
|---|---|---|---|---|
| 1. Manage Garden Center | Master customer record: details, credentials, size, active/inactive, branding. Bulk spreadsheet import. Resend login link | Admin Customers — nearly the same field list as `[PB §7.12]` | 3 | ☐ Yes ☐ No |
| 2. Page 2 Subscription | Yearly package selection: toggle on/off, **autosave each change**, confirm locks it, generates **PDF**, emails admin, admin-driven renewal | Marketing Packages + Plans | 1 / Ph2 | ☐ Yes ☐ No |
| 3. Page 1 Folders | Up to 18 configurable items each with on/off, size, add-ons. **Auto-calculated totals and a recommended package** | Running total on plan cards; Suggested Opportunity block | 1 | ☐ Yes ☐ No |
| 4. CMS Management | Registry of which content pages exist per year and segment; drives the front-end menu centrally | Roadmap module in the Development Portal — **S5** | Roadmap | ☐ Yes ☐ No |
| 5. CMS Content Pages | Five simple one-page editors: title, description, banner image | Contact; public pages if ever made editable | 3 | ☐ Yes ☐ No |
| 6. Marketingmiddelen | Yearly content editor for a marketing page and subpages, per account type, with testimonials | Service landing pages; Content Library | 2 / 3 | ☐ Yes ☐ No |
| 7. Separate Registration | Public sign-up for the **Krasactie** scratch-card add-on: promo content, opt-in, calculated price, submit → **emails admin instead of activating** | Scratch Game, and the general submit-by-email demo shortcut | 2 | ☐ Yes ☐ No |
| 8. Ad Content | Monthly ad approval: staff upload draft content for Facebook/Google/TikTok, customer comments and approves or rejects each item and uploads media, **auto-approved after two weeks** | Campaign Request Flow + Notifications — this is the request/status logic `[QP-7]` asked for | 2 | ☐ Yes ☐ No |
| 9. Planning Tool | Quarterly campaign calendar with date ranges, budgets, colour-coded categories; customer date-change requests; admin bulk Excel import | Roadmap module — **S5**. Also "Planned campaigns" `[PB §7.11]` | Roadmap | ☐ Yes ☐ No |
| 10. Statistics | Admin uploads per-channel performance data per year; customer sees a dashboard | Campaign Reporting — **but the approach differs.** See **S6** | 2 | ☐ Yes ☐ No |
| 11. Email Marketing | Template library + assign-to-customers batches with a content snapshot and a **magic login link per recipient**; history; unsubscribe | Roadmap module — **S5**. Email Templates sub-screen | Roadmap / 3 | ☐ Yes ☐ No |
| 12. Subscribers Overview | Cross-year report of registrations, finalised vs draft, Excel/CSV export, re-download PDF | Admin Subscriptions | 3 | ☐ Yes ☐ No |
| 13. Admin Dashboard | 4 quick counters + 3 mini reports | Admin Dashboard — the older mockup is exactly this shape | 1 | ☐ Yes ☐ No |

## The five patterns most worth reusing `[TEAM]`

| # | Pattern | Why it is valuable here | Phase |
|---|---|---|---|
| 1 | **Autosave every change** `[GRS §2]` | Nothing lost mid-selection; looks polished | Phase 2 |
| 2 | **Confirm → PDF → email** `[GRS §2]` `[GRS §3]` | Gives a buyer a tangible record of a sale — a strong demo moment | Phase 2 |
| 3 | **Auto-approve after a timeout** `[GRS §8]` | Work never stalls waiting for a customer | Phase 2 |
| 4 | **Submit → email admin, never auto-provision** `[GRS §7]` | Ideal for a demo: looks complete, almost no backend | **Phase 1** |
| 5 | **Magic login link** `[GRS §11]` | Removes the password barrier when showing buyers around | Phase 2 |

## One thing we will not copy

The GRS document records that the "single most important goal" for its Marketingmiddelen module today is to **stop content being accidentally destroyed on save** `[GRS §6]` — a known data-loss bug. Any reused logic will be written so it cannot wipe existing content. `[TEAM]`

---

# PART E — The four genuinely new items

Everything else we found is already covered by the 26-item register. These four are not.

| # | Item | Why it matters | Related |
|---|---|---|---|
| **NEW-1** | ~~The full 8-card Marketing Packages list.~~ **CLOSED.** All eight artboards have now been read: Newsletter €129, Product Promotion Email €179, Landing Page €249, Custom Campaign Support €299, Scratch Game €334, Social Media Advertising €549, Google Advertising €549, TikTok Advertising €849. The range matches €129–€849 exactly, and each card's inclusion list is recorded in document 00 §1.1 | Wave 1 screen 5 can now be built without guessing | **C7** — still confirm the plan overview |
| **NEW-5** | **Six content issues on the package cards.** The Newsletter add-ons are garden-centre wording ("4x pet newsletter", "4x barbecue newsletter"); the Scratch Game card includes printed point-of-sale material and describes campaigns per **year** while charging per **month**; Social Media and Google are both €549; reporting is quarterly on two ad cards but monthly on the third; two cards have no add-ons at all | These are the cards a buyer studies most closely on the revenue screen | See document 00 questions 36–41 |
| **NEW-2** | **The complete list of 16 modules.** The white-label screen shows "Active Modules 12 / 16" but only 5 are visible | The module activation panel is part of Wave 1 screen 9 | — |
| **NEW-3** | **What are the "Request Types"?** An admin submodule with no description anywhere | Wave 3, low urgency | — |
| **NEW-4** | **What goes in the Content Library?** You asked for it in the menu `[QP-7]` and it appears in the newer designs, but there is no design and no description | It sits in both the customer and admin menus from Wave 1's shell onward, so we need at least a placeholder definition | — |

### And one question for you, not the client

**Complete your question A2** — "For front website, we have to think for …". We have prepared the section on our best reading, but the sentence stops mid-way.

---

# PART F — What to take into the meeting

The decisions all live in the existing register. This document does not add a parallel list.

## The six that cannot slip `[REG]`

| ID | Item | Our position |
|---|---|---|
| **S1** | Confirm the Wave 1 nine-screen list | Proceed as listed in `[EP §6.1]` |
| **S2** | Capacity — one developer, two developers, or a later date | **Unchanged by the stack decision.** Still needs an answer |
| **C3** | Reconcile the two plan vocabularies | Services / Packages / Plans; five customer-facing plan names everywhere |
| **C1** | Franchise plan price | €999, correct the Upgrade screen |
| **D4** | Design cut-off date | Wed 20 Aug |
| **X1** | MVP-phase working agreement | Signed before Stage 1 |

## Additional items we specifically want answered

| ID | Item | Why we are raising it here |
|---|---|---|
| **S6** | Reporting dashboard — iframe or native | A genuine conflict between the brief and the Execution Plan. We are building **neither** until it is settled |
| **S4** | Which optional enhancements | We recommend **live white-label re-theming** — ranked first, and cheap on the chosen stack |
| **C4** | Confirm eMagazine is withdrawn | Affects the service catalogue, package cards, menus and reporting |
| **C5 / C6** | Homepage logos and statistics | Commercial and legal exposure on the most public screen of the asset |
| **D2 / D3** | Token values and the navy gradient | Needed at Gate M1, Tue 18 Aug |
| **X4** | GRS read-only access | The live system is still collecting real email addresses. Please confirm read-only in writing |

## And one thing we must tell you

**Execution Plan v1.0 is now out of date on technology** — §3.1 (static HTML Phase 1), §3.2 and §13 (Laravel 11 / PHP 8.2 Phase 2). The build will use Laravel 13 / PHP 8.3+ from the start. **That document should be corrected before the client relies on it.** See Part B and [06-MVP-Build-Approach.md](06-MVP-Build-Approach.md).

---

## Sources used for this document

**Read in full:** Project Brief (18 sections) · Development Handover (6 sections) · Quick Feedback Pitch (10 slides + notes) · GRS Online Module Overview (13 modules) · Execution Plan v1.0 (24 pages) · Open Decisions & Blockers (9 pages, 26 items) · MVP Delivery Roadmap (2 pages) · 17 design images.

**Not read:** `Source_Vision_MVP_Summary.pdf` (4 pages) — it appears to condense the Execution Plan, which we have read in full. Tell us if it contains anything the Plan does not and we will read it. Also `Customer_Dashboard.mov` (29 MB) — no video tooling on this machine; please share key frames or a short written summary.
