#!/usr/bin/env python3
"""
Optiserv Consulting — static page generator.

The SITE IS PLAIN HTML. This script exists only so that the header, footer and
cookie banner live in one place instead of in eighteen. Run it after editing
chrome or page content:

    python3 tools/build.py

It writes real, self-contained .html files to the project root. You never need
to run it to *serve* the site.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))

SITE = "https://optiservconsulting.com/"
EMAIL = "sunil.s@optiservconsulting.com"

SERVICES = [
    ("staff-augmentation.html",  "Dedicated staffing",     "Engineers, QA, design — working only on your product"),
    ("operational-staffing.html","Operational staffing",   "HR, payroll, infrastructure, team management"),
    ("recruitment-rpo.html",     "Recruitment &amp; RPO",  "Full-cycle, project, or a recruiter on demand"),
    ("qa-testing.html",          "QA &amp; testing",       "Manual, automation, mobile, performance, security"),
    ("automation.html",          "Automation",             "Scoped per project"),
]

ARROW = ('<svg width="14" height="10" viewBox="0 0 14 10" fill="none" aria-hidden="true">'
         '<path d="M9 1l4 4-4 4M13 5H0" stroke="currentColor" stroke-width="1.6"/></svg>')
ARROW_SM = ARROW.replace('width="14" height="10"', 'width="13" height="9"')


def head(title, desc, slug, extra=""):
    canonical = SITE if slug == "index.html" else SITE + slug
    return f"""<!doctype html>
<html lang="en">
<head>
<script>document.documentElement.className+=" js";</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/logo.webp">
<link rel="preload" href="assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css">
<script defer src="assets/js/main.js"></script>
{extra}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header():
    drop = "\n".join(
        f'            <a href="{h}">{label}<span>{sub}</span></a>'
        for h, label, sub in SERVICES)
    return f"""
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="index.html" aria-label="Optiserv Consulting — home">
      <img src="assets/img/logo.webp" alt="Optiserv Consulting" width="459" height="127">
    </a>

    <nav aria-label="Primary">
      <ul class="nav">
        <li>
          <button class="nav-trigger" type="button" aria-expanded="false" aria-controls="dd-services">
            Services
            <svg width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5"/></svg>
          </button>
          <div class="dropdown" id="dd-services">
{drop}
          </div>
        </li>
        <li><a href="industries.html">Industries</a></li>
        <li><a href="case-studies.html">Case studies</a></li>
        <li><a href="pricing.html">Pricing</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="team.html">Team</a></li>
        <li><a href="careers.html">Careers</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>

    <div class="hdr-cta"><a class="btn btn-primary" href="contact.html">Book a call</a></div>

    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span></button>
  </div>
</header>

<div class="drawer" id="drawer" hidden>
  <nav aria-label="Mobile">
    <a href="index.html">Home</a>
    <a href="services.html">Services</a>
    <div class="sub">
{chr(10).join(f'      <a href="{h}">{re.sub("&amp;", "&", label)}</a>' for h, label, _ in SERVICES)}
    </div>
    <a href="industries.html">Industries</a>
    <a href="case-studies.html">Case studies</a>
    <a href="pricing.html">Pricing</a>
    <a href="about.html">About</a>
    <a href="team.html">Team</a>
    <a href="careers.html">Careers</a>
    <a href="insights.html">Insights</a>
    <a href="contact.html">Contact</a>
    <a class="btn btn-primary" href="contact.html">Book a call</a>
  </nav>
</div>
"""


def footer():
    svc = "\n".join(f'          <li><a href="{h}">{label}</a></li>' for h, label, _ in SERVICES)
    return f"""
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div class="ftr-brand">
        <img src="assets/img/logo.webp" alt="Optiserv Consulting" width="459" height="127">
        <p>Dedicated offshore teams, recruitment and automation, delivered from India and the Philippines.</p>
      </div>
      <div>
        <h2 class="ftr-h">Services</h2>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h2 class="ftr-h">Company</h2>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="industries.html">Industries</a></li>
          <li><a href="case-studies.html">Case studies</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="careers.html">Careers</a></li>
          <li><a href="insights.html">Insights</a></li>
        </ul>
      </div>
      <div>
        <h2 class="ftr-h">Offices</h2>
        <address>
          <strong>Hyderabad, India</strong>
          Aditya Trade Centre, #303<br>
          3rd Floor, Ameerpet<br>
          Hyderabad 500038, Telangana
        </address>
        <address style="margin-top:var(--s4)">
          <strong>Cebu, Philippines</strong>
          Delivery centre
        </address>
        <ul style="margin-top:var(--s4)">
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:+918088238040">+91 808-823-8040</a></li>
          <li><a href="tel:+919902612737">+91 990-261-2737</a></li>
        </ul>
      </div>
    </div>
    <div class="ftr-bottom">
      <p>&copy; 2026 Optiserv Consulting. All rights reserved.</p>
      <ul>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="terms.html">Terms</a></li>
        <li><a href="cookies.html">Cookies</a></li>
        <li><a href="https://www.linkedin.com/company/optiserv-consulting/" rel="noopener">LinkedIn</a></li>
      </ul>
    </div>
  </div>
</footer>

<div class="cookie" id="cookie" hidden role="region" aria-label="Cookie notice">
  <div class="cookie-in">
    <p>We use essential cookies to run this site, and analytics cookies to understand what people read. You choose.
      <a href="cookies.html">Cookie policy</a></p>
    <div class="cookie-actions">
      <button class="btn btn-ghost" type="button" data-cookie="essential">Essential only</button>
      <button class="btn btn-primary" type="button" data-cookie="accept">Accept analytics</button>
    </div>
  </div>
</div>

</body>
</html>
"""


def page(slug, title, desc, body, extra_head=""):
    html = head(title, desc, slug, extra_head) + header() + body + footer()
    with open(os.path.join(ROOT, slug), "w") as f:
        f.write(html)
    return slug


def hero(kicker, h1, lead, actions="", mod=""):
    """Interior page opener. Deliberately not the homepage hero."""
    act = f'<div class="hero-actions" data-reveal style="--d:140ms">{actions}</div>' if actions else ""
    return f"""
  <section class="page-hero {mod}">
    <div class="wrap">
      <p class="page-kicker" data-reveal><span class="node" aria-hidden="true"></span>{kicker}</p>
      <h1 data-reveal style="--d:60ms">{h1}</h1>
      <p class="lead" data-reveal style="--d:100ms">{lead}</p>
      {act}
    </div>
  </section>
"""


def cta(h2="Tell us the role. We will show you the people.",
        p="A 30-minute call to scope what you need. No obligation, and no pressure to take the shortlist if it is not right."):
    return f"""
  <section class="section navy-band cta-band">
    <div class="wrap">
      <h2 data-reveal>{h2}</h2>
      <p class="lead" data-reveal style="--d:60ms">{p}</p>
      <div class="cta-actions" data-reveal style="--d:120ms">
        <a class="btn btn-primary" href="contact.html">Book a call {ARROW}</a>
        <a class="btn btn-ghost" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <p class="cta-meta" data-reveal style="--d:180ms">Hyderabad, India &middot; Cebu, Philippines</p>
    </div>
  </section>
"""
