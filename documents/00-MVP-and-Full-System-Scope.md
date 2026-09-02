# Source Vision — MVP and Full System Scope

**Date:** 12 August 2026 · **Version:** 1.0
**Purpose:** This is the main planning document. Everything is planned from here.

---

# 1. What needs to be covered in MVP

The MVP is a **demo**. Its job is to make a buyer understand the value of Source Vision in about ten minutes.

It is not a finished product. Nothing needs to work in the background. Every screen must look real and complete, and every link must open something.

**Target date:** Tuesday 1 September 2026

---

## 1.1 The nine screens

### 1. Login + demo role switch

- Source Vision logo, clean professional login page
- Email and password fields, login button
- A role switch to move between Customer, Admin and Developer views without logging in again

### 2. Public homepage

- Main headline, short text, two buttons
- A logo strip of well-known companies
- Six feature cards — Email & Newsletter, Scratch Game, Marketing Plans, Marketing Packages, Landing Pages, Campaign Support
- A dark section with headline numbers
- Closing section with a call to action
- Top menu with two dropdown menus and the orange Subscribe button

### 3. Customer dashboard — the most important screen

Seven blocks:

1. **Active marketing package** — plan name, start date, renewal date, a progress bar such as "7 of 10 services used", and a details button
2. **Available services** — eight service icons and a "Request a service" button
3. **Current campaigns** — campaign name, type, status label, and date range
4. **Lead generation results** — total leads, split by source, and a trend chart
5. **Latest newsletter performance** — open rate, click rate, conversions, with up or down arrows
6. **Suggested opportunity** — a recommendation with an action button
7. **Recent activity** — a list of recent actions with date and time

### 4. Marketing services catalogue

- All eight services: Newsletter, Scratch Game, Product Promotion Email, Landing Page, Custom Campaign Support, Social Media Advertising, Google Advertising, TikTok Ads
- Each with a short description
- This page only shows what the platform can do. No prices here.
- Print portal shown as "Coming soon"

### 5. Marketing packages — 8 cards

One card for each single service. All eight are designed and priced.

| # | Package | Price / month | Optional add-ons |
|---|---|---|---|
| 1 | Newsletter | €129 | 2 |
| 2 | Product Promotion Email | €179 | 2 |
| 3 | Landing Page | €249 | 2 |
| 4 | Custom Campaign Support | €299 | 2 |
| 5 | Scratch Game | €334 | none |
| 6 | Social Media Advertising | €549 | 1 |
| 7 | Google Advertising | €549 | none |
| 8 | TikTok Advertising | €849 | 1 |

Each card shows the service name and icon, the price per month, the list of what is included, optional add-ons with yes/no switches, an on/off switch, a "Get Started" button, and the monthly total at the bottom.

**What is included in each package:**

**1. Newsletter — €129**
- Weekly personalised newsletter
- Add your own offer or content block at no extra cost
- One monthly newsletter with a discount coupon
- *Optional:* 4x pet newsletter, 4x barbecue newsletter — see question 36

**2. Product Promotion Email — €179**
- Professionally designed product promotion email
- One dedicated promotional email campaign per month
- Custom product or offer spotlight
- Responsive design for desktop and mobile
- *Optional:* A/B subject line testing, extra promotional email send

**3. Landing Page — €249**
- Custom campaign landing page
- Mobile-friendly responsive layout
- Lead form or contact form integration
- Conversion-focused design and structure
- Basic analytics setup
- *Optional:* copywriting support, extra revision round

**4. Custom Campaign Support — €299**
- Tailored campaign consultation and setup
- Strategic planning for custom promotions
- Asset and communication coordination
- Performance check-ins and optimisation advice
- Cross-channel campaign support
- *Optional:* priority support, additional campaign variation

**5. Scratch Game — €334**
- Digital scratch game, 2 campaigns per year
- Online scratch game campaign
- Scratch game POS package
- Seasonal win campaign, 4 campaigns per year
- Online seasonal win campaign
- Seasonal win POS package
- Customer data management and landing page
- See questions 37 and 38

**6. Social Media Advertising — €549**
- Monthly targeted social media advertising campaigns
- Tailored advertising strategy
- Consistent online reach growth
- Audience insights and targeting
- Quarterly performance reports
- Advertising budget **not** included
- *Optional:* Facebook CAPI support

**7. Google Advertising — €549**
- Google Ads account management
- Product and keyword research
- Custom opportunity analysis
- Weekly maintenance and optimisation
- Monthly performance reports
- Advertising budget **not** included

**8. TikTok Advertising — €849**
- Three targeted TikTok advertising campaigns per month
- Tailored advertising strategy
- Powerful audience targeting
- High engagement potential
- Viral growth opportunities
- Quarterly performance reports
- Advertising budget **not** included
- *Optional:* TikTok CAPI support

### 6. Marketing plans — 5 tiers

| Plan | Price per month |
|---|---|
| Starter | €199 |
| Growth | €349 |
| Full Service | €699 |
| Franchise | €999 |
| Agency | €1,299 |

Each plan card shows:
- Plan name and description
- Price
- List of included services
- Optional add-ons with their prices
- Upgrade option
- Active or inactive state

### 7. Admin dashboard

- Four top cards: Total Customers 348, Active Campaigns 56, Qualified Leads 1,286, Monthly Recurring Revenue €148,750 — each with a small trend line
- Recent customers table with company, segment, plan, status, last activity and renewal date
- Subscriptions and requests summary
- Revenue chart split by plan
- Campaign performance table
- Lead and request pipeline
- Left sidebar menu: Dashboard, Customers, Campaigns, Subscriptions, Leads, Requests, Content Library, User Management, Reports, Settings

### 8. Development / settings portal overview

- Which modules are active today and which are coming later
- Integration status list — SendGrid, Google Analytics, Print.com, Stripe, HubSpot
- Email delivery status
- System status
- Roadmap list, so a buyer can see what the platform can grow into

### 9. White-label configuration

This screen carries the main sales message: the buyer owns and brands their own platform.

- Platform name
- Logo and favicon upload
- Primary, secondary and accent colour pickers
- Font selection
- Header style options
- Login page style options
- Custom domain
- Email sender name
- Module on/off switches
- Live preview, so changing a colour changes the whole platform in front of the buyer

---

## 1.2 Naming — there are four different dashboards

The word "dashboard" is used for four separate things in this project, and mixing them up causes real confusion. This is what each one means.

| Dashboard | Whose | Where | What it shows |
|---|---|---|---|
| **Customer dashboard** | Ours | MVP screen 3 | The end customer's home screen — active package, services, campaigns, leads, newsletter results, next opportunity, recent activity |
| **Admin dashboard** | Ours | MVP screen 7 | The buyer's business view — number of customers, recurring revenue, pipeline, recent customers |
| **Campaign reporting dashboard** | Ours | Later, not in MVP | Deep marketing results — emails sent, open and click rates, leads collected, scratch game participants, landing page signups, best campaigns, plus Meta, Google and website statistics |
| **Partner dashboard** | **Not ours** | To be decided | A finished analytics dashboard built and hosted by an outside partner, **Meneer Online**. The brief **instructs us to embed it** in a frame |

### About the partner dashboard

It is already built and running, so nothing has to be developed for it. It needs no database or backend from us, because it pulls data itself from each client's own analytics accounts, such as Google Analytics, and updates almost immediately. It is already responsive, each client can have their own branded version, and **Ruben** looks after it once it is connected.

#### This is a written requirement, not a suggestion

The brief has a section headed **"Integration Requirements"** listing five tasks for us:

1. Embed the dashboard using an iframe
2. Use a clean page without a header or footer
3. Remove any irrelevant widgets or data
4. Connect the required analytics accounts
5. Apply the Source Vision brand colours

It also states that Ruben maintains the dashboard **"after the integration is complete"**, and it gives us a screen recording so we can see how it works.

This is the most detailed instruction in the whole brief. Most screens only say "design by Blue Virtue"; this one gives us five specific jobs. **So we cannot simply leave it out. Changing this needs a written decision from you.**

#### But the brief contradicts itself

The name "Customer Dashboard" is used for two different things:

| Where in the brief | What it says |
|---|---|
| Screen 2 | "One of the most important screens", seven required blocks, **designed by Blue Virtue** |
| Inside section 10 | "The customer dashboard **is built and hosted by our external partner**. It is production-ready" |

Both cannot be true of the same screen. One says Blue Virtue designs it and we build it. The other says the partner has already built it and we only embed it.

#### Which one it probably means

Three things all point to the same answer:

1. The instruction **sits inside section 10**, the campaign reporting section — not next to screen 2.
2. **Screen 2 cannot come from an analytics tool.** Active package, available services, "request a service", suggested opportunity — that is all platform data. Google Analytics does not hold any of it.
3. **Section 10 asks for exactly what the partner dashboard gives** — it lists "Meta stats, Google stats, website stats", which is what a Google Analytics dashboard produces.

So the embed almost certainly belongs to the **campaign reporting dashboard**, and "Customer Dashboard" is most likely the partner's own name for their product. That is the better outcome, because it affects one screen that is not in the MVP rather than the most important screen that is.

The one thing against this reading is that the screen recording is named "Customer_Dashboard". We have not been able to open the video yet.

#### The three problems with using it

1. It is **in Dutch**, and our demo is English only.
2. It pulls **live data from real analytics accounts**, which breaks our fake-data-only rule.
3. It shows a "no data available" message when no account is connected, and it does not match the Source Vision brand.

**Our recommendation:** build the reporting screen ourselves for the demo, in English and on brand, and connect the partner dashboard afterwards. Because this changes a written requirement, please confirm it in writing. See question 9.

---

## 1.3 Rules for the MVP

| Rule | Detail |
|---|---|
| **Demo first** | We are not building a finished product yet. Looks and clarity come first. |
| **Fake data only** | No real customer, consumer, financial, email or login data anywhere. |
| **Every screen must be responsive** | Desktop, tablet and mobile. |
| **Everything must look modern** | Clean white surfaces, good spacing, rounded cards, soft shadows. |
| **English only** | One language for the demo. |
| **Nothing sends or saves** | Forms and buttons look real but do not send email or store data. |
| **Presenter-led** | A person walks the buyer through the demo. Buyers do not get their own login. |
| **One set of numbers** | Every screen takes its figures from one place, so no two screens can show different numbers. |

---

## 1.4 Not in the MVP

These are all planned for later, and are listed in section 2:

- Campaign request flow
- Campaign reporting dashboard
- Notifications panel
- Scratch game screens
- Landing page and lead generation screens
- Newsletter screens
- Upgrade plan page
- Service landing pages
- All detailed admin screens
- Content library
- Real payments, real email sending, real integrations

---

## 1.5 Plan and dates

| Stage | Dates | Work |
|---|---|---|
| Decisions locked | 12 – 14 Aug | Answer the questions in section 3 |
| Foundation | 17 – 18 Aug | Colours, fonts, shared components, demo data |
| Clickable shell | 18 – 19 Aug | All menus and all nine pages open, still empty |
| Customer screens | 19 – 24 Aug | Homepage, login, dashboard, services, packages, plans |
| Admin and developer screens | 24 – 27 Aug | Admin dashboard, development portal, white-label |
| Content and numbers | 27 – 28 Aug | Final text, matching figures across all screens |
| Extra polish | 28 Aug | Live re-theming and small improvements, if time allows |
| Testing and delivery | 28 – 31 Aug | Responsive check, browser check, deploy, screenshots |
| Dry run | 31 Aug – 1 Sep | Practice the walkthrough, fix issues, hand over |

**Work needed:** about 124 to 170 hours.
**Available with one developer:** about 66 to 78 hours.
This gap must be closed by adding a second developer, reducing the screen list, or moving the date. See question 2.

---

# 2. What is the scope of full system

This section describes the complete platform, not the demo. This is what Source Vision becomes when it is fully built.

Where a part is marked **(From GRS)**, that functionality already exists in the older GRS system and is proven. We reuse the working idea instead of designing it again.

---

## 2.1 Public website

| Part | What it does |
|---|---|
| Homepage | Sells the platform to new visitors |
| Service landing pages (8) | One page per service, with benefits and a request button |
| Contact page | Company details and a contact form **(From GRS)** — simple page editor with title, description and banner image |
| Editable content | Staff can change page text, images and menus without a developer **(From GRS)** — a central page registry decides which pages exist and drives the website menu from one list |
| White-label website | When a buyer rebrands the platform, the public website rebrands with it |
| SEO and cookie notice | Needed once the website goes public |

---

## 2.2 Customer portal

For the end customer — for example a shop that buys marketing services.

### Dashboard
The seven blocks from the MVP, plus live data instead of fixed numbers.

### Marketing services — the eight things a customer can buy

These are the individual services. A customer can buy one service on its own as a package, or get several of them together in a plan. Each service also has its own page on the public website with benefits and a request button.

| # | Service | What the customer gets | Delivered by |
|---|---|---|---|
| 1 | Newsletter | A regular email newsletter to their own contact list | Platform + staff |
| 2 | Scratch Game | A prize game that collects email addresses | Platform |
| 3 | Product Promotion Email | One-off promotional emails about products or offers | Platform + staff |
| 4 | Landing Page | A single campaign page built to collect contact details | Platform |
| 5 | Custom Campaign Support | Hands-on help from the marketing team | People |
| 6 | Social Media Advertising | Paid ads on Facebook and Instagram | People + ad platforms |
| 7 | Google Advertising | Paid search and display ads on Google | People + ad platforms |
| 8 | TikTok Ads | Short video ad campaigns on TikTok | People + ad platforms |

#### 1. Newsletter

A regular email newsletter sent to the customer's own contact list. The design and content are prepared, the send is scheduled, and results come back after every send.

The platform must hold contact lists, hold the newsletter designs, schedule and send, and then record the results. The customer sees planned, sent and draft newsletters, each with its approval status, send date and audience, plus emails sent, open rate, click rate, unsubscribes and leads generated.

**(From GRS)** — this is the proven email engine of the old system, described under "the email engine" below.

#### 2. Scratch Game

A prize game used as a promotion. A visitor plays a scratch card for a chance to win something, and leaves their email address to take part. The customer grows their contact list and gets engagement at the same time. This is the service that separates Source Vision from an ordinary email tool.

The platform must let staff set up the game and the prize, publish a public page for it, capture every entry, and report participants, email addresses collected, conversion rate and campaign status.

**(From GRS)** — the old system ran exactly this as a scratch-card promotion. It had a public page with promotional content where the visitor opted in, saw the calculated monthly price and submitted, and the request was **emailed to the office for manual setup instead of activating anything automatically**. It also kept scratch-card results as their own reporting channel.

#### 3. Product Promotion Email

A one-off promotional email about specific products or a specific offer — a seasonal promotion, new arrivals, a clearance, a single product push. It is not the regular newsletter.

The difference matters for planning: the **newsletter is regular and builds the relationship**, while a **product promotion email is occasional and sells something**. Same sending engine, different purpose, different template, and usually a different audience selection.

The platform must let staff pick a template, add the products, images and text, choose who receives it, get the customer's approval, send it, and report the results.

**(From GRS)** — uses the same email engine, template library and send batches as the newsletter.

#### 4. Landing Page

A single focused web page for one campaign, built to collect contact details rather than to be browsed.

Typical pages: newsletter signup, seasonal campaign, scratch game entry, promotion signup, and a download or brochure request.

The platform must build and publish these pages, capture every form submission straight into the lead database, and report page views, signups, conversion rate, leads collected and which campaign the page belongs to.

#### 5. Custom Campaign Support

Hands-on help from the marketing team for anything the standard services do not cover. This is a people service — the platform's job is to run the workflow and keep the record.

What is included:
- Tailored campaign consultation and setup
- Strategic planning for custom promotions
- Coordination of assets and communication
- Performance check-ins and optimisation advice
- Support across several channels at once

Optional extras: priority support, and an additional campaign variation.

The platform must provide the request and briefing flow, file upload, tracking through the six statuses, a comment thread between both sides, and approval of the finished work.

**(From GRS)** — the old system kept bespoke campaigns as their own reporting channel, and its content approval workflow is the same pattern we reuse here.

#### 6. Social Media Advertising

Paid advertising on social platforms, mainly Facebook and Instagram, planned and managed for the customer.

What is included: account management, audience and creative work, weekly maintenance and optimisation, and monthly performance reports.

**Important:** the advertising budget is **not** included in the service price. The platform and the team manage the campaign; the customer funds the ad spend separately. See question 26.

The platform must let staff prepare each month's ad content, send it to the customer for review **before any money is spent**, show a calendar of planned campaigns with the budget breakdown, and report performance afterwards.

**(From GRS)** — this is the old system's ad content workflow, and it is one of the strongest things we inherit. Each month staff prepared draft ad content for Facebook, Google and TikTok and uploaded it. The customer reviewed it on their own portal, left comments, approved or rejected each item, and uploaded their own images or videos. Staff saw the feedback come back and revised until everything was approved. Content the customer never answered was **approved automatically after two weeks**, so campaigns never stalled. Facebook advertising also had its own yearly reporting channel.

#### 7. Google Advertising

Paid search and display advertising on Google.

What is included: Google Ads account management, product and keyword research, custom opportunity analysis, weekly maintenance and optimisation, and monthly performance reports.

**The advertising budget is not included** — this is stated on the service card itself.

The platform must provide the same monthly review-and-approve cycle and reporting as social advertising.

**(From GRS)** — the same ad content approval workflow covered Google campaigns, and Google advertising had its own yearly reporting channel.

#### 8. TikTok Ads

Short video advertising campaigns on TikTok.

What is included: campaign setup and management, coordination of the video creative, and performance reporting. The advertising budget is not included.

The platform must provide the same review-and-approve cycle, with more attention to video files because the creative is video rather than images.

**(From GRS)** — the same ad content approval workflow already covered TikTok campaigns.

---

### How the money works on the three advertising services

This is worth being clear about, because it changes both the pricing story and the system:

- The **service fee** is what the customer pays Source Vision for planning, managing and reporting the campaign.
- The **ad budget** is what is paid to Facebook, Google or TikTok for the actual advertising, and it is separate.

As it stands, the platform never handles ad spend. It manages the work and reports the results. If that should change, it is a much bigger piece of work — see question 26.

---

### Two more services planned for later

#### eMagazine

A digital magazine or brochure that the customer publishes or sends out, with page views tracked as the measure of success.

This is currently **crossed out in the project brief** and has no design, so we treat it as removed for now. It is written here because it existed in the old system and may come back.

**(From GRS)** — the old system kept e-magazine results as their own yearly reporting channel.

#### Print portal

Ordering printed marketing material — folders, leaflets and similar — through the platform, including print quantities and distribution. Currently shown as "Coming soon".

**(From GRS)** — this was the largest and oldest part of the old system, and it is well proven. A customer chose a main print package for the year, then configured up to **eighteen individual numbered folders**, each with its own on/off switch, print-run size and add-on options. The system calculated running totals as they worked and suggested a recommended package based on the customer's own market data and business size. Every save produced a PDF confirmation and an internal spreadsheet export, and the final selection was locked once submitted. Folder distribution also had its own yearly reporting channel.

If the print portal returns, this is the model to build from — but it is a large module, not a small one. See question 32.

---

### The email engine behind the newsletter and product emails

Both email services sit on one shared engine. **(From GRS)** — all of the following is proven in the old system:

- **Template library** — staff design an email once and reuse it any number of times
- **Send to selected customers** — one send creates a batch with its own saved copy of the content, so the history of what was sent never changes when a template is edited later
- **Send history** — a full record of what went out, to whom and when, kept separate from what is still waiting to go
- **Unsubscribe handling** — anyone who opts out of promotional emails is never included again
- **Password-free login link** — each email can carry a personal link that takes the customer straight into their portal without a password

The volume this engine has to carry, and how sending is set up, is covered in section 2.5.

### Marketing packages and plans
- Eight single-service packages and five bundled plans
- Optional add-ons on every card
- **Autosave (From GRS)** — every switch is saved the moment it is clicked, so a customer never loses a half-finished selection
- **Confirm step with PDF (From GRS)** — a final confirm locks the selection, creates a PDF summary and emails it to the office. Both sides get a clear record of exactly what was ordered.
- **Running total and suggested package (From GRS)** — the monthly total updates as add-ons are switched on, and the system suggests the right package based on the customer's own size and data
- Upgrade and downgrade between plans
- **Yearly renewal (From GRS)** — staff can carry a customer's selection forward into the next period, so the customer does not have to choose everything again

### Campaign requests
- Five steps: choose campaign type, choose goal, add briefing, upload files, submit
- Six statuses: New request, In progress, Waiting for input, Waiting for approval, Scheduled, Completed
- **Review and approval workflow (From GRS)** — staff prepare the campaign content, the customer reviews it, comments, and approves or rejects each item, and uploads their own images or videos. All comments stay attached to the campaign as a record of what was agreed.
- **Auto-approve after two weeks (From GRS)** — if a customer never answers, the content is approved automatically so the work never gets stuck
- **Date change request (From GRS)** — the customer can ask to move a campaign date, and the office is notified

### Contacts and lists

Every email service depends on the customer's contact list, so the platform must manage it properly:

- Contacts collected automatically from landing pages and scratch game entries
- Contacts imported by the customer or by staff from a spreadsheet
- **List cleaning at import (From GRS)** — bad and duplicate addresses removed before they can damage delivery
- **Unsubscribe list per customer (From GRS)** — kept separately for each customer, and never mixed between them
- Segments, so a promotion can be sent to part of a list rather than all of it

See question 30 on who is allowed to upload contacts.

### Reports
- Emails sent, open rate, click rate, leads collected, scratch game participants, landing page signups, best performing campaigns
- Meta, Google and website statistics
- **Per-channel yearly statistics (From GRS)** — performance data kept separately for each channel and each year, so old years stay available for comparison

### Content library
- Downloads, campaign assets, brand files and past newsletters
- **Content and testimonial editor (From GRS)** — staff update the content, images and testimonials themselves each year, without a developer

### Other
- Notifications panel with action-required items
- Contact page
- My account and profile

---

## 2.3 Admin portal

For the buyer's own staff — the agency, franchise or retail head office.

### Dashboard
**(From GRS)** — quick counters plus small summary reports, so staff see account volume and activity the moment they log in.

### Customers
- Company name, contact person, email, phone, website, logo, brand colours, selected services, plan and account status
- Create, edit, assign services, view campaign history and view customer activity
- **Master customer record (From GRS)** — one place to onboard a new customer, correct details, and switch an account on or off. Every other module reads from this record.
- **Bulk import from a spreadsheet (From GRS)** — add many customers at once instead of typing each one
- **Resend the login link (From GRS)** — send a customer their access link again at any time

### Campaigns
- All campaigns across all customers, with status and performance
- **Monthly ad content workflow (From GRS)** — staff prepare draft content for Facebook, Google and TikTok, and the customer approves it before any money is spent
- **Campaign planning calendar (From GRS)** — a calendar view per quarter showing every planned campaign with its dates, budget breakdown and colour-coded category. Customers can see what is planned without asking, and staff can import campaigns from a spreadsheet.

### Subscriptions
- Every customer's plan and package selection
- **Registration report (From GRS)** — one screen showing who registered for what and when, across all years, and whether it is a finished registration or a saved draft
- **Excel and CSV export (From GRS)** — export any view for reporting
- **Re-download documents (From GRS)** — fetch a customer's confirmation PDF again without asking them to resend it

### Plans and pricing
- Create and edit services, packages and plans
- Set price, description, what is included, add-on options and active state
- The buyer builds their own business model inside the platform

### Leads
- All leads across customers and campaigns
- Lead sources — ads, landing pages, newsletter, scratch game
- Pipeline stages with counts and values
- Lead export and handover to the customer

### Requests
- All incoming service and campaign requests, filtered by status
- Request types
- Assign a request, move it forward, ask the customer for input

### Content management
- Content library for customers
- **Central page registry (From GRS)** — controls which pages exist, for which year and which customer type, and automatically creates the matching page for a second customer type so staff do not do the work twice
- **Simple page editors (From GRS)** — light editors for standard pages such as home and contact
- **Marketing materials editor (From GRS)** — a yearly content editor for the marketing information page and its subpages, kept separate per customer type

### Users and roles
- Staff users
- Five roles: System Administrator, Marketing Manager, Content Manager, Client, Developer
- **Activity log (From GRS)** — a record of what each user did

### Reports
- Standard and custom reports
- **Yearly channel statistics (From GRS)** — upload and manage performance data per channel per year

### Settings
- General platform settings
- Integration connections

---

## 2.4 Settings / development portal

For the buyer's technical owner. This is the part that proves the platform can be owned, branded and extended.

| Part | What it does |
|---|---|
| White-label configuration | Platform name, logo, favicon, colours, font, header style, login page style |
| Live re-theming | Change a colour and the entire platform changes immediately |
| Domain management | Multiple domains with SSL status, primary domain, add new domain |
| Module activation | Switch modules on and off, marked as core or add-on |
| Roles and permissions | Create roles and control what each role can access |
| Integrations | SendGrid, Google Analytics, Print.com, Stripe, HubSpot, CRM, AI assistant, payments |
| Email templates | **(From GRS)** reusable email design library |
| System status | Health, versions, database, server, environment, last backup |
| Audit logs | Record of system actions |
| API and webhooks | Keys and webhook configuration so other systems can connect |

---

## 2.5 Technical scope of the full system

| Area | Plan |
|---|---|
| Application | Laravel with Vue and Inertia, MySQL database |
| Multi-client | One database with a client column, and branding applied per client through the same colour settings used in the demo |
| Email volume | 20,000 to 500,000 addresses per client, one newsletter per fortnight. At the top of that range a single client sends over 1,000,000 emails a month. This is the main constraint of the whole platform. |
| Email sending | Use a managed delivery provider. Do not run our own mail server. |
| Email reputation | Each client gets their own sending subdomain with its own SPF, DKIM and DMARC records. Shared IP pool for small clients, dedicated IP above roughly 100,000 emails per send. One client's bad list must never damage another client's delivery. |
| Sending speed | A 500,000 send needs a paced queue of around 100 emails per second, which takes about ten hours. A new dedicated IP needs four to eight weeks of warm-up before it can send 100,000 a day, so a large client cannot be onboarded in a week. |
| Plan limits | Charge on contacts stored as the main measure, with emails sent as a secondary cap, a per-thousand overage charge, and a dedicated IP as a paid add-on |
| Hosting | Application, database and queue on the client's own server; email delivery through the managed provider |
| Suppression and list hygiene | Per-client unsubscribe lists with automatic pause, and list cleaning at import |

---

## 2.6 Later phases

These are real parts of the full vision, but they come after the main system:

- Payment and invoicing
- Print portal
- eMagazine
- AI campaign assistant
- CRM integration
- Marketplace
- Advanced multi-client architecture
- Partner reporting dashboard integration

---

# 3. Questions

We need answers to plan properly.

| Group | What it covers | Who answers |
|---|---|---|
| 3.1 | Blocks the work — nothing can start without these | Asset owner and design |
| 3.2 | Needed soon | Asset owner and design |
| 3.3 | The marketing services | Asset owner |
| 3.4 | The eight package cards | Asset owner and design |
| **3.5** | **Bigger questions — whether the plan matches the goal** | **Asset owner** |

**Please do not skip 3.5.** Questions 1 to 41 check details. Section 3.5 asks whether the plan actually achieves what the project set out to do, and it includes three points where the current plan appears to work against the project's own stated priorities.

---

## 3.1 Need answers first

**1. Are the nine MVP screens correct?**
Please confirm the list in section 1.1. Every hour until 1 September is planned against it. A change after 18 August means removing a screen.

**2. One developer or two?**
The MVP needs about 124 to 170 hours. One developer has about 66 to 78 hours before 1 September. There are three choices:
- Two developers, all nine screens by 1 September
- One developer, six screens by 1 September, the rest by mid-September
- One developer, all nine screens plus most of the next group, by 30 September

**3. Which plan names do we use?**
The customer screens use Starter, Growth, Full Service, Franchise and Agency. The admin screens use Enterprise, Growth, Professional, Basic and Trial. Two name sets in one demo look like two different products. We suggest using the five customer names everywhere.

**4. What is the Franchise plan price?**
One screen shows €999 and another shows €1,049. We suggest €999.

**5. What is the design cut-off date?**
We suggest Wednesday 20 August. After that date we build from the agreed design rules, and any later design change becomes a change request.

**6. Can we have the working agreement in place before we start?**
A short one-page agreement covering scope, effort, ownership of the code, and confidentiality.

**7. Who designs the missing screens, and by when?**
The login screen and the marketing services catalogue have no design yet, and both are in the MVP. The white-label screen is only partly designed. About half of the later screens also have no design.

**8. Can we get the full package list?**
We have prices for only two of the eight package cards. We need the price and the included items for all eight.

**9. Do we build the reporting dashboard ourselves, or use the partner dashboard?**
See section 1.2 for what each of these means.

The brief **instructs** us to embed the partner dashboard — it has a section headed "Integration Requirements" listing five tasks. So this is a written requirement, and leaving it out needs your written approval. We are not treating it as optional.

Two things need answering:

**(a) Which screen was it meant for?** The brief calls it the "customer dashboard", but screen 2 of the same brief is also called the Customer Dashboard and is assigned to Blue Virtue. Our reading is that the embed belongs to the **campaign reporting dashboard**, because the instruction sits inside that section, screen 2 needs platform data an analytics tool cannot supply, and the reporting section asks for exactly the Meta, Google and website statistics this dashboard produces. Please confirm.

**(b) Do we still embed it for the demo?** It is in Dutch, it pulls live data from real analytics accounts, which breaks the fake-data rule, and it shows an error with no account connected.
Our recommendation: build the reporting screen ourselves for the demo, in English and on brand, and connect the partner dashboard afterwards for the real system.

**10. Is eMagazine removed?**
It is crossed out everywhere in the brief and it has no design. We will treat it as removed unless you tell us otherwise.

**11. Can we replace the company logos on the homepage?**
The homepage currently shows Cisco, Morgan Stanley, BNY, Moderna and Uber under the words "Trusted by leading companies". These are not customers. A buyer who checks this will stop trusting the rest of the demo. We suggest using invented company names instead.

**12. Are the homepage numbers acceptable as example figures?**
The page claims around 100,000 employees using the platform, 2.4 million campaigns, 8,700 businesses and 98% satisfaction. A buyer will ask where these came from.

---

## 3.2 Need answers soon

**13. Where do we use a switch, and where do we use a request status?**
Our understanding: keep the on/off switch on the package and plan cards, because there it means "what I have". Use a request status on the dashboard services, because there it means "what I have asked for".

**14. Is the font Space Grotesk everywhere, including buttons?**
The design document says Space Grotesk, but one line mentions Inter. We will use Space Grotesk.

**15. Can we get the exact design values?**
We need the grey shades, border colour, corner radius, spacing steps, and the colours of the navy gradient. Right now we measure them from screenshots. We will send a sheet with our values for approval.

**16. Which extra features do you want, if there is time?**
In order of value: live white-label re-theming, a working notification panel, a live price calculator on the plan cards, and success messages on forms. **We strongly recommend live re-theming** — it is the single strongest moment in the whole demo, and it is cheap to build.

**17. Where is the demo hosted, and is it password protected?**
We suggest we host it and protect it with a password, so it cannot be found publicly before the listing goes live. Are the domains in the design the real ones?

**18. Can you confirm in writing that GRS access is read-only?**
The old GRS mail system is still running and is still collecting real email addresses. We will only take reference screenshots, and only after all real recipient data is removed. We will not change anything.

**19. Who writes the sales material?**
The demo storyline, the demo script, the updated listing text and the screenshot set. We assume this sits with the design and sales side, not with development.

**20. What are the sixteen modules?**
The white-label screen shows "12 of 16 modules active" but only five are visible in the design.

**21. What are the request types?**
The admin area has a "request types" section with no description.

**22. What goes in the content library?**
It appears in both menus but there is no design and no description. Downloads, campaign assets, brand files, past newsletters?

**23. Is billing monthly or yearly?**
Every price in the design is monthly. The brief mentions monthly or yearly. We will build monthly.

**24. Can the demo and the code be sold or transferred?**
Ownership is currently shared with the old GRS business. A buyer will ask this in the first call, so it should be clear in writing before the listing goes live.

**25. Please complete this note:** "For front website, we have to think for …"
The sentence is unfinished in the project notes. We have planned the website as one homepage in the MVP and eight service pages later, but please tell us what you had in mind.

---

## 3.3 Questions about the marketing services

These came up while writing the full scope of the eight services.

**26. Who pays and manages the advertising budget?**
The Google service card says the advertising budget is not included. So the customer pays Facebook, Google and TikTok directly, and pays Source Vision only the service fee. Please confirm.
If instead the platform is ever expected to hold or bill the ad budget, that is a much larger piece of work — it would need payments, spend tracking per customer, and monthly reconciliation.

**27. Do we connect to the real advertising accounts?**
Two very different options:
- **Option A** — staff work inside Facebook Business, Google Ads and TikTok Ads Manager as they do today, and only the results are entered or imported into Source Vision. Simple.
- **Option B** — Source Vision connects to those platforms directly through their APIs and pulls live campaign data. Much more work, and each platform has its own approval process.

We assume Option A for the full system, with Option B as a later step.

**28. Who actually delivers the advertising work?**
Is it the buyer's own marketing team, or is it given to an outside agency? If outside people are involved, the platform needs a supplier or partner role with limited access, and that changes the roles list.

**29. Product promotion email and newsletter — one tool or two?**
Our plan is one sending engine with different templates and audience selection, listed as two services to the customer. Please confirm that is right, and tell us whether a product promotion email needs the customer's approval before it goes out, or whether staff can send it directly.

**30. Who is allowed to upload contact lists?**
Can a customer import their own contacts, or may only staff do it? Is there a limit on list size, and do we need to check where the contacts came from before sending to them? This matters because one customer's poor list can damage email delivery for every other customer on the platform.

**31. Is "priority support" a real commitment?**
It is sold as an optional extra on the Custom Campaign Support service. Does it mean a guaranteed response time, and if so what is the time? If it is only a label, we will build it as a label.

**32. Is the print portal coming back, and in what form?**
The old system had a large print module: a main package plus up to eighteen individually configured folders with print quantities and add-ons, running totals, a recommended package, PDF confirmations and spreadsheet exports.
Please tell us whether the print portal should eventually work that way, or as something much simpler. Right now it stays as "Coming soon".

**33. Is eMagazine removed permanently or only paused?**
It is crossed out in the brief and has no design, so we have removed it. If it is only paused, it needs a service page, a package card, a menu entry and a reporting figure — that is new work, not an edit.

**34. Is the two-week auto-approve period right for Source Vision?**
In the old system, ad content the customer never replied to was approved automatically after two weeks so work never got stuck. It is a good rule, but two weeks may be too long or too short here. Please confirm the period, and confirm that automatic approval is acceptable at all.

**35. Does the scratch game need to be playable, and where does it live?**
For the demo it is only a set of screens. In the full system, does the game itself run inside Source Vision, on the customer's own website, or on a separate public page we publish? The old system used a separate public page.

---

## 3.4 Questions about the eight package cards

We have now read all eight cards. The prices run from €129 to €849 as expected, but a few things on them need a decision.

**36. The newsletter add-ons look like they came from the old system.**
The Newsletter package offers "4x pet newsletter" and "4x barbecue newsletter" as optional extras. These make sense for a garden centre, which is what the old system served, but not for a platform sold to any agency or retail chain.
**We suggest replacing them with neutral options** such as extra newsletter sends, a seasonal campaign block or A/B testing. A buyer reading "pet newsletter" on a white-label platform will ask why.

**37. The scratch game package includes printed in-store material.**
It lists a "scratch game POS package" and a "seasonal win POS package". POS means point of sale, so this is physical material for the shop floor.
Is that intended? It sits oddly in a digital marketing platform, and it overlaps with the print portal. If it stays, we need to know who prints and ships it.

**38. The scratch game package mixes yearly and monthly counts.**
The price is €334 per month, but the contents are described as "2 campaigns per year" and "4 campaigns per year". On one card that reads as a contradiction. Should the counts be per month, or should the price be yearly?

**39. Are Social Media and Google Advertising both meant to be €549?**
Both cards show the same price. It may well be deliberate, but two identical prices side by side usually means one was copied.

**40. Should the reporting frequency be the same across the three advertising packages?**
At the moment Social Media gives quarterly reports, TikTok gives quarterly reports, but Google gives monthly reports. A buyer comparing the three cards will notice.

**41. Two packages have no optional add-ons.**
Scratch Game and Google Advertising have none, while the other six have one or two. Is that intended, or is the list unfinished? The add-ons are useful because they demonstrate upselling.

---

## 3.5 Bigger questions — things that may not fit the goal

Questions 1 to 41 are about detail. These are different. They are about whether the plan actually achieves what the project set out to do.

We are raising them because we would rather be told "we have already thought about that" than stay quiet and watch the relisting go the same way as the last one. Several of these are for the asset owner rather than for the design side.

### A. What is actually being sold

**42. What does a buyer receive on day one?**
The demo is a prototype of a new product. The thing being sold is the existing mail system and marketing platform. Those are not the same. A serious buyer will ask to see the real working system and the real code, not the prototype.
So what transfers on completion — the demo, the existing code, the brand, or a plan? The asset list says "platform foundation and system structure" is included. Is that the existing code, or is it the demo?

**43. Is the demo at risk of over-promising?**
Every screen looks finished, but almost nothing works. If a buyer is walked through nine polished screens and then discovers the working system looks different, we lose the trust the demo was built to create. How do we present the demo honestly — is it described as a prototype, a design concept, or the product?

**44. The revenue figures in the demo are invented, and revenue is what a buyer values.**
The demo shows 348 customers and €148,750 monthly recurring revenue. Those numbers are made up, and correctly so under our fake-data rule. But monthly revenue is the single number an acquirer values a business on. As soon as a buyer asks for the real figure, the invented one becomes a problem.
How do we handle that moment? Do we keep real and demo numbers clearly separate in the listing?

**45. Are the prices researched or placeholders?**
Plans run €199 to €1,299 and packages €129 to €849. If a buyer builds a revenue model on those numbers, they need to hold up. Were they set against real market rates, or chosen to look right in a design?

**46. Ownership is still shared, and that is the first question a buyer asks.**
Ownership sits partly with the old retail business, and whether that business stays involved after a sale is still unknown. This should be settled in writing before the listing reopens, not during a buyer conversation.

**47. The old mail system is still live and still collecting real email addresses.**
The asset description says no customer or consumer data is included in the sale. But the live system is collecting consumer data right now. Where does that data go on completion, who is responsible for it in the meantime, and does it need to be dealt with before the listing goes up?

### B. Will the demo actually work on a buyer

**48. Who is the buyer, exactly?**
The pitch aims at agencies, franchises, retail groups and multi-location businesses. Those are people who would *use* the platform. But listings like this often attract financial buyers who care about revenue, churn and retention rather than screens.
The demo is built for the first group. If the real audience is the second, nine screens will not be what convinces them. Which one are we selling to?

**49. Has anyone read the fifty responses from the last listing?**
The plan says roughly fifty responses showed the old proposition was too broad and hard to grasp. Those responses are the most valuable evidence in this whole project, because they show exactly where buyers got lost.
Has anyone gone through what those people actually asked? Right now the nine-screen list is based on judgement. It could be based on the real objections that stopped the last sale.

**50. If buyers are never given a login, is a clickable demo the right thing to build?**
The plan states that buyers are walked through the demo and are not given hands-on access. But a listing brings in enquiries at volume, and most of those people will never book a call.
So what does an interested buyer see in the first ten minutes on their own? If the answer is a recorded video and screenshots, then the video and the screenshots are the real product, and the clickable demo mainly exists to make them. That is worth being deliberate about rather than assuming.

**51. Should we test the demo on a real buyer before relisting?**
The final step is a rehearsal with our own team against our own script. But the reason we are doing this project is that the proposition failed with buyers, not with us. Reviewing it only internally risks repeating the same mistake.
Could one or two of the previous fifty enquirers be shown the demo before the listing goes live?

**52. How will we know if this worked?**
There is no stated measure of success — not a number of enquiries, not a quality of buyer, not a price. Without one, nobody can judge afterwards whether the money and the three weeks paid off.

### C. Where the plan does not match the project's own priorities

**53. The two features that carry the main message are both outside the MVP.**
The whole repositioning rests on one sentence: this is more than an email tool. The brief supports that with two specific things:
- The scratch game, which the brief calls a key differentiator against standard email platforms
- The campaign request flow, which the brief says proves the platform manages marketing work, not just email

**Neither is in the nine screens going live on 1 September.** Both are in the next group.
So the demo that carries the message deliberately leaves out the two features that make the message true. This looks like the most important scope question in the project. Should one of them replace something in the nine?

**54. The strongest moment in the demo is the first thing scheduled to be cut.**
The brief calls white-label settings critical for the sales story. The plan calls live re-theming — changing a colour and watching the whole platform re-skin — the single sentence the entire asset is sold on.
But it sits in the optional stage, which is described as the first thing dropped if anything slips. The most persuasive thirty seconds in the demo is also the least protected.
Should live re-theming be moved into the protected list instead?

**55. Removing eMagazine leaves traces behind.**
eMagazine is being treated as withdrawn. But it still appears as an example card on the customer dashboard and as a metric on the reporting screen in the brief.
If it is gone, those need to go too, otherwise the demo shows results for a service that does not exist.

**56. "Coming soon" becomes the buyer's promise.**
The print portal is shown as coming soon. Once someone buys the platform, that label becomes a commitment they inherit and have to deliver.
Are we comfortable showing roadmap items as near-ready, and is the roadmap realistic enough for a buyer to rely on?

**57. Is three weeks of build the best use of the money?**
The MVP needs roughly 124 to 170 hours and one developer has 66 to 78. The gap gets closed by adding people, cutting screens, or moving the date.
Before choosing, it is worth asking the harder version of the question: would the same budget spent on fewer, better screens plus a properly produced demo video and a rewritten listing produce more buyer interest than nine screens? We are not saying it would. We are saying nobody has compared the two.
