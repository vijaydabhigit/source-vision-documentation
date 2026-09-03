---
name: source-vision-design
description: Source Vision brand and UI design system — Blue Virtue design authority, mandatory responsive and modern SaaS rules, colours (#192A4B navy, #001FFA blue, #FD5104 orange), Space Grotesk typography and type scale, button and state rules, logo usage, layout and component patterns for the customer/admin/settings portals. Use this skill whenever writing or reviewing any Vue component, Blade view, CSS, Tailwind theme, colour, font, spacing, breakpoint, mobile/tablet layout, button, card, chart, badge, table or layout for Source Vision, and whenever a design mockup is being turned into code.
---

# Source Vision — Design System

Authoritative design rules for the Source Vision demo platform.

**Every rule below is traceable.** Source marks: `[DH]` = `Source Vision – Development Handover.docx`, `[IMG:x]` = design mockup, `[QP-n]` = pitch slide n, `[PB]` = Project Brief, `[TEAM]` = our decision (not from client).
Full paths and explanations: [01-Requirement-Understanding.md](../../documents/01-Requirement-Understanding.md#8-design-rules-from-the-development-handover-document)

---

## STEP 0 — Always do this first (mandatory)

Before you apply any rule in this skill:

```bash
bash documents/check-sources.sh
```

- Output `OK` → this skill matches the client's files. Continue.
- Output `CHANGED` / `NEW` / `MISSING` → **stop**. Follow [04-Skill-Update-Rules.md](../../documents/04-Skill-Update-Rules.md), update this skill from the new source, then continue.

Never apply a stale rule. If a rule here conflicts with the client's source file, **the source file wins** and this skill must be corrected.

---

## THE THREE STANDING DESIGN RULES

These three rules apply to **every** screen, component and state. No exceptions, no "we will fix it later".

### Rule A — Blue Virtue's guidance is the design authority

**Blue Virtue owns the design.** The Project Brief assigns them "the design direction, visual styling, UX structure, branding, interface look & feel, and sales presentation layer" `[PB §2]`. Our side (Nexuslink) owns "the technical development, platform structure, demo functionality, backend logic, user roles, and implementation of the MVP scope" `[PB §2]`.

So on any visual or UX question:

1. **Follow Blue Virtue's instruction/guide.** Their written guidance outranks this skill, outranks the mockups, and outranks our own preference.
2. **Do not invent design.** If Blue Virtue has not specified something, do not quietly decide it and ship it. Use the nearest documented rule, mark the decision `[TEAM]`, and raise it in [02-Open-Questions.md](../../documents/02-Open-Questions.md).
3. **Do not "improve" their design.** If something looks wrong, ask — do not silently correct it.
4. **New Blue Virtue guidance is a requirement change.** Route it through [04-Skill-Update-Rules.md](../../documents/04-Skill-Update-Rules.md) Rule 2: update the documentation, then update this skill, then code.

**The Blue Virtue guidance we hold today** `[TEAM]`:

| Item | File |
|---|---|
| Visual guidelines (colours, type, buttons, logo, direction) | `Source Vision – Development Handover.docx` = `[DH]` |
| Screen references (17 images) | `03_Design & Templates/` = `[IMG:*]` |
| Design corrections | Pitch feedback slide = `[QP-7]` |

If you receive design direction that is **not** in that list, treat it as new input and follow point 4 above.

### Rule B — Everything must be responsive

Every screen must work on **desktop, tablet and mobile**. A layout that only works at desktop width is not finished. See §7 for the concrete rules.

### Rule C — Everything must look modern

Clean, current, professional SaaS. `[DH §5]` defines this and §5 below turns it into concrete patterns. Nothing dated: no heavy borders everywhere, no grey gradients on buttons, no cramped spacing, no clip-art icons, no hard drop shadows.

---

## 1. Colour tokens

| Token | Hex | Use for | Source |
|---|---|---|---|
| `navy` | `#192A4B` | Nav bars, sidebars, dark hero, structural brand areas | `[DH §1]` |
| `blue` | `#001FFA` | Primary buttons, active nav, links, selected controls, progress bars, UI icons | `[DH §1]` |
| `orange` | `#FD5104` | **Commercial actions only** — Subscribe, Upgrade, Purchase. Plus small highlights | `[DH §1]` |
| `white` | `#FFFFFF` | Page background, cards, light surfaces | `[DH §1]` |
| `black` | `#000000` | Monochrome logo, high-contrast text | `[DH §1]` |
| greys | neutral scale | Borders, dividers, disabled, inactive, secondary surfaces | `[DH §1]` |

### Hard rules
1. **Orange is an accent only.** Never use orange for general interface elements, never for a normal primary button. `[DH §1]`
2. **Destructive actions must NOT be orange.** Use a distinct error red so delete is never confused with Subscribe. `[DH §3]`
3. All colour pairs must keep accessible contrast. `[DH §1]`
4. Do not invent new brand colours. Chart series and status colours are the only place extra hues are allowed (see §6).

### Tailwind 4 theme block
Put brand tokens in `resources/css/app.css` inside `@theme`:

```css
@theme {
    --color-sv-navy: #192A4B;
    --color-sv-blue: #001FFA;
    --color-sv-orange: #FD5104;

    --font-display: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
    --font-sans: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
}
```

Then use `bg-sv-navy`, `text-sv-blue`, `bg-sv-orange` etc. Never hardcode a hex in a component.

> The Laravel skeleton ships `--font-sans: 'Instrument Sans'` and a Bunny fonts plugin in `vite.config.js`. Space Grotesk is supplied as local font files in the client ZIP, so self-host it and remove the Instrument Sans default. `[TEAM]`

---

## 2. Typography

**Typeface: Space Grotesk.** Files supplied by client: variable font plus static Light / Regular / Medium / SemiBold / Bold in
`Documentation/11-Aug/.../03_Design & Templates/Visual Identity/Space_Grotesk_Font/`.

| Element | Weight | Source |
|---|---|---|
| Main page title | Bold 700 | `[DH §2]` |
| Section and card heading | Bold 700 | `[DH §2]` |
| Intro text / subtitle under a heading | Medium 500 | `[DH §2]` |
| Interface and body text | Regular 400 | `[DH §2]` |

### Type scale `[DH §2]`

| Element | Desktop | Tablet | Mobile |
|---|---|---|---|
| Main page title | 40–48 px | 30–36 px | 26–30 px |
| Section heading | 24–32 px | | |
| Card heading | 18–22 px | | |
| Intro text under heading | 16–20 px | | |
| Body copy, navigation | 14–16 px | | |
| Labels, captions, metadata | 12–14 px | | |
| Buttons | 14–16 px | | |

### Text rules `[DH §2]`
- **Sentence case** for headings, nav items, buttons and labels. Not Title Case. Not UPPERCASE.
- Avoid excessive uppercase. Uppercase is allowed **only** for short plan names, package labels, and compact status chips — the mockups do use uppercase plan names like `STARTER PLAN` with wide letter-spacing `[IMG:Marketing_Plans]`.
- Keep readable line length, consistent vertical rhythm, clear hierarchy.

### Known conflict — resolved by assumption
`[DH §2]` says buttons use "**Inter** Medium 500 or SemiBold 600", and `[IMG:Part_2/White_Label_Portal]` shows Font Family "Inter". Everything else says Space Grotesk.
**Current decision:** use Space Grotesk for buttons. `[TEAM]`
This is **open question Q6** — if the client answers Inter, update this section and the `@theme` block.

---

## 3. Buttons

| Variant | Style | Source |
|---|---|---|
| Primary | Solid `#001FFA`, white text | `[DH §3]` |
| Commercial (Subscribe / Upgrade / Buy) | Solid `#FD5104`, white text | `[DH §3]` |
| Secondary | White background, blue text, blue border | `[DH §3]` |
| Disabled | Neutral grey, reduced emphasis | `[DH §3]` |
| Destructive | Clear error colour, must not resemble orange | `[DH §3]` |

- Focus, hover and pressed states must be visible and identical in behaviour across every component. `[DH §3]`
- Mockups show fully rounded pill buttons for the orange `Subscribe` in the top nav `[IMG:Dashboard]`, and rounded-rectangle buttons inside cards `[IMG:Marketing_Plans]`.
- Buttons in mockups often carry a trailing arrow `→` for forward actions ("Get Started →", "Request Support →"). `[IMG:Campaign customer journey]`

---

## 4. Logo

Assets: 5 SVG, 2 PNG, 3 JPG, plus `.ai` source. Logo type is Space Grotesk Bold.

| Rule | Detail | Source |
|---|---|---|
| Navy logo | On white / very light backgrounds | `[DH §4]` |
| White logo | On navy, dark gradient, photo backgrounds — only with enough contrast. Also on the approved navy-gradient panel | `[DH §4]` |
| Full horizontal logo | Website headers and primary navigation | `[DH §4]` |
| Symbol only | Only where space is tight — favicon, app icon, collapsed sidebar | `[DH §4]` |
| Never | Stretch, distort, rotate, change proportions | `[DH §4]` |
| Never | Recolour, outline, add shadow or effects | `[DH §4]` |
| Always | Keep clear space around it | `[DH §4]` |

Client feedback: **use the Source Vision logo on every screen.** `[QP-7]`

---

## 5. Visual direction `[DH §5]`

- Clean, modern, professional SaaS.
- Bright white surfaces, generous spacing, rounded cards, restrained shadows, clear hierarchy.
- Navy = trust and structure. Blue = interaction and active state. Orange = commercial emphasis.
- Primary product / subscription / marketing pages → may use a strong branded hero.
- Secondary, account and utility pages → compact, left-aligned headings.
- Decoration must support content, never compete with it.

### What "modern" means concretely (Rule C)

`[DH §5]` gives the direction; this table makes it checkable. Derived from `[DH §5]` plus what the mockups actually do `[TEAM]`.

| Do this | Not this |
|---|---|
| White / very light grey surfaces | Heavy colour fills on content areas |
| Generous padding (20–32 px in cards) | Cramped, edge-to-edge content |
| Rounded corners (~12–16 px on cards, ~8 px on inputs/buttons) | Sharp 0 px corners, or pill-shaped everything |
| Soft, low-opacity shadows + a 1 px light ring | Hard dark drop shadows, or heavy 2 px borders everywhere |
| Flat solid brand colours | Gradients on buttons, bevels, emboss, glossy effects |
| Consistent thin-line outline icons (as in the mockups) | Mixed icon styles, clip-art, emoji as UI icons |
| Clear type hierarchy from the `[DH §2]` scale | Many competing sizes and weights |
| Whitespace to separate sections | Divider lines between every element |
| Subtle, quick transitions (~150–200 ms) on hover/focus | No feedback at all, or slow/bouncy animation |
| Pale tinted status chips with darker text | Saturated blocks of colour, or colour as the only signal |
| Skeletons or spinners for loading states | A frozen or blank screen |

Also required for a modern, credible product `[TEAM]`:
- Every interactive element has visible **hover, focus and pressed** states `[DH §3]`.
- **Empty states** are designed (short message + an action), never a blank panel.
- **Loading and error states** exist for anything that fetches.
- Keyboard focus is always visible — never `outline: none` with nothing in its place.

### Observed layout patterns (from mockups)
- **Card**: white surface, ~12–16 px radius, 1 px light grey ring, very soft shadow, 20–32 px inner padding. `[IMG:Dashboard]`
- **KPI card**: pastel circular icon (top-left), label, large bold number, "+12% vs last week ↑" in green, small sparkline. `[IMG:Part_2/Admin_Dshboard]`
- **Customer portal shell**: white top navigation bar, logo left, menu centre, orange `Subscribe` + user avatar right. `[IMG:Dashboard]`
- **Admin portal shell**: fixed navy left sidebar with grouped/collapsible items, active item is a solid blue rounded block; white content area; page title top-left; bell with red count badge and user block top-right; date-range picker below the header. `[IMG:Part_2/Admin_Dshboard]`
- **Footer inside admin**: `© 2025 Source Vision System. All rights reserved.` left, version right. `[IMG:Part_2/Admin_Dshboard]`
- **Dropdown menu**: white panel, small caret pointing to its trigger, one row per item with a blue outline icon and a thin divider between rows. `[IMG:MENU_Marketing Serivices _ Plans _ PACKAGES]`
- **Section heading on marketing pages**: centred, with a short orange underline accent below. `[IMG:Campaign customer journey]`
- **Numbered process steps**: circular blue numbered badge on a card, dashed arrows between cards. `[IMG:Campaign customer journey]`

---

## 6. Status, badge and chart colours

The brand palette has no success/warning/error colours, so these come from the mockups. `[TEAM]`

### Status chips (pill, pale tinted background, darker text)
| Status | Colour family | Seen in |
|---|---|---|
| Active / Subscribed / Completed (positive) | Green | `[IMG:Dashboard]` `[IMG:Part_2/Admin_Dshboard]` |
| Scheduled / Deadline soon / informational | Blue | `[IMG:Dashboard]` `[IMG:Notifcations_Action quired]` |
| Trial | Light blue | `[IMG:Part_2/Admin_Dshboard]` |
| Missing content / In progress (attention) | Amber / orange tint | `[IMG:Notifcations_Action quired]` |
| Past Due / Approval needed (problem) | Red | `[IMG:Part_2/Admin_Dshboard]` `[IMG:Notifcations_Action quired]` |
| Recommended | Green tint | `[IMG:Dashboard]` |

Keep the amber "attention" tint visibly different from brand orange `#FD5104`, or use orange only for commercial CTAs on that screen. `[TEAM]`

### Charts
Mockups use a multi-hue categorical set for the MRR donut (blue, teal/cyan, green, purple, orange) and single-hue line/area charts in brand blue. `[IMG:Part_2/Admin_Dshboard]` `[IMG:Dashboard]`
When building any chart, **load the `dataviz` skill first**, then map its palette onto these brand colours.

---

## 7. Responsive — mandatory (Rule B)

`[DH §2]` defines three tiers through the type scale: **desktop / tablet / mobile**. Build for all three, always.

### 7.1 Breakpoints
The client gave tier names but no pixel values, so these map the tiers onto Tailwind's defaults `[TEAM]` — confirm with Blue Virtue:

| Tier | Width | Tailwind | Title size `[DH §2]` |
|---|---|---|---|
| Mobile | < 768 px | (base) | 26–30 px |
| Tablet | 768–1023 px | `md:` | 30–36 px |
| Desktop | ≥ 1024 px | `lg:` | 40–48 px |

Write **mobile-first**: base classes are mobile, then `md:` and `lg:` add to them. Never write desktop-first and patch downward.

### 7.2 What must reflow, per pattern

| Pattern | Desktop | Tablet | Mobile |
|---|---|---|---|
| Admin sidebar `[IMG:Part_2/Admin_Dshboard]` | Fixed navy sidebar | Collapsed to icons, or drawer | Off-canvas drawer behind the ☰ button |
| Customer top nav `[IMG:Dashboard]` | Full horizontal menu | Full or condensed | Hamburger; dropdowns become stacked/accordion |
| KPI card row (4 cards) | 4 across | 2 × 2 | 1 per row, stacked |
| Dashboard blocks (7 blocks) | 3-column grid | 2 columns | 1 column, in the numbered order |
| Plan cards (5 plans) `[IMG:Marketing_Plans]` | 3 + 2 layout | 2 per row | 1 per row, full width |
| Service icon grid (8 services) | 4 × 2 | 4 × 2 or 3 wide | 2 per row |
| Data tables `[IMG:Part_2/Admin_Dshboard]` | Full table | Horizontal scroll in its own container | Horizontal scroll, or one stacked card per row |
| Notifications panel `[IMG:Notifcations_Action quired]` | Dropdown panel | Dropdown panel | Full-width sheet |
| Charts | Full size | Full width, reduced height | Full width; drop non-essential gridlines/labels |

### 7.3 Hard responsive rules
1. **The page body must never scroll sideways.** Wide content (tables, charts, code) scrolls inside its own `overflow-x: auto` container.
2. **Touch targets ≥ 44 × 44 px** on tablet and mobile — buttons, toggles, nav items, table row actions.
3. **No fixed pixel widths** on containers. Use `max-width`, flex or grid. Images and embeds get `max-width: 100%`.
4. **Nothing important is hidden on mobile.** You may collapse, stack or move it behind a control, but a buyer must be able to reach every feature on a phone — the demo may well be shown on one.
5. **Test all three widths** before calling a screen done.
6. **The Campaign Reporting Dashboard is built natively** (the Meneer Online iframe was rejected — register L6, 31 Aug 2026) and is a **Wave 1** screen. Style its charts and stat tiles to the brand and make them responsive like any other screen. See `source-vision-functionality` §8 and [07-Scope-Review-and-Decisions-Sep-2026.md](../../documents/07-Scope-Review-and-Decisions-Sep-2026.md).
7. Modals, dropdowns and date pickers must stay inside the viewport at every width.

---

## 8. Mockups are references, NOT specifications

The client states this explicitly:

> The supplied screens are visual references intended to guide development... They **should not be treated as final functional specifications**. Features, workflows, labels, pricing, content, data and component behaviour **may change**. `[DH §6]`

Therefore:
1. **Never hardcode** prices, plan names, service names, counts or labels in a component. Read them from config, database or a seeder. **Pricing is an *example monetisation model*** (Blue Virtue, 31 Aug 2026 — L16/L17): show a small "example configuration, set by the platform owner" label wherever plan/package prices appear.
2. Build reusable components (KpiCard, StatusChip, PlanCard, ServiceIcon) rather than copying a mockup pixel by pixel.
3. When a mockup and a written document disagree, **the written document wins** and the difference is logged as an open question.

### Known mockup conflicts — do not "fix" silently
| Conflict | Status |
|---|---|
| Franchise Plan €999 `[IMG:Marketing_Plans]` vs €1,049 `[IMG:Upgrade ur plan]` | Open — Q5 |
| Nav label "Marketing" `[IMG:Dashboard]` vs "Marketing Services" `[IMG:MENU_...]` | Open — pick one, currently "Marketing Services" `[TEAM]` |
| White-label screen shows `#2563EB` / `#0F172A` / `#10B981` and font Inter `[IMG:Part_2/White_Label_Portal]` — these are **not** brand colours | Treated as sample values inside the white-label form, not as the brand palette `[TEAM]` |
| Two different admin sidebars exist | Open — Q1. Use the newer `Part_2` version `[TEAM]` |
| Homepage shows real company logos (Cisco, Morgan Stanley, BNY, Moderna, Uber) and invented statistics `[IMG:Homepage_Soruce_Vision]` | **Do not build the real logos.** Breaks Rule 4 dummy-data-only `[PB Rule 4]` and implies false endorsement. Open — Q11 |

---

## 9. Design checklist before finishing any UI task

- [ ] `check-sources.sh` reported OK
- [ ] **Rule A** — follows Blue Virtue's guidance; nothing invented; any gap raised as a question, not guessed
- [ ] **Rule B** — checked at mobile, tablet AND desktop widths; correct reflow per §7.2; no sideways page scroll; touch targets ≥ 44 px
- [ ] **Rule C** — matches the "modern" table in §5; hover/focus/pressed, empty, loading and error states all exist
- [ ] No raw hex values — brand tokens only
- [ ] Orange used only for commercial CTA; destructive action is not orange
- [ ] Space Grotesk applied, correct weight for the element
- [ ] Font sizes inside the `[DH §2]` scale
- [ ] Sentence case; uppercase only for plan/package labels and chips
- [ ] Focus, hover, pressed, disabled states all present
- [ ] Correct logo version for the background; not distorted
- [ ] Cards: white, rounded, light ring, soft shadow, generous padding
- [ ] Contrast is accessible
- [ ] No hardcoded price, plan name or label
- [ ] Any new mockup conflict recorded in [02-Open-Questions.md](../../documents/02-Open-Questions.md)

---

## 10. Maintaining this skill

This skill is generated from client source files and **must be updated whenever they change**.

Trigger to update: `check-sources.sh` reports drift, OR a client answer arrives, OR a new design file is delivered.
Procedure: [04-Skill-Update-Rules.md](../../documents/04-Skill-Update-Rules.md)

| Version | Date | Based on | Change |
|---|---|---|---|
| 1.0 | 2026-08-12 | 11-Aug ZIP snapshot | First version. Built from `[DH]`, `[PB]`, `[QP]` and 17 design images |
| 1.1 | 2026-08-12 | Client instruction | Added the three standing rules: **A** follow Blue Virtue's guidance as the design authority `[PB §2]`, **B** everything responsive (§7 rewritten with breakpoints, per-pattern reflow table and 7 hard rules), **C** everything modern (§5 "modern means" table + required states) |
