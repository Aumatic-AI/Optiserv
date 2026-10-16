# Optiserv Consulting — Website Design Spec

**Date:** 2026-10-16
**Deliverable:** Static multi-page marketing website (HTML + CSS + JS only, no build step)
**Replaces:** https://optiservconsulting.com/ (WordPress)

---

## 1. Background

Three sources describe Optiserv, and they disagree:

| | Live site | LinkedIn | Internal PDF checklist |
|---|---|---|---|
| Age | "established 10 years ago" | Founded 2017 | **Incorporated January 2025** |
| Pitch | TaaS for telecom & service integrators | "World-class remote teams" (gaming + IT) | **"Build your team. Not your overhead."** |
| Offer | none stated | none | **Dedicated members from $1,500/mo, 30-day trial** |
| Locations | Hyderabad | Hyderabad | **Hyderabad + Cebu, Philippines** |
| Audience | generic | generic | **Founders/CEOs/MDs/COOs/CTOs/HR heads — UK, USA, Australia, Canada** |
| Email | sunil.s@ (personal) | — | **"No personal email on the page"** |

The PDF (`Optiserv Landing Page Requirements Checklist (1).pdf`) is the most recent and most authoritative source. It states verbatim:

> "The current website has blank stat counters, typos, text from another product, a '10 years' claim (the company was incorporated in January 2025), and no Philippines details."
> "Please do not invent or estimate any claim, number or testimonial."

**Resolution (approved by client):** lead with the PDF; pull supporting material from the live site and LinkedIn where it is genuine and non-contradictory.

---

## 2. Approved decisions

| # | Decision | Choice |
|---|---|---|
| 1 | Tenure claims | **No "10 years."** No blank counters, no invented figures. Lead on capability and delivery model. |
| 2 | Positioning | **"Build your team. Not your overhead."** — offshore dedicated teams, India + Philippines |
| 3 | Scope | **Full multi-page site**, 18 pages |
| 4 | Pricing | **Show "from $1,500/month" + 30-day trial**, terms marked TO CONFIRM |
| 5 | Design direction | **"Signal"** — circuit-trace motif from the logo |
| 6 | iGaming | Included as one industry of six; **not** the lead |
| 7 | Imagery | Branded SVG placeholders for **all people**; real stock photography only for **atmospheric/contextual** shots, stored locally |

---

## 3. Design system — "Signal"

### Concept
The Optiserv logo is a hexagon built from circuit traces and connection nodes — a genuinely distinctive asset in a category full of abstract swooshes. The entire visual system is derived from it: thin traces as layout structure, nodes as markers, a datasheet-like information hierarchy. The result reads as engineering rigour, which is what an offshore technical-staffing buyer needs to feel.

Reference register: engineering schematic × editorial business press. Not SaaS-gradient, not stock-photo consultancy.

### Color tokens
Extracted directly from `Optiserv-Consulting-Logo.webp`.

```
--bg:        #FFFFFF   dominant background
--surface:   #F4F9FB   alternating section tint (cyan-cast off-white)
--ink:       #06212E   body copy, maximum contrast
--navy:      #024C71   headings, structure, primary buttons   [logo]
--navy-700:  #013A57   hover/pressed states
--cyan:      #00AAD4   traces, nodes, accents, active states  [logo]
--cyan-100:  #D6F1F9   soft fills, highlight backgrounds
--grey:      #696969   secondary text                          [logo]
--grey-300:  #D9E1E6   hairlines, borders, dividers
```

**Strategy: restrained ground, committed bands.** White is the dominant surface, as the client
pinned. But a page that is white end-to-end has no pace, so two or three regions go **full-bleed
navy** — the overhead ledger, the overlap strip, and the closing CTA. Those bands give the scroll
rhythm and solve the contrast problem at the same time: `--cyan` fails AA on white, but sings on
navy at 7.4:1. So cyan is decorative on white and functional on navy.

### Typography
Two families, not three. A tighter stack is both faster and more committed.

- **Archivo** (variable) — display *and* body. Hierarchy comes from weight and width, not from
  swapping families. A real grotesque with a point of view; deliberately not Inter.
- **Martian Mono** (variable) — reserved strictly for **figures and measurement**: prices, the
  cost ledger, the timezone strip, spec tables. Never as a costume for "technical."

Dropped from the earlier draft: **IBM Plex Mono** and **Inter Tight**. Both sit on the list of
training-data default faces that make a design guessable from its category alone.

Scale is fluid via `clamp()`. Display tracking bottoms out at `-0.03em` (never past `-0.04em`).
Body measure is held to 65–75ch.

### Signature elements
The world is **PCB silkscreen and engineering schematic** — a real graphic tradition, not a
generic "technical hairline" look. Its grammar is strict and that strictness is the point.

1. **Routed traces** — 1px cyan paths that turn only at **90° and 45°**, exactly as copper routes
   on a board, terminating in square solder nodes. They carry layout structure, connect related
   blocks, and draw themselves in once via `stroke-dashoffset`.
2. **The overhead ledger** — a genuine two-column cost table: what an in-house hire costs you,
   line by line, against what Optiserv absorbs. Mono is legitimate here because it is data.
3. **The overlap strip** — a 24-hour band showing real working-hours overlap between
   Hyderabad/Cebu and London, New York and Sydney. The single most load-bearing objection an
   offshore buyer has, answered with a measurement instead of a sentence.
4. **Asymmetric routed layout** — service blocks sit as stations along a trace at varying scale
   and density. Explicitly **not** a grid of same-size icon cards.
5. **Tabular numerics** (`font-variant-numeric: tabular-nums`) on every figure.

**Removed from the earlier draft**, as category defaults rather than decisions:
mono eyebrow labels above every section, and `01 / 02 / 03` section numbering. Numbering survives
in exactly one place — *How it works* — where the sequence genuinely carries information.

### Motion
Restrained and purposeful. Scroll reveals translate 12px with a 400ms ease-out; traces draw in; nav compacts on scroll. No parallax, no bounce, no counters that spin. All motion is wrapped in `prefers-reduced-motion: reduce` guards.

---

## 4. Site structure (18 pages)

```
index.html                        Home
about.html                        Who we are · Vision · Mission · RISE · why Optiserv
team.html                         Founder/CEO + leadership + account managers
services.html                     Services hub
  staff-augmentation.html         Dev, QA, design + tech stack
  operational-staffing.html       HR, payroll, infrastructure, team management   [new, from PDF]
  recruitment-rpo.html            Full-Cycle · Project · Recruiter On Demand
  qa-testing.html                 Manual, automation, QTP, mobile, 508, perf, pen
  automation.html                 Process/workflow automation                    [new, from PDF]
industries.html                   IT & Non-IT · E-Commerce · Product · Service-based · Consulting · iGaming
pricing.html                      from $1,500/mo · 30-day trial · inclusions
careers.html                      3 live roles carried over
insights.html                     Blog/Articles index (replaces "Resources")
contact.html                      Form + Hyderabad & Cebu offices
privacy.html                      [PDF requirement]
terms.html                        [PDF requirement]
cookies.html                      [PDF requirement]
404.html                          Styled not-found page
```

### Navigation
Primary: Services (dropdown) · Industries · Pricing · About (→ Team) · Careers · Insights · Contact
Persistent CTA: **Book a call**
Mobile: full-screen overlay drawer, focus-trapped, Escape to close.

---

## 5. Page content

### index.html — Home
1. **Hero** — `Build your team. Not your overhead.` Sub: dedicated offshore teams from India and the Philippines, from $1,500/month, with a 30-day trial. Dual CTA: *Book a call* / *See pricing*. Trace artwork derived from the logo hexagon.
2. **Offer strip** — $1,500/mo · 30-day trial · India + Philippines · no recruitment fees. Tabular numerics.
3. **The overhead problem** — contrast block: what an in-house hire costs you (recruitment, payroll, HR, office, equipment, IT, management) vs what Optiserv absorbs.
4. **Services** — four cards: Dedicated Staffing · Operational Staffing · Recruitment & RPO · Automation.
5. **How it works** — 4 steps: Scope → Shortlist → 30-day trial → Scale. Connected by trace line.
6. **Delivery locations** — Hyderabad, India · Cebu, Philippines. Timezone-overlap framing for UK/US/AU/CA clients.
7. **Industries** — six compact tiles.
8. **Founder** — portrait placeholder + 70–90 word first-person note slot, LinkedIn + booking links.
9. **Proof** — testimonials/case studies/client logos, rendered as clearly-labelled empty slots awaiting real content.
10. **Final CTA** + footer.

### about.html
Who we are (PDF-aligned, no tenure claim) · **Vision** and **Mission** verbatim from the live site · **RISE** values (Respect, Integrity, Sustainability, Excellence) with trace-connected layout · Why Optiserv (collaboration, agile delivery, cost efficiency, scalability — tenure claim removed) · delivery-centre summary.

### team.html
Founder/CEO section (large portrait placeholder, bio slot, first-person note slot, LinkedIn + calendar links) · Leadership grid · Account managers & recruiters grid. Names from LinkedIn used as placeholders: Sunil Chandra Goud, Priti Singh, Satyapraveen Reddy, Praveen Reddy — each marked for confirmation.

### Service pages
Shared template: mono label → headline → intro → capability grid → process → proof slot → FAQ → CTA.
- **staff-augmentation.html** — Web, Mobile, QA, UI/UX. Tech stack carried over: Java, .NET, Python, ReactJS, Angular, Salesforce, SAP S/4HANA, Pega, DevOps, SailPoint, CyberArk.
- **operational-staffing.html** — HR, payroll, infrastructure, team management (from PDF; new page).
- **recruitment-rpo.html** — three models: Full-Cycle RPO, Project RPO, Recruiter On Demand. Benefit claims retained but flagged.
- **qa-testing.html** — Manual, Automation (Selenium, Nightwatch.js), QTP, Mobile (iOS/Android), Non-functional: Section 508, Performance Engineering, Penetration Testing.
- **automation.html** — scoped-per-project framing; example slots awaiting real case detail.

### industries.html
Six sections: IT & Non-IT · E-Commerce (platform strategy, storefront UX, expansion, analytics, marketing; four-stage Discovery → Strategy → Execution → Optimization method) · Product Companies · Service-Based Companies · Consulting Firms · iGaming.

### pricing.html
From $1,500 per month. What's included: recruitment, HR and payroll, office seat, equipment, IT support, account manager. 30-day trial terms (TO CONFIRM). Automation priced per project. Comparison against in-house cost. FAQ.

### careers.html
Three roles carried from the live site: Senior Developer (NestJS, NextJS, GraphQL, Automation) · MS Entra ID Developer · Automation Test Engineer (Nightwatch, 3:30 PM–12 AM shift). All remote, full-time.

### insights.html
Article index with filter chips and card grid. Ships with clearly-marked placeholder entries.

### contact.html
Form: Name · Work email · Company · Country · Roles needed · Message. Client-side validation, inline errors, success state. `action=""` placeholder for Formspree/Web3Forms.
Offices: Hyderabad — Aditya Trade Centre, #303, 3rd Floor, Ameerpet, Hyderabad 500038, Telangana. Cebu, Philippines — address TO BE ADDED.
Email: `hello@optiservconsulting.com` (must be created). Phones: +91 808-823-8040, +91 990-261-2737. WhatsApp Business + virtual UK/US numbers: slots reserved.

### Legal pages
Privacy Policy, Terms, Cookie Policy — structured templates with company-specific sections marked for legal review. Not presented as legal advice.

---

## 6. Content integrity rules

Derived from the PDF's instruction not to invent claims.

1. No "10 years" or any tenure claim anywhere.
2. No stat counter ships with a number that has not been confirmed.
3. No testimonial, case study, client logo, review badge or certification is fabricated. Each is a labelled empty slot.
4. No personal email address on any page.
5. Every carried-over claim that cannot be verified is wrapped in `data-verify="<id>"` and listed in `VERIFY.md` with its source and location. Examples: RPO "50–60% cost per hire reduction", "~40% time-to-hire reduction", LinkedIn's "51–200 employees" and "Founded 2017".
6. People are never represented by stock faces. Branded SVG placeholders only.
7. Stock photography is permitted only for atmospheric context (workspace, city, infrastructure), must be genuinely relevant, and is stored locally in `assets/img/`.

---

## 7. Technical architecture

### Files
```
index.html … 404.html              18 pages
assets/css/main.css                tokens, base, components, utilities
assets/js/main.js                  nav, reveal, form, cookie banner, accordions
assets/img/                        logo, og images, local stock photography
assets/img/placeholders/           branded SVG person/office placeholders
VERIFY.md                          unconfirmed claims register
README.md                          structure, how to edit, deploy notes
robots.txt · sitemap.xml
```

### Decisions
- **No build step.** Plain files, openable directly, deployable to any static host.
- **Header and footer are duplicated into each page**, not JS-injected. Costs maintenance, but guarantees correct first paint and SEO — non-negotiable for a page that will receive paid traffic.
- **Fonts self-hosted** under `assets/fonts/` with `font-display: swap`, avoiding a third-party request on the critical path.
- **CSS** is a single file organised as tokens → reset → base → layout → components → page-specific → utilities → media queries. Custom properties throughout so a palette change is a one-line edit.
- **JS** is vanilla, no dependencies, deferred, and feature-detected. Every enhancement degrades gracefully: with JS disabled the site is fully readable and navigable.
- **Components** are isolated and independently understandable: each has one job, a documented class API, and no reliance on another component's internals.

### Quality targets
- Responsive 320px → 2560px, tested at 360 / 768 / 1024 / 1440.
- Semantic landmarks, visible focus rings, keyboard-operable nav and accordions, `aria-*` on interactive widgets.
- WCAG AA contrast on all text. Note: `--cyan` on white fails AA for body text and is therefore never used for body copy — only for 3px+ graphical elements and large display type.
- `prefers-reduced-motion` honoured for all animation.
- Per-page meta: title, description, canonical, Open Graph, Twitter card. `Organization` and `LocalBusiness` JSON-LD.
- Lighthouse targets: Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95.

### Error handling
- Form: inline field-level validation on blur and submit, `aria-live` error summary, disabled submit during send, explicit success and failure states. No silent failure.
- Images: `alt` on every image, `loading="lazy"` below the fold, explicit `width`/`height` to prevent layout shift.
- JS: every DOM query guarded; a missing element never throws and never blocks the rest of the script.
- 404: styled page matching the system.

---

## 8. Open items for the client

Tracked in `VERIFY.md`, each rendering as a visible placeholder until supplied:

1. 30-day trial terms — free or paid, and what happens on dissatisfaction (one plain sentence).
2. Whether $1,500 is per person or per team, and whether it varies by role or by India vs Philippines.
3. Founder photo, name, title, bio, 70–90 word first-person note, LinkedIn URL, booking calendar URL.
4. Team member names, photos, roles.
5. Testimonials, case studies, client logos — with written permission.
6. Confirmed figures: clients served, people placed, active team members, retention, days to shortlist, and since when.
7. Cebu office address, phone, team size, roles delivered.
8. Real office and team photographs.
9. WhatsApp Business number; virtual UK/US numbers.
10. `hello@optiservconsulting.com` mailbox creation.
11. Registered company name and registration number.
12. Legal copy review for Privacy, Terms, Cookies.
13. Form endpoint (Formspree / Web3Forms / custom) and analytics IDs.
14. Decision on `optiservsolutions.com` — the PDF flags it as showing placeholder text and another company's email, to be taken down or hidden.

---

## 9. Out of scope

CMS or admin interface · blog authoring system · backend form handling · hosting and DNS setup · live analytics configuration · copywriting for individual blog articles · legal drafting.
