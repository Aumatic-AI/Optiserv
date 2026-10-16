# Optiserv Consulting Website — Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship an 18-page static marketing site for Optiserv Consulting that leads with
"Build your team. Not your overhead.", makes no unverified claim, and executes the pinned
"Signal" direction at full fidelity.

**Architecture:** Plain HTML/CSS/JS, no build step. One token-driven stylesheet, one dependency-free
script. Header and footer markup is duplicated per page for correct first paint and SEO.

**Tech Stack:** HTML5 · CSS custom properties · vanilla ES2020 · self-hosted variable fonts (Archivo, Martian Mono) · inline SVG.

**Testing note:** There is no test runner here and introducing one for a static brochure site would
be ceremony, not safety. Verification is therefore: rendered-browser inspection at 360/768/1440,
`detect.mjs` (the mechanical design detector), keyboard-and-contrast checks, and HTML validation.
Each task names its own check.

## Global Constraints

- **No tenure claim.** Never "10 years", never "since 2017". Company incorporated January 2025.
- **No invented claim, number, testimonial, client logo, review badge or certification.**
- Every unverified carried-over claim carries `data-verify="<id>"` and an entry in `VERIFY.md`.
- **No personal email.** `hello@optiservconsulting.com` only.
- People are shown as branded SVG placeholders, never stock faces.
- Stock photography only for atmospheric context, stored locally under `assets/img/`.
- Palette is exactly `#024C71` / `#00AAD4` / `#696969` / `#FFFFFF`. White dominant.
- Faces are **Archivo** and **Martian Mono** only. Mono is for figures and measurement, never decoration.
- **No mono eyebrow above every section. No 01/02/03 numbering** except in *How it works*.
- **No grid of same-size icon-heading-text cards** as page structure.
- Traces route at 90°/45° only, terminating in square nodes.
- All motion wrapped in `prefers-reduced-motion: reduce`.
- Body text contrast ≥ 4.5:1. `--cyan` never carries body copy on white.

---

### Task 1: Foundation — tokens, fonts, reset

**Files:** Create `assets/css/main.css`, `assets/fonts/`, `assets/img/`

- [ ] Fetch Archivo + Martian Mono variable woff2; fall back to a Google Fonts `<link>` if the network blocks it, and record the fallback in README
- [ ] Write `@font-face` with `font-display: swap` and explicit `unicode-range`
- [ ] Write the `:root` token block: color, fluid type scale, spacing scale, radii, shadow, motion
- [ ] Write reset + base element styles, `:focus-visible` ring, `prefers-reduced-motion` guard
- [ ] **Check:** open a scratch page, confirm both faces load and tokens resolve in DevTools

### Task 2: Shared chrome — header, footer, trace system

**Files:** Modify `assets/css/main.css`; Create `assets/js/main.js`

- [ ] Build the header: logo, primary nav, Services dropdown, persistent "Book a call", scroll-compaction
- [ ] Build the mobile drawer: full-screen overlay, focus trap, Escape to close, `aria-expanded`
- [ ] Build the footer: nav columns, both offices, legal row, no personal email
- [ ] Write the routed-trace SVG utility — 90°/45° paths, square nodes, `stroke-dashoffset` draw-in
- [ ] **Check:** keyboard-only pass — tab through nav, open/close drawer and dropdown, no trap escape failures

### Task 3: Homepage

**Files:** Create `index.html`

- [ ] Write the direction contract as an HTML comment at the top of the emitted markup
- [ ] Hero: statement left, live routed-trace network right, dual CTA
- [ ] Offer strip: $1,500/mo · 30-day trial · India + Philippines · no recruitment fees
- [ ] **Overhead ledger** — full-bleed navy, two-column cost table, mono figures
- [ ] Services as routed stations at varying scale — not a card grid
- [ ] How it works: Scope → Shortlist → 30-day trial → Scale, numbered (sequence carries meaning)
- [ ] **Overlap strip** — full-bleed navy, 24h band, Hyderabad/Cebu vs London/New York/Sydney
- [ ] Industries, founder block, labelled-empty proof slots, closing CTA
- [ ] Per-page meta, Open Graph, `Organization` JSON-LD
- [ ] **Check:** screenshot 360 + 1440; confirm a first-time visitor can state what this is and what to do

### Task 4: Interaction layer

**Files:** Modify `assets/js/main.js`

- [ ] Scroll-reveal via `IntersectionObserver`, content visible by default if JS fails
- [ ] Trace draw-in, fired once, bounded
- [ ] Accordion/FAQ with correct `aria-expanded` / `aria-controls`
- [ ] Cookie banner with `localStorage` persistence and an analytics slot
- [ ] Contact form: blur + submit validation, `aria-live` error summary, success and failure states
- [ ] **Check:** disable JS — page still readable, navigable, and the form still submits

### Task 5: About and Team

**Files:** Create `about.html`, `team.html`

- [ ] About: who we are, Vision, Mission, RISE values routed on traces, why Optiserv (no tenure claim)
- [ ] Team: founder block with bio + 70–90 word note slots, leadership grid, account managers
- [ ] Branded SVG person placeholders with initials and role, labelled "photo to be added"
- [ ] **Check:** confirm zero stock faces and zero unmarked placeholder names

### Task 6: Services hub and five service pages

**Files:** Create `services.html`, `staff-augmentation.html`, `operational-staffing.html`, `recruitment-rpo.html`, `qa-testing.html`, `automation.html`

- [ ] Hub routing to all five
- [ ] Staff augmentation incl. the carried tech stack
- [ ] Operational staffing (HR, payroll, infrastructure, team management)
- [ ] RPO: Full-Cycle, Project, Recruiter On Demand — benefit figures wrapped in `data-verify`
- [ ] QA: manual, automation, QTP, mobile, Section 508, performance, penetration
- [ ] Automation: scoped-per-project, example slots left labelled-empty
- [ ] **Check:** grep for `data-verify` and confirm every instance has a `VERIFY.md` row

### Task 7: Industries and Pricing

**Files:** Create `industries.html`, `pricing.html`

- [ ] Six industries, iGaming present but not leading
- [ ] Pricing: inclusions, trial terms marked TO CONFIRM, in-house cost comparison, FAQ
- [ ] **Check:** confirm no price appears anywhere without its TO CONFIRM marker in `VERIFY.md`

### Task 8: Careers, Insights, Contact

**Files:** Create `careers.html`, `insights.html`, `contact.html`

- [ ] Three real roles carried from the live site
- [ ] Insights index with filter chips and clearly-labelled placeholder entries
- [ ] Contact: form, both offices, `LocalBusiness` JSON-LD, Cebu marked TO BE ADDED
- [ ] **Check:** submit the form empty, with a bad email, and valid — all three states correct

### Task 9: Legal, 404, crawl files

**Files:** Create `privacy.html`, `terms.html`, `cookies.html`, `404.html`, `robots.txt`, `sitemap.xml`

- [ ] Three legal templates with company-specific sections marked for legal review
- [ ] Styled 404 matching the system
- [ ] `sitemap.xml` covering all 17 indexable pages
- [ ] **Check:** every URL in the sitemap resolves to a real file

### Task 10: Handoff documents

**Files:** Create `VERIFY.md`, `README.md`

- [ ] `VERIFY.md`: every `data-verify` id, its claim, source, page location, and the 14 open client items
- [ ] `README.md`: structure, how to edit nav/content, form endpoint wiring, deploy notes
- [ ] **Check:** `data-verify` count in the HTML equals the row count in `VERIFY.md`

### Task 11: Inspection and finish

- [ ] Batched screenshot round — desktop and mobile together
- [ ] `node ~/.claude/skills/impeccable/scripts/detect.mjs --json <targets>`
- [ ] Fix everything both surface, in one batch
- [ ] One confirming round, then stop — two rounds is the ceiling
- [ ] Spawn `impeccable-finish-reviewer`, apply its material fixes once
- [ ] Spawn `impeccable-documenter` to write `DESIGN.md` from the built world
