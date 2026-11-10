# -*- coding: utf-8 -*-
"""
Génère les pages nationales de dev.jercat.fr à partir de gen/content.py.
Usage (depuis la racine du dépôt) :  python3 gen/build.py
Le dossier gen/ n'est pas publié (voir .vercelignore).
"""
import json, os, re, html, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SERVICES, CASES, ARTICLES, TEL, TEL_LINK  # noqa: E402

BASE = "https://dev.jercat.fr"
TODAY = date.today().isoformat()
esc = lambda s: html.escape(s, quote=True)
strip = lambda s: re.sub(r"<[^>]+>", "", s)

CITY_PAGES = [("creation-site-internet-saint-quentin", "Saint-Quentin"), ("creation-site-internet-laon", "Laon"),
              ("creation-site-internet-soissons", "Soissons"), ("creation-site-internet-chauny", "Chauny"),
              ("creation-site-internet-tergnier", "Tergnier"), ("developpeur-web-freelance-aisne", "Aisne (02)")]
GUIDES = [("prix-site-internet-2026", "Prix d'un site internet en 2026"), ("creation-site-artisan", "Site pour artisan"),
          ("creation-site-commercant", "Site pour commerçant")]

HEAD_FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
              '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
              '  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Cinzel:wght@400;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />\n'
              '  <link rel="stylesheet" href="/jercat.css" />')


def head(title, desc, path, schema, og_type="website"):
    url = BASE + path
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <!-- Page générée par gen/build.py à partir de gen/content.py : modifier le contenu là-bas puis relancer le script. -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="author" content="Jercat" />
  <meta name="theme-color" content="#0a0a08" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="Jercat — Développeur Web Freelance" />
  <meta property="og:title" content="{esc(title.replace(' | Jercat', ''))}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:image" content="{BASE}/preview.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:locale" content="fr_FR" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{BASE}/preview.png" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
  </script>
  {HEAD_FONTS}
</head>
<body class="sub-page">
"""


HEADER = f"""
  <header class="site-header">
    <a href="/" class="logo" aria-label="Jercat, accueil"><img src="/logo-jercat-icone.webp" alt="Logo Jercat" width="44" height="44">JERCAT</a>
    <nav aria-label="Navigation principale">
      <a href="/creation-site-internet">Création de site</a>
      <a href="/developpement-application-web">Applications</a>
      <a href="/automatisation-ia">IA</a>
      <a href="/etudes-de-cas">Études de cas</a>
      <a href="/#tarifs">Tarifs</a>
      <a href="/blog">Blog</a>
    </nav>
    <div class="header-actions">
      <a href="{TEL_LINK}" class="header-tel">📞 {TEL}</a>
      <a href="/#contact" class="header-cta">Devis gratuit</a>
    </div>
  </header>
  <main>
"""

REASSURE = """
  <section class="reassure" aria-label="Engagements">
    <div><strong>Un seul interlocuteur</strong><span>du premier appel à la mise en ligne</span></div>
    <div><strong>Prix fixé avant de commencer</strong><span>devis gratuit et détaillé</span></div>
    <div><strong>50 % / 50 %</strong><span>solde payé à la livraison</span></div>
    <div><strong>Réponse sous 24 h</strong><span>téléphone, email ou Telegram</span></div>
    <div><strong>Partout en France</strong><span>projets menés à distance</span></div>
  </section>
"""


def footer():
    serv = "".join(f'<li><a href="/{s["slug"]}">{esc(s["nav"])}</a></li>' for s in SERVICES)
    guides = "".join(f'<li><a href="/{g}">{esc(n)}</a></li>' for g, n in GUIDES)
    guides += '<li><a href="/blog">Blog</a></li><li><a href="/etudes-de-cas">Études de cas</a></li>'
    cities = " · ".join(f'<a href="/{c}">{esc(n)}</a>' for c, n in CITY_PAGES)
    return f"""
  </main>
  <footer class="site-footer">
    <div class="footer-cols">
      <div><p class="footer-title">Jercat</p><p class="footer-txt">Développeur web freelance. Création de sites internet, applications web et automatisations pour les TPE, indépendants, commerçants, artisans et associations, partout en France.</p>
        <p class="footer-txt"><a href="{TEL_LINK}">📞 {TEL}</a><br>jercat.bilman@gmail.com</p></div>
      <div><p class="footer-title">Services</p><ul>{serv}</ul></div>
      <div><p class="footer-title">Ressources</p><ul>{guides}</ul></div>
    </div>
    <p class="footer-local">Interventions sur place dans l'Aisne : {cities}</p>
    <p class="footer-copy">© {date.today().year} Jercat — Développeur web indépendant · <a href="/#contact">Devis gratuit</a> · Mentions légales, confidentialité et CGV sur la <a href="/">page d'accueil</a></p>
  </footer>
  <div class="mobile-cta"><a href="{TEL_LINK}" class="m-tel">📞 Appeler</a><a href="/#contact" class="m-devis">Devis gratuit</a></div>
</body>
</html>
"""


def cta_block(title, text):
    return f"""
  <section class="cta" style="border-top:1px solid var(--border);">
    <h2>{title}</h2>
    <p>{text} Vous préférez en parler ? Appelez-moi au <a href="{TEL_LINK}">{TEL}</a>.</p>
    <a href="/#contact" class="btn-gold">Demander mon devis gratuit</a>
  </section>
"""


def faq_html(faq, title_em):
    items = "".join(f"""
      <details class="faq-item">
        <summary><h3>{esc(q)}</h3></summary>
        <div class="faq-answer">{esc(a)}</div>
      </details>""" for q, a in faq)
    return f"""
  <section class="section" style="padding-top:60px;">
    <div class="section-tag">Questions fréquentes</div>
    <h2 class="section-title">Vos questions <em>{title_em}</em></h2>
    <div class="ornament">✦</div>
    <div class="faq-list">{items}
    </div>
  </section>
"""


def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p} for i, (n, p) in enumerate(items)]}


def case_card(c, small=False):
    return f"""<a class="case-mini" href="/etudes-de-cas#{c['id']}"><img src="/{c['img']}" alt="Aperçu du site {esc(c['name'])}" width="800" height="500" loading="lazy" decoding="async"><span><strong>{esc(c['name'])}</strong>{esc(c['type'])} — lire l'étude de cas →</span></a>"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("écrit", path)


# ---------------------------------------------------------------- pages de services
def build_service(s):
    path = "/" + s["slug"]
    offer = {"@type": "Offer", "priceCurrency": "EUR", "availability": "https://schema.org/InStock",
             "priceSpecification": {"@type": "PriceSpecification", "minPrice": s["min_price"], "priceCurrency": "EUR"}} if s["min_price"] else None
    service = {"@type": "Service", "name": s["service_name"], "serviceType": s["service_name"], "url": BASE + path,
               "description": s["desc"], "provider": {"@id": BASE + "/#business"},
               "areaServed": {"@type": "Country", "name": "France"},
               "audience": {"@type": "BusinessAudience", "audienceType": "TPE, PME, indépendants, commerçants, artisans, associations"}}
    if offer:
        service["offers"] = offer
    schema = {"@context": "https://schema.org", "@graph": [service, crumbs([("Accueil", "/"), (s["nav"], path)]), faq_schema(s["faq"])]}
    case = next(c for c in CASES if c["id"] == s["case"])
    toc = "".join(f'<li><a href="#s{i}">{esc(t)}</a></li>' for i, (t, _) in enumerate(s["sections"]))
    sections = "".join(f'\n      <h2 id="s{i}">{esc(t)}</h2>\n      {b}' for i, (t, b) in enumerate(s["sections"]))
    steps = "".join(f'<li><span class="step-n">{i+1:02d}</span><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for i, (a, b) in enumerate(s["steps"]))
    others = "".join(f'<li><a href="/{o["slug"]}">{esc(o["nav"])}</a></li>' for o in SERVICES if o["slug"] != s["slug"])
    guides = "".join(f'<li><a href="/{g}">{esc(n)}</a></li>' for g, n in GUIDES) + "".join(
        f'<li><a href="/blog/{a["slug"]}">{esc(a["title"].split(":")[0])}</a></li>' for a in ARTICLES)
    page = head(s["title"], s["desc"], path, schema) + HEADER + f"""
  <section class="hero hero-sub-page">
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › {esc(s['nav'])}</nav>
    <p class="hero-tag">{esc(s['tag'])}</p>
    <h1>{s['h1']}</h1>
    <div class="ornament">✦</div>
    <p class="hero-sub">{esc(s['sub'])}</p>
    <div class="hero-actions">
      <a href="/#contact" class="btn-gold">Demander un devis gratuit</a>
      <a href="{TEL_LINK}" class="btn-outline-gold" aria-label="Appeler Jercat au {TEL}">📞 {TEL}</a>
    </div>
  </section>
{REASSURE}
  <section class="section avantages">
    <div class="prose">
      <nav class="toc" aria-label="Sommaire"><p>Sommaire</p><ol>{toc}</ol></nav>{sections}
      <h2>Comment se déroule le projet</h2>
      <ol class="steps">{steps}</ol>
      <div class="inline-cta"><p><strong>Votre projet en trois champs.</strong> Décrivez votre besoin, je vous réponds sous 24 h avec un devis gratuit et sans engagement.</p><a href="/#contact" class="btn-gold">Obtenir mon devis</a></div>
      <h2>Un exemple de réalisation</h2>
      {case_card(case)}
    </div>
  </section>
{faq_html(s['faq'], 'fréquentes')}
{cta_block('Parlons de <em>votre projet.</em>', 'Devis gratuit et sans engagement, réponse sous 24 h, partout en France.')}
  <section class="related" aria-label="Pages liées">
    <div class="related-grid">
      <div><p class="related-title">Autres services</p><ul>{others}</ul></div>
      <div><p class="related-title">Guides &amp; articles</p><ul>{guides}</ul></div>
    </div>
  </section>
""" + footer()
    write(s["slug"] + ".html", page)


# ---------------------------------------------------------------- études de cas
def build_cases():
    path = "/etudes-de-cas"
    blocks = ""
    for c in CASES:
        sol = "".join(f"<li>{esc(x)}</li>" for x in c["solution"])
        blocks += f"""
    <article class="case" id="{c['id']}">
      <a href="{c['url']}" target="_blank" rel="noopener" class="case-img"><img src="/{c['img']}" alt="Page d'accueil du site {esc(c['name'])}" width="800" height="500" loading="lazy" decoding="async"></a>
      <div class="case-body">
        <p class="case-type">{esc(c['type'])}</p>
        <h2>{esc(c['name'])}</h2>
        <dl>
          <dt>Client</dt><dd>{esc(c['where'])}</dd>
          <dt>Besoin</dt><dd>{esc(c['need'])}</dd>
          <dt>Ce que j'ai réalisé</dt><dd><ul>{sol}</ul></dd>
          <dt>Technologies</dt><dd>{esc(c['tech'])}</dd>
          <dt>Résultat</dt><dd>{esc(c['result'])}</dd>
        </dl>
        <p><a href="{c['url']}" target="_blank" rel="noopener">Voir le site en ligne ↗</a></p>
      </div>
    </article>"""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": "Études de cas — Jercat", "url": BASE + path,
         "hasPart": [{"@type": "CreativeWork", "name": c["name"], "url": c["url"]} for c in CASES]},
        crumbs([("Accueil", "/"), ("Études de cas", path)])]}
    page = head("Études de cas : sites et applications réalisés | Jercat",
                "Études de cas des sites réalisés par Jercat : artisan, restaurant avec fidélité, boutique en ligne, site éditorial SEO. Le besoin, la solution, le résultat.",
                path, schema) + HEADER + f"""
  <section class="hero hero-sub-page">
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › Études de cas</nav>
    <p class="hero-tag">Portfolio détaillé</p>
    <h1>Études <em>de cas.</em></h1>
    <div class="ornament">✦</div>
    <p class="hero-sub">Le besoin de départ, ce que j'ai réalisé et le résultat, projet par projet.</p>
    <div class="hero-actions"><a href="/#contact" class="btn-gold">Un projet similaire ? Devis gratuit</a></div>
  </section>
{REASSURE}
  <section class="section cases">{blocks}
  </section>
{cta_block('Votre site sera <em>le prochain.</em>', 'Décrivez votre projet en trois champs, je vous réponds sous 24 h.')}
""" + footer()
    write("etudes-de-cas.html", page)


# ---------------------------------------------------------------- blog
def build_blog():
    cards = "".join(f"""
      <a class="post-card" href="/blog/{a['slug']}"><span class="post-cat">{esc(a['cat'])} · {a['read']}</span><strong>{esc(a['title'])}</strong><span>{esc(a['desc'])}</span></a>""" for a in ARTICLES)
    cards += """
      <a class="post-card" href="/prix-site-internet-2026"><span class="post-cat">Prix · Guide</span><strong>Prix d'un site internet en 2026</strong><span>Combien coûte un site vitrine, un e-commerce ou une refonte, et pourquoi les prix varient autant.</span></a>"""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "name": "Blog Jercat — création de site, SEO et IA", "url": BASE + "/blog",
         "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{BASE}/blog/{a['slug']}", "datePublished": a["date"]} for a in ARTICLES]},
        crumbs([("Accueil", "/"), ("Blog", "/blog")])]}
    page = head("Blog : création de site internet, SEO et IA pour TPE | Jercat",
                "Guides pratiques pour TPE, indépendants et associations : créer son site internet, prix, référencement Google, automatisation et intelligence artificielle.",
                "/blog", schema) + HEADER + f"""
  <section class="hero hero-sub-page">
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › Blog</nav>
    <p class="hero-tag">Guides pratiques</p>
    <h1>Le <em>blog.</em></h1>
    <div class="ornament">✦</div>
    <p class="hero-sub">Des réponses claires pour créer, améliorer et faire connaître votre site internet, sans jargon.</p>
  </section>
  <section class="section"><div class="post-grid">{cards}
  </div></section>
{cta_block('Une question sur <em>votre projet ?</em>', 'Je vous réponds sous 24 h, gratuitement.')}
""" + footer()
    write("blog.html", page)

    for a in ARTICLES:
        path = f"/blog/{a['slug']}"
        body = "".join(f"\n      <h2>{esc(t)}</h2>\n      {b}" for t, b in a["body"])
        rel = "".join(f'<li><a href="/{r}">{esc(next(s["nav"] for s in SERVICES if s["slug"] == r))}</a></li>' for r in a["related"])
        schema = {"@context": "https://schema.org", "@graph": [
            {"@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "url": BASE + path,
             "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "fr-FR",
             "author": {"@id": BASE + "/#person"}, "publisher": {"@id": BASE + "/#business"},
             "image": BASE + "/preview.png", "mainEntityOfPage": BASE + path},
            crumbs([("Accueil", "/"), ("Blog", "/blog"), (a["title"], path)])]}
        page = head(a["title"] + " | Jercat", a["desc"], path, schema, "article") + HEADER + f"""
  <section class="hero hero-sub-page hero-article">
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/blog">Blog</a> › {esc(a['cat'])}</nav>
    <p class="hero-tag">{esc(a['cat'])} · {a['read']} de lecture</p>
    <h1>{a['h1']}</h1>
    <div class="ornament">✦</div>
    <p class="hero-sub">{esc(a['desc'])}</p>
    <p class="post-meta">Par Jercat, développeur web freelance · publié le {date.fromisoformat(a['date']).strftime('%d/%m/%Y')}</p>
  </section>
  <section class="section avantages"><article class="prose">{body}
      <div class="inline-cta"><p><strong>Besoin d'aide pour votre site ?</strong> Devis gratuit sous 24 h, partout en France.</p><a href="/#contact" class="btn-gold">Demander un devis</a></div>
      <h2>Pour aller plus loin</h2><ul>{rel}<li><a href="/blog">Tous les articles</a></li></ul>
  </article></section>
""" + footer()
        write(f"blog/{a['slug']}.html", page)


# ---------------------------------------------------------------- sitemap
def build_sitemap():
    urls = ["/"] + ["/" + s["slug"] for s in SERVICES] + ["/etudes-de-cas", "/blog"] + [f"/blog/{a['slug']}" for a in ARTICLES] \
        + ["/" + g for g, _ in GUIDES] + ["/" + c for c, _ in CITY_PAGES]
    seen, out = set(), []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        out.append(f"  <url>\n    <loc>{BASE}{'' if u == '/' else u}{'/' if u == '/' else ''}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(out) + "\n  <!-- Généré par gen/build.py -->\n</urlset>\n")


if __name__ == "__main__":
    for s in SERVICES:
        build_service(s)
    build_cases()
    build_blog()
    build_sitemap()
