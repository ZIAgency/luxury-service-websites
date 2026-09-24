# -*- coding: utf-8 -*-
"""Génère la landing page portfolio ZYAGENCY (39 sites)."""
import html, io, os

OUT = "/home/user/luxury-service-websites/index.html"

CART = ('<svg class="cart" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>'
        '<path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>')

# (slug, nom, étiquette, description, [3 couleurs], lien d'aperçu, en_ligne)
SECTIONS = [
 ("Plomberie", "Des artisans de l'eau à qui l'on confie ses clés.", "plomberie/", [
  ("aqua-lumiere","Aqua Lumière","Atelier privé","Une plomberie de prestige, au service d'une clientèle qui attend le même soin qu'un hôtel cinq étoiles.",["#0E6E8C","#C8A24B","#101418"],"plomberie/01-aqua-lumiere/",True),
  ("meridian","Meridian","Précision d'ingénieur","Pour l'artisan qui rassure par la méthode : chaque chantier documenté, chaque devis limpide.",["#D7263D","#1A2A3A","#F2F2F2"],"plomberie/02-meridian/",True),
  ("copperline","Copperline & Sons","Maison familiale","L'entreprise transmise de père en fils, dont la réputation se construit depuis 1962.",["#B87333","#2B2118","#EFE6D8"],"plomberie/03-copperline/",True),
  ("stillwater","Stillwater","Confort & bien-être","Pour ceux qui vendent moins une réparation qu'un foyer apaisé. Entretien par abonnement.",["#3E7C8B","#DCEBEA","#12242A"],"plomberie/04-stillwater/",True),
  ("nexa","NEXA","Maison connectée","L'installateur tourné vers demain : pilotage de l'eau, détection de fuite, suivi en direct.",["#00E0B8","#0B0F1A","#7A8CA3"],"plomberie/05-nexa/",True),
 ]),
 ("Serrurerie", "La sécurité se vend d'abord par la confiance qu'on inspire.", "serrurerie/", [
  ("bastion-clef","Bastion & Clef","Atelier d'exception","Serrurerie haut de gamme pour biens d'exception : discrétion, savoir-faire, sur-mesure.",["#0E0E10","#B8973F","#E8E4DA"],"serrurerie/01-bastion-clef/",True),
  ("keystone-lock","Keystone Lock Co.","Expertise technique","L'expert qui démontre : mécanismes expliqués, contrôle qualité affiché, tarifs sans surprise.",["#E8631A","#121110","#F0EDE6"],"serrurerie/02-keystone-lock/",True),
  ("ironhaven","Ironhaven & Sons","Héritage d'atelier","Depuis 1954. Le poids de l'histoire familiale comme meilleure garantie de sérieux.",["#C1440E","#1A1512","#D9C7A3"],"serrurerie/03-ironhaven/",True),
  ("haven-hour","Haven & Hour","Urgence rassurante","Pensé pour l'appel de 3 h du matin : un ton calme, une présence, une intervention rapide.",["#1B2A4A","#E4B35A","#EDEFF5"],"serrurerie/04-haven-hour/",True),
  ("aperio","Aperio Systems","Contrôle d'accès","Pour l'entreprise qui équipe résidences et bureaux : badges, accès, gestion centralisée.",["#2D7FF9","#0A0E14","#AEB9C7"],"serrurerie/05-aperio/",True),
 ]),
 ("Taxis & chauffeurs", "Du trajet quotidien à la course de prestige.", "taxis/", [
  ("onyx-chauffeur","ONYX Chauffeurs","Grande remise","Clientèle affaires et soirées : voitures noires, chauffeurs en costume, ponctualité absolue.",["#0A0A0A","#C9A24B","#E8E8E8"],"taxis/01-onyx-chauffeur/",True),
  ("vector-taxi","Vector Taxi Co.","Prix forfaitaire","L'argument qui convertit : le prix connu d'avance, affiché avant même la réservation.",["#E4C04A","#101216","#F4F4F0"],"taxis/02-vector-taxi/",True),
  ("checker-cab","Checker & Sons","Institution locale","Depuis 1947. La compagnie que toute la ville connaît, et qu'on appelle par réflexe.",["#F2C200","#000000","#FFFFFF"],"taxis/03-checker-cab/",True),
  ("lumen-ride","Lumen Rides","Trajet serein","Le transport doux : véhicules silencieux, conduite posée, pour une clientèle qui veut souffler.",["#243B55","#E9A857","#F3EEE6"],"taxis/04-lumen-ride/",True),
  ("pulse-taxi","PULSE","Réservation instantanée","La flotte réactive : commande immédiate, véhicule suivi en direct, temps d'attente affiché.",["#00D97E","#0A0D12","#9AA7B4"],"taxis/05-pulse-taxi/",True),
 ]),
 ("Dentistes", "Un cabinet dentaire se choisit autant à la confiance qu'au sourire.", "dentistes/", [
  ("eclat-dental","Éclat Dental","Esthétique du sourire","Facettes et blanchiment pour une patientèle exigeante, prête à investir dans son sourire.",["#0F3A36","#D29B85","#FAF5EC"],"dentistes/01-eclat-dental/",True),
  ("arcline-dental","Arcline Dental Studio","Cabinet moderne","Pour les patients qui veulent comprendre : diagnostics illustrés et forfaits transparents.",["#1848C8","#0B1526","#FFFFFF"],"dentistes/02-arcline-dental/",True),
  ("hollyfield-dental","Hollyfield Family Dental","Cabinet de famille","Depuis 1961. Trois générations de patients, des enfants aux grands-parents.",["#1E3B2C","#B08D4A","#F7F1E3"],"dentistes/03-hollyfield-dental/",True),
  ("still-point-dental","Still Point Dental","Sans appréhension","Conçu pour les patients anxieux : ton apaisant, parcours rassurant, options de confort.",["#5B8A8A","#EAF1F0","#1B2E2E"],"dentistes/04-still-point-dental/",True),
  ("nova-smile","NOVA Smile Lab","Sourire sur mesure","La projection du résultat avant le traitement : l'argument qui déclenche la décision.",["#7B5CFF","#0A0A12","#B9C0D0"],"dentistes/05-nova-smile/",True),
 ]),
 ("Ophtalmologie", "De la consultation de quartier au plateau chirurgical.", "ophtalmologie/", [
  ("iris-prive","Iris Privé","Lunetterie d'auteur","L'optique comme pièce de créateur, pour une clientèle attachée au geste et à la matière.",["#1C3F5A","#C9A24B","#EDE7DA"],"ophtalmologie/01-iris-prive/",True),
  ("meridian-eye","Meridian Eye Institute","Institut chirurgical","Chirurgie réfractive : rassurer par les chiffres, les protocoles et les résultats mesurés.",["#0E63C4","#0B1420","#DCE6F2"],"ophtalmologie/02-meridian-eye/",True),
  ("hawthorne-eye","Hawthorne Eye Care","Cabinet de quartier","Depuis 1968. L'ophtalmologiste de famille, connu et recommandé de bouche à oreille.",["#2E4A3A","#B99653","#F1EBDD"],"ophtalmologie/03-hawthorne-eye/",True),
  ("serene-vision","Serene Vision","Douceur & pédiatrie","Sécheresse oculaire et jeunes patients : un univers rassurant pour les parents.",["#7FB0C4","#EAF4F6","#183642"],"ophtalmologie/04-serene-vision/",True),
  ("vizn-lab","VIZN Lab","Dépistage avancé","L'imagerie rétinienne comme différenciateur : détecter plus tôt, expliquer mieux.",["#00C2FF","#05070D","#8B98A8"],"ophtalmologie/05-vizn-lab/",True),
 ]),
 ("Médecins généralistes", "Six cabinets, six façons d'installer la confiance dès la page d'accueil.", None, [
  ("cabinet-des-cedres","Cabinet des Cèdres","Médecine de famille · Lyon","Le suivi d'un médecin de famille, sans l'attente. Prise de rendez-vous mise en avant.",["#1B3A2B","#C9A24B","#F2EFE7"],None,False),
  ("praxis","Praxis","Cabinet de groupe · Bordeaux","Plusieurs praticiens, un seul parcours limpide : choisir, réserver, être reçu.",["#0E1B2E","#3E82E0","#EEF2F7"],None,False),
  ("maison-bariol","Maison Bariol","Cabinet familial · Toulouse","Le cabinet qui voit grandir les enfants : un ton chaleureux qui fidélise les familles.",["#2C211A","#E4A79A","#F5ECE2"],None,False),
  ("maison-vernier","Maison Vernier","Suivi privilégié · Paris","La médecine avec les égards d'une conciergerie, pour une patientèle exigeante.",["#14120E","#C9B48A","#EDE7DA"],None,False),
  ("racine-sante","Racine Santé","Approche globale · Annecy","Soigner la cause, pas seulement le symptôme. Pour une patientèle en quête de sens.",["#2E3320","#B79A67","#EDE7D6"],None,False),
  ("cabinet-des-tilleuls","Cabinet des Tilleuls","Cabinet apaisé · Nantes","Un cabinet où l'on respire : l'antidote à la salle d'attente anxiogène.",["#12403E","#E8765A","#EAF1F0"],None,False),
 ]),
 ("Santé — spécialistes", "Des spécialités où la réassurance fait la prise de rendez-vous.", None, [
  ("vision-etoile-paris","Vision Étoile","Ophtalmologie · Paris","Retrouver une vue nette, durablement. Tarifs, équipe et réponses aux craintes.",["#0E1A2B","#C9A24B","#EDE7DA"],None,False),
  ("verveine","Verveine","Sage-femme · Nantes","Accompagnées du premier jour au dernier : grossesse, naissance et post-partum.",["#26331F","#C98A9B","#F0EBE0"],None,False),
  ("les-petits-pas","Les Petits Pas","Pédiatrie · Bordeaux","De la première visite aux grands pas : un parcours par âge qui parle aux parents.",["#123A56","#F0A6B0","#F5EFE6"],None,False),
 ]),
 ("Artisanat & services à domicile", "Les métiers où l'on gagne l'appel avant même le devis.", None, [
  ("braise-chauffage","Braise","Chauffagiste · 24/7","Installation, dépannage et entretien. L'urgence traitée comme un argument de vente.",["#16110E","#FF5A1F","#F3E9E1"],None,False),
  ("boreal-climatisation","Boréal","Climatisation & pompes à chaleur","Température, pureté de l'air et silence : trois promesses chiffrées, donc crédibles.",["#0E1620","#4FB0DB","#EAF1F6"],None,False),
  ("aupres-domicile","Auprès","Aide à domicile","Rester chez soi, entouré. Un ton juste qui s'adresse aux proches autant qu'aux aînés.",["#1B3628","#C08457","#F3EEE6"],None,False),
  ("plombier-bleu-confiance","Bleu Confiance","Plombier chauffagiste","Le plombier qu'on rappelle : zones d'intervention, avis clients et devis en deux clics.",["#0F172A","#38B6EF","#F8FAFC"],None,False),
  ("serrurier-acier-laiton","Acier & Laiton","Serrurier · urgence","Votre porte rouverte en trente minutes. Pensé pour capter la recherche d'urgence locale.",["#16181D","#C1902C","#F6F5F2"],None,False),
 ]),
]


def card(s):
    slug, name, tag, desc, cols, href, live = s
    img = f"assets/previews/{slug}.jpg"
    preview = href if live else img
    label = "Voir le site" if live else "Voir le visuel"
    soon = "" if live else '<span class="badge-soon">Mise en ligne prochaine</span>'
    sw = "".join(f'<i style="background:{c}"></i>' for c in cols)
    attr = f' data-preview-pending="{slug}"' if not live else ""
    return (
      f'<article class="card">'
      f'<a class="card-media" href="{preview}" target="_blank" rel="noopener" aria-label="Aperçu de {html.escape(name)}">'
      f'<img src="{img}" alt="Aperçu du site {html.escape(name)}" loading="lazy" width="1440" height="960">'
      f'{soon}<span class="media-cta">{label} ↗</span></a>'
      f'<div class="card-body">'
      f'<div class="swatches">{sw}</div>'
      f'<span class="tag">{tag}</span><h3>{name}</h3><p>{desc}</p></div>'
      f'<div class="card-actions">'
      f'<a class="card-demo" href="{preview}"{attr} target="_blank" rel="noopener">{label} ↗</a>'
      f'<a class="btn-buy" data-site="{slug}" href="#contact" aria-label="Acheter le site {html.escape(name)}">'
      f'{CART}<span>Acheter ce site</span></a></div></article>'
    )


def section(title, lede, hub, sites, idx):
    head = (f'<div class="series-head"><div><h2>{title}</h2><p class="series-lede">{lede}</p></div>'
            + (f'<a class="idx" href="{hub}">Voir la série ↗</a>' if hub
               else f'<span class="idx">{len(sites)} sites</span>')
            + '</div>')
    cards = "\n        ".join(card(s) for s in sites)
    return f'''    <!-- {title.upper()} -->
    <section class="series container" id="s{idx}">
      {head}
      <div class="grid">
        {cards}
      </div>
    </section>
'''


CSS = """
    @font-face{font-family:'Sentient';src:url('assets/fonts/Sentient-Extralight.woff') format('woff');font-weight:200;font-style:normal;font-display:swap}
    @font-face{font-family:'Sentient';src:url('assets/fonts/Sentient-LightItalic.woff') format('woff');font-weight:300;font-style:italic;font-display:swap}
    :root{
      --bg:#000;--fg:#fff;--primary:#FFC700;--primary-2:#E0AE00;
      --border:#424242;--muted:rgba(255,255,255,.6);--panel:#0A0A0A;
      --mono:ui-monospace,'SFMono-Regular','Menlo','Consolas',monospace;
    }
    *{margin:0;padding:0;box-sizing:border-box}
    html{scroll-behavior:smooth}
    body{background:var(--bg);color:var(--fg);font-family:Arial,Helvetica,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
    .container{width:min(1240px,92%);margin-inline:auto}
    i.em{font-family:'Sentient',serif;font-weight:300;font-style:italic;color:var(--primary)}
    a{color:inherit;text-decoration:none}
    img{display:block;max-width:100%}

    header{position:sticky;top:0;z-index:50;background:rgba(0,0,0,.74);backdrop-filter:blur(14px);border-bottom:1px solid var(--border)}
    .nav{display:flex;align-items:center;justify-content:space-between;height:68px}
    .brand{display:flex;align-items:center;gap:.7rem}
    .brand svg{width:26px;height:26px}
    .brand .word{font-family:'Sentient',serif;font-weight:200;font-size:1.15rem;letter-spacing:.28em}
    .nav-cta{font-family:var(--mono);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;font-weight:700;color:#000;background:linear-gradient(to bottom,#fff,#d4d4d4);padding:.6rem 1.1rem;border-radius:999px;transition:transform .3s ease}
    .nav-cta:hover{transform:scale(1.05)}

    .hero{padding:7rem 0 5rem;border-bottom:1px solid var(--border);position:relative;overflow:hidden}
    .hero::before{content:"";position:absolute;top:-30%;right:-10%;width:640px;height:640px;background:radial-gradient(circle,rgba(255,199,0,.14),transparent 62%);filter:blur(20px);pointer-events:none}
    .eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.24em;text-transform:uppercase;color:var(--primary);margin-bottom:1.6rem}
    h1{font-family:'Sentient',serif;font-weight:200;font-size:clamp(2.7rem,6.6vw,5.2rem);line-height:1.04;letter-spacing:-.01em;max-width:980px}
    .lede{font-family:var(--mono);font-size:.95rem;color:var(--muted);max-width:640px;margin-top:2rem;line-height:1.85}
    .cta-row{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2.6rem}
    .btn{cursor:pointer;border:0;border-radius:999px;padding:1rem 2rem;font-size:1rem;font-weight:600;color:#000;transition:transform .3s ease;display:inline-flex;align-items:center;gap:.5rem}
    .btn-white{background:linear-gradient(to bottom,#fff,#d4d4d4);box-shadow:0 8px 30px rgba(255,255,255,.15)}
    .btn-yellow{background:linear-gradient(to bottom,var(--primary),var(--primary-2));box-shadow:0 8px 30px rgba(255,199,0,.25)}
    .btn:hover{transform:scale(1.05)}

    .stats{display:grid;grid-template-columns:repeat(2,1fr);gap:2.4rem 1rem;padding:4rem 0;border-bottom:1px solid var(--border)}
    @media(min-width:900px){.stats{grid-template-columns:repeat(4,1fr)}}
    .stat b{font-family:'Sentient',serif;font-weight:200;font-size:clamp(2.6rem,5vw,3.4rem);color:var(--primary);display:block;line-height:1}
    .stat span{font-family:var(--mono);font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);display:block;margin-top:.7rem}

    .series{padding:5rem 0 1rem}
    .series-head{display:flex;align-items:flex-end;justify-content:space-between;gap:2rem;flex-wrap:wrap;padding-bottom:1.6rem;margin-bottom:2.2rem;border-bottom:1px solid var(--border)}
    .series-head h2{font-family:'Sentient',serif;font-weight:200;font-size:clamp(1.9rem,4vw,2.7rem)}
    .series-lede{font-family:var(--mono);font-size:.8rem;color:var(--muted);margin-top:.7rem;max-width:56ch;line-height:1.7}
    .series-head .idx{font-family:var(--mono);font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--primary);white-space:nowrap}

    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:1.4rem}
    .card{position:relative;display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--border);border-radius:18px;overflow:hidden;transition:transform .5s cubic-bezier(.16,1,.3,1),border-color .4s,box-shadow .5s}
    .card:hover{transform:translateY(-6px);border-color:rgba(255,199,0,.55);box-shadow:0 30px 60px -30px rgba(0,0,0,.9)}
    .card-media{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:#111;border-bottom:1px solid var(--border)}
    .card-media img{width:100%;height:100%;object-fit:cover;object-position:top center;transition:transform .7s cubic-bezier(.16,1,.3,1)}
    .card:hover .card-media img{transform:scale(1.045)}
    .media-cta{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(.94);font-family:var(--mono);font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:#000;background:var(--primary);padding:.62rem 1.1rem;border-radius:999px;opacity:0;transition:opacity .35s,transform .35s;white-space:nowrap}
    .card-media::after{content:"";position:absolute;inset:0;background:rgba(0,0,0,.45);opacity:0;transition:opacity .35s}
    .card:hover .card-media::after{opacity:1}
    .card:hover .media-cta{opacity:1;transform:translate(-50%,-50%) scale(1)}
    .badge-soon{position:absolute;top:.85rem;left:.85rem;z-index:2;font-family:var(--mono);font-size:.58rem;text-transform:uppercase;letter-spacing:.12em;color:var(--primary);background:rgba(0,0,0,.72);border:1px solid rgba(255,199,0,.4);border-radius:999px;padding:.3rem .65rem;backdrop-filter:blur(4px)}
    .card-body{padding:1.5rem 1.6rem .2rem;flex:1 1 auto}
    .swatches{display:flex;gap:.4rem;margin-bottom:1rem}
    .swatches i{width:19px;height:19px;border-radius:50%;border:1.5px solid rgba(255,255,255,.14)}
    .card .tag{display:block;font-family:var(--mono);font-size:.66rem;text-transform:uppercase;letter-spacing:.14em;color:var(--primary);margin-bottom:.5rem}
    .card h3{font-family:'Sentient',serif;font-weight:200;font-size:1.5rem;margin-bottom:.55rem}
    .card p{font-size:.87rem;color:var(--muted);line-height:1.65}
    .card-actions{margin-top:1.4rem;padding:1.2rem 1.6rem 1.6rem;display:flex;flex-direction:column;gap:.85rem;border-top:1px solid var(--border)}
    .card-demo{font-family:var(--mono);font-size:.71rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);transition:color .3s}
    .card-demo:hover{color:var(--fg)}
    .btn-buy{display:inline-flex;align-items:center;justify-content:center;gap:.6rem;width:100%;padding:.95rem 1.2rem;border-radius:999px;background:linear-gradient(to bottom,var(--primary),var(--primary-2));color:#000;font-weight:700;font-size:.97rem;box-shadow:0 8px 30px rgba(255,199,0,.25);transition:transform .3s ease,box-shadow .3s ease}
    .btn-buy:hover{transform:scale(1.04);box-shadow:0 12px 38px rgba(255,199,0,.4)}
    .btn-buy:focus-visible{outline:3px solid #fff;outline-offset:2px}

    .how{border-top:1px solid var(--border);margin-top:5rem;padding:5rem 0 1rem}
    .how h2{font-family:'Sentient',serif;font-weight:200;font-size:clamp(1.9rem,4vw,2.8rem);max-width:700px}
    .steps{display:grid;gap:2.2rem;margin-top:3rem;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
    .step b{font-family:var(--mono);font-size:.76rem;color:var(--primary);display:block;margin-bottom:.9rem;letter-spacing:.14em}
    .step h3{font-family:'Sentient',serif;font-weight:200;font-size:1.4rem;margin-bottom:.5rem}
    .step p{font-size:.88rem;color:var(--muted);line-height:1.65}

    .final{text-align:center;padding:6rem 0;margin-top:4rem;border-top:1px solid var(--border);position:relative;overflow:hidden}
    .final::before{content:"";position:absolute;bottom:-40%;left:50%;transform:translateX(-50%);width:700px;height:500px;background:radial-gradient(circle,rgba(255,199,0,.12),transparent 60%);pointer-events:none}
    .final h2{font-family:'Sentient',serif;font-weight:200;font-size:clamp(2.2rem,5vw,3.6rem);max-width:800px;margin:0 auto 1.6rem}
    .final p{font-family:var(--mono);font-size:.9rem;color:var(--muted);max-width:560px;margin:0 auto 2.4rem;line-height:1.8}

    footer{border-top:1px solid var(--border);padding:2.6rem 0}
    .foot{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;font-family:var(--mono);font-size:.74rem;color:var(--muted);letter-spacing:.04em}
    .foot .brand .word{font-size:.95rem}
    @media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

def build():
    secs = "\n".join(section(t, l, h, s, i + 1) for i, (t, l, h, s) in enumerate(SECTIONS))
    total = sum(len(s) for _, _, _, s in SECTIONS)
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self'; img-src 'self' data:; connect-src 'self'; form-action 'self'; base-uri 'self'; object-src 'none'; frame-src 'none'; upgrade-insecure-requests">
  <meta name="referrer" content="strict-origin-when-cross-answer">
  <title>ZYAGENCY — {total} sites vitrines prêts à l'emploi</title>
  <meta name="description" content="Découvrez {total} sites vitrines conçus par ZYAGENCY pour les métiers de proximité et les professions de santé. Choisissez le vôtre, nous l'adaptons à votre marque et le mettons en ligne.">
  <link rel="icon" href="assets/zy-logo.svg">
  <style>{CSS}  </style>
</head>
<body>
  <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><g id="zy">
    <path fill="currentColor" d="M101.141 53H136.632C151.023 53 162.689 64.6662 162.689 79.0573V112.904H148.112V79.0573C148.112 78.7105 148.098 78.3662 148.072 78.0251L112.581 112.898C112.701 112.902 112.821 112.904 112.941 112.904H148.112V126.672H112.941C98.5504 126.672 86.5638 114.891 86.5638 100.5V66.7434H101.141V100.5C101.141 101.15 101.191 101.792 101.289 102.422L137.56 66.7816C137.255 66.7563 136.945 66.7434 136.632 66.7434H101.141V53Z"/>
    <path fill="currentColor" d="M65.2926 124.136L14 66.7372H34.6355L64.7495 100.436V66.7372H80.1365V118.47C80.1365 126.278 70.4953 129.958 65.2926 124.136Z"/>
  </g></defs></svg>

  <header>
    <div class="container nav">
      <a class="brand" href="#top" aria-label="ZYAGENCY — accueil">
        <svg viewBox="0 0 180 180" style="color:var(--primary)"><use href="#zy"/></svg>
        <span class="word">ZYAGENCY</span>
      </a>
      <a class="nav-cta" href="#contact">Parlons de vos objectifs</a>
    </div>
  </header>

  <main id="top">
    <section class="hero">
      <div class="container">
        <p class="eyebrow">Nos réalisations</p>
        <h1>Votre futur site,<br><i class="em">déjà dessiné.</i></h1>
        <p class="lede">{total} sites vitrines pensés pour les métiers de proximité et les professions de santé. Chacun a sa propre identité, sa voix et son parcours de réservation. Choisissez celui qui vous ressemble : nous l'habillons à vos couleurs, vos textes et vos photos, puis nous le mettons en ligne.</p>
        <div class="cta-row">
          <a class="btn btn-white" href="#s1">Découvrir les réalisations</a>
          <a class="btn btn-yellow" href="#contact">Parlons de vos objectifs</a>
        </div>
      </div>
    </section>

    <section class="container">
      <div class="stats">
        <div class="stat"><b>{total}</b><span>Sites prêts à l'emploi</span></div>
        <div class="stat"><b>12</b><span>Métiers couverts</span></div>
        <div class="stat"><b>+8 ans</b><span>D'expérience</span></div>
        <div class="stat"><b>98%</b><span>Clients satisfaits</span></div>
      </div>
    </section>

{secs}
    <section class="how container">
      <p class="eyebrow">Comment ça se passe</p>
      <h2>De la réalisation qui vous plaît<br>à votre site <i class="em">en ligne.</i></h2>
      <div class="steps">
        <div class="step"><b>01</b><h3>Vous choisissez</h3><p>Parcourez les réalisations et retenez celle dont l'univers correspond à votre métier et à votre clientèle.</p></div>
        <div class="step"><b>02</b><h3>Nous l'habillons</h3><p>Votre nom, vos couleurs, vos textes, vos photos et vos prestations. Le site devient le vôtre, pas une copie.</p></div>
        <div class="step"><b>03</b><h3>Nous le mettons en ligne</h3><p>Nom de domaine, référencement local, formulaires de contact et de réservation connectés à votre boîte mail.</p></div>
        <div class="step"><b>04</b><h3>Nous le faisons vivre</h3><p>Référencement, campagnes et contenus : votre site continue de vous amener des clients, mois après mois.</p></div>
      </div>
    </section>

    <section class="final" id="contact">
      <div class="container">
        <p class="eyebrow" style="margin-bottom:1.2rem">Votre partenaire digital</p>
        <h2>Un site à la hauteur de <i class="em">votre savoir-faire</i> ?</h2>
        <p>Sites vitrines, e-commerce, référencement, campagnes et réseaux sociaux. Dites-nous où vous voulez aller, nous construisons le chemin.</p>
        <a class="btn btn-yellow" href="https://zyagency.fr" target="_blank" rel="noopener">Parlons de vos objectifs</a>
      </div>
    </section>
  </main>

  <footer>
    <div class="container foot">
      <a class="brand" href="#top">
        <svg viewBox="0 0 180 180" width="22" height="22" style="color:var(--primary)"><use href="#zy"/></svg>
        <span class="word">ZYAGENCY</span>
      </a>
      <span>© 2026 ZYAGENCY · Votre partenaire digital</span>
      <a class="card-demo" href="https://zyagency.fr" target="_blank" rel="noopener">zyagency.fr ↗</a>
    </div>
  </footer>
</body>
</html>
'''

if __name__ == "__main__":
    out = build()
    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print("written", OUT, len(out), "bytes")
