# VERIFY — claims awaiting confirmation

Generated from the site itself by `python3 tools/verify.py`. Every row below corresponds to a
`data-verify` marker in the HTML. **Nothing in this file is a claim the site currently makes as
fact** — each one renders as a visible, labelled placeholder.

The internal landing-page checklist is explicit about why this file exists:

> "Please do not invent or estimate any claim, number or testimonial."

There are **13** markers across **7** pages.

## How to clear a row

1. Get the confirmed fact from the owner named below.
2. Edit the relevant file in `tools/content_*.py` — replace the placeholder text and delete the
   `data-verify="..."` attribute.
3. Run `python3 tools/make.py` to rebuild, then `python3 tools/verify.py` to regenerate this file.

## Markers in the HTML

| ID | What needs confirming | Source of the claim | Owner | Appears on |
|----|----------------------|---------------------|-------|------------|
| `analytics-provider` | Which analytics provider, and the cookies it sets. | Internal PDF, section F | Marketing | cookies.html |
| `automation-price` | A starting price for automation work, or confirmation that it stays 'scoped per project'. | Internal PDF, section A | Delivery team | automation.html |
| `founder-name` | Founder's name as it should be published. LinkedIn says 'Sunil Chandra Goud'; the supplied photo file is named chandan.webp. CONFIRM WHICH IS CORRECT before launch — the site currently shows the LinkedIn name. | LinkedIn / photo filename | Founder | index.html, team.html |
| `founder-note` | The 70-90 word first-person note. Current text is our draft and must be replaced. | Internal PDF, section B | Founder | index.html, team.html |
| `founder-title` | Founder's exact title. | Inferred | Founder | index.html, team.html |
| `illustrative-engagements` | Five of the seven case-studies entries are engagement PATTERNS, not client outcomes, and are badged ENGAGEMENT PATTERN on the page. Replace each with a real, named case study once a client gives written permission. | Authored for this build | Delivery team / Sales | case-studies.html |
| `payment-terms` | Invoicing currency and payment terms. | Not yet stated anywhere | Management | pricing.html |
| `price-basis` | Whether $1,500 is per person or per team, and whether it varies by role or by India vs Philippines. | Internal PDF, section A | Management | index.html, pricing.html |
| `team-2` | Confirm name, role and photograph. | LinkedIn | HR | team.html |
| `team-2-role` | Confirm this person's role. | LinkedIn | HR | team.html |
| `team-3` | Confirm name, role and photograph. | LinkedIn | HR | team.html |
| `team-4` | Confirm name, role and photograph. | LinkedIn | HR | team.html |
| `trial-terms` | 30-day trial: free or paid, and what happens if the client is not satisfied. Needed as one plain sentence. | Internal PDF, section A | Management | index.html, pricing.html, staff-augmentation.html |

## Decisions taken against the internal checklist

These were raised, discussed and settled. They are recorded here so nobody re-opens them by
accident, and so the divergence from the checklist is deliberate and visible.

| Decision | The checklist said | What was chosen, and by whom |
|---|---|---|
| **Automation case studies carry no partner credit** | Section C: *"Case studies: client type, what they needed, team built, result with numbers. Must be real."* | Kinetix and Atlas are real delivered systems, built with Repeatless as delivery partner. At the client's direction the partner is **not** named on the page &mdash; a standard white-label arrangement where Optiserv is the contracting and accountable party. **Kinetix and Atlas are the names of the systems built, not client names**, so no third-party permission is required to show them; the clients themselves appear by sector only ("a marketing agency", "a B2B sales team"). Confirm only that the commercial arrangement genuinely makes Optiserv accountable for this work. |
| **Contact address is `sunil.s@optiservconsulting.com`** | Section F: *"Company-domain email, for example hello@optiservconsulting.com. No personal email on the page."* | The client directed us to use the existing working address rather than wait on a new mailbox. It is a company-domain address, so it satisfies the first half of the requirement; it is a named individual, so it does not satisfy the second. Revisit if the volume from paid traffic makes a shared inbox preferable. |

## Items the site is waiting on

These come from the internal checklist. Each one renders on the site as a visible,
labelled placeholder until it arrives. Nothing is silently faked.

| # | Item | Owner |
|---|------|-------|
| 1 | 30-day trial terms, written as one plain sentence | Management |
| 2 | Whether $1,500 is per person or per team, and how it varies | Management |
| 3 | Founder photo, name, title, bio, 70-90 word note, LinkedIn URL, booking link | Founder |
| 4 | Names, photographs and roles of account managers and recruiters | HR |
| 5 | Testimonials: quote, name, title, company, photo, **written permission** | Sales |
| 6 | Case studies: client type, need, team built, result with numbers | Delivery |
| 7 | Confirmed figures: clients served, people placed, active team members, retention, days to shortlist, and since when | Management |
| 8 | Client logos we hold written permission to show | Sales |
| 9 | Any real reviews (Google, Clutch, GoodFirms, Trustpilot) or certifications held | Marketing |
| 10 | Cebu office: full address, phone, team size, roles delivered | Operations |
| 11 | Real photographs of both offices and the team | Operations |
| 12 | WhatsApp Business number; virtual UK / US numbers | Management |
| 13 | Registered company name and registration number | Legal |
| 14 | Legal review of Privacy, Terms and Cookie policies | Legal |
| 15 | Form endpoint (Formspree / Web3Forms / custom) and analytics IDs | Marketing |
| 16 | Decision on `optiservsolutions.com` — the checklist flags it for takedown | Management |

## Claims we deliberately did **not** carry over

| Claim on the old site | Why it is gone |
|---|---|
| "Established 10 years ago" / "10+ years of industry experience" | The internal checklist states the company was **incorporated January 2025** and lists this claim as a thing to fix before ads go live. |
| Blank stat counters ("Years of Quality Service", "Skilled IT Resources", "Countries we Operate") | They rendered empty. No number ships unconfirmed. |
| "Specialised talent solutions for telecommunications and service integrators" | Superseded by the current positioning. |
| LinkedIn's "Founded 2017" and "51-200 employees" | Conflicts with the January 2025 incorporation date. Neither is published. |
