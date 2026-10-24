# -*- coding: utf-8 -*-
"""Careers, Insights, Contact, legal pages, 404."""
from build import ARROW, ARROW_SM, cta, hero, EMAIL
from content_b import faq

CAREERS = hero(
    "Careers",
    "Work with teams that actually ship.",
    "We hire in Hyderabad and Cebu for roles on client engagements and for our own operations. "
    "You are employed by Optiserv, with a seat, equipment and an account manager behind you.",
    f'<a class="btn btn-primary" href="mailto:{EMAIL}?subject=Application">Send us your CV {ARROW}</a>',
) + f"""
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Open roles</h2>
      <p class="lead">Carried over from our previous listings. Confirm current status with us before applying.</p>
    </div>

    <div data-reveal>
      <article class="job">
        <div>
          <h3 class="hsub">Senior Developer &mdash; NestJS, NextJS, GraphQL and Automation</h3>
          <p>Server-side and front-end development across NestJS and NextJS with GraphQL, plus hands-on test automation. For an engineer who is comfortable owning a feature from schema to screen.</p>
          <div class="job-meta"><span class="tag">Remote</span><span class="tag">Full-time</span><span class="tag">NestJS</span><span class="tag">NextJS</span><span class="tag">GraphQL</span></div>
        </div>
        <a class="btn btn-ghost" href="mailto:{EMAIL}?subject=Senior%20Developer%20application">Apply</a>
      </article>

      <article class="job">
        <div>
          <h3 class="hsub">MS Entra ID Developer</h3>
          <p>Identity and Access Management work focused on administering and integrating a Microsoft Entra ID environment. Suits someone who has run IAM in production rather than only configured it in a lab.</p>
          <div class="job-meta"><span class="tag">Remote</span><span class="tag">Full-time</span><span class="tag">Entra ID</span><span class="tag">IAM</span></div>
        </div>
        <a class="btn btn-ghost" href="mailto:{EMAIL}?subject=MS%20Entra%20ID%20Developer%20application">Apply</a>
      </article>

      <article class="job">
        <div>
          <h3 class="hsub">Automation Test Engineer &mdash; Nightwatch</h3>
          <p>Building and maintaining automation frameworks in Nightwatch.js. This role runs a 3:30 PM to 12:00 AM shift to overlap with client working hours.</p>
          <div class="job-meta"><span class="tag">Remote</span><span class="tag">Full-time</span><span class="tag">15:30&ndash;00:00 IST</span><span class="tag">Nightwatch.js</span></div>
        </div>
        <a class="btn btn-ghost" href="mailto:{EMAIL}?subject=Automation%20Test%20Engineer%20application">Apply</a>
      </article>
    </div>
  </section>

  <section class="section navy-band">
    <div class="wrap split">
      <div data-reveal><h2>What you get working here</h2></div>
      <ul class="checks" data-reveal style="--d:80ms">
        <li><div><b>A real desk.</b> An office seat in Hyderabad or Cebu, with equipment and IT support provided.</div></li>
        <li><div><b>One client, properly.</b> You are dedicated to an engagement rather than split three ways across accounts.</div></li>
        <li><div><b>Shift clarity.</b> Where a role needs an evening shift to overlap with a client, it says so in the posting.</div></li>
        <li><div><b>An account manager.</b> Someone whose job is to notice when something is going wrong for you, not only for the client.</div></li>
      </ul>
    </div>
  </section>

  <section class="section-tight wrap">
    <hr class="trace-h" style="margin-bottom:var(--s7)">
    <div class="section-head" data-reveal>
      <h3 style="font-size:var(--t-d3)">Nothing matching right now?</h3>
      <p class="muted" style="font-size:var(--t-sm);margin-top:var(--s3)">
        We recruit continuously for client engagements across engineering, QA, design and
        operations. Send a CV and tell us what you want to work on.
      </p>
    </div>
    <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Speculative%20application">Send a speculative application {ARROW}</a>
  </section>
"""


INSIGHTS = hero(
    "Insights",
    "Notes on building teams abroad.",
    "Practical writing on offshore hiring, timezone overlap, QA practice and the economics of "
    "headcount. Published when we have something worth saying.",
) + """
  <section class="section wrap">
    <div class="section-head" data-reveal>
      <h2>Coming soon</h2>
    </div>

    <div data-reveal>
      <article class="art" aria-disabled="true">
        <div class="art-meta"><span>COMING SOON</span><span>OFFSHORE HIRING</span></div>
        <h3 class="hsub">What a hire actually costs once you count the nine lines underneath the salary</h3>
        <p>A line-by-line breakdown of recruitment, payroll, HR, seat, equipment, IT and management load &mdash; and which of them disappear under a dedicated-team model.</p>
      </article>
      <article class="art" aria-disabled="true">
        <div class="art-meta"><span>COMING SOON</span><span>DISTRIBUTED TEAMS</span></div>
        <h3 class="hsub">Timezone overlap is a shift decision, not a geography problem</h3>
        <p>How many live hours you actually get with Hyderabad or Cebu from London, New York and Sydney, and what shift pattern buys each one.</p>
      </article>
      <article class="art" aria-disabled="true">
        <div class="art-meta"><span>COMING SOON</span><span>QUALITY</span></div>
        <h3 class="hsub">When to automate a test suite, and when automating it is the expensive mistake</h3>
        <p>The stability threshold a surface has to cross before an automated suite stops costing more to maintain than it saves.</p>
      </article>
      <article class="art" aria-disabled="true">
        <div class="art-meta"><span>COMING SOON</span><span>RECRUITMENT</span></div>
        <h3 class="hsub">Why good candidates drop out at the scheduling stage</h3>
        <p>The unglamorous process failures that lose more strong hires than compensation does.</p>
      </article>
    </div>
  </section>
""" + cta()


CONTACT_HEAD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Optiserv Consulting",
  "url": "https://optiservconsulting.com/",
  "email": "sunil@optiservsolutions.com",
  "telephone": "+91-808-823-8040",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Aditya Trade Centre, #303, 3rd Floor, Ameerpet",
    "addressLocality": "Hyderabad",
    "postalCode": "500038",
    "addressRegion": "Telangana",
    "addressCountry": "IN"
  }
}
</script>
"""

CONTACT = hero(
    "Contact",
    "Tell us the role. We will show you the people.",
    "A 30-minute call to scope what you need. No obligation, and no pressure to take the "
    "shortlist if it is not right.",
) + f"""
  <section class="section wrap">
    <div class="split">
      <div data-reveal>
        <h2 style="font-size:var(--t-d2)">Send us the brief</h2>
        <p class="lead" style="margin-top:var(--s5)">
          The more specific you are about the role and the hours, the more useful our first
          reply will be.
        </p>

        <div style="margin-top:var(--s8)">
          <h3 class="hsub" style="font-size:1.05rem;margin-bottom:var(--s4)">Hyderabad, India</h3>
          <address style="font-style:normal;font-size:var(--t-sm);color:#3A4F5B;line-height:1.7">
            Aditya Trade Centre, #303<br>
            3rd Floor, Ameerpet<br>
            Hyderabad 500038, Telangana
          </address>
          <p style="margin-top:var(--s4);font-size:var(--t-sm)">
            <a class="link" href="tel:+918088238040">+91 808-823-8040</a><br>
            <a class="link" href="tel:+919902612737">+91 990-261-2737</a>
          </p>
        </div>

        <div style="margin-top:var(--s7)">
          <h3 class="hsub" style="font-size:1.05rem;margin-bottom:var(--s4)">Cebu, Philippines</h3>
          <p style="font-size:var(--t-sm);color:#3A4F5B;line-height:1.7">
            Our Philippines delivery centre, covering Australia and US west-coast hours.
          </p>
        </div>

        <div style="margin-top:var(--s7)">
          <h3 class="hsub" style="font-size:1.05rem;margin-bottom:var(--s4)">Email</h3>
          <p><a class="link" href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
      </div>

      <div data-reveal style="--d:80ms">
        <form id="enquiry" novalidate>
          <div class="form-errors" id="formErrors" hidden role="alert"></div>
          <div class="form-status" id="formStatus" hidden role="status"></div>

          <div class="field">
            <label for="f-name">Your name</label>
            <input id="f-name" name="name" type="text" required data-label="Your name" autocomplete="name">
            <span class="err" id="f-name-err"></span>
          </div>

          <div class="field">
            <label for="f-email">Work email</label>
            <input id="f-email" name="email" type="email" required data-label="Work email" autocomplete="email" placeholder="you@company.com">
            <span class="err" id="f-email-err"></span>
          </div>

          <div class="field">
            <label for="f-company">Company</label>
            <input id="f-company" name="company" type="text" required data-label="Company" autocomplete="organization">
            <span class="err" id="f-company-err"></span>
          </div>

          <div class="field">
            <label for="f-country">Where are you based?</label>
            <select id="f-country" name="country" required data-label="Country">
              <option value="">Select a country</option>
              <option>United Kingdom</option>
              <option>United States</option>
              <option>Australia</option>
              <option>Canada</option>
              <option>Other</option>
            </select>
            <span class="err" id="f-country-err"></span>
          </div>

          <div class="field">
            <label for="f-roles">What roles do you need? <span class="opt">optional</span></label>
            <input id="f-roles" name="roles" type="text" placeholder="e.g. two React engineers and a QA automation engineer">
            <span class="err" id="f-roles-err"></span>
          </div>

          <div class="field">
            <label for="f-msg">Anything else we should know?</label>
            <textarea id="f-msg" name="message" required minlength="20" data-label="Your message"
              placeholder="Timezone you need covered, stack, start date, anything that would change our answer."></textarea>
            <span class="err" id="f-msg-err"></span>
          </div>

          <button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">
            Send the brief {ARROW}
          </button>
          <p style="margin-top:var(--s4);font-size:var(--t-xs);color:var(--grey);text-align:center">
            We reply from a person, not an autoresponder. See our
            <a class="link" href="privacy.html" style="font-size:inherit">privacy policy</a>.
          </p>
        </form>
      </div>
    </div>
  </section>
"""


def _legal(title, kicker, intro, sections):
    body = "".join(f"<h2>{h}</h2>{b}" for h, b in sections)
    return hero(kicker, title, intro) + f"""
  <section class="section wrap">
    <div class="legal" data-reveal style="--d:60ms">
{body}
    </div>
  </section>
"""


PRIVACY = _legal(
    "Privacy Policy", "Legal",
    "How Optiserv Consulting collects, uses and protects personal information.",
    [
      ("Who we are", '<p>Optiserv Consulting, with its registered office at Aditya Trade Centre, #303, 3rd Floor, Ameerpet, Hyderabad 500038, Telangana, India, and a delivery centre in Cebu, Philippines.</p><p>For any question about this policy, contact <a class="link" href="mailto:sunil@optiservsolutions.com" style="font-size:inherit">sunil@optiservsolutions.com</a>.</p>'),
      ("What we collect", '<p>When you submit the enquiry form we collect your name, work email address, company, country, the roles you describe and your message.</p><p>When you visit the site we may collect standard technical information such as IP address, browser type, pages viewed and referring page, subject to your cookie choice.</p><p>When you apply for a role we collect the information contained in your application and CV.</p>'),
      ("Why we use it", '<ul><li>To respond to your enquiry and provide the services you ask about.</li><li>To administer a recruitment application.</li><li>To understand which pages are read, where you have consented to analytics.</li><li>To meet legal and regulatory obligations.</li></ul>'),
      ("Legal basis", '<p>We rely on <b>legitimate interests</b> to respond to a business enquiry you send us and to keep this site secure; on <b>consent</b> for analytics cookies, which load only if you accept them; on <b>contract</b> where we are providing services to you; and on <b>legal obligation</b> where a law requires us to keep or disclose information.</p>'),
      ("Sharing", '<p>We share personal information with service providers who help us operate &mdash; our email provider, our website host, and an analytics provider where you have consented to analytics. We do not sell personal information, and we do not share it for advertising.</p>'),
      ("Retention", '<p>We keep enquiry correspondence for as long as needed to answer you and for a reasonable period afterwards in case you come back to us. Recruitment applications are kept for the duration of that process, and afterwards only if you ask us to keep you on file. You can ask us to delete any of it at any time.</p>'),
      ("Your rights", '<p>Depending on where you live you may have the right to access, correct, delete or port your personal information, to object to or restrict processing, and to withdraw consent. To exercise any of these, email us at the address above.</p>'),
      ("International transfers", '<p>We operate from India and the Philippines and serve clients in the UK, the US, Australia and Canada, so your information may be processed outside the country you are in. Where that happens we rely on appropriate safeguards, including contractual protections with the parties involved.</p>'),
      ("Changes", '<p>We will post any change to this policy on this page with a revised effective date.</p>'),
    ])

TERMS = _legal(
    "Terms of Use", "Legal",
    "The terms on which this website is made available.",
    [
      ("These terms", '<p>By using this website you accept these terms. If you do not accept them, please do not use the site.</p>'),
      ("Who we are", '<p>Optiserv Consulting, registered office Aditya Trade Centre, #303, 3rd Floor, Ameerpet, Hyderabad 500038, Telangana, India. Contact us at <a class="link" href="mailto:sunil@optiservsolutions.com" style="font-size:inherit">sunil@optiservsolutions.com</a>.</p>'),
      ("Use of the site", '<p>You may view and print pages for your own use. You may not use the site in any way that is unlawful, that interferes with its operation, or that attempts to gain unauthorised access to it.</p>'),
      ("Accuracy", '<p>We take care that information on this site is correct and keep it up to date. Pricing, availability and service descriptions are indicative and do not constitute a binding offer &mdash; the terms that apply to any engagement are the ones set out in your contract with us.</p>'),
      ("Intellectual property", '<p>All content on this site, including text, design, graphics and the Optiserv name and logo, belongs to Optiserv Consulting or its licensors and may not be reproduced without permission.</p>'),
      ("Third-party links", '<p>Where we link to a third-party site we do not control it and are not responsible for its content.</p>'),
      ("Liability", '<p>This website is provided as it is. We do not accept liability for loss arising from reliance on information published here, from any interruption to the site, or from any third-party site we link to. Nothing in these terms limits liability that cannot be limited by law. Liability in respect of services we provide is governed by your contract with us, not by this page.</p>'),
      ("Governing law", '<p>These terms are governed by the laws of India, and the courts of Hyderabad, Telangana have jurisdiction over any dispute arising from use of this website. Services we provide are governed by the law stated in the relevant contract.</p>'),
      ("Contact", '<p>Questions about these terms: <a class="link" href="mailto:sunil@optiservsolutions.com" style="font-size:inherit">sunil@optiservsolutions.com</a>.</p>'),
    ])

COOKIES = _legal(
    "Cookie Policy", "Legal",
    "What this site stores on your device, and how to change it.",
    [
      ("What cookies are", '<p>Cookies are small files a website stores on your device. Some are required for a site to function; others help the owner understand how the site is used.</p>'),
      ("What we use", '<p><b>Essential.</b> We store your cookie choice locally so that we do not ask again on every page. This is set only once you choose, and it carries no identifier.</p><p data-verify="analytics-provider"><b>Analytics.</b> If you accept analytics, we load an analytics provider so we can see which pages people read and where they arrive from. It is never loaded unless you accept it, and nothing is used to identify you personally or to target advertising.</p>'),
      ("Your choice", '<p>You are asked once, on your first visit, and your choice is remembered. You can change it at any time by clearing this site&rsquo;s data in your browser, which will cause the notice to appear again.</p><p>No analytics is loaded unless you accept it.</p>'),
      ("Browser controls", '<p>Every major browser lets you block or delete cookies in its settings. Blocking essential storage may mean the cookie notice reappears on each visit.</p>'),
      ("Contact", '<p>Questions: <a class="link" href="mailto:sunil@optiservsolutions.com" style="font-size:inherit">sunil@optiservsolutions.com</a>.</p>'),
    ])


NOT_FOUND = f"""
  <main id="main">
  <section class="nf wrap">
    <div>
      <span class="fig">404</span>
      <h1 style="font-size:var(--t-d1);margin-top:var(--s5)">That page is not on the board.</h1>
      <p class="lead" style="margin:var(--s5) auto 0;max-width:46ch">
        The link may be old, or the page may have moved when we rebuilt this site.
      </p>
      <div class="cta-actions" style="margin-top:var(--s7)">
        <a class="btn btn-primary" href="index.html">Back to the home page {ARROW}</a>
        <a class="btn btn-ghost" href="contact.html">Contact us</a>
      </div>
    </div>
  </section>
  </main>
"""
