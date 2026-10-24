#!/usr/bin/env python3
"""Assemble every page. Run:  python3 tools/make.py"""
import os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build
from build import page, ROOT, SITE
import content_a as A, content_b as B, content_c as C, content_d as D, content_e as E

HOME_MAIN = open(os.path.join(HERE, "_home_main.html")).read()
CONTRACT  = open(os.path.join(HERE, "_contract.html")).read()

ORG_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Optiserv Consulting",
  "url": "https://optiservconsulting.com/",
  "logo": "https://optiservconsulting.com/assets/img/logo.webp",
  "description": "Dedicated offshore teams, recruitment and automation services, delivered from Hyderabad, India and Cebu, Philippines.",
  "email": "sunil@optiservsolutions.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Aditya Trade Centre, #303, 3rd Floor, Ameerpet",
    "addressLocality": "Hyderabad",
    "postalCode": "500038",
    "addressRegion": "Telangana",
    "addressCountry": "IN"
  },
  "sameAs": ["https://www.linkedin.com/company/optiserv-consulting/"]
}
</script>
"""

# Wrap section markup in <main> unless the body supplies its own.
_orig_page = page
def page(slug, title, desc, body, extra_head="", contract=""):
    if "<main" not in body:
        body = '<main id="main">\n' + body + "\n</main>\n"
    html = (build.head(title, desc, slug, extra_head) + build.header() + body + build.footer())
    if contract:
        html = html.replace("<head>\n", "<head>\n" + contract + "\n", 1)
    with open(os.path.join(ROOT, slug), "w") as f:
        f.write(html)
    return slug


PAGES = [
    ("index.html",
     "Optiserv Consulting — Build your team. Not your overhead.",
     "Dedicated engineers, QA, designers and operations staff in Hyderabad and Cebu, from $1,500 a month. We hire, house, pay and manage them. You direct the work.",
     HOME_MAIN, ORG_LD, CONTRACT),

    ("about.html", "About — Optiserv Consulting",
     "Optiserv Consulting builds and runs dedicated teams for companies in the UK, US, Australia and Canada, delivered from Hyderabad and Cebu.",
     A.ABOUT, "", ""),

    ("team.html", "Team — Optiserv Consulting",
     "The founder, leadership and the account managers and recruiters behind every Optiserv engagement.",
     A.TEAM, "", ""),

    ("services.html", "Services — Optiserv Consulting",
     "Dedicated staffing, operational staffing, recruitment and RPO, and automation. One contract, one account manager.",
     A.SERVICES_HUB, "", ""),

    ("staff-augmentation.html", "Dedicated staffing — Optiserv Consulting",
     "Developers, QA engineers, designers and analysts employed by us in Hyderabad or Cebu and embedded in your team.",
     B.STAFF_AUG, "", ""),

    ("operational-staffing.html", "Operational staffing — Optiserv Consulting",
     "HR, payroll, infrastructure and team management staffed as a unit, so growth does not land on the people who should be building.",
     B.OPERATIONAL, "", ""),

    ("recruitment-rpo.html", "Recruitment & RPO — Optiserv Consulting",
     "Full-cycle RPO, project RPO and recruiter on demand, for the roles you intend to put on your own payroll.",
     B.RPO, "", ""),

    ("qa-testing.html", "QA & testing — Optiserv Consulting",
     "Manual and automated testing, mobile, Section 508 accessibility, performance engineering and penetration testing.",
     C.QA, "", ""),

    ("automation.html", "Automation — Optiserv Consulting",
     "Test, workflow and reporting automation, scoped per project. Where a task genuinely repeats, automating it beats hiring for it.",
     C.AUTOMATION, "", ""),

    ("industries.html", "Industries — Optiserv Consulting",
     "IT and non-IT, e-commerce, product companies, service businesses, consulting firms and iGaming.",
     C.INDUSTRIES, "", ""),

    ("case-studies.html", "Case studies — Optiserv Consulting",
     "Delivered projects and engagement patterns across dedicated teams, QA, recruitment, operations and automation.",
     E.CASE_STUDIES, "", ""),

    ("pricing.html", "Pricing — Optiserv Consulting",
     "From $1,500 a month per dedicated team member, with recruitment, payroll, seat, equipment, IT and an account manager included.",
     C.PRICING, "", ""),

    ("careers.html", "Careers — Optiserv Consulting",
     "Open roles in Hyderabad and Cebu across engineering, QA, identity and operations.",
     D.CAREERS, "", ""),

    ("insights.html", "Insights — Optiserv Consulting",
     "Practical writing on offshore hiring, timezone overlap, QA practice and the economics of headcount.",
     D.INSIGHTS, "", ""),

    ("contact.html", "Contact — Optiserv Consulting",
     "Tell us the role and we will show you the people. Offices in Hyderabad, India and Cebu, Philippines.",
     D.CONTACT, D.CONTACT_HEAD, ""),

    ("privacy.html", "Privacy Policy — Optiserv Consulting",
     "How Optiserv Consulting collects, uses and protects personal information.", D.PRIVACY, "", ""),
    ("terms.html", "Terms of Use — Optiserv Consulting",
     "The terms on which the Optiserv Consulting website is made available.", D.TERMS, "", ""),
    ("cookies.html", "Cookie Policy — Optiserv Consulting",
     "What the Optiserv Consulting website stores on your device, and how to change it.", D.COOKIES, "", ""),

    ("404.html", "Page not found — Optiserv Consulting",
     "That page is not on the board.", D.NOT_FOUND, "", ""),
]

written = [page(*p) for p in PAGES]

# ---- sitemap + robots ----------------------------------------------------
today = "2026-10-16"
indexable = [s for s in written if s != "404.html"]
urls = "\n".join(
    f"  <url><loc>{SITE if s == 'index.html' else SITE + s}</loc>"
    f"<lastmod>{today}</lastmod>"
    f"<priority>{'1.0' if s == 'index.html' else '0.8' if s in ('pricing.html','services.html','contact.html','case-studies.html') else '0.6'}</priority></url>"
    for s in indexable)
open(os.path.join(ROOT, "sitemap.xml"), "w").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n'
    f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

open(os.path.join(ROOT, "robots.txt"), "w").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")

print(f"Wrote {len(written)} pages + sitemap.xml + robots.txt")
for s in written:
    print("  ", s)
