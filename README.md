# Optiserv Consulting — website

Static marketing site. 18 pages of plain HTML, one stylesheet, one script, no framework and
no build step required to run or deploy it.

```
index.html … 404.html        18 pages, ready to serve
assets/css/main.css          design tokens + every component
assets/js/main.js            nav, reveal, overlap table, form, cookie banner
assets/fonts/                Archivo + Martian Mono, self-hosted variable woff2
assets/img/logo.webp         the logo
sitemap.xml · robots.txt
VERIFY.md                    every claim still awaiting confirmation  ← read this first
tools/                       optional generator (see below)
docs/superpowers/            the design spec and implementation plan
PRODUCT.md                   product truth, positioning, constraints
```

## Running it

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Deploy by uploading the whole folder to any static host (Netlify, Cloudflare Pages, S3, Apache,
nginx). There is nothing to compile.

---

## Before this goes live

**Read `VERIFY.md`.** It lists 30 markers in the HTML covering claims, figures, names, addresses
and legal text that are not yet confirmed. Each renders on the page as a visible, labelled
placeholder — the site never states an unverified thing as fact.

Three that block an ad campaign specifically:

1. **The form has no endpoint.** `contact.html` validates fully but `<form id="enquiry">` has no
   `action`. Until you add one, submitting shows a message telling the visitor to email instead —
   it does not pretend to have sent. See *Wiring the form* below.
2. **`sunil.s@optiservconsulting.com` must exist.** Every page links to it. The old personal address
   was removed deliberately, per the internal checklist.
3. **No analytics is loaded.** The cookie banner records consent in `localStorage` under
   `optiserv.cookie.v1`. Add your tags at the marked slot in `assets/js/main.js` (search for
   `Analytics slot`), and only inside the `accept` branch.

---

## Editing content

Every `.html` file in the root is a real, complete page — you can edit one directly and it will
work. **But** the header, footer and cookie banner are duplicated into all 18 pages (deliberately:
it keeps first paint and SEO correct, which matters for paid traffic). Editing the nav by hand
means editing it 18 times.

So there is an optional generator:

```bash
python3 tools/make.py      # rebuild all 18 pages from the shared chrome + content
python3 tools/verify.py    # regenerate VERIFY.md from the markers actually in the HTML
```

| File | Owns |
|---|---|
| `tools/build.py` | `<head>`, header, nav, footer, cookie banner, shared helpers |
| `tools/content_a.py` | About, Team, Services hub |
| `tools/content_b.py` | Dedicated staffing, Operational staffing, Recruitment & RPO |
| `tools/content_c.py` | QA & testing, Automation, Industries, Pricing |
| `tools/content_d.py` | Careers, Insights, Contact, legal pages, 404 |
| `tools/_home_main.html` | the homepage body |
| `tools/make.py` | assembles everything, writes `sitemap.xml` and `robots.txt` |

If you would rather not use Python at all, delete `tools/` and hand-edit the HTML. Nothing in the
shipped site depends on it.

### Adding a nav item

Edit `SERVICES` in `tools/build.py` (for the Services dropdown) or the `<ul class="nav">` block in
the same file, then run `python3 tools/make.py`.

---

## Wiring the form

`assets/js/main.js` already handles validation, inline errors, an `aria-live` error summary and
the disabled/sending state. You only need a destination.

**Formspree / Web3Forms / Basin** — add the action and method to the `<form>` in
`tools/content_d.py`, then rebuild:

```html
<form id="enquiry" novalidate action="https://formspree.io/f/YOUR_ID" method="POST">
```

The script detects the `action` and lets the browser submit normally.

---

## Design system

Everything is driven by custom properties at the top of `assets/css/main.css`. Changing the
palette is a one-line edit per token.

| Token | Value | Use |
|---|---|---|
| `--navy` | `#024C71` | headings, structure, primary buttons |
| `--cyan` | `#00AAD4` | traces, nodes, accents |
| `--grey` | `#696969` | secondary text |
| `--navy-900` | `#01293E` | full-bleed band backgrounds |
| `--bg` | `#FFFFFF` | dominant background |

All three brand colors are sampled directly from `Optiserv-Consulting-Logo.webp`.

**One accessibility constraint worth knowing:** `--cyan` on white is below WCAG AA for body text.
It is therefore used only for graphical elements (1px+ traces, nodes, rules) and on navy
backgrounds, where it reaches 5.55:1. Do not set paragraph text in cyan on white.
Where cyan must carry meaning on white — focus rings, the FAQ state icon — the darker
`--cyan-ink` (`#0089AD`, 4.05:1) is used instead.

**Typefaces.** Archivo (display and body, variable weight + width) and Martian Mono (figures and
dense data only — never as a decorative label). Both self-hosted under `assets/fonts/`, so there
is no third-party request on the critical path.

**Motion.** All of it sits behind `prefers-reduced-motion: reduce`. The reveal animation is scoped
behind a `.js` class set inline in `<head>`, so if the script ever fails to load, nothing is
hidden — the page just renders static.

---

## Browser support

Modern evergreen browsers. Degrades gracefully:

- **JavaScript off** — every page is fully readable and navigable; the form still submits once an
  endpoint is set; the overlap table shows the UK figures as authored in the HTML.
- **`IntersectionObserver` missing** — all content renders immediately.
- **`localStorage` blocked** — the cookie banner fails silently rather than throwing.
