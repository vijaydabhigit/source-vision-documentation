# Open Questions for Client

**Date:** 12 August 2026
**From:** Development team (Nexuslink)
**Last updated:** 13 August 2026 — Q15 to Q20 added while building Wave 1; Q2 and Q11 marked answered. **Q19 and Q20 are blocking.**
**Please note:** Questions Q1 to Q6 and Q14 are **blocking**. We can start the design system and login screen without answers, but we cannot finish the package, plan and admin screens until these are answered.

Source marks used here are explained in [01-Requirement-Understanding.md](01-Requirement-Understanding.md#how-to-read-the-source-marks).

---

## BLOCKING QUESTIONS

### Q1. Which admin menu is correct?
Two different admin sidebars exist in the design files.

- **Older** `[IMG:Source_Vision_Images/Back-End Menu.png]` — Dashboard, User Management, Contacts, Packages (8 services listed one by one), Advertising, Campaign Planning Tool, Content Library, Email Marketing, CMS Management. These are mostly **GRS module names**.
- **Newer** `[IMG:Part_2/Admin_Dshboard.png]` — Dashboard, Customers, Campaigns, Subscriptions, Leads, Requests, Content Library, User Management, Reports, Settings. These are **business names**.

The KPI cards are also different (Total Accounts / New Registrations / Emails Sent / Page Visits vs Total Customers / Active Campaigns / Qualified Leads / MRR).

**Our assumption:** the newer `Part_2` version is correct, because it includes Content Library which you asked for in the pitch feedback `[QP-7]`.

**Question:** Should we build the newer `Part_2` menu and drop the older one? Or do you want the GRS-style modules (CMS Management, Campaign Planning Tool, Email Marketing) kept as well?

---

### Q2. Is the public marketing website in our scope?
The Project Brief lists only portal screens (login, dashboards, settings) `[PB §7]`.
But the design folder also has full public website pages:
- Homepage `[IMG:Homepage_Soruce_Vision.png]`
- A service detail marketing page with a 4-step process `[IMG:Part_2/Campaign customer journey..png]`

**Question:** Do we build the public website too, or only the logged-in portals? If yes, how many public pages, and is the content ready?

---

### Q3. Toggle switch, or request + status flow?
Your pitch feedback says: *"Replace simple switches with request/status logic"* `[QP-7]`.
But the design screens still show simple ACTIVE/INACTIVE and ON/OFF toggles `[IMG:Marketing_Plans.png]` `[IMG:Packages/Artboard 2.jpg]`.

**Our assumption:** we follow your feedback and build the request + status flow using your 6 statuses (New request, In progress, Waiting for input, Waiting for approval, Scheduled, Completed) `[PB §7.5]`.

**Question:** Please confirm. Also: when a customer clicks "Get Started" on a plan, should it (a) create a request that admin must approve, or (b) activate the plan immediately in the demo?

---

### Q4. Final list of mandatory screens
The brief says screens **1, 2, 3, 4** are mandatory and the "Additional" list was left empty `[PB §7]`. It also says *"we should determine along the way what screens will be mandatory"*.

We also found two gaps in the brief:
- There is **no screen number 9**. The list jumps from 8 to 10 `[PB §7]`. Was a screen deleted by mistake?
- **eMagazine** and **Print portal** are listed as services in the brief `[PB §7.3]` but they are **missing** from the design menu, which shows only 8 services `[IMG:MENU_Marketing Serivices _ Plans _ PACKAGES .png]`. Should we add them?

**Question:** Please give the final mandatory list, in priority order. With about 3 weeks left (see Q10), we can realistically build 8 to 10 screens well, not 15.

---

### Q5. Pricing — three conflicts
We found the same item with different prices in different files. We will not guess.

| Item | Price A | Price B |
|---|---|---|
| Franchise Plan | **€999** / month `[IMG:Marketing_Plans.png]` | **€1,049** / month `[IMG:Upgrade ur plan.jpg]` |
| Google Advertising | **€549** / month as own package `[IMG:Packages/Artboard 9.jpg]` | **€79** / month as plan add-on `[IMG:Marketing_Plans.png]` |
| Custom Campaign Support | **€299** / month as own package `[IMG:Packages/Artboard 2.jpg]` | **€99** / month as plan add-on `[IMG:Marketing_Plans.png]` |

For the second and third rows we think the logic is: the cheap price is an add-on for someone who already pays for a plan, and the high price is a full standalone service. But we are not sure.

**Question:** Which prices are correct? And is the add-on vs standalone difference intentional?

---

### Q6. Which font — Space Grotesk or Inter?
The Development Handover says the typeface is **Space Grotesk** and gives its weights `[DH §2]`. Space Grotesk font files are also supplied in the ZIP.
But in the same document, the button rule says *"14–16 px, **Inter** Medium 500 or SemiBold 600"* `[DH §2]`.
And the White-Label design screen shows Font Family = **"Inter"** `[IMG:Part_2/White_Label_Portal.png]`.

**Our assumption:** Space Grotesk everywhere, including buttons. The word "Inter" looks like leftover text from an older brand guide.

**Question:** Please confirm Space Grotesk is used for buttons too.

---

## NON-BLOCKING QUESTIONS

### Q7. Screen recording and dashboard access
The ZIP has a 29 MB video: `03_Design & Templates/Dashboard_Screenrecording/Customer_Dashboard.mov`. This machine has no video tool, so **we have not watched it yet**.
The brief also gives a Google Drive link for the same recording `[PB §10]`.

**Questions:**
1. Can you share the important frames as images, or a short written summary of what the video shows?
2. For the Meneer Online dashboard `[PB §10]` — can we get a **test embed URL** now? We need it to build the iframe page. Who is our contact — Ruben or Meneer Online directly?
3. Which analytics accounts should be connected for the demo? Real accounts, or a demo account with dummy data (Rule 4 says dummy data only `[PB Rule 4]`)?

---

### Q8. Who writes the sales documents?
The deliverables list has 12 items `[PB §17]`. Four of them look like sales/marketing work, not development work:
- Demo storyline
- Product demo script
- Updated Acquire listing copy
- Screenshot set for sales/listing

**Question:** Will Blue Virtue or Sonny prepare these? We assume we only deliver the working demo plus the technical documents (technical overview, role/access matrix, roadmap, feature overview). Please confirm.

---

### Q9. Should we read the extra document?
There is a file `Documentation/Source_Vision_Understanding_and_Technology_Brief.docx` (166 KB) in the Documentation root folder. It was **not** in your list of files to read.

**Question:** Should we read it? Is it an older version of our own understanding, or new input from you?

---

### Q10. Timeline confirmation
The brief targets "beginning of September" `[PB §Main Objective]` and assumed about 200 developer hours over 1.5 months `[PB §3]`.
Today is **12 August 2026**. Beginning of September is about **3 weeks** away, which is roughly **90 hours** at 30 hours per week — less than half of the planned 200 hours.

**Question:** Is the September date fixed (for example, an Acquire listing date), or is there flexibility? If it is fixed, we should agree now on a smaller screen list (see Q4) instead of building 15 screens badly.

---

### Q11. Two problems on the homepage design
We want to raise these before building, because they can hurt you in a buyer conversation.

1. **Real company logos.** The homepage shows **Cisco, Morgan Stanley, BNY, Moderna and Uber** under the heading *"Trusted by leading companies"* `[IMG:Homepage_Soruce_Vision.png]`. These companies are not Source Vision customers. Publishing this suggests a false endorsement, and it also breaks your own Rule 4 (dummy data only) `[PB Rule 4]`. A buyer who checks this may lose trust.
   **Our suggestion:** replace them with clearly invented brand names, same as the fake company names already used in the dashboards (NovaWave, Lumina Studio, etc.).

2. **Invented statistics.** The homepage shows *"~100,000 employees using Source Vision platforms worldwide"*, *"2.4M+ campaigns launched"*, *"8.7K+ active businesses"* and *"98% customer satisfaction"* `[IMG:Homepage_Soruce_Vision.png]`. In a sales demo these read as real claims.
   **Our suggestion:** keep them but label the page clearly as a demo, or reduce them to obviously sample figures.

**Question:** Do you agree with both changes? We will not build the real logos into the demo until you confirm.

---

### Q12. Language of this documentation
You asked for the document in "simple Indian language". We have written it in **simple, plain English**, because all client files are in English and English is the common working language for the team.

**Question:** Is simple English correct? If you want **Hindi** or **Hinglish** (Hindi written in English letters), tell us and we will prepare that version too. We can also keep both.

---

### Q13. Demo hosting
**Questions:**
1. Where will the demo be hosted — your server, our server, or a temporary demo domain?
2. Should the demo be public, or protected by a password?
3. The design shows domains `app.sourcevision.com`, `sourcevision.com`, `staging.sourcevision.com` `[IMG:Part_2/White_Label_Portal.png]`. Are these real domains that we will use?

---

### Q14. Responsive designs — for Blue Virtue
It is now confirmed that **every design must be responsive** (desktop, tablet, mobile) and must follow Blue Virtue's guide — see section 8.0 of the understanding document.

However, **all 17 supplied design screens are desktop only.** We measured them: the dashboards are 1671 × 941 px, the admin screens 5792 × 4344 px, the plan pages 4092 × 5448 px. There is no tablet or mobile version of any screen. The Development Handover gives font sizes for tablet and mobile `[DH §2]` but no layouts.

Since Blue Virtue owns the design and we must not invent design (Rule A), we need one of these:

1. **Blue Virtue supplies tablet and mobile designs** for the mandatory screens (at least Login, Customer Dashboard, Service Selection, Packages/Plans), or
2. **Blue Virtue approves our reflow rules** — we have written a per-component reflow table (sidebar → drawer, 4 KPI cards → 2 × 2 → stacked, 5 plan cards → 1 per row, tables → horizontal scroll, and so on) in the design skill, and we build to that, or
3. Responsive is limited to a smaller set of screens for the September demo.

**Questions:**
1. Which of the three options above?
2. Please confirm our breakpoints, since only tier names were given, not pixel values: **mobile < 768 px, tablet 768–1023 px, desktop ≥ 1024 px**.
3. Will the demo be presented on a phone or tablet at any point? That decides how much polish the small screens need.
4. Is the Development Handover `[DH]` + the 17 screens + the feedback slide `[QP-7]` the **complete** Blue Virtue guide, or is there a fuller design system / Figma file we have not received?

---

### Q15. Public website — three design gaps found while building the homepage
The homepage was built on 13 August 2026. Blue Virtue's homepage screen `[IMG:Homepage_Soruce_Vision.png]` covers everything down to the final call to action, but three things it does not cover had to be decided to ship the page. We have used the nearest documented rule in each case and marked it `[TEAM]`, per design Rule A.

1. **There is no footer design.** The mockup ends at the "Start building better marketing today." band. We built a footer from rules that already exist: navy surface with the white logo `[DH §4]`, sentence case, and the copyright/version line taken from the admin screen `[IMG:Part_2/Admin_Dshboard.png]`.
2. **There is no hero photography.** The hero shows three overlapping photo panels (ocean imagery) and the insights band uses a particle-field photo. No image files were supplied. We used the **approved navy-gradient panel** `[DH §4]` instead of sourcing stock photography, because we must not invent design.
3. **The logo files carry ~24% empty canvas.** Measured on `LogoSV_1..png`: the artwork occupies 4.95:1 inside a 2.91:1 canvas. At any header height that fits a 72 px bar, the logo rendered far smaller than in your mockup. Our web copies therefore use a trimmed `viewBox` that keeps about 10% of the glyph height as clear space. **No path was changed** — the logo is not distorted, recoloured or re-proportioned `[DH §4]`.

**Questions:** Will Blue Virtue supply a footer design and the hero/insights imagery? And is the trimmed logo clear space acceptable, or do you want a specific clear-space ratio?

---

### Q16. Google and TikTok brand marks in the services menu
The services menu uses the real Google "G" and the TikTok note as the icons for `Google Advertising` and `TikTok Ads` `[IMG:Menu_Source Vision_Frontend.jpg]`. Naming the advertising channel is normal; **reproducing the brand marks** is a trademark question, and it also sits close to your own Rule 4 `[PB Rule 4]`.

**Our decision for now:** both use neutral outline icons in the same line style as the other six (a search icon and a video icon). `[TEAM]`

**Question:** Do you want the real brand marks restored? If so, please confirm you hold permission to use them in the demo and in the sales listing.

---

### Q17. Uppercase section labels vs the sentence-case rule
`[DH §2]` says use sentence case for headings and labels and to avoid excessive uppercase. But every small blue label on your homepage is uppercase — "SMARTER MARKETING. BETTER RESULTS.", "ALL-IN-ONE MARKETING PLATFORM", "AI-POWERED INSIGHTS", "READY TO GROW?".

**Our decision:** follow the mockup and render them uppercase, because Blue Virtue's design is the authority on visual styling. The copy is stored in sentence case in the data file and only rendered uppercase, so switching to the written rule is a one-line change. `[TEAM]`

**Question:** Confirm uppercase eyebrows are intended, and that `[DH §2]` means "avoid uppercase in body and headings", not "never".

---

### Q18. "You're on our top plan" on a plan that is not the top plan
The Full Service plan card prints **"You're on our top plan."** under *Upgrade option* `[IMG:Marketing_Plans.png]`. But Full Service (€699) sits below Franchise (€999) and Agency (€1,299), and the card is shown INACTIVE, so the sentence is wrong twice over.

We have **not** silently corrected it — the copy is stored as supplied so you decide.

**Question:** Should Full Service read "Unlock more features with a higher plan." like the others, and should that sentence appear only on whichever plan the customer is actually on?

---

### Q19. The mockups use campaign statuses that are not on your list of six
Your brief fixes **six** campaign statuses: New request · In progress · Waiting for input · Waiting for approval · Scheduled · Completed `[PB §7.5]`.

But the dashboards print **"Active"** on campaign chips `[IMG:Customer_Dasboard.png]` `[IMG:Part_2/Admin_Dshboard.png]`, which is not one of the six.

**What we did:** the written brief wins over a mockup, so "Active" is shown as **In progress** on every campaign. We did not add a seventh status.

Separately, the dashboard services grid uses **Active / Requested / Completed / Available**. We read those as a *different* axis — the state of a service you hold, not the state of a campaign request — and kept them as their own small vocabulary. This matches register item D5.

**Questions:** Confirm campaign chips should read "In progress", not "Active". And confirm the four service states are intentional and separate from the six campaign statuses.

---

### Q20. Two Wave 1 screens have no design at all
Both are on the protected Wave 1 list `[EP §6]`, and neither has a mockup:

1. **Login** — the brief describes it in words only: logo, professional SaaS look, login, optional demo role switch `[PB §7.1]`. We built it from documented rules: the approved navy-gradient panel with the white logo `[DH §4]`, a white form card, and standard button variants. Note that your White-Label screen offers **four "Login page style" presets** `[IMG:Part_2/White_Label_Portal.png]`, which implies four login layouts exist somewhere.
2. **Marketing Services catalogue** — screen 3 is mandatory `[PB §7.3]` but only the *menu* was designed `[IMG:Menu_Source Vision_Frontend.jpg]`. We reused the homepage feature-card treatment.

**Questions:** Will Blue Virtue design these two? And do the four login presets exist as designs we have not received?

---

## Answer tracking

| Q | Topic | Blocking | Status | Answer |
|---|---|---|---|---|
| Q1 | Admin menu version | Yes | Waiting | |
| Q2 | Public website in scope | Yes | **Answered** | **In scope.** Public Homepage is a Wave 1 screen; Service Landing Page template ×8 is Wave 2 `[EP §6]` |
| Q3 | Toggle vs request/status | Yes | Waiting | |
| Q4 | Final mandatory screens | Yes | Waiting | |
| Q5 | Pricing conflicts | Yes | Waiting | |
| Q6 | Space Grotesk vs Inter | Yes | Waiting | |
| Q7 | Video + dashboard embed | No | Waiting | |
| Q8 | Who writes sales docs | No | Waiting | |
| Q9 | Extra .docx file | No | Waiting | |
| Q10 | Timeline | No | Waiting | |
| Q11 | Homepage logos and stats | No | **Answered** | **C5** — neutral placeholders replace the real logos. **C6** — the statistics are illustrative, not audited. Both applied on the built homepage |
| Q12 | Document language | No | Waiting | |
| Q13 | Demo hosting | No | Waiting | |
| Q14 | Responsive designs for tablet/mobile (Blue Virtue) | **Yes** | Waiting | |
| Q15 | Public site: no footer, no hero imagery, logo clear space | No | Waiting | Built to the nearest documented rule `[TEAM]` |
| Q16 | Google / TikTok brand marks as service icons | No | Waiting | Neutral outline icons used for now `[TEAM]` |
| Q17 | Uppercase eyebrows vs the sentence-case rule | No | Waiting | Following the mockup `[TEAM]` |
| Q18 | "You're on our top plan" on the wrong plan | No | Waiting | Copy kept as supplied, not corrected `[TEAM]` |
| Q19 | Mockup chips say "Active", not one of your six statuses | **Yes** | Waiting | Written brief wins: shown as "In progress" `[TEAM]` |
| Q20 | Login and Services catalogue have no design | **Yes** | Waiting | Built from documented rules only `[TEAM]` |

When an answer arrives: fill the Answer column, update [01-Requirement-Understanding.md](01-Requirement-Understanding.md), update the affected skill, and add a line to [03-Change-Log.md](03-Change-Log.md).
