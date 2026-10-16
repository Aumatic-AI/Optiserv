# -*- coding: utf-8 -*-
"""QA, Automation, Industries, Pricing."""
from build import ARROW, ARROW_SM, cta, hero
from content_b import faq, capability_grid

QA = hero(
    "QA &amp; testing",
    "Find it before your customers do.",
    "Manual and automated testing, mobile, accessibility, performance and security &mdash; run "
    "by engineers who own release sign-off rather than file tickets over a wall.",
    f'<a class="btn btn-primary" href="contact.html">Scope a QA team {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Functional testing</h2>
      <p class="lead">The day-to-day work of proving a release does what it claims.</p>
    </div>
    <div class="g3">
{capability_grid([
  ("Manual", "Exploratory and scripted", "Test cases written from the spec, executed systematically, with defects documented with reproduction steps and screenshots rather than &ldquo;it broke&rdquo;."),
  ("Automation", "Selenium and Nightwatch.js", "Regression suites that run consistently across environments and browsers, so the same checks happen every release instead of when there is time."),
  ("QTP", "Functional and regression", "QuickTest Professional for validating application behaviour against expected outcomes on platforms that call for it."),
])}
    </div>
  </section>

  <section class="section surface">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <h2>Beyond &ldquo;does it work&rdquo;</h2>
        <p class="lead">The testing that is skipped first and regretted most.</p>
      </div>
      <div class="g4">
{capability_grid([
  ("Mobile", "iOS and Android", "Device and OS coverage, UI responsiveness, and the behaviour that only shows up on a real handset."),
  ("Accessibility", "Section 508", "Compliance testing against Section 508, including screen-reader behaviour and keyboard operation."),
  ("Performance", "Load and scale", "Performance engineering to establish where a system actually breaks, rather than assuming where it might."),
  ("Security", "Penetration testing", "Structured penetration testing to surface vulnerabilities before somebody else does."),
])}
      </div>
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap split">
      <div data-reveal><h2>How QA engagements usually start</h2></div>
      <ul class="checks" data-reveal style="--d:80ms">
        <li><div><b>Regression is eating your sprint.</b> Automating the repeatable half gives the sprint back.</div></li>
        <li><div><b>Releases keep slipping on defects found late.</b> Testing moves earlier, into the branch rather than after the merge.</div></li>
        <li><div><b>You have no QA function yet.</b> One manual engineer first, automation once there is enough stable surface to automate.</div></li>
        <li><div><b>A compliance or accessibility deadline landed.</b> Scoped project work against a named standard.</div></li>
      </ul>
    </div>
  </section>
""" + faq([
  ("Manual or automation first?",
   "<p>Manual, almost always. Automating an interface that is still changing weekly produces a suite you rewrite monthly. We automate once the surface is stable enough that the suite will survive.</p>"),
  ("Do you work in our existing framework?",
   "<p>Yes. We would rather extend what you have than argue for a rewrite. If the existing framework genuinely cannot carry the work, we will say so and explain why.</p>"),
  ("Can QA engineers be dedicated to us?",
   '<p>Yes &mdash; that is the usual arrangement. See <a class="link" href="staff-augmentation.html" style="font-size:inherit">dedicated staffing</a> for how it works contractually.</p>'),
]) + cta()


AUTOMATION = hero(
    "Automation",
    "Staffing a loop is the expensive way to run one.",
    "Test, workflow and reporting automation, scoped per project. Where a task genuinely "
    "repeats, automating it beats hiring for it &mdash; and we will tell you when that is the case.",
    f'<a class="btn btn-primary" href="contact.html">Scope a project {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>What we automate</h2>
    </div>
    <div class="g3">
{capability_grid([
  ("Quality", "Test automation", "Regression suites, smoke tests and CI integration so that a failing build is caught by a machine at 3am rather than a person at 10am."),
  ("Operations", "Workflow automation", "The handoffs between systems that are currently somebody copying a value from one tab into another."),
  ("Reporting", "Data and reporting", "Scheduled extraction, transformation and distribution of the reports that are currently rebuilt by hand every Monday."),
])}
    </div>
  </section>

  <section class="section surface">
    <div class="wrap split">
      <div data-reveal>
        <h2>How a project is scoped</h2>
        <p class="lead" style="margin-top:var(--s5)">
          Automation is priced per project rather than per seat, because the value is in the
          thing built, not the hours spent building it.
        </p>
      </div>
      <ol class="checks" data-reveal style="--d:80ms">
        <li><div><b>Observe.</b> We watch the process as it actually runs, not as the documentation describes it.</div></li>
        <li><div><b>Qualify.</b> Volume, variability and stability. A process that changes every month is usually not ready to automate.</div></li>
        <li><div><b>Scope and price.</b> A fixed scope with a fixed price, and an explicit statement of what is out of scope.</div></li>
        <li><div><b>Build and hand over.</b> Documented, in your repository, with your team able to maintain it.</div></li>
      </ol>
    </div>
  </section>

  <section class="section-tight wrap">
    <hr class="trace-h" style="margin-bottom:var(--s7)">
    <div class="split">
      <div data-reveal>
        <h2 style="font-size:var(--t-d2)">Systems we have built</h2>
      </div>
      <div data-reveal style="--d:80ms">
        <p class="lead" style="max-width:52ch">
          Kinetix, an AI ad-generation platform with automated budget reallocation. Atlas, an
          outbound workflow that replaced five disconnected tools with one dashboard.
        </p>
        <a class="btn btn-ghost" href="case-studies.html" style="margin-top:var(--s6)">
          Read the case studies {ARROW_SM}
        </a>
      </div>
    </div>
  </section>
""" + faq([
  ("What does an automation project cost?",
   '<p data-verify="automation-price">Scoped per project, with a fixed price agreed before work starts. The variable is how much of your process is genuinely repeatable &mdash; which is exactly what the first conversation establishes, at no cost.</p>'),
  ("Will we be locked into you to maintain it?",
   "<p>No. It is built in your repository, in a stack your team can read, and handed over documented. If you want us to maintain it afterwards that is a separate, optional arrangement.</p>"),
  ("When should we not automate?",
   "<p>When the process still changes materially month to month, when the volume is genuinely low, or when the real problem is that the underlying process is wrong. We will say so rather than take the project.</p>"),
]) + cta()


INDUSTRIES = hero(
    "Industries",
    "Where we have built teams.",
    "The mechanics are the same everywhere &mdash; we employ, you direct. What changes is the "
    "shape of the team and the hours it needs to keep.",
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Sectors we staff</h2>
    </div>
    <div class="g2">
{capability_grid([
  ("Sector", "IT &amp; non-IT", "Engineering, support, finance and back-office roles staffed from a single contract. The most common starting point, and the broadest."),
  ("Sector", "E-commerce", "Platform and storefront work, CMS and backend integration, UI and performance improvement, analytics, and paid, organic and lifecycle marketing support. Discovery, strategy, execution, optimisation."),
  ("Sector", "Product companies", "Dedicated squads working alongside your own on your roadmap and your release train, rather than a separate vendor track that has to be integrated later."),
  ("Sector", "Service businesses", "Delivery capacity that scales with the contract book instead of ahead of it, so a won account does not become a resourcing problem."),
  ("Sector", "Consulting firms", "Bench depth on demand. A won pitch becomes a staffed project rather than a scramble, and an unwon one does not leave you carrying idle cost."),
  ("Sector", "iGaming", "Game testing, release QA and operational staffing &mdash; a specialism we have carried since the start, and one of the areas where our bench is deepest."),
])}
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <h2>The method does not change</h2>
        <p class="lead">Whatever the sector, an engagement runs the same four stages.</p>
      </div>
      <ol class="steps">
        <li class="step" data-reveal><div class="step-n">STAGE 01</div><h3 class="hsub">Discovery</h3><p>What you run today, where it strains, and what a good outcome looks like in numbers.</p></li>
        <li class="step" data-reveal style="--d:70ms"><div class="step-n">STAGE 02</div><h3 class="hsub">Strategy</h3><p>A staffing or delivery plan matched to that, with the roles, the hours and the sequence written down.</p></li>
        <li class="step" data-reveal style="--d:140ms"><div class="step-n">STAGE 03</div><h3 class="hsub">Execution</h3><p>People onboarded into your tools and rituals, working to your definition of done.</p></li>
        <li class="step" data-reveal style="--d:210ms"><div class="step-n">STAGE 04</div><h3 class="hsub">Optimisation</h3><p>Reviewed against the original numbers, adjusted where the plan met reality.</p></li>
      </ol>
    </div>
  </section>

  <section class="section-tight wrap">
    <hr class="trace-h" style="margin-bottom:var(--s7)">
    <div class="split">
      <div data-reveal>
        <h2 style="font-size:var(--t-d2)">What this looks like in practice</h2>
      </div>
      <div data-reveal style="--d:80ms">
        <p class="lead" style="max-width:52ch">
          Delivered systems and the engagement patterns our staffing work follows, sector by
          sector.
        </p>
        <a class="btn btn-ghost" href="case-studies.html" style="margin-top:var(--s6)">
          Case studies {ARROW_SM}
        </a>
      </div>
    </div>
  </section>
""" + cta()


PRICING = hero(
    "Pricing",
    "One monthly fee. Everything around the hire included.",
    "No placement fee, no payroll administration, no equipment capex and no recruitment retainer. "
    "You pay for the person; we carry the rest.",
    "", "navy-band",
) + f"""
  <section class="section wrap">
    <div class="split">
      <div data-reveal>
        <div class="price-card">
          <div class="block-mark"><span class="node" aria-hidden="true"></span>Dedicated team member</div>
          <div class="price-amt">
            <b class="num">$1,500</b>
            <span>per month, from</span>
          </div>
          <p class="muted" style="font-size:var(--t-sm)" data-verify="price-basis">
            Per dedicated team member, billed monthly. The rate depends on the role, the
            seniority you need and which delivery centre the person sits in.
          </p>
          <a class="btn btn-primary" href="contact.html">Get a quote for your role {ARROW}</a>
          <p style="margin-top:var(--s4);font-size:var(--t-xs);color:var(--grey);text-align:center">
            30-day trial &middot; no placement fee
          </p>
        </div>
      </div>
      <div data-reveal style="--d:80ms">
        <h2 style="font-size:var(--t-d2)">What the monthly fee covers</h2>
        <ul class="checks" style="margin-top:var(--s5)">
          <li><div><b>Recruitment and vetting.</b> Sourcing, screening and shortlisting for the role, at no separate placement fee.</div></li>
          <li><div><b>Employment, salary and statutory payroll.</b> The person is on our books, in our entity, under local employment law.</div></li>
          <li><div><b>HR and compliance.</b> Contracts, records, leave and the paperwork that comes with employing someone.</div></li>
          <li><div><b>Office seat, power and connectivity.</b> A real desk in Hyderabad or Cebu, not a home-broadband gamble.</div></li>
          <li><div><b>Laptop, peripherals and licences.</b> Provisioned and maintained by us.</div></li>
          <li><div><b>IT support and device security.</b> Access management, helpdesk and security hygiene.</div></li>
          <li><div><b>An account manager.</b> One named person responsible for the engagement and for raising problems before you notice them.</div></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section surface">
    <div class="wrap split">
      <div data-reveal>
        <h2>The 30-day trial</h2>
        <p class="lead" style="margin-top:var(--s5)">
          Thirty days to work with the people we put in front of you, on real work, inside your
          own tools, before the engagement becomes a commitment.
        </p>
      </div>
      <div data-reveal style="--d:80ms">
        <ul class="checks">
          <li><div><b>They start properly.</b> Seat, laptop, accounts and access on day one &mdash; not a trial period spent waiting for a login.</div></li>
          <li><div><b>They work on your backlog.</b> Not a sample task. The trial is only useful if it tests the actual job.</div></li>
          <li><div><b>Your account manager checks in.</b> Twice inside the thirty days, with a written note on how it is going.</div></li>
        </ul>
        <div class="legal-note" data-verify="trial-terms" style="margin-top:var(--s6);margin-bottom:0">
          <b style="color:var(--navy)">Thirty days is long enough to know.</b><br>
          Long enough to see how someone handles a real ticket, a code review and a
          disagreement &mdash; which is what you are actually buying. If it is not working,
          say so and we will deal with it. The exact terms are set out in your contract
          before you commit to anything.
        </div>
      </div>
    </div>
  </section>

  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Other services</h2>
    </div>
    <div class="g3">
      <div class="block" data-reveal>
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Recruitment &amp; RPO</div>
        <h3 class="hsub">Priced per engagement</h3>
        <p style="margin-top:var(--s3)">Full-cycle and project RPO are priced per engagement; a recruiter on demand is priced monthly. Depends on volume and discipline.</p>
      </div>
      <div class="block" data-reveal style="--d:70ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Automation</div>
        <h3 class="hsub">Scoped per project</h3>
        <p style="margin-top:var(--s3)">Fixed scope, fixed price, with what is out of scope written down alongside what is in it.</p>
      </div>
      <div class="block" data-reveal style="--d:140ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Operational staffing</div>
        <h3 class="hsub">Same monthly basis</h3>
        <p style="margin-top:var(--s3)">HR, payroll, infrastructure and team management roles are priced on the same per-person monthly basis.</p>
      </div>
    </div>
  </section>
""" + faq([
  ("Is $1,500 per person or for a whole team?",
   '<p data-verify="price-basis">Per dedicated team member. It is a starting rate &mdash; a senior engineer costs more than a junior one, and Hyderabad and Cebu price differently. Tell us the role and we will give you the actual figure rather than a range.</p>'),
  ("Are there setup fees?",
   "<p>No placement fee and no recruitment retainer for dedicated staffing. If a role needs unusual equipment or licensing, we will tell you before you commit, not after.</p>"),
  ("What currency and payment terms?",
   '<p data-verify="payment-terms">Invoicing currency and payment terms are set out in your contract. Most clients invoice monthly in USD or GBP; tell us what suits your finance team and we will work to it.</p>'),
  ("What happens if we need to scale down?",
   "<p>Notice terms are set in the contract and are deliberately not punitive. The point of this model is that capacity can move in both directions.</p>"),
]) + cta("Get a number for your actual role.",
         "Tell us the role, the seniority and the hours you need covered, and we will come back with a real figure rather than a range.")
