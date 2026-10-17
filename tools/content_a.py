# -*- coding: utf-8 -*-
"""About, Team, Services hub."""
from build import ARROW, ARROW_SM, cta, hero, SERVICES


def photo(src, alt, ratio="4 / 5", cls=""):
    """A real photograph in the branded frame."""
    return f"""<div class="portrait photo {cls}" style="aspect-ratio:{ratio}">
          <img src="{src}" alt="{alt}" width="520" height="671" loading="lazy">
        </div>"""


def portrait(initials, ratio="4 / 5", label="Portrait placeholder"):
    """Branded placeholder. We never stand a stock face in for a real person."""
    return f"""<div class="portrait" style="aspect-ratio:{ratio}">
          <svg viewBox="0 0 320 400" role="img" aria-label="{label}">
            <rect width="320" height="400" fill="#EAF3F7"/>
            <path d="M40,300 H110 L160,250 H280" stroke="#A5E2F2" stroke-width="1.25" fill="none"/>
            <path d="M40,340 H140 L180,300 H280" stroke="#A5E2F2" stroke-width="1.25" fill="none"/>
            <rect x="36" y="296" width="8" height="8" fill="#00AAD4"/>
            <rect x="36" y="336" width="8" height="8" fill="#00AAD4"/>
            <text x="160" y="195" text-anchor="middle" font-family="Archivo, sans-serif"
                  font-size="74" font-weight="650" fill="#024C71" letter-spacing="-3">{initials}</text>
          </svg>
          </div>"""


ABOUT = hero(
    "About Optiserv",
    "We take the overhead, you keep the team.",
    "Optiserv Consulting builds and runs dedicated teams for companies in the UK, the US, "
    "Australia and Canada, delivered from Hyderabad and Cebu. We employ the people, so you "
    "do not have to.",
) + """
  <section class="section wrap">
    <div class="split">
      <div data-reveal>
        <h2>Who we are</h2>
      </div>
      <div class="prose" data-reveal style="--d:80ms">
        <p>
          Hiring abroad is rarely blocked by a shortage of good people. It is blocked by
          everything attached to employing them &mdash; an entity, a payroll, a contract that
          holds up, a desk, a laptop, an IT policy, and somebody senior enough to notice when
          things drift.
        </p>
        <p>
          Optiserv exists to carry that part. We source and vet the people, employ them on our
          books in India or the Philippines, give them a seat and the equipment to do the job,
          and put an account manager over the engagement. What reaches you is a named person
          who turns up to your stand-up and works on your product.
        </p>
        <p>
          We also run recruitment as a standalone service for roles you want on your own
          payroll, and we automate work where automating it is plainly better than staffing it.
        </p>
      </div>
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap">
      <div class="g2">
        <div class="block" data-reveal>
          <div class="block-mark"><span class="node" aria-hidden="true"></span>Vision</div>
          <h3 style="font-size:var(--t-d3)">Be a preferred partner to our valued customers by delivering sustainable and innovative technology solutions.</h3>
        </div>
        <div class="block" data-reveal style="--d:80ms">
          <div class="block-mark"><span class="node" aria-hidden="true"></span>Mission</div>
          <h3 style="font-size:var(--t-d3)">Empower all our customers with sustainability and excellence through strategic technology partnership.</h3>
        </div>
      </div>
    </div>
  </section>

  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>RISE</h2>
      <p class="lead">Four words we use to settle arguments internally. They are not decoration &mdash; they are the tie-breakers.</p>
    </div>
    <div class="g4">
      <div class="block" data-reveal>
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Respect</div>
        <h3 class="hsub">Different views, taken seriously</h3>
        <p>Teams spread across three continents only work if difference is treated as information rather than friction.</p>
      </div>
      <div class="block" data-reveal style="--d:70ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Integrity</div>
        <h3 class="hsub">What we say holds up</h3>
        <p>We would rather lose a deal than win it on a number we cannot evidence. That rule shaped this website.</p>
      </div>
      <div class="block" data-reveal style="--d:140ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Sustainability</div>
        <h3 class="hsub">Built to last past the first quarter</h3>
        <p>Retention matters more than placement. A team that stays is worth more to you than a team that is cheap.</p>
      </div>
      <div class="block" data-reveal style="--d:210ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Excellence</div>
        <h3 class="hsub">Better than last month</h3>
        <p>Performance is tracked and reviewed, and the account manager owns the gap when there is one.</p>
      </div>
    </div>
  </section>

  <section class="section surface">
    <div class="wrap split">
      <div data-reveal>
        <h2>Why companies pick us</h2>
      </div>
      <ul class="checks" data-reveal style="--d:80ms">
        <li><div><b>You direct the work, we employ the people.</b> No agency margin on a body you still have to manage yourself.</div></li>
        <li><div><b>Two delivery centres, one contract.</b> Hyderabad and Cebu give you a genuine choice of timezone and cost base.</div></li>
        <li><div><b>Shift hours are a decision, not an excuse.</b> We staff to your working day, including the evening shifts that make a US overlap real.</div></li>
        <li><div><b>A 30-day trial before you commit.</b> If the person is not right, that is our problem to fix, not yours to absorb.</div></li>
        <li><div><b>Scale down as easily as up.</b> The contract flexes with the team rather than against it.</div></li>
      </ul>
    </div>
  </section>

  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Where the work happens</h2>
    </div>
    <div class="g2">
      <div class="block" data-reveal>
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Hyderabad, India</div>
        <h3 class="hsub">Engineering, QA and recruitment</h3>
        <p style="margin-top:var(--s3)">Aditya Trade Centre, #303, 3rd Floor, Ameerpet, Hyderabad 500038, Telangana. Our registered office and the base for most delivery roles.</p>
      </div>
      <div class="block" data-reveal style="--d:80ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Cebu, Philippines</div>
        <h3 class="hsub">Operations and support</h3>
        <p style="margin-top:var(--s3)">Our Philippines delivery centre, giving clients in Australia and on the US west coast a working-day overlap that India alone cannot cover.</p>
      </div>
    </div>
  </section>
""" + cta()


TEAM = hero(
    "People",
    "The people behind the engagement.",
    "An account manager owns your engagement end to end. Below them sit the recruiters who "
    "find your people and the operations team who keep them working.",
) + f"""
  <section class="section wrap">
    <div class="spotlight">
      <div class="spot-photo" data-reveal>
        <img src="assets/img/founder.jpg" alt="Sunil Chandra Goud, founder of Optiserv Consulting" width="520" height="671" loading="lazy">
        <div class="spot-chip spot-chip-name">
          <b data-verify="founder-name">Sunil Chandra Goud</b>
          <span data-verify="founder-title">Founder, Optiserv Consulting</span>
        </div>
        <div class="spot-chip spot-chip-loc"><i aria-hidden="true"></i>Hyderabad, India</div>
      </div>
      <div class="spot-copy" data-reveal style="--d:80ms">
        <h2>From the founder</h2>
        <p class="quote" data-verify="founder-note">
          &ldquo;Most of the companies we talk to do not have a talent problem. They have an
          overhead problem wearing a talent problem&rsquo;s clothes. Our job is to take the
          hiring, the payroll, the desks and the management off your plate, and leave you with
          the one thing you actually wanted: good people, working on your product, at hours
          that match yours.&rdquo;
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="contact.html">Book time with the founder</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section surface">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <h2>The team</h2>
        <p class="lead">The people who run engagements, source your shortlists and keep the operation moving.</p>
      </div>
      <div class="people">
        <div class="person" data-reveal>{photo("assets/img/founder.jpg", "Founder of Optiserv Consulting", "1 / 1")}<b data-verify="founder-name">Sunil Chandra Goud</b><span>Founder</span></div>
        <div class="person" data-reveal style="--d:70ms">{portrait("PS", "1 / 1")}<b data-verify="team-2">Priti Singh</b><span data-verify="team-2-role">CMS Site Manager, India</span></div>
        <div class="person" data-reveal style="--d:140ms">{portrait("SR", "1 / 1")}<b data-verify="team-3">Satyapraveen Reddy</b></div>
        <div class="person" data-reveal style="--d:210ms">{portrait("PR", "1 / 1")}<b data-verify="team-4">Praveen Reddy</b></div>
      </div>
    </div>
  </section>

  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Who you actually deal with</h2>
      <p class="lead">Three functions sit behind every engagement. You will know the first one by name.</p>
    </div>
    <div class="g3">
      <div class="block" data-reveal>
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Account management</div>
        <h3 class="hsub">One named owner</h3>
        <p style="margin-top:var(--s3)">A single person responsible for your engagement end to end &mdash; performance reviews, escalations, and raising problems before you notice them.</p>
      </div>
      <div class="block" data-reveal style="--d:70ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Recruitment</div>
        <h3 class="hsub">Specialists by discipline</h3>
        <p style="margin-top:var(--s3)">Recruiters who source against a written brief in their own discipline, rather than generalists working from a keyword list.</p>
      </div>
      <div class="block" data-reveal style="--d:140ms">
        <div class="block-mark"><span class="node" aria-hidden="true"></span>Operations</div>
        <h3 class="hsub">The part you never see</h3>
        <p style="margin-top:var(--s3)">Payroll, contracts, IT, equipment and the office seats in both centres &mdash; run by people whose whole job that is.</p>
      </div>
    </div>
  </section>
""" + cta("Want to meet the team first?",
          "We will put you on a call with the account manager who would actually run your engagement, not a salesperson.")


_svc_cards = "\n".join(f"""      <a class="block" href="{h}" style="text-decoration:none" data-reveal>
        <div class="block-mark"><span class="node" aria-hidden="true"></span>NET 0{i+1}</div>
        <h3 class="hsub">{label}</h3>
        <p>{sub}.</p>
        <span class="link" style="margin-top:var(--s5)">Read more {ARROW_SM}</span>
      </a>""" for i, (h, label, sub) in enumerate(SERVICES))

SERVICES_HUB = hero(
    "Services",
    "Four ways to add capacity.",
    "Start with one person or a whole function. Everything below runs on the same contract, "
    "the same account manager and the same 30-day trial.",
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>What each one covers</h2>
    </div>
    <div class="g3">
{_svc_cards}
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <h2>Not sure which one you need?</h2>
        <p class="lead">A short rule of thumb, and then a call where we work it out properly.</p>
      </div>
      <ul class="checks" data-reveal style="--d:80ms">
        <li><div><b>The work is ongoing and you want it owned.</b> Dedicated staffing. The person is yours day to day; the employment is ours.</div></li>
        <li><div><b>The work is a function, not a role.</b> Operational staffing. HR, payroll, infrastructure or team management as a unit.</div></li>
        <li><div><b>You want the person on your own payroll.</b> Recruitment and RPO. We find and vet; you employ.</div></li>
        <li><div><b>The task repeats identically every time.</b> Automation. Staffing a loop is the expensive way to run one.</div></li>
      </ul>
    </div>
  </section>
""" + cta()
