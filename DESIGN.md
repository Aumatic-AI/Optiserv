# DESIGN.md — Optiserv Consulting, "Console"

Recorded from the built site. If the code and this file disagree, the code is right.

## 2026-10-16 redesign: "Console"

Rebuilt in the register of a global people platform (Deel was the reference for *intent*, not
layout). It is confident, product-led and calm. The changes:

- **Type does the selling.** Archivo at 720–760 weight, 106% width, set very large. The hero is
  centred and close to 6rem.
- **The product is shown as product.** The hero "stage" is a navy panel of illustrated UI cards:
  the team roster, one invoice, overlap hours and a trial ring. They show how an engagement looks.
  They are not screenshots, and they name roles, never people.
- **A self-select question** ("What do you need help with?") with five chips that route to the
  service pages.
- **A ticker of stacks we staff** in place of a logo wall. There are no client logos to show
  honestly, so the ticker shows the skills instead.
- **A bento product grid** of uneven tinted tiles, each with its own mini UI.
- **Soft geometry.** Pill buttons and chips, 14/22/36px radii. Dark and tinted bands sit *inset*
  from the viewport as rounded panels, and so does the footer.
- **The logo hexagon survives** as a faint routed watermark on dark bands and interior heroes.
- **The founder spotlight** uses the real photograph (`assets/img/founder.jpg`) with name and
  location chips.
- The palette is unchanged and comes from the logo. It adds two panel tints, `--mist` `#E6F5FB`
  and `--sky` `#CFEFF8`. Headings are `--ink` `#0A2433`.

Truth constraints are unchanged: no invented stats, logos or testimonials. Every figure on the
page is one the offer already states.

---

## Previous system ("Signal"), kept for reference


---

## The world

**PCB silkscreen and engineering schematic.** The Optiserv logo is a hexagon built from circuit
traces and solder nodes — a genuinely distinctive asset in a category full of abstract swooshes.
The entire system is derived from it.

The thesis the homepage commits to: *a commissioning datasheet for a team you can switch on.*
It refuses the two things every offshore-staffing site ships — the stock-photo handshake hero and
the three-icon service grid.

The grammar is strict, and the strictness is the point:

- Traces turn at **90° and 45° only**, exactly as copper routes on a board. Never a curve.
- Traces terminate in **square solder pads**, never arrowheads or dots.
- Traces carry structure: they connect blocks, mark section boundaries, and underline the one
  word in the headline that matters.
- The hero network draws itself in once via `stroke-dashoffset`, then stops.

## Color

Sampled directly from `Optiserv-Consulting-Logo.webp`.

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#FFFFFF` | dominant ground |
| `--surface` | `#F4F9FB` | alternating section tint |
| `--ink` | `#06212E` | body copy — 16.6:1 |
| `--navy` | `#024C71` | headings, structure, primary buttons — 9.2:1 |
| `--navy-900` | `#01293E` | full-bleed band ground |
| `--cyan` | `#00AAD4` | traces, nodes, accents |
| `--cyan-ink` | `#0089AD` | cyan that must carry meaning on white — 4.1:1 |
| `--grey` | `#696969` | secondary text — 5.5:1 |

**Strategy: restrained ground, committed bands.** White dominates, because the client pinned it.
But a page that is white end to end has no pace, so three regions go full-bleed navy — the
overhead ledger, the overlap strip and the closing CTA. They give the scroll rhythm.

**The cyan rule, which is load-bearing:** `#00AAD4` is 2.7:1 on white. That is below AA for text
*and* below the 3:1 WCAG non-text minimum. So on white it is decoration only — traces, nodes,
rules. Anything that conveys state or focus uses `--cyan-ink` (4.1:1). On navy, cyan reaches
5.6:1 and becomes fully functional. Cyan is therefore rationed on white and generous on navy,
which is both the accessibility answer and the aesthetic one.

## Type

Two families, not three.

- **Archivo** (variable, 100–900 weight, 62–125% width) — display *and* body. Hierarchy comes
  from weight and width, never from swapping family.
- **Martian Mono** (variable) — **figures and dense data only**: the ledger, the overlap strip,
  spec tables, tags. Never a decorative "technical" label.

Both self-hosted as variable woff2 under `assets/fonts/` (~240KB total), so there is no
third-party request on the critical path.

Large display figures use `.num` — Archivo with `tabular-nums` — because Martian Mono reads
visibly smaller beside Archivo at the same size. Mono is reserved for small, dense contexts
where its width is an asset.

Display tracking bottoms out at `-0.03em`. Body measure held to 65–75ch.

## What this system refuses

These were considered and rejected as category defaults, not as bans:

- **Mono eyebrow labels above every section.** One page-level kicker (`.page-kicker`) is a
  system; an eyebrow on every section is grammar you did not choose. Section transitions are
  carried by trace routing and typographic scale instead.
- **01 / 02 / 03 section numbering.** Survives in exactly one place — *How it works* — where the
  sequence genuinely carries information.
- **A grid of same-size icon-heading-text cards as page structure.** The homepage services block
  is a full-width lead station with its own internal composition, plus a supporting row.
- **IBM Plex Mono, Inter-as-display, Space Grotesk.** Training-data defaults that make a design
  guessable from its category alone.
- **Stock faces for real people.** Branded SVG placeholders with initials, labelled
  "PHOTO TO BE ADDED", until real photographs arrive.

## Motion

One authored moment: traces draw themselves in. Everything else is restrained — content rises
12px on reveal, the header swaps background and border on scroll.

No animated layout properties anywhere. The header compacts instantly rather than transitioning
`height`; overlap bars fade in via `opacity` rather than transitioning `left`/`width`.

All motion sits behind `prefers-reduced-motion: reduce`.

**The reveal is scoped behind a `.js` class** set inline in `<head>`. If the script ever fails to
load, `[data-reveal]` is never hidden and the page renders static and complete. This is the single
most important robustness decision in the stylesheet.

## Components

| Class | What it is |
|---|---|
| `.trace-h` / `.node` / `.trace-svg` | the board grammar — rules, pads, routed networks |
| `.navy-band` | full-bleed dark region; flips every text token |
| `.rail` | the four-fact offer strip under the hero |
| `.ledger` | the overhead cost table |
| `.ovl` | the 24-hour timezone overlap strip |
| `.station` (`.lead`, `.third`) | services, deliberately uneven |
| `.steps` / `.step` | the only numbered sequence |
| `.block` / `.g2` `.g3` `.g4` / `.split` | interior page composition |
| `.slot` | an honestly empty proof slot |
| `.checks` | diamond-marked list |
| `.spec` | data table, mono values |
| `.faq` | accordion, correct `aria-expanded`/`aria-controls` |
| `.portrait` + `.ph-tag` | branded person placeholder |
| `.page-hero` + `.page-kicker` | interior opener, one kicker per page |

## Verified

Measured on the built pages, not asserted:

- All 18 pages: exactly one `h1`, no heading-level skips, no duplicate IDs, every image has
  `alt`, canonical + meta description + skip link + `main` landmark present.
- No broken internal links, no missing assets.
- No horizontal overflow at 390px or 1440px.
- Contrast: body 16.6:1, navy 9.2:1, lead 8.6:1, grey 5.5:1, on-navy muted 8.1:1 — all AA.
- Form: empty submit, bad email and valid states all behave; `aria-live` summary fires.
- Accordion toggles `aria-expanded` and `hidden` correctly.
- Overlap arithmetic: UK 8h, US East 4.5h, Australia 7h — standard time, 09:00–18:00 both sides.
- Impeccable design detector: clean.
