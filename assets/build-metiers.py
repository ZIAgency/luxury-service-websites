#!/usr/bin/env python3
"""Génère les sites orientés client du portfolio (un fichier de données par famille
dans assets/sites/*.py : bâtiment, plomberie, serrurerie, taxis, dentistes,
ophtalmologie, paysagistes, avocats).

Modèle de départ : platriers/01-morel-platrerie. Feuille de style commune : assets/metiers-base.css.
même logique (hero avec photo du métier, situations qui préremplissent le devis,
services, étapes, chantiers, engagements, FAQ, formulaire court, barre mobile),
mais chaque site a sa palette, ses polices, sa mise en page de hero et ses textes.

Usage : python3 assets/build-metiers.py
Les photos (hero.jpg) sont téléchargées à part, depuis Pexels (clé "photo" de chaque site).

Clés facultatives d'un site :
  form    "devis" (défaut), "rdv" (santé, droit) ou "taxi" (réservation de course)
  urgent  True : l'appel devient le bouton principal du hero
  shop    True : commerce avec boutique (« Où nous trouver »)
  jobs_eyebrow, jobs_h2 : titres de la section d'exemples
"""
import html
import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Adresse du portfolio : à remplacer par le domaine du client à la livraison.
BASE_URL = "https://luxury-service-websites.vercel.app"
UPDATED = ("2026-09-30", "30 septembre 2026")

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1Z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 16.2-3.5-3.5L4 14.2l5 5 11-11-1.4-1.4Z"/></svg>'
TOP_ICONS = [
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm1 10.4V6h-2v7.6l5 3 1-1.7Z"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5Z"/></svg>',
]

# ─────────────────────────────── Sites ───────────────────────────────

# ─────────────────────────────── Couleurs ───────────────────────────────

def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def hexc(c):
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(v))) for v in c)

def mix(a, b, t):
    ra, rb = rgb(a), rgb(b)
    return hexc([ra[i] + (rb[i] - ra[i]) * t for i in range(3)])

def rgba_prefix(h):
    r, g, b = rgb(h)
    return f"rgba({r}, {g}, {b},"

def palette(p):
    ink, acc = p["ink"], p["accent"]
    return {
        "#FBFAF6": p["paper"], "#F4F1EA": p["chalk"], "#1E2A33": ink,
        "#2C3B46": mix(ink, "#FFFFFF", .10), "#58646E": p["muted"], "#DDD7CA": p["line"],
        "#D98B3A": acc, "#A45F18": p["deep"], "#E59A4C": mix(acc, "#FFFFFF", .15),
        "#D6DCE0": mix(ink, "#FFFFFF", .85), "#C3CCD2": mix(ink, "#FFFFFF", .78),
        "#9FABB3": mix(ink, "#FFFFFF", .62), "#3A4A56": mix(ink, "#FFFFFF", .20),
        "#33444F": mix(ink, "#FFFFFF", .15), "#141D23": mix(ink, "#000000", .35),
        "#CFC8B8": mix(p["line"], "#000000", .08),
        "rgba(30, 42, 51,": rgba_prefix(ink), "rgba(217, 139, 58,": rgba_prefix(acc),
        "rgba(251, 250, 246,": rgba_prefix(p["paper"]),
    }

VARIANT_CSS = """
/* Variantes de hero */
.hero h1.eyebrow { font-size: .82rem; font-weight: 600; letter-spacing: .08em; line-height: 1.4; margin: 0 0 12px; }
.hero .headline { font-family: var(--head); font-size: clamp(2rem, 4vw, 3.1rem); font-weight: 800; line-height: 1.12; letter-spacing: -.025em; margin: 0; }
.hero .headline em { font-style: normal; color: var(--ochre-deep); }
.hero.split-left .hero-visual { order: -1; }
.hero.split-left .hero-badge { left: auto; right: -24px; }
.hero.overlay { position: relative; padding: 0; background: var(--ink); color: #fff; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; margin: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-bg::after { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, INKA.95) 0%, INKA.86) 55%, INKA.35) 100%); }
.hero.overlay .hero-grid { position: relative; grid-template-columns: minmax(0, 680px); min-height: min(720px, 88vh); align-content: center; padding: 72px 0; }
.hero.overlay .lead, .hero.overlay .proofs li { color: #fff; }
.hero.overlay .lead { color: ONINK; }
.hero.overlay .headline em { color: var(--ochre); }
.hero.overlay .eyebrow { color: var(--ochre); }
.hero.overlay .btn-ghost { border-color: rgba(255, 255, 255, .7); color: #fff; }
.hero.overlay .btn-ghost:hover { background: #fff; color: var(--ink); }
.hero.overlay .hero-note { color: ONINK2; }
.hero.overlay .hero-badge { position: static; display: inline-flex; margin-top: 28px; background: rgba(255, 255, 255, .08); border: 1px solid rgba(255, 255, 255, .2); box-shadow: none; }
.hero.overlay .hero-badge strong { color: var(--ochre); }
.hero.overlay .hero-badge span { color: ONINK; }
.signature { margin-top: 26px; font-size: .95rem; color: var(--muted); }
.signature strong { color: var(--ink); font-family: var(--head); }
@media (max-width: 860px) {
  .hero.split-left .hero-badge { right: auto; left: 12px; }
  .hero-bg::after { background: linear-gradient(180deg, INKA.72) 0%, INKA.9) 55%, INKA.96) 100%); }
  .hero.overlay .hero-grid { min-height: 0; padding: 56px 0 64px; }
}
"""

# ─────────────────────────────── Gabarits ───────────────────────────────

e = html.escape


def img_size(path):
    """Largeur et hauteur d'un JPEG, lues dans l'en-tête (1280 × 853 par défaut)."""
    try:
        data = path.read_bytes()
    except FileNotFoundError:
        return 1280, 853
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            return int.from_bytes(data[i + 7:i + 9], "big"), int.from_bytes(data[i + 5:i + 7], "big")
        i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    return 1280, 853

def hero(s):
    h1a, h1b = s["h1"]
    proofs = "\n".join(f"            <li>{ICON_CHECK}{e(p)}</li>" for p in s["proofs"])
    call = f'''            <a class="btn {"btn-primary" if s.get("urgent") else "btn-ghost"}" href="tel:{s["tel"]}">
              {ICON_PHONE}
              {"Appeler maintenant · " if s.get("urgent") else ""}{s["phone"]}
            </a>'''
    form_link = f'            <a class="btn {"btn-ghost" if s.get("urgent") else "btn-primary"}" href="#devis">{e(s["cta"])}</a>'
    ctas = call + "\n" + form_link if s.get("urgent") else form_link + "\n" + call
    copy = f'''        <div class="hero-copy">
          <h1 class="eyebrow">{e(s.get("seo_h1", s["eyebrow"]))}</h1>
          <p class="headline">{e(h1a)} <em>{e(h1b)}</em></p>
          <p class="lead">{e(s["lead"])}</p>
          <ul class="proofs">
{proofs}
          </ul>
          <div class="hero-ctas">
{ctas}
          </div>
          <p class="hero-note">{e(s["note"])}</p>{{BADGE_IN}}
        </div>'''
    badge = f'''<div class="hero-badge">
            <strong>{e(s["badge"][0])}</strong>
            <span>{s["badge"][1]}</span>
          </div>'''
    w, h = img_size(ROOT / s["dir"] / "hero.jpg")
    img = f'<img src="hero.jpg" alt="{e(s["alt"])}" width="{w}" height="{h}" fetchpriority="high">'
    if s["layout"] == "overlay":
        return f'''    <section class="hero overlay">
      <figure class="hero-bg">{img}</figure>
      <div class="wrap hero-grid">
{copy.replace("{BADGE_IN}", chr(10) + "          " + badge)}
      </div>
    </section>'''
    visual = f'''        <div class="hero-visual">
          <figure class="hero-photo">
            {img}
          </figure>
          {badge}
        </div>'''
    return f'''    <section class="hero {s["layout"]}">
      <div class="wrap hero-grid">
{copy.replace("{BADGE_IN}", "")}

{visual}
      </div>
    </section>'''


LABELS = {
    "devis": dict(eyebrow="Devis gratuit", mobile="Devis gratuit", submit="Envoyer ma demande",
                  skip="Aller au formulaire de devis", hint="Cliquez sur votre situation : le formulaire se remplit tout seul."),
    "rdv": dict(eyebrow="Rendez-vous", mobile="Rendez-vous", submit="Demander un rendez-vous",
                skip="Aller au formulaire de rendez-vous", hint="Cliquez sur votre situation : le motif de rendez-vous se remplit tout seul."),
    "taxi": dict(eyebrow="Réservation", mobile="Réserver", submit="Réserver ma course",
                 skip="Aller au formulaire de réservation", hint="Cliquez sur votre trajet : le formulaire de réservation se remplit tout seul."),
}


def labels(s):
    return {**LABELS[s.get("form", "devis")], **s.get("labels", {})}


def f_input(fid, label, rule=None, typ="text", ph="", err="", opt=False, auto="", mode="", maxlen=80):
    attrs = f'type="{typ}" id="{fid}" name="{fid}"'
    if typ not in ("date", "time"):
        attrs += f' maxlength="{maxlen}"'
    if auto:
        attrs += f' autocomplete="{auto}"'
    if mode:
        attrs += f' inputmode="{mode}"'
    if ph:
        attrs += f' placeholder="{e(ph)}"'
    if rule:
        attrs += f' data-rule="{rule}"'
        if rule != "email":
            attrs += " required"
    o = ' <span class="opt">(facultatif)</span>' if opt else ""
    er = f'\n              <p class="err">{e(err)}</p>' if err else ""
    return f'''            <div class="field">
              <label for="{fid}">{e(label)}{o}</label>
              <input {attrs}>{er}
            </div>'''


def f_select(fid, label, options, required=True, err="Faites un choix dans la liste.", first="Choisissez"):
    opts = "\n".join(f"                <option>{e(o)}</option>" for o in options)
    head = f'                <option value="">{first}</option>\n' if first else ""
    req = ' data-rule="req" required' if required else ""
    er = f'\n              <p class="err">{e(err)}</p>' if required else ""
    return f'''            <div class="field">
              <label for="{fid}">{e(label)}</label>
              <select id="{fid}" name="{fid}"{req}>
{head}{opts}
              </select>{er}
            </div>'''


def row(*fields):
    return '          <div class="row">\n' + "\n".join(fields) + "\n          </div>"


def solo(field):
    return field.replace("            <", "          <", 1).replace("\n            </div>", "\n          </div>")


def form_html(s, L):
    kind = s.get("form", "devis")
    xid, xlabel, xph, _ = s["extra"]
    extra = f_input(xid, xlabel, ph=xph, opt=True)
    work = solo(f_select("work", s["work_label"], s["works"]))
    details = f'''          <div class="field">
            <label for="details">{e(s.get("details_label", "Précisez votre demande"))} <span class="opt">(facultatif)</span></label>
            <textarea id="details" name="details" rows="3" maxlength="800" placeholder="{e(s["details_ph"])}"></textarea>
          </div>'''
    who = row(f_input("name", "Nom", "name", err="Indiquez votre nom.", auto="name"),
              f_input("phone", "Téléphone", "phone", "tel", err="Un numéro à 10 chiffres pour vous joindre.", auto="tel", maxlen=20))
    email = solo(f_input("email", "E-mail", "email", "email", err="Cette adresse ne semble pas valide.", opt=True, auto="email", maxlen=120))
    chips = '''          <fieldset class="field">
            <legend>Quand vous rappeler ?</legend>
            <div class="chips">
              <label class="chip"><input type="radio" name="when" value="Matin" checked><span>Le matin</span></label>
              <label class="chip"><input type="radio" name="when" value="Midi"><span>Entre 12 h et 14 h</span></label>
              <label class="chip"><input type="radio" name="when" value="Après-midi"><span>L'après-midi</span></label>
            </div>
          </fieldset>'''
    if kind == "taxi":
        parts = [work,
                 row(f_input("from", "Adresse de départ", "req", ph="Ex. : 12 rue de la Gare", err="Indiquez l'adresse de départ.", maxlen=120),
                     f_input("to", "Destination", "req", ph=s.get("to_ph", "Ex. : aéroport, gare, adresse"), err="Indiquez la destination.", maxlen=120)),
                 row(f_input("date", "Date", "req", "date", err="Choisissez une date."),
                     f_input("time", "Heure de prise en charge", "req", "time", err="Choisissez une heure.")),
                 row(f_select("pax", "Passagers", ["1", "2", "3", "4", "5 à 7"], required=False, first=""), extra),
                 details, who, email]
    elif kind == "rdv":
        parts = [work,
                 row(extra, f_select("avail", "Vos disponibilités", s.get("avail", ["Dès que possible", "Cette semaine", "Dans le mois", "Je préfère en parler"]), required=False, first="")),
                 details, who, email, chips]
    else:
        parts = [work,
                 row(extra, f_input("zip", "Code postal", "zip", ph="", err=f"5 chiffres, par exemple {s['cp']}.", auto="postal-code", mode="numeric", maxlen=5)),
                 details, who, email, chips]
    body = "\n\n".join(parts)
    legal = s.get("legal", "Vos coordonnées servent uniquement à vous recontacter pour cette demande.")
    return f'''        <form class="quote-form" id="quoteForm" novalidate>
          <div class="hp" aria-hidden="true">
            <label for="website">Ne pas remplir</label>
            <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
          </div>

{body}

          <button class="btn btn-primary btn-block" type="submit">{L["submit"]}</button>
          <p class="form-legal">{e(legal)}</p>

          <div class="success" id="success" role="status" aria-live="polite" hidden>
            <svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22"/><path d="m14 24 7 7 13-14"/></svg>
            <h3>Demande bien reçue</h3>
            <p id="successMsg"></p>
          </div>
        </form>'''


def page(s):
    zone_txt = ", ".join(s["zone"])
    nav = s["nav"]
    sits = "\n".join(f'''          <button class="sit" data-prefill="{e(p)}">
            <span class="sit-q">{e(q)}</span>
            <span class="sit-a">{e(a)}</span>
          </button>''' for q, a, p in s["sits"])
    servs = "\n".join(f'''          <article class="serv">
            <span class="serv-n">{i:02d}</span>
            <h3>{e(t)}</h3>
            <p>{e(d)}</p>
          </article>''' for i, (t, d) in enumerate(s["servs"], 1))
    steps = "\n".join(f'''          <li>
            <span class="step-n">{i}</span>
            <h3>{e(t)}</h3>
            <p>{e(d)}</p>
          </li>''' for i, (t, d) in enumerate(s["steps"], 1))
    l1, l2 = s["job_labels"]
    jobs = "\n".join(f'''          <article class="job">
            <p class="job-where">{e(w)}</p>
            <h3>{e(t)}</h3>
            <dl>
              <div><dt>{l1}</dt><dd>{e(a)}</dd></div>
              <div><dt>{l2}</dt><dd>{e(b)}</dd></div>
            </dl>
          </article>''' for w, t, a, b in s["jobs"])
    signature = (f'\n          <p class="signature"><strong>{e(s["founder"][0])}</strong>, {e(s["founder"][1])}</p>'
                 if s.get("founder") else "")
    pledges = "\n".join(f"            <li><strong>{e(a)}</strong> {e(b)}</li>" for a, b in s["pledges"])
    reviews = "\n".join(f'''          <figure class="review">
            <blockquote>{e(q)}</blockquote>
            <figcaption>{e(c)}</figcaption>
          </figure>''' for q, c in s["reviews"])
    faq = "\n".join(f'''          <details>
            <summary>{e(q)}</summary>
            <p>{e(a)}</p>
          </details>''' for q, a in s["faq"])
    works = "\n".join(f"              <option>{e(w)}</option>" for w in s["works"])
    xid, xlabel, xph, xopt = s["extra"]
    opt = ' <span class="opt">(facultatif)</span>' if xopt else ""
    shop = s.get("shop")
    head_font, head_q, body_font, body_q = s["fonts"]

    url = f"{BASE_URL}/{s['dir']}/"
    h1a, h1b = s["h1"]
    biz = {
        "@type": s["schema"], "@id": url + "#entreprise", "name": s["name"], "url": url,
        "description": s["desc"], "slogan": f"{h1a} {h1b}", "telephone": s["tel"],
        "image": url + "hero.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": s["street"], "postalCode": s["cp"], "addressLocality": s["city"], "addressCountry": "FR"},
        "areaServed": [{"@type": "Place", "name": z} for z in s["zone"]],
        "openingHours": s["hours_schema"],
        "knowsAbout": [t for t, _ in s["servs"]],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["serv_h2"], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d, "areaServed": s["zone_short"], "provider": {"@id": url + "#entreprise"}}} for t, d in s["servs"]]},
    }
    if s.get("founder"):
        biz["founder"] = {"@type": "Person", "name": s["founder"][0], "jobTitle": s["founder"][1]}
    webpage = {"@type": "WebPage", "@id": url, "url": url, "name": s["title"], "description": s["desc"],
               "inLanguage": "fr-FR", "dateModified": UPDATED[0], "about": {"@id": url + "#entreprise"},
               "primaryImageOfPage": url + "hero.jpg"}
    faqld = {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
    graph = {"@context": "https://schema.org", "@graph": [biz, webpage, faqld]}
    ld = lambda o: '  <script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=2) + "\n  </script>"

    zone_label = s.get("zone_label") or ("Où nous trouver" if shop else "Nous intervenons à")
    L = labels(s)
    jobs_eyebrow = s.get("jobs_eyebrow") or f'{nav[2]} récent{"e" if nav[2].endswith("ions") else ""}s'
    jobs_h2 = s.get("jobs_h2", "Quelques exemples de ces derniers mois.")
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; form-action 'self'; base-uri 'self'; object-src 'none'; frame-src 'none'; upgrade-insecure-requests">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{e(s["title"])}</title>
  <meta name="description" content="{e(s["desc"])}">
  <link rel="icon" href="data:image/svg+xml,{favicon(s)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={head_q}&family={body_q}&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="{e(s["name"])}">
  <meta property="og:title" content="{e(s["title"])}">
  <meta property="og:description" content="{e(s["desc"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{url}hero.jpg">
  <meta property="og:image:alt" content="{e(s["alt"])}">
  <meta name="twitter:card" content="summary_large_image">
{ld(graph)}
</head>
<body>

  <a class="skip" href="#devis">{L["skip"]}</a>

  <!-- Bandeau infos pratiques -->
  <div class="topbar">
    <div class="wrap topbar-inner">
      <span>{TOP_ICONS[0]}{e(s["zone_short"])}</span>
      <span class="hide-sm">{TOP_ICONS[1]}{e(s["hours"])}</span>
      <span class="hide-sm">{TOP_ICONS[2]}{e(s["top3"])}</span>
    </div>
  </div>

  <!-- Navigation -->
  <header class="nav" id="nav">
    <div class="wrap nav-inner">
      <a class="brand" href="#top" aria-label="{e(s["name"])}, accueil">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 32 32">{s["icon"]}</svg>
        </span>
        <span class="brand-text">{e(s["name"])}<small>{e(s["tagline"])}</small></span>
      </a>
      <nav class="links" id="navLinks" aria-label="Navigation principale">
        <a href="#services">{nav[0]}</a>
        <a href="#deroulement">{nav[1]}</a>
        <a href="#chantiers">{nav[2]}</a>
        <a href="#faq">{nav[3]}</a>
        <a href="#devis" class="links-cta">{e(s["cta"])}</a>
      </nav>
      <a class="nav-phone" href="tel:{s["tel"]}">
        {ICON_PHONE}
        <span>{s["phone"]}</span>
      </a>
      <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <main id="top">

{hero(s)}

    <!-- SITUATIONS -->
    <section class="situations" aria-labelledby="sit-title">
      <div class="wrap">
        <h2 id="sit-title" class="h-small">{e(s["sit_title"])}</h2>
        <div class="sit-grid">
{sits}
        </div>
        <p class="sit-hint">{L["hint"]}</p>
      </div>
    </section>

    <!-- SERVICES -->
    <section class="services" id="services" aria-labelledby="serv-title">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">{e(s["serv_eyebrow"])}</p>
          <h2 id="serv-title">{e(s["serv_h2"])}</h2>
        </div>
        <div class="serv-grid">
{servs}
        </div>
      </div>
    </section>

    <!-- DÉROULEMENT -->
    <section class="steps" id="deroulement" aria-labelledby="steps-title">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">{nav[1]}</p>
          <h2 id="steps-title">{e(s["steps_h2"])}</h2>
        </div>
        <ol class="step-list">
{steps}
        </ol>
      </div>
    </section>

    <!-- RÉALISATIONS -->
    <section class="jobs" id="chantiers" aria-labelledby="jobs-title">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">{e(jobs_eyebrow)}</p>
          <h2 id="jobs-title">{e(jobs_h2)}</h2>
        </div>
        <div class="job-grid">
{jobs}
        </div>
      </div>
    </section>

    <!-- ENGAGEMENTS + AVIS -->
    <section class="trust" aria-labelledby="trust-title">
      <div class="wrap trust-grid">
        <div>
          <p class="eyebrow">Nos engagements</p>
          <h2 id="trust-title">{e(s["pledges_h2"])}</h2>
          <ul class="pledges">
{pledges}
          </ul>{signature}
        </div>
        <div class="reviews">
{reviews}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq" id="faq" aria-labelledby="faq-title">
      <div class="wrap faq-grid">
        <div class="sec-head">
          <p class="eyebrow">Questions fréquentes</p>
          <h2 id="faq-title">Ce qu'on nous demande le plus souvent.</h2>
          <p class="faq-more">Votre question n'est pas là ?<br>Appelez-nous au <a href="tel:{s["tel"]}">{s["phone"]}</a>.</p>
        </div>
        <div class="faq-list">
{faq}
        </div>
      </div>
    </section>

    <!-- DEVIS -->
    <section class="quote" id="devis" aria-labelledby="quote-title">
      <div class="wrap quote-grid">
        <div class="quote-side">
          <p class="eyebrow">{L["eyebrow"]}</p>
          <h2 id="quote-title">{e(s["quote_h2"])}</h2>
          <p>{e(s["quote_p"])}</p>
          <div class="contact-card">
            <a class="contact-line big" href="tel:{s["tel"]}">
              {ICON_PHONE}
              {s["phone"]}
            </a>
            <p class="contact-line">{e(s["hours"])}</p>
            <p class="contact-line">{e(s["street"])}, {s["cp"]} {e(s["city"])}</p>
            <p class="zone"><strong>{zone_label}</strong> {e(zone_txt)}.</p>
          </div>
        </div>

{form_html(s, L)}
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap footer-inner">
      <p><strong>{e(s["name"])}</strong> · {e(s["tagline"])} · {e(s["street"])}, {s["cp"]} {e(s["city"])}</p>
      <p>SIRET 000 000 000 00000 · Assurance n° à préciser · Page mise à jour le <time datetime="{UPDATED[0]}">{UPDATED[1]}</time> · <a href="#top">Retour en haut</a></p>
    </div>
  </footer>

  <!-- Barre d'action mobile -->
  <div class="mobile-bar">
    <a href="tel:{s["tel"]}" class="mb-call">
      {ICON_PHONE}
      Appeler
    </a>
    <a href="#devis" class="mb-quote">{L["mobile"]}</a>
  </div>

  <script src="script.js"></script>
</body>
</html>
'''


def favicon(s):
    ink, acc = s["pal"]["ink"], s["pal"]["accent"]
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='{ink}'/>"
           f"<g color='{acc}' fill='{acc}'>{s['icon'].replace(chr(34), chr(39))}</g></svg>")
    return svg.replace("#", "%23").replace("<", "%3C").replace(">", "%3E")


def css(s):
    base = (ROOT / "assets/metiers-base.css").read_text()
    for k, v in sorted(palette(s["pal"]).items(), key=lambda kv: -len(kv[0])):
        base = base.replace(k, v)
    head_font, _, body_font, _ = s["fonts"]
    base = base.replace('"Archivo"', f'"{head_font}"').replace('"Public Sans"', f'"{body_font}"')
    base = base.replace("/* Morel Plâtrerie · plâtre, ardoise et ocre */", f"/* {s['name']} */")
    ink = s["pal"]["ink"]
    v = (VARIANT_CSS.replace("INKA", rgba_prefix(ink) + " ")
         .replace("ONINK2", mix(ink, "#FFFFFF", .62)).replace("ONINK", mix(ink, "#FFFFFF", .8)))
    return base + v


JS = r"""/* __NAME__ · navigation, préremplissage et formulaire de démonstration */
(() => {
  "use strict";

  const nav = document.getElementById("nav");
  const burger = document.getElementById("burger");
  const links = document.getElementById("navLinks");

  // Ombre de la barre de navigation au défilement
  const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Menu mobile
  burger.addEventListener("click", () => {
    const open = burger.getAttribute("aria-expanded") === "true";
    burger.setAttribute("aria-expanded", String(!open));
    burger.setAttribute("aria-label", open ? "Ouvrir le menu" : "Fermer le menu");
    links.classList.toggle("open", !open);
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      burger.setAttribute("aria-expanded", "false");
      links.classList.remove("open");
    })
  );

  // Situations : préremplit le motif puis descend au formulaire
  const work = document.getElementById("work");
  document.querySelectorAll("[data-prefill]").forEach((btn) =>
    btn.addEventListener("click", () => {
      work.value = btn.dataset.prefill;
      work.closest(".field").classList.remove("invalid");
      document.getElementById("devis").scrollIntoView({ behavior: "smooth" });
      window.setTimeout(() => {
        work.classList.remove("flash");
        void work.offsetWidth;
        work.classList.add("flash");
        const next = document.querySelector("#quoteForm [data-rule]:not(#work)");
        if (next) next.focus({ preventScroll: true });
      }, 600);
    })
  );

  // Apparition douce des blocs
  const targets = document.querySelectorAll(".serv, .step-list li, .job, .review, .sit");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.15 });
    targets.forEach((t) => { t.classList.add("reveal"); io.observe(t); });
  }

  // Formulaire (démonstration : rien n'est envoyé)
  const form = document.getElementById("quoteForm");
  const loadedAt = Date.now();
  const date = form.querySelector('input[type="date"]');
  if (date) date.min = new Date().toISOString().slice(0, 10);
  const tests = {
    req: (v) => v.trim() !== "",
    name: (v) => v.trim().length >= 2,
    zip: (v) => /^\d{5}$/.test(v.trim()),
    phone: (v) => /^0\d{9}$/.test(v.replace(/[\s.\-]/g, "").replace(/^\+33/, "0")),
    email: (v) => v.trim() === "" || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()),
  };
  const fields = [...form.querySelectorAll("[data-rule]")];
  const check = (el) => {
    const ok = tests[el.dataset.rule](el.value);
    el.closest(".field").classList.toggle("invalid", !ok);
    el.setAttribute("aria-invalid", String(!ok));
    return ok;
  };
  fields.forEach((el) => el.addEventListener("blur", () => { if (el.value !== "") check(el); }));

  const WHEN = { "Matin": "le matin", "Midi": "entre 12 h et 14 h", "Après-midi": "l'après-midi" };
  form.addEventListener("submit", (ev) => {
    ev.preventDefault();
    // Robots : champ piège rempli ou envoi en moins de 3 secondes
    if (document.getElementById("website").value !== "" || Date.now() - loadedAt < 3000) return;
    const bad = fields.filter((el) => !check(el));
    if (bad.length) { bad[0].focus(); return; }
    const first = document.getElementById("name").value.trim().split(/\s+/)[0];
    const picked = form.querySelector('input[name="when"]:checked');
    const when = picked ? WHEN[picked.value] : "";
    document.getElementById("successMsg").textContent =
      __SUCCESS__.replace("{first}", first).replace("{when}", when);
    document.getElementById("success").hidden = false;
  });
})();
"""


def js(s):
    msg = s.get("success") or "Merci {first}. Nous vous rappelons {when} pour " + s["success_end"] + "."
    return JS.replace("__NAME__", s["name"]).replace("__SUCCESS__", json.dumps(msg, ensure_ascii=False))


def llms(s):
    url = f"{BASE_URL}/{s['dir']}/"
    L = labels(s)
    out = [f"# {s['name']}", "", f"> {s['desc']}", "",
           f"Mis à jour le {UPDATED[1]}.", "",
           "## Contact", "",
           f"- Téléphone : {s['phone']} ({s['hours']})",
           f"- Adresse : {s['street']}, {s['cp']} {s['city']}",
           f"- Zone : {', '.join(s['zone'])}",
           f"- {L['eyebrow']} : [formulaire]({url}#devis)"]
    if s.get("founder"):
        out.append(f"- Interlocuteur : {s['founder'][0]}, {s['founder'][1]}")
    out += ["", "## Services", ""] + [f"- **{t}** : {d}" for t, d in s["servs"]]
    out += ["", "## Engagements", ""] + [f"- **{a}** {b}" for a, b in s["pledges"]]
    out += ["", "## Questions fréquentes", ""]
    for q, a in s["faq"]:
        out += [f"### {q}", "", a, ""]
    return "\n".join(out)


def load_sites():
    sites = []
    for f in sorted((ROOT / "assets/sites").glob("*.py")):
        sites += runpy.run_path(str(f))["SITES"]
    return sites


def main():
    import sys
    only = sys.argv[1:]
    for s in load_sites():
        if only and not any(o in s["dir"] for o in only):
            continue
        d = ROOT / s["dir"]
        d.mkdir(parents=True, exist_ok=True)
        out = page(s)
        assert "—" not in out, s["dir"]
        (d / "index.html").write_text(out)
        (d / "styles.css").write_text(css(s))
        (d / "script.js").write_text(js(s))
        (d / "llms.txt").write_text(llms(s))
        print("ok", s["dir"])


if __name__ == "__main__":
    main()
