# -*- coding: utf-8 -*-
"""The five service pages."""
from build import ARROW, ARROW_SM, cta, hero


def faq(items):
    rows = []
    for i, (q, a) in enumerate(items):
        rows.append(f"""      <div class="faq-item">
        <h3 style="font-size:inherit;margin:0">
          <button type="button" aria-expanded="false" aria-controls="faq-{i}">
            <span>{q}</span><span class="faq-ic" aria-hidden="true"></span>
          </button>
        </h3>
        <div class="faq-panel" id="faq-{i}" hidden>{a}</div>
      </div>""")
    return f"""
  <section class="section wrap">
    <div class="section-head" data-reveal><h2>Questions we get asked</h2></div>
    <div class="faq" data-accordion data-reveal>
{chr(10).join(rows)}
    </div>
  </section>
"""


def capability_grid(items):
    out = []
    for i, (mark, title, body) in enumerate(items):
        out.append(f"""      <div class="block" data-reveal style="--d:{i*60}ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>{mark}</div>
        <h3 class="hsub">{title}</h3>
        <p style="margin-top:var(--s3)">{body}</p>
      </div>""")
    return chr(10).join(out)


STAFF_AUG = hero(
    "Dedicated staffing",
    "Engineers who work only on your product.",
    "Developers, QA engineers, designers and analysts, employed by us in Hyderabad or Cebu and "
    "embedded in your team. They do not rotate between clients and they do not disappear when "
    "another account gets busy.",
    f'<a class="btn btn-primary" href="contact.html">Scope a role {ARROW}</a>'
    '<a class="btn btn-ghost" href="pricing.html">See pricing</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>What we staff</h2>
      <p class="lead">Build, test and design roles, at the seniority the work actually needs.</p>
    </div>
    <div class="g3">
{capability_grid([
  ("Development", "Web and backend", "Product and platform engineers across Java, .NET, Python, Node and the JavaScript ecosystem, working in your repo and your release process."),
  ("Development", "Mobile", "iOS, Android and cross-platform engineers, including release management and store submission."),
  ("Testing", "Quality assurance", "Manual and automation engineers who own regression, release sign-off and defect triage. See <a class=\"link\" href=\"qa-testing.html\" style=\"font-size:inherit\">QA &amp; testing</a>."),
  ("Design", "UI and UX", "Product designers and UI engineers working in your design system rather than inventing a parallel one."),
  ("Data", "Analytics", "Analysts and data engineers for reporting, pipelines and the dashboards your team actually opens."),
  ("Enterprise", "Platform specialists", "Salesforce, SAP S/4HANA, Pega, SailPoint and CyberArk practitioners for platform-specific work."),
])}
    </div>
  </section>

  <section class="section surface">
    <div class="wrap split">
      <div data-reveal>
        <h2>Technologies we recruit for</h2>
        <p class="lead" style="margin-top:var(--s5)">
          If a stack is not listed, ask. This is where we have active bench depth rather than
          an exhaustive list of everything we would be willing to try.
        </p>
      </div>
      <div data-reveal style="--d:80ms">
        <table class="spec">
          <tr><th>Backend</th><td>Java · .NET · Python · Node.js</td></tr>
          <tr><th>Frontend</th><td>ReactJS · Angular · NextJS</td></tr>
          <tr><th>Mobile</th><td>iOS · Android · cross-platform</td></tr>
          <tr><th>Quality</th><td>Selenium · Nightwatch.js · QTP</td></tr>
          <tr><th>Platform</th><td>DevOps · Salesforce · SAP S/4 HANA · Pega</td></tr>
          <tr><th>Identity &amp; security</th><td>SailPoint · CyberArk · MS Entra ID</td></tr>
        </table>
      </div>
    </div>
  </section>

  <section class="section wrap">
    <div class="section-head" data-reveal><h2>How an engagement runs</h2></div>
    <ol class="steps">
      <li class="step" data-reveal><div class="step-n">STEP 01</div><h3 class="hsub">Role brief</h3><p>Stack, seniority, working hours and the definition of a good first month.</p><div class="step-when">You and us</div></li>
      <li class="step" data-reveal style="--d:70ms"><div class="step-n">STEP 02</div><h3 class="hsub">Shortlist</h3><p>We source and vet against the brief. You interview everyone you want to.</p><div class="step-when">You decide</div></li>
      <li class="step" data-reveal style="--d:140ms"><div class="step-n">STEP 03</div><h3 class="hsub">Onboard</h3><p>Seat, laptop, accounts and access. They join your rituals from week one.</p><div class="step-when">Day 1</div></li>
      <li class="step" data-reveal style="--d:210ms"><div class="step-n">STEP 04</div><h3 class="hsub">Review</h3><p>Your account manager runs performance checks and owns any gap.</p><div class="step-when">Ongoing</div></li>
    </ol>
  </section>
""" + faq([
  ("Who do they actually report to?",
   "<p>Day to day, you. They take work from your backlog, join your stand-ups and are reviewed against your definition of done. We stay responsible for employment, performance management and anything to do with their contract, pay or equipment.</p>"),
  ("Can they work our hours?",
   "<p>Yes, and this is the part most people underestimate. We staff to shift. A UK-facing team runs an afternoon-to-evening shift in Hyderabad; an Australia-facing team runs a normal day in Cebu. Our own current job postings include a 3:30 PM to midnight shift for exactly this reason.</p>"),
  ("What if the person is not right?",
   '<p data-verify="trial-terms">There is a 30-day trial. The precise terms are being finalised and will be published on the <a class="link" href="pricing.html" style="font-size:inherit">pricing page</a> rather than described vaguely here.</p>'),
  ("Is there a minimum team size?",
   "<p>No. One person is a normal way to start, and most engagements that grow started that way.</p>"),
]) + cta()


OPERATIONAL = hero(
    "Operational staffing",
    "The functions around the product.",
    "HR, payroll, infrastructure and team management, staffed as a unit. The work that keeps a "
    "growing company running, and that usually lands on whoever has least time to refuse it.",
    f'<a class="btn btn-primary" href="contact.html">Talk it through {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>What we cover</h2>
      <p class="lead">Staffed roles, not a managed service you have no visibility into.</p>
    </div>
    <div class="g2">
{capability_grid([
  ("HR", "People operations", "Onboarding, records, leave, performance paperwork and the day-to-day questions that otherwise reach a founder."),
  ("Finance", "Payroll administration", "Payroll runs, statutory filings and the reconciliation around them, handled by people who do it every month."),
  ("Technology", "Infrastructure and IT support", "Device provisioning, access management, helpdesk and the security hygiene that audits ask about."),
  ("Delivery", "Team management", "Team leads and coordinators who hold a distributed group together, run the rituals and escalate early."),
])}
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap split">
      <div data-reveal><h2>When this makes sense</h2></div>
      <ul class="checks" data-reveal style="--d:80ms">
        <li><div>Your engineers are spending real hours on IT, access and onboarding admin.</div></li>
        <li><div>Payroll and HR are being run by somebody whose job title says something else.</div></li>
        <li><div>You are opening a second location and the operational load is about to double.</div></li>
        <li><div>You have the headcount budget but not the management bandwidth to supervise it.</div></li>
      </ul>
    </div>
  </section>
""" + faq([
  ("How is this different from an outsourced BPO?",
   "<p>You get named people, not a queue. They sit in your tools, attend your meetings where it makes sense, and you can speak to them directly. We employ them; you work with them.</p>"),
  ("Can we start with one function?",
   "<p>Yes. Most engagements start with whichever function is causing the most friction, usually IT support or payroll, and expand once it is working.</p>"),
  ("Do they cover our timezone?",
   '<p>Yes &mdash; shift is a staffing decision. See the overlap table on the <a class="link" href="index.html#main" style="font-size:inherit">home page</a> for how the hours actually work out by market.</p>'),
]) + cta()


RPO = hero(
    "Recruitment &amp; RPO",
    "Hiring run as a process, not a scramble.",
    "For roles you intend to put on your own payroll. We take the sourcing, screening and "
    "scheduling, and hand you a shortlist worth interviewing.",
    f'<a class="btn btn-primary" href="contact.html">Discuss a hiring plan {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Three engagement models</h2>
      <p class="lead">Pick the one that matches how much of the process you want to keep.</p>
    </div>
    <div class="g3">
{capability_grid([
  ("Model 01", "Full-cycle RPO", "We own the hiring process end to end &mdash; workforce forecasting, sourcing, screening, scheduling, offer management and onboarding."),
  ("Model 02", "Project RPO", "A dedicated recruiting team stood up for a defined push: a funding round, a new market, a product launch. It ends when the hiring does."),
  ("Model 03", "Recruiter on demand", "One or more recruiters added to your existing talent team for a specific discipline or a specific stretch."),
])}
    </div>
  </section>

  <section class="section surface">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <h2>What outsourcing the process changes</h2>
      </div>
      <div class="g2">
        <div data-reveal>
          <ul class="checks">
            <li><div><b>Cost per hire.</b> No per-role agency placement fee. Sourcing cost is absorbed into the engagement rather than charged again on every hire.</div></li>
            <li><div><b>Time to hire.</b> A team working one brief, rather than a contingency recruiter splitting attention across a dozen open roles at other companies.</div></li>
            <li><div><b>Candidate experience.</b> Scheduling, feedback and offer communication stop slipping, which is where most good candidates are actually lost.</div></li>
          </ul>
        </div>
        <div data-reveal style="--d:80ms">
          <ul class="checks">
            <li><div><b>Quality of shortlist.</b> Structured screening against a written brief, so you interview four people rather than fourteen.</div></li>
            <li><div><b>Scalability.</b> Hiring volume can double for a quarter without you hiring recruiters to hire people.</div></li>
            <li><div><b>Employer brand.</b> Consistent, prompt communication with every candidate, including the ones you reject.</div></li>
          </ul>
        </div>
      </div>
    </div>
  </section>
""" + faq([
  ("Do you recruit outside India and the Philippines?",
   "<p>Our sourcing strength is in India and the Philippines. For other markets, talk to us first &mdash; we will tell you honestly whether we are the right partner for that search.</p>"),
  ("How do you charge for RPO?",
   "<p>It depends on the model and the volume. Full-cycle and project RPO are usually priced per engagement; recruiter on demand is usually priced monthly. We will give you a number on the call rather than a range on a webpage.</p>"),
  ("Can RPO and dedicated staffing run together?",
   "<p>Yes, and it is a common combination: dedicated staff for the roles you want us to employ, RPO for the roles you want on your own books.</p>"),
]) + cta()
