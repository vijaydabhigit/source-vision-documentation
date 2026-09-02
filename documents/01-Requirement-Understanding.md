# Source Vision — Requirement Understanding (Simple Language)

**Document date:** 12 August 2026
**Written by:** Development team (Nexuslink)
**Language note:** This document is written in simple English so that every team member can read it easily.
**Status:** Draft for client confirmation. Please read [02-Open-Questions.md](02-Open-Questions.md) also.

---

## How to read the source marks

Every point in this document has a source mark in brackets. This tells you **from where** we got that information.
Never trust a line in this document that has no source mark.

| Mark | Meaning | Full file path |
|---|---|---|
| `[PB]` | Project Brief | `Documentation/11-Aug/.../02_Project briefings & understanding/Project Brief – Source Vision MVP - 140726.docx` |
| `[DH]` | Development Handover (design rules) | `Documentation/11-Aug/.../02_Project briefings & understanding/Source Vision – Development Handover.docx` |
| `[QP-n]` | Quick Feedback Pitch, slide number n | `Documentation/11-Aug/.../02_Project briefings & understanding/Source_Vision_Quick_Feedback_Pitch.pptx` |
| `[IMG:name]` | Design image (screen mockup) | `Documentation/11-Aug/.../03_Design & Templates/...` |
| `[GRS]` | **OTHER PROJECT** — GRS Online Module Overview | `Documentation/GRS-Online-Module-Overview.docx` |
| `[TEAM]` | Our own understanding / assumption. **Not** from client. Needs approval. | — |

> **Important:** `[GRS]` is a **different, older project** (GRS Online — garden centre platform).
> It is **not** Source Vision. We only study it to reuse some working ideas.
> Wherever you see `[GRS]`, that functionality comes from the other project and must be confirmed before we build it here.

---

## 1. What is Source Vision? (In one line)

Source Vision is a **white-label marketing platform**. One company buys it, puts their own logo and colours on it, and then sells marketing services to their own customers. `[PB §Main Objective]` `[QP-3]`

Who will buy it: agencies, franchise companies, retail chains, purchasing groups, and businesses with many branches. `[QP-3]`

---

## 2. Why are we building this? (Very important to understand)

This is the most important point of the whole project. Please read carefully.

The client is **selling a business asset** on a website called Acquire. `[PB §1 Background]`
Right now they are only selling the "GRS Mailsystem". But an email system alone looks small and cheap. `[PB §1]`

So the client wants to join two old systems — the **GRS Mailsystem** and the **GRS Marketing Platform** — and show them as one new, bigger product named **Source Vision**. `[PB §1]`
The purpose is to increase the **selling price** of the asset. `[PB §1]`

**So our real job is:** make a demo that makes a buyer say "this is a valuable platform, I will pay more for it". `[PB §2]`

**Our job is NOT:** to build a complete, finished SaaS product. `[PB §Main Objective]` `[PB §2]`

The client's own rule for this project is:

> **"Demo first. Product later."** `[PB §2]` `[QP-1]`

And the test for every single task is one question:

> **"Does this help a buyer understand the value of Source Vision faster?"**
> If yes → build it now. If no → put it in the roadmap list. `[PB §2]`

### What this means for us as developers

| Normal project | This project |
|---|---|
| Real data, real users | Dummy (fake) data only `[PB Rule 4]` |
| Full backend logic | Only enough logic to make the screen look real `[PB §4]` |
| Perfect architecture | Speed and looks are more important now `[PB §2]` |
| Every feature working | Some features can be shown as "Coming soon" `[PB §7.3]` |

Target date: **beginning of September** (demo ready). `[PB §Main Objective]` `[PB §17]`

---

## 3. Who does what

| Person / Company | Work | Source |
|---|---|---|
| **Blue Virtue** | Design, visual style, UX structure, branding, look & feel, sales presentation. **Their instruction/guide is the design authority — we follow it and never invent design.** See section 8.0 | `[PB §2]` |
| **Nexuslink (us)** | Technical development, platform structure, demo functionality, backend logic, user roles, MVP implementation | `[PB §2]` |
| **Madalina** | Design work — 4 to 8 hours per week | `[PB §3]` |
| **Sonny** | Direction — 4 to 8 hours per week | `[PB §3]` |
| **Jelle** | 4 hours per week | `[PB §3]` |
| **Ruben** | To be confirmed. Will maintain the embedded dashboard after integration | `[PB §3]` `[PB §10]` |
| **Meneer Online** | External partner. They own and host the customer analytics dashboard | `[PB §10]` |

**Developer time given in the brief:** about 30 hours per week, 1 developer, around 200 hours total over 1.5 months. `[PB §3]`
The brief itself writes "(please verify)" next to this. `[PB §3]`

---

## 4. The platform has 3 parts (portals)

The demo must clearly show three separate areas. `[PB §4]` `[QP-5]`

### 4.1 Customer Portal
This is for the **end customer** (for example, a shop owner who buys marketing services).
It sells the value of the platform. `[QP-5]`
Contains: customer dashboard, service selection, campaign requests, reports and leads. `[QP-5]`

### 4.2 Admin Portal
This is for the **buyer's own staff** (the agency or franchise head office).
It shows that one company can manage many customers from one place. `[QP-5]` `[PB §11]`
Contains: accounts, subscriptions, campaign activity, service requests. `[QP-5]`

### 4.3 Settings / Development Portal
This shows **white-label power** and technical readiness. `[QP-5]`
Contains: white-label setup, logo and colours, modules, roles, integrations. `[QP-5]`

---

## 5. The demo story (this is the flow we must show)

The client wants the demo to tell this story in a few minutes: `[QP-6]`

```
1. Create customer account
        ↓
2. Select plan or package
        ↓
3. Request marketing service
        ↓
4. Launch campaign
        ↓
5. Generate leads
        ↓
6. Report results
```

The money logic is simple: **platform access + recurring service packages + campaign add-ons**. `[QP-6]`

---

## 6. Very important: Services vs Packages vs Plans

The client's own pitch says this point is **not yet clear** and must be fixed:

> "Clarify Plans vs Packages vs Services" `[QP-7]`

From the design screens, this is what we understand today `[TEAM]`:

### 6.1 Marketing Services — the 8 basic items
These are the individual things a customer can get. The menu shows exactly 8: `[IMG:MENU_Marketing Serivices _ Plans _ PACKAGES]`

1. Newsletter
2. Scratch Game
3. Product Promotion Email
4. Landing Page
5. Custom Campaign Support
6. Social Media Advertising
7. Google Advertising
8. TikTok Ads

The Project Brief also lists **eMagazine** and **Print portal (Coming soon)** as services. `[PB §7.3]`
These two are **not** in the design menu. This is a gap — see question Q4.

### 6.2 Marketing Packages — one service sold alone, with its own price
Each service can be sold as its own package card, with an ON/OFF switch. `[IMG:Packages/Artboard 2..9]`

Examples from the design:
- Custom Campaign Support Package — **€299 / month** `[IMG:Packages/Artboard 2]`
- Google Advertising Package — **€549 / month** `[IMG:Packages/Artboard 9]`

Each package card shows: price per month, "Included services" list, optional add-ons with NO/YES switches, a "Get Started" button, and a monthly subscription total at the bottom. `[IMG:Packages/Artboard 2]`

### 6.3 Marketing Plans — many services bundled into one tier
These are the big bundles. Five plans exist in the design: `[IMG:Marketing_Plans]`

| Plan | Price / month | Included services |
|---|---|---|
| Starter Plan | €199 | Newsletter, Product Promotion Email |
| Growth Plan | €349 | Newsletter, Scratch Game, Landing Page |
| Full Service Plan | €699 | 7 services |
| Franchise Plan | €999 | 7 services |
| Agency Plan | €1,299 | 8 services |

Source: `[IMG:Marketing_Plans]`. The Project Brief lists the same five plan names. `[PB §7.4]`

Each plan card also shows: included services, optional add-ons with price, upgrade option, and an ACTIVE / INACTIVE switch. `[IMG:Marketing_Plans]` `[PB §7.4]`

### 6.4 Price problems we found (please see questions)
- **Franchise Plan** is **€999** on the Marketing Plans page `[IMG:Marketing_Plans]` but **€1,049** on the Upgrade page `[IMG:Upgrade ur plan]`. Two different prices for the same plan.
- **Google Advertising** costs **€549/month** as a standalone package `[IMG:Packages/Artboard 9]` but only **€79/month** as an add-on inside a plan `[IMG:Marketing_Plans]`.
- **Custom Campaign Support** costs **€299/month** as a package `[IMG:Packages/Artboard 2]` but **€99/month** as an add-on `[IMG:Marketing_Plans]`.

We will not guess these numbers. See Q5 in [02-Open-Questions.md](02-Open-Questions.md).

---

## 7. Screen by screen requirement

The Project Brief lists the screens. It says numbers **1, 2, 3, 4 are mandatory** and the rest still need to be decided. `[PB §7]`

### 7.1 Screen 1 — Login (MANDATORY) `[PB §7.1]`
- Source Vision logo and name
- Professional SaaS look
- Login option
- Optional: role selection, only for demo purpose (so we can switch between Customer / Admin / Developer quickly)

### 7.2 Screen 2 — Customer Dashboard (MANDATORY) `[PB §7.2]`
The brief calls this "one of the most important screens".
The design mockup numbers the blocks 1 to 7, and they match the brief exactly: `[IMG:Dashboard]`

| # | Block | What it shows in the design |
|---|---|---|
| 1 | Active Marketing Package | "Growth Plan", start date, renew date, progress bar "7 of 10 services used — 70%", button "View package details" |
| 2 | Available Services | 8 service icons in a grid + blue button "Request a service" |
| 3 | Current Campaigns | Campaign list with thumbnail, name, type, status chip (Active / Scheduled / Completed) and date range |
| 4 | Lead Generation Results | Big number "428 Total Leads", split by From Ads / From Landing Pages / From Newsletter, and a line chart |
| 5 | Latest Newsletter Performance | Email preview image, Open Rate 42.6%, Click Rate 12.3%, Conversions 28, each with up/down arrow |
| 6 | Suggested Opportunity | "Recommended" chip, suggestion text, button "Launch Google Ads Campaign" |
| 7 | Recent Activity | Time-wise activity list with date and time on the right |

Top menu in the design: Dashboard, Marketing, My Packages, Content Library, Contact, orange **Subscribe** button, user icon. `[IMG:Dashboard]`

### 7.3 Screen 3 — Service Selection (MANDATORY) `[PB §7.3]`
Show all services available to a customer. Brief list includes Newsletter package, Product promotion emails, Scratch Game, eMagazine, Landing pages, Custom campaign support, Social media ads, TikTok Ads, Google Ads, and Print portal marked "Coming soon". `[PB §7.3]`

### 7.4 Screen 4 — Package / Subscription Builder (MANDATORY) `[PB §7.4]`
The brief says this screen is "very important because it visualizes the revenue model".
Each package must show: included services, monthly or yearly price, optional add-ons, upgrade possibility, active/inactive status. `[PB §7.4]`

### 7.5 Screen 5 — Campaign Request Flow `[PB §7.5]`
Steps: choose campaign type → choose campaign goal → add briefing or remarks → upload files or images → submit request.

**Statuses required** (please note these 6, we must use exactly these names):
1. New request
2. In progress
3. Waiting for input
4. Waiting for approval
5. Scheduled
6. Completed

The design also shows a simpler 4-step public version: Select service → Share brief → Approve delivery → Track results. `[IMG:Campaign customer journey]`

### 7.6 Screen 6 — Newsletter Overview `[PB §7.6]`
Show planned / sent / draft newsletters, basic statistics, approval status, send date, audience list.
Statistics: emails sent, open rate, click rate, unsubscribes, leads generated.
Purpose: show the value that already exists in the old GRS Mailsystem. `[PB §7.6]`

### 7.7 Screen 7 — Scratch Game Overview `[PB §7.7]`
The brief calls this "a key differentiator compared to standard email platforms".
Show: active Scratch Game campaigns, example campaign, number of participants, collected email addresses, prize/reward setup, conversion rate, campaign status.

### 7.8 Screen 8 — Landing Page / Lead Generation Overview `[PB §7.8]`
Examples: newsletter signup page, seasonal campaign page, Scratch Game page, promotion signup page, download/brochure request page.
Metrics: page views, signups, conversion rate, leads collected, connected campaign.

> **Note:** The brief jumps from number 8 to number 10. There is **no screen number 9** in the document. `[PB §7]` See Q4.

### 7.9 Screen 10 — Campaign Reporting Dashboard `[PB §7.10]`
Metrics: emails sent, open rate, click-through rate, leads collected, Scratch Game participants, landing page signups, eMagazine views, best performing campaigns, META stats, Google stats, Website stats.

**Very important technical point for this screen** `[PB §10]`:
- This dashboard is **built and hosted by an external partner, Meneer Online**. It is already production-ready.
- We must **embed it using an iframe**. We do **not** build it.
- Use a **blank page with no header and no footer**.
- **No extra backend or database is needed.** The dashboard pulls data itself through API from each client's analytics accounts (for example Google Analytics), and updates almost instantly.
- It is already responsive for mobile and tablet.
- Each client can have a separate dashboard with their own branding and colours.
- Our tasks: embed iframe, clean page, remove irrelevant widgets, connect analytics accounts, apply Source Vision brand colours.
- **Ruben** maintains it after integration.
- A screen recording is provided: `03_Design & Templates/Dashboard_Screenrecording/Customer_Dashboard.mov` (29 MB). **We have not reviewed this video yet** — see Q7.

### 7.10 Screen 11 — Admin Dashboard `[PB §7.11]`
Required blocks from brief: total accounts, active subscriptions, open campaign requests, planned campaigns, monthly recurring revenue indicator, top performing services, accounts needing attention, recent activity.

The design shows these KPI cards: Total Customers 348, Active Campaigns 56, Qualified Leads 1,286, Monthly Recurring Revenue €148,750 — each with "% vs last week" and a small sparkline. `[IMG:Part_2/Admin_Dshboard]`
Lower widgets: Recent Customers table, Subscriptions & Requests Overview, Recurring Revenue Overview (donut chart by plan), Campaign Performance table, Lead & Request Pipeline. `[IMG:Part_2/Admin_Dshboard]`

### 7.11 Screen 12 — Account Management `[PB §7.12]`
Fields: company name, contact person, email, phone number, website, logo, brand colours, selected services, subscription type, account status.
Actions: create account, edit account, assign services, view campaign history, view customer activity.

### 7.12 Screen 13 — Service / Package Management `[PB §7.13]`
Fields: service name, description, price, included in package, add-on option, active/inactive status.

### 7.13 Screen 14 — White-Label Settings `[PB §7.14]`
The brief says "This is critical for the sales story."
Fields: platform name, logo, brand colours, custom domain, email sender name, login page branding, module activation, language settings.

The design screen shows much more detail: `[IMG:Part_2/White_Label_Portal]`
- Top cards: White-Label Brand, Active Domains (3), Active Modules (12 / 16), Integrations (6 Active)
- White-Label Configuration: logo, favicon, primary / secondary / accent colour pickers, font family dropdown, header style chooser (3 options), login page style chooser (4 options)
- Domain Management: primary domain + other domains, each with SSL status
- Modules: on/off switches, each marked Core or Add-on
- Roles & Permissions: System Administrator, Marketing Manager, Content Manager, Client, Developer — with user count for each
- Integrations: SendGrid (Connected), Google Analytics (Connected), Print.com API (In Progress), Stripe (Connected), HubSpot (Disabled)
- System Status: System Health, PHP Version, Database, Server, Environment, Last Backup

### 7.14 Screen 15 — Development / Settings Dashboard `[PB §7.15]`
Elements: active modules, future modules, API/integration status, email delivery status, system status, roadmap overview.
Example integration statuses given in the brief: SendGrid Active, Google Analytics Active, Print.com API Roadmap, CRM integration Roadmap, AI Campaign Assistant Roadmap, Payment integration Roadmap. `[PB §7.15]`

### 7.15 Extra screens found only in design (not in the brief)
- **Public marketing website / homepage** — hero section, feature cards, statistics band, call-to-action. `[IMG:Homepage_Soruce_Vision]`
- **Notifications panel ("Action Required")** — shows 4 items needing attention, each with a coloured icon, a status chip (Approval needed / Missing content / Deadline soon) and an action button (Review / Upload / View), plus "Mark all as read" and "View all actions". `[IMG:Notifcations_Action quired]`
- **Upgrade Your Plan page** — shows current plan and 4 upgrade cards. `[IMG:Upgrade ur plan]`
- **Service detail marketing page** — for example Custom Campaign Support with a 4-step process section. `[IMG:Campaign customer journey]`

See Q2 — we need to know if the public website is in our scope.

---

## 8. Design rules (from the Development Handover document)

All points in this section come from `[DH]`, except section 8.0 which is a standing client instruction.

### 8.0 Three standing design rules (apply to every screen)

These three rules are confirmed by the client and apply everywhere. No exceptions.

**Rule A — Blue Virtue's instruction/guide must be followed.**
Blue Virtue owns "the design direction, visual styling, UX structure, branding, interface look & feel, and sales presentation layer" `[PB §2]`. We own the technical development `[PB §2]`.
So for any visual or UX question, Blue Virtue's written guidance is the highest authority — above our own preference, and above the mockups.
We must **never invent design**. If Blue Virtue has not specified something, we use the nearest documented rule, mark it `[TEAM]`, and ask — we do not decide quietly.
The Blue Virtue guidance we hold today is the Development Handover `[DH]`, the 17 design screens `[IMG:*]`, and the design feedback slide `[QP-7]` `[TEAM]`.

**Rule B — Every design must be responsive.**
Desktop, tablet and mobile — all three, every screen. `[DH §2]` already gives three type-size tiers for exactly these devices.
A layout that only works at desktop width is not finished. The page must never scroll sideways, and touch targets must be at least 44 px on tablet and mobile `[TEAM]`.
This matters commercially too: the demo may be shown to a buyer on a phone or tablet, so it must look correct there.

**Rule C — Every design must look modern.**
`[DH §5]` asks for "a clean, modern and professional SaaS design direction" with "bright white surfaces, generous spacing, rounded cards, restrained shadows and a clear content hierarchy".
Nothing dated: no gradients on buttons, no hard drop shadows, no heavy borders everywhere, no cramped spacing, no mixed icon styles.
Every interactive element needs visible hover, focus and pressed states `[DH §3]`, and every screen needs designed empty, loading and error states `[TEAM]`.

Full developer detail for all three rules, including breakpoints and a per-component reflow table, is in the design skill: `skills/source-vision-design/SKILL.md`.

### 8.1 Colours

| Colour | Hex | Where to use |
|---|---|---|
| Primary navy | `#192A4B` | Core brand elements, navigation, sidebars, dark hero sections, main structure |
| Primary blue | `#001FFA` | Primary buttons, active navigation, links, selected controls, progress indicators, interface icons |
| Accent orange | `#FD5104` | Only for commercial actions — subscribe, upgrade, purchase. Also small highlights |
| White | `#FFFFFF` | Page backgrounds, cards, light surfaces |
| Black | `#000000` | Monochrome logo, high contrast text |
| Light greys | — | Borders, dividers, disabled controls, inactive states |

**Strict rule:** Orange must stay an accent colour only. Do **not** use orange as a general interface colour. `[DH §1]`
All colour combinations must keep enough contrast and stay accessible. `[DH §1]`

### 8.2 Typography — Space Grotesk

Font files are provided in `03_Design & Templates/Visual Identity/Space_Grotesk_Font/` (variable font + 5 static weights: Light, Regular, Medium, SemiBold, Bold).

| Use | Weight |
|---|---|
| Main page titles | Space Grotesk Bold (700) |
| Section and card headings | Space Grotesk Bold (700) |
| Intro text / subtitle below a heading | Space Grotesk Medium (500) |
| Interface and body text | Space Grotesk Regular |

**Size scale** `[DH §2]`:

| Element | Desktop | Tablet | Mobile |
|---|---|---|---|
| Main page title | 40–48 px | 30–36 px | 26–30 px |
| Section heading | 24–32 px | — | — |
| Card heading | 18–22 px | — | — |
| Intro text below heading | 16–20 px | — | — |
| Body copy and navigation | 14–16 px | — | — |
| Labels, captions, metadata | 12–14 px | — | — |
| Buttons | 14–16 px | — | — |

**Text rules** `[DH §2]`:
- Use **sentence case** for headings, navigation, buttons and labels (not Title Case, not UPPERCASE) — unless an approved design shows otherwise.
- Keep readable line length and consistent vertical spacing.
- Avoid too much UPPERCASE. Uppercase is allowed only for short plan names, package labels, or small status chips.

> **Conflict found:** the same document says buttons should use "**Inter** Medium 500 or SemiBold 600" `[DH §2]`, but the whole typography section says the font is **Space Grotesk**. The White-Label design screen also shows Font Family = "Inter" `[IMG:Part_2/White_Label_Portal]`. See Q6.

### 8.3 Buttons and interactive colours `[DH §3]`

| Type | Style |
|---|---|
| Primary action | Solid primary blue `#001FFA`, white text |
| Commercial / subscription action | Accent orange `#FD5104`, white text |
| Secondary action | White background, primary blue text and border |
| Active nav, selected card, enabled toggle | Primary blue `#001FFA` |
| Navigation, sidebar, branded hero | Primary navy `#192A4B` or approved navy gradient |
| Disabled / inactive | Neutral grey, low emphasis |
| Destructive action | A clear error colour. **Must not look like the orange commercial accent** |

Focus, hover and pressed states must be clearly visible and used the same way everywhere. `[DH §3]`

### 8.4 Logo rules `[DH §4]`
- Navy logo → use on white or very light backgrounds.
- White logo → use on navy, dark gradient, or photo backgrounds (only if contrast is enough). Also use white logo on the approved navy-gradient panel.
- Keep clear space around the logo.
- Do **not** stretch, distort, rotate, or change proportions.
- Do **not** recolour, outline, or add shadow/effects.
- Use the **full horizontal logo** in website headers and main navigation.
- Use the **symbol only** where space is small — app icon, favicon, collapsed menu.

Logo files provided: SVG (5 files), PNG (2), JPG (3), and an Illustrator `.ai` source. The `.ai` package report confirms the logo uses **Space Grotesk Bold (OTF)**. `[IMG:Logo_Source Vision/.../logoSource VIsion Report.txt]`

### 8.5 Overall visual direction `[DH §5]`
- Clean, modern, professional SaaS style.
- Bright white surfaces, generous spacing, rounded cards, light shadows, clear hierarchy.
- Navy = trust and structure. Blue = interaction and active state. Orange = commercial emphasis only.
- Main product / subscription / marketing pages → can use a strong branded hero.
- Secondary, account and utility pages → use compact, left-aligned headings.
- Keep navigation and layout consistent and easy to scan. Decoration must not fight with content.

### 8.6 Design status — READ THIS CAREFULLY `[DH §6]`

The client wrote this warning in the handover document:

> The supplied screens are **visual references** to guide development.
> They **should not be treated as final functional specifications**.
> Features, workflows, labels, pricing, content, data and component behaviour **may change** during development, testing and stakeholder review.

**Meaning for us:** do not hardcode prices, labels or content. Keep them in config or database so they can change easily. `[TEAM]`

---

## 9. Feedback already given by the client (must be applied)

The pitch deck has a slide of design feedback. These are corrections to the current mockups. `[QP-7]`

| # | Feedback | What it means for development |
|---|---|---|
| 1 | Use Source Vision logo everywhere | Check all screens use the correct logo `[QP-7]` |
| 2 | Add Content Library to the menu | Already present in newer design `[IMG:MENU_...]` `[QP-7]` |
| 3 | Clarify Plans vs Packages vs Services | Still open — see section 6 and Q5 `[QP-7]` |
| 4 | **Replace simple switches with request/status logic** | Important. The plan/package cards currently show a simple ON/OFF toggle `[IMG:Marketing_Plans]`. The client wants a **request + status** flow instead (like the 6 statuses in section 7.5) `[QP-7]` |
| 5 | Keep screenshots as visual examples for development | Mockups are reference only, same as §8.6 `[QP-7]` |

> Point 4 is the biggest functional change. The design images still show the old toggle style.
> We plan to follow the feedback (request/status), not the toggle. Please confirm — Q3.

---

## 10. What we are NOT building now `[PB §5]`

These are **roadmap items**, not September MVP:

- Full SaaS architecture
- Full multi-tenant backend
- Full invoicing system
- Complete API integrations
- Complete Print.com integration
- Full AI functionality
- Complete rebuild of the current systems
- Advanced CRM integrations
- Full marketplace functionality

---

## 11. Project rules (client's own rules) `[PB §16]`

| Rule | Detail |
|---|---|
| **Rule 1 — Demo First** | We are not building a complete SaaS product yet |
| **Rule 2 — Sales Value First** | Every feature must help explain value to a buyer |
| **Rule 3 — Avoid Scope Creep** | If a feature is too complex, move it to roadmap |
| **Rule 4 — Dummy Data Only** | No real customer data, consumer data, financial data, emails or login details |
| **Rule 5 — Keep It Simple** | A clear simple demo is better than a complex unfinished product |

---

## 12. Final deliverables expected by beginning of September `[PB §17]`

1. Working Source Vision demo environment
2. Customer Portal demo
3. Admin Portal demo
4. Development / Settings Portal demo
5. Demo storyline
6. Product demo script
7. Updated Acquire listing copy
8. Screenshot set for sales / listing
9. Technical overview document
10. User role / access matrix
11. Roadmap overview
12. Feature overview for buyers

Note: items 5, 6, 7, 8 are sales documents. Items 9, 10, 11, 12 are documentation. Please confirm who prepares these — Q8. `[TEAM]`

---

## 13. What we learn from the OTHER project (GRS Online)

> **Reminder:** Everything in this section comes from `[GRS]` — the file `Documentation/GRS-Online-Module-Overview.docx`.
> This is a **different project** (GRS Online, a platform for garden centres). It is **not** Source Vision.
> The Project Brief says Source Vision is built "from the existing value of the GRS Mailsystem and the GRS Marketing System" `[PB §Main Objective]`, so the old system's working logic is useful reference.

### 13.1 Why this matters
The old GRS admin menu appears almost directly in one Source Vision design. The screen `[IMG:Back-End Menu]` has a sidebar with: Dashboard, User Management (Roles & Permissions, Manage User, User Center Log, Generate Login), Contacts (Registrations, Unsubscribers), Packages (8 service names), Advertising, Campaign Planning Tool, Content Library, Email Marketing, CMS Management.

Many of these names are GRS module names, not Source Vision names. `[TEAM]`

### 13.2 Which GRS logic is useful for which Source Vision screen

| GRS module `[GRS]` | What it does in GRS | Useful for Source Vision |
|---|---|---|
| **1. Manage Garden Center** | Master customer record: company details, login credentials, business size, active/inactive status, branding (logo, social links). Also bulk import from spreadsheet, and re-send emailed login link | **Screen 12 — Account Management** `[PB §7.12]`. Almost the same field list |
| **2. Page 2 Subscription** | Yearly package selection. Customer browses packages by category, switches them on/off, **every change autosaves immediately**. Final confirm step locks the selection, generates a **PDF summary** and emails it to admin. Admin can carry packages forward to next year | **Screen 4 — Package / Subscription Builder** `[PB §7.4]`. The autosave + confirm + PDF pattern is proven and worth copying |
| **3. Page 1 Folders** | Print folder package selection with up to 18 numbered folders, each with on/off, print-run size, add-ons. Auto-calculates totals and suggests a recommended package | Idea of **auto-calculated total + recommended package** is useful for the plan/package screens |
| **4. CMS Management** | Central registry of which content pages exist, per year and per customer segment. Drives the front-end navigation menu from one list | Matches the **CMS Management** item in `[IMG:Back-End Menu]`. Useful if we need editable content pages |
| **5. CMS Content Pages** | Five simple one-page editors (Home, Contact, etc.) — title, description, banner image | Same as above |
| **6. Marketingmiddelen** | Yearly content editor for a marketing information page and its subpages, separate per account type | Similar to a **Content Library** / service detail page editor |
| **7. Separate Registration** | Public sign-up page for the "Krasactie" (**scratch-card**) add-on. Customer sees promo content, opts in, sees calculated monthly price, submits — which **emails admin instead of creating a live subscription** | Direct match for **Screen 7 — Scratch Game** `[PB §7.7]`. Also shows a good demo shortcut: submit → email, no real provisioning |
| **8. Ad Content** | Monthly ad approval workflow. Admin uploads draft ad content (Facebook, Google, TikTok) as Excel. Customer reviews, comments, approves or rejects each item, uploads own images/videos. **Content not answered within two weeks is auto-approved** | Strong match for the **request/status logic** the client asked for in `[QP-7]`, and for the **Notifications "Action Required"** screen `[IMG:Notifcations_Action quired]` |
| **9. Planning Tool** | Calendar view of upcoming campaigns per quarter, with date range, budget breakdown, colour-coded category. Customer can request a date change → emails admin. Admin can bulk import via Excel | Matches **Campaign Planning Tool** in `[IMG:Back-End Menu]`, and "Planned campaigns" in Admin Dashboard `[PB §7.11]` |
| **10. Statistics** | Admin uploads performance data per channel per year (Facebook/Folder ads, Google ads, scratch-card, folder distribution, E-magazine, custom). Customer sees it as a dashboard | Related to **Screen 10 — Campaign Reporting** `[PB §7.10]`. **But note:** in Source Vision this data comes live via API from Meneer Online's dashboard, **not** by manual upload `[PB §10]`. Different approach |
| **11. Email Marketing** | Two parts: **Email Templates** (reusable library) and **Assigned Templates** (send template to selected customers, creates a batch with a content snapshot and a **personalised magic-login link per recipient**). Plus Template History and unsubscribe support | Matches **Email Marketing** + **Email Templates** in the design menus `[IMG:Back-End Menu]` `[IMG:Part_2/White_Label_Portal]`. Also explains **Generate Login** (magic link) and **Unsubscribers** |
| **12. Subscribers Overview** | Cross-year admin report of who registered or saved a selection on any package screen. Shows finalized vs draft. Exports to Excel/CSV. Can re-download the confirmation PDF | Matches **Registrations** in `[IMG:Back-End Menu]`, and "Active subscriptions" in Admin Dashboard `[PB §7.11]` |
| **13. Admin Dashboard** | Admin landing page: 4 quick counters + 3 mini reports (subscribers overview, marketing packages overview, folder packages overview) | Matches **Screen 11 — Admin Dashboard** `[PB §7.11]` and `[IMG:Back-End Menu]` (which shows exactly 4 counters + a packages overview) |

### 13.3 Three useful patterns we want to copy from GRS `[TEAM]`

1. **Autosave every change immediately** — GRS Page 2 saves each toggle at once so nothing is lost mid-selection. `[GRS §2]`
2. **Confirm step → PDF + email** — a clear "locked" record of what the customer selected. `[GRS §2]` `[GRS §3]`
3. **Auto-approve after a timeout** — GRS auto-approves ad content the customer never answers within two weeks, so work never gets stuck. `[GRS §8]`

### 13.4 Important warning about GRS
The GRS document also records a real problem: for the Marketingmiddelen module, the "single most important goal today" is to **protect content from being accidentally destroyed on save**. `[GRS §6]`
So GRS has a known data-loss bug on save. If we copy any GRS logic, we must not copy this weakness. `[TEAM]`

---

## 14. Technical notes for us

### 14.1 Two different admin menus exist in the design
This is a real conflict we must resolve. `[TEAM]`

| Older design `[IMG:Back-End Menu]` | Newer design `[IMG:Part_2/Admin_Dshboard]` |
|---|---|
| Dashboard | Dashboard |
| User Management (Roles & Permissions, Manage User, User Center Log, Generate Login) | Customers |
| Contacts (Registrations, Unsubscribers) | Campaigns |
| Packages (8 service names listed one by one) | Subscriptions (All Subscriptions, Plans & Pricing) |
| Advertising | Leads (All Leads, Lead Sources) |
| Campaign Planning Tool | Requests (All Requests, Request Types) |
| Content Library | Content Library |
| Email Marketing | User Management (Users, Roles & Permissions) |
| CMS Management | Reports (Overview, Custom Reports) |
| — | Settings (General, Integrations) |

The older one uses **GRS module names**. The newer one uses **business names** and includes Content Library, which the client asked for in `[QP-7]`.
**Our understanding:** the newer `Part_2` design is the correct direction. `[TEAM]` Please confirm — Q1.

### 14.2 Dummy data volume seen in the design
Useful for building seeders `[TEAM]`:
- Admin (newer): Total Customers 348, Active Campaigns 56, Qualified Leads 1,286, MRR €148,750, Active Subscriptions 312, Pending Requests 23, New Requests Today 18, Renewals This Month 34 `[IMG:Part_2/Admin_Dshboard]`
- Admin (older): Total Accounts 165, New Registrations 48, Emails Sent 12,540, Page Visits 8,342 `[IMG:Back-End Menu]`
- Customer: 428 total leads, open rate 42.6%, click rate 12.3%, 28 conversions `[IMG:Dashboard]`
- Company names used: NovaWave, Lumina Studio, Vertex Labs, BrightPath Co., Northpeak Digital, Orion Works, Maple & Co., Elevate Partners, Green & Co. `[IMG:Part_2/Admin_Dshboard]` `[IMG:Dashboard]`
- Account statuses used: Active, Trial, Past Due, Subscribed `[IMG:Part_2/Admin_Dshboard]` `[IMG:Back-End Menu]`
- Segments used: Enterprise, Growth, SMB / Business account, Agency account `[IMG:Part_2/Admin_Dshboard]` `[IMG:Back-End Menu]`
- Currency is **EUR (€)** everywhere, and one label says "All amounts in EUR" `[IMG:Part_2/Admin_Dshboard]`

### 14.3 Environment shown in the design
The White-Label screen shows PHP 8.2.12, MySQL 8.0, nginx/1.24.0, Production. `[IMG:Part_2/White_Label_Portal]`
This is only dummy text inside a mockup, not a real requirement. `[TEAM]`
Our actual installed stack is Laravel 13.25.0 on PHP 8.5.9 with Inertia 3 and Vue 3.5 `[TEAM]`.

### 14.4 Roles seen in the design `[IMG:Part_2/White_Label_Portal]`
System Administrator (full access), Marketing Manager (marketing & reports), Content Manager (content & campaigns), Client (limited access), Developer (system & settings).
This is a good starting point for deliverable 10, the user role / access matrix `[PB §17]`.

---

## 15. Risks we want to raise now `[TEAM]`

| # | Risk | Why |
|---|---|---|
| 1 | **Timeline is very short** | Today is 12 August 2026. Target is "beginning of September" `[PB §Main Objective]`. That is about 3 weeks, not the 1.5 months / 200 hours the brief assumed `[PB §3]` |
| 2 | **Real company logos in the design** | The homepage mockup shows Cisco, Morgan Stanley, BNY, Moderna and Uber under the words "Trusted by leading companies" `[IMG:Homepage_Soruce_Vision]`. These companies are not customers. Showing them suggests a false endorsement, and it also breaks Rule 4 (dummy data only) `[PB Rule 4]`. We recommend replacing them with clearly fake brand names |
| 3 | **Invented statistics on homepage** | "~100,000 employees using Source Vision platforms worldwide", "2.4M+ campaigns launched", "8.7K+ active businesses", "98% customer satisfaction" `[IMG:Homepage_Soruce_Vision]`. In a buyer demo these numbers can be read as real claims. We suggest marking them clearly as sample data |
| 4 | **Price conflicts** | See section 6.4. We cannot build a pricing screen with two different prices for the same plan |
| 5 | **Toggle vs request/status** | Design shows toggles, client feedback says use request/status `[QP-7]`. Building the wrong one wastes time |
| 6 | **Screens not finalised** | The brief itself says only screens 1–4 are mandatory and the rest "still need to prioritize" `[PB §7]`. Without a final list we cannot plan the 3 weeks properly |

---

## 16. Our suggested build order (for discussion) `[TEAM]`

Based on "mandatory first" `[PB §7]` and the demo story `[QP-6]`:

**Week 1 — foundation + mandatory screens**
1. Design system setup (colours, Space Grotesk font, buttons, cards) from `[DH]`
2. Login with demo role switch (Screen 1)
3. Layouts: customer top-nav shell + admin sidebar shell
4. Customer Dashboard with all 7 blocks (Screen 2)

**Week 2 — money screens + admin**
5. Service Selection (Screen 3)
6. Packages and Plans + Upgrade page (Screen 4)
7. Admin Dashboard (Screen 11)
8. Account Management (Screen 12)

**Week 3 — workflow + white-label + polish**
9. Campaign Request flow with the 6 statuses (Screen 5)
10. Notifications "Action Required" panel
11. White-Label Settings (Screen 14) + Development/Settings dashboard (Screen 15)
12. Reporting: embed Meneer Online iframe (Screen 10)
13. Newsletter, Scratch Game, Landing Page overview screens (Screens 6, 7, 8)
14. Demo data seeding, demo script, screenshots

This order is our proposal only. Final priority must come from the client. `[TEAM]`

---

## 17. Document maintenance rule

This document must never go out of date. The rule is:

1. When any new file arrives from the client, run:
   ```bash
   bash check-sources.sh
   ```
2. If the script reports **CHANGED** or **NEW**, then update, in this order:
   - this document (`01-Requirement-Understanding.md`)
   - the two skills in `skills/`
   - then re-run the script with `--update` to save the new fingerprints
3. Write what changed in [03-Change-Log.md](03-Change-Log.md).

Full rule details: [04-Skill-Update-Rules.md](04-Skill-Update-Rules.md)

---

## 18. Source file list (what we read to write this)

Read and used:

| File | Type | Used for |
|---|---|---|
| `Project Brief – Source Vision MVP - 140726.docx` | Text | Sections 1–7, 10–12 |
| `Source Vision – Development Handover.docx` | Text | Section 8 |
| `Source_Vision_Quick_Feedback_Pitch.pptx` (10 slides) | Text | Sections 4, 5, 9 |
| `GRS-Online-Module-Overview.docx` (13 modules) | Text | Section 13 |
| 14 design images (dashboards, menus, plans, white-label, notifications, homepage) | Image | Sections 6, 7, 14 |
| 3 package artboards (of 8) | Image | Section 6.2 |
| `logoSource VIsion Report.txt` | Text | Section 8.4 |
| Space Grotesk font folder | Font | Section 8.2 |

**Not yet reviewed:**

| File | Reason |
|---|---|
| `Dashboard_Screenrecording/Customer_Dashboard.mov` (29 MB) | No video tool available on this machine. See Q7 |
| `Packages/Artboard 3,4,5,6,7,8.jpg` | We checked 3 of 8. The other 5 follow the same card pattern |
| `Gradient_Image.jpg` (30184 × 11305 px) | Very large background asset, no information needed from it |
| `logoSource VIsion.ai` | Illustrator source, needs Illustrator |
| `Source_Vision_Understanding_and_Technology_Brief.docx` | This file is in the Documentation root but was not part of your instruction. Please tell us if we should read it — Q9 |

**Empty folders in the ZIP** (no files inside): `01_Administration`, `04_Web & Technology`, `05_Reports`, `99_Archive`.

**Note on the two ZIP snapshots:** the `7-Aug` and `11-Aug` folders contain the same 50 files. We compared them byte by byte. Only the two `.docx` files differ, and their **text content is exactly the same** (only internal save metadata changed). So `11-Aug` is the current version and nothing was added between 7 and 11 August. `[TEAM]`
