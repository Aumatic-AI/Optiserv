# -*- coding: utf-8 -*-
"""Case studies — one continuous list, no category sections.

Seven entries covering every service, ordered for narrative strength rather than
grouped by type. Each entry carries its own badge:

  DELIVERED    Real work we have shipped. Kinetix and Atlas are the names of the
               SYSTEMS built, not client names — the clients themselves are
               described by sector only.

  ILLUSTRATIVE An engagement pattern. Real operational detail (team composition,
               shift pattern, sequence) but no named client and no delivered
               metric. Replace with a real case study once a client gives written
               permission. See VERIFY.md.
"""
from build import ARROW, ARROW_SM, cta, hero


def entry(sector, service, title, outcome, rows, tags, kind="real"):
    # Self-describing labels, so the page needs no legend to be read correctly.
    badge = ('<span class="badge badge-real">DELIVERED PROJECT</span>' if kind == "real"
             else '<span class="badge badge-illus">ENGAGEMENT PATTERN</span>')
    defs = "\n".join(f'        <div><dt>{dt}</dt><dd>{dd}</dd></div>' for dt, dd in rows)
    tagmk = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""      <article class="cs" data-reveal>
        <div>
          <div class="cs-mark">{badge}<b>{sector}</b><span class="sep">/</span><span>{service}</span></div>
          <h2>{title}</h2>
          <p class="cs-outcome">{outcome}</p>
        </div>
        <div>
          <dl class="cs-grid">
{defs}
          </dl>
          <div class="cs-tags">{tagmk}</div>
        </div>
      </article>"""


ENTRIES = [
    # 1 — dedicated staffing, the core offer
    entry(
        "SaaS, United Kingdom", "Dedicated staffing",
        "An engineering pod with a real afternoon overlap",
        "Pattern: 3&ndash;5 engineers &middot; 13:30&ndash;22:30 IST &middot; 8 h live overlap with London",
        [("Shape", "Two to four engineers plus a QA engineer, working the client&rsquo;s backlog, in the client&rsquo;s repo, inside the client&rsquo;s stand-up. Employed by us, directed by them."),
         ("Why the shift matters", "On a standard Indian day a London team gets about three and a half hours of overlap. Moved to 13:30&ndash;22:30 IST, the same team is online for eight of London&rsquo;s nine working hours."),
         ("What we carry", "Employment, payroll, office seat, equipment, IT and an account manager. The client carries the roadmap and nothing else.")],
        ["ReactJS", "Node.js", "Shift alignment"], kind="illustrative"),

    # 2 — automation, real
    entry(
        "Automation", "Built for a marketing agency", "Kinetix",
        "One agency ad&rsquo;s budget now tests many in a day.",
        [("The system", "<b>Kinetix</b> &mdash; an AI ad-generation platform we designed and built, with automated A/B testing and budget reallocation built in."),
         ("Problem", "Ad production and budget allocation were manual. One concept at a time reached the market, and the spend behind it was reallocated by hand, after the fact."),
         ("Effect", "Variants are produced, tested and funded without a person in the loop. A single budget exercises many creative variants inside a day instead of one at a time across a cycle.")],
        ["AI generation", "A/B testing", "Budget automation"]),

    # 3 — QA as a standing squad
    entry(
        "iGaming", "QA &amp; testing", "A release-QA squad on the operator&rsquo;s train",
        "Pattern: 4&ndash;6 QA engineers &middot; Hyderabad &middot; release-aligned shift",
        [("Shape", "A lead plus three to five engineers, split between manual release validation and an automated regression suite that grows with each cycle."),
         ("Why offshore works here", "Release QA is cyclical and intense. Carrying that capacity in-house means paying for peak staffing year-round; carrying it with us means the squad flexes with the release calendar."),
         ("Shift", "Aligned to the operator&rsquo;s release windows rather than to Indian office hours, so sign-off never waits a timezone.")],
        ["Release QA", "Selenium", "Game testing"], kind="illustrative"),

    # 4 — automation, real
    entry(
        "Automation", "Built for a B2B sales team", "Atlas",
        "A 5-tool workflow collapsed into one system.",
        [("The system", "<b>Atlas</b> &mdash; a unified outbound dashboard we designed and built, covering prospecting, personalised outreach and intent classification in one place."),
         ("Problem", "Outbound ran across five disconnected tools. Prospecting, personalisation and qualification each lived somewhere else, and the handoffs leaked."),
         ("Effect", "The workflow stops being a chain of exports between tools and becomes a single system with one place to look.")],
        ["Prospecting", "Intent classification", "Consolidation"]),

    # 5 — RPO
    entry(
        "Scale-up", "Recruitment &amp; RPO", "A hiring surge that does not require hiring recruiters",
        "Pattern: dedicated recruiting team &middot; fixed window &middot; roles land on the client&rsquo;s payroll",
        [("Shape", "A recruiting team stood up for a defined push &mdash; a funding round, a market entry, a product launch &mdash; running sourcing, screening, scheduling and offer management."),
         ("Why project rather than full-cycle", "The need has an end date. Full-cycle RPO suits a standing hiring function; a surge suits a team that stands down when the surge does."),
         ("Where the people land", "On the client&rsquo;s own payroll. This is recruitment, not staffing &mdash; we find and vet, the client employs.")],
        ["Full-cycle sourcing", "Structured screening", "Offer management"], kind="illustrative"),

    # 6 — operational staffing
    entry(
        "Scaling company", "Operational staffing", "The back office, staffed before it breaks",
        "Pattern: 2&ndash;4 people &middot; people ops, payroll admin and IT helpdesk as one unit",
        [("Shape", "A small operations unit covering HR records and onboarding, payroll administration and statutory filing, and device provisioning with first-line IT support."),
         ("Why it comes up", "These tasks rarely get a job title until they are already late. They land on a founder at eleven at night, or on an engineer who was hired to build something else."),
         ("What changes", "The function gets an owner who is not also the CTO, and the people who should be building go back to building.")],
        ["People ops", "Payroll admin", "IT helpdesk"], kind="illustrative"),

    # 7 — QA as a scoped project
    entry(
        "Regulated sector", "QA &amp; testing", "An accessibility and performance programme with a deadline",
        "Pattern: scoped project &middot; Section 508 audit &middot; load and penetration testing",
        [("Shape", "A fixed-scope engagement rather than a standing team: a Section 508 accessibility audit, performance engineering to establish real breaking points, and penetration testing."),
         ("Why project rather than headcount", "A compliance date is a date. It needs a team that arrives, produces evidence against a named standard, and hands over &mdash; not a permanent cost line."),
         ("What is handed over", "Findings mapped to the standard, each with severity, reproduction steps and the remediation it implies. Evidence an auditor will accept, not a summary.")],
        ["Section 508", "Performance engineering", "Penetration testing"], kind="illustrative"),
]


CASE_STUDIES = hero(
    "Case studies",
    "Work, and the shape of work.",
    "Projects we have delivered, and the engagement patterns our work follows &mdash; across "
    "dedicated teams, QA, recruitment, operations and automation.",
    f'<a class="btn btn-primary" href="contact.html">Discuss your own {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="cs-list" data-verify="illustrative-engagements">
{chr(10).join(ENTRIES)}
    </div>
  </section>

  <section class="section-tight wrap">
    <hr class="trace-h" style="margin-bottom:var(--s7)">
    <div class="split">
      <div data-reveal>
        <h3 style="font-size:var(--t-d3)">Why we have not filled this page with logos</h3>
      </div>
      <div class="prose" data-reveal style="--d:80ms">
        <p>
          Plenty of firms in this market publish client names and round numbers they cannot
          evidence. We would rather show you real projects, and be straight about which of these
          are delivered work and which describe how we staff an engagement.
        </p>
        <p>
          If you want references, ask on the call. We will put you in touch with people who can
          speak to the work rather than point you at a page.
        </p>
      </div>
    </div>
  </section>
""" + cta("Tell us what you are trying to fix.",
          "Whether it is a team to build or a process to automate, the first call is the same: thirty minutes, no obligation.")
