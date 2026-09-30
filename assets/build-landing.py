# -*- coding: utf-8 -*-
"""Génère la landing page portfolio ZYAGENCY."""
import html, io, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")

CART = ('<svg class="cart" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>'
        '<path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>')

# (slug, nom, étiquette, description, [3 couleurs], lien d'aperçu, en_ligne)
SECTIONS = [
 ("Plomberie", "Cinq plombiers, cinq clientèles : de la salle de bains de luxe à la fuite introuvable.", None, [
  ("aqua-lumiere","Aqua Lumière","Salles de bains · Paris 16e","Rénovation de salles de bains haut de gamme : plan 3D offert, chef de chantier unique, date de livraison écrite dans le devis.",['#0F2A33', '#C8A24B', '#EFEAE0'],"plomberie/01-aqua-lumiere/",True),
  ("meridian","Plomberie Méridien","Plombier · Grenoble","Pour le client qui craint l'arnaque : prix annoncé avant d'intervenir, compte rendu photo après chaque dépannage.",['#1A2A3A', '#F2665A', '#EAEEF3'],"plomberie/02-meridian/",True),
  ("copperline","Lefèvre & Fils","Plombiers depuis 1962 · Reims","L'entreprise familiale de quartier : dépannage sous 24 h, entretien de chaudière, salles de bains adaptées aux seniors.",['#2B2118', '#D08A4E', '#F1E7DA'],"plomberie/03-copperline/",True),
  ("stillwater","Onde Claire","Entretien eau et chauffage · Annecy","Vendre la tranquillité plutôt que la réparation : contrat d'entretien annuel, dépannage prioritaire, sans engagement.",['#173238', '#7CC3C9', '#E6F0F0'],"plomberie/04-stillwater/",True),
  ("nexa","NEXA Plomberie","Recherche de fuite · Montpellier","Recherche de fuite sans casse et rapport pour l'assurance : capter les propriétaires qui voient leur facture d'eau exploser.",['#0B1A24', '#2FE0BC', '#E6EEF2'],"plomberie/05-nexa/",True),
 ]),
 ("Serrurerie", "Du dépannage de nuit au contrôle d'accès : la confiance se gagne dès l'appel.", None, [
  ("bastion-clef","Bastion & Clef","Haute sécurité · Paris 8e","Portes blindées et serrures A2P pour une clientèle exigeante : audit de sécurité gratuit, discrétion absolue.",['#0E0E10', '#C9A54B', '#ECE7DC'],"serrurerie/01-bastion-clef/",True),
  ("keystone-lock","Clé de Voûte","Serrurier · Nantes, 7 j/7","Le serrurier anti-arnaque : prix affichés, devis signé avant d'agir, facture identique. L'appel passe en premier.",['#121110', '#F07A2E', '#EEEBE4'],"serrurerie/02-keystone-lock/",True),
  ("ironhaven","Serrurerie Hardy","Clés et serrures depuis 1954 · Strasbourg","La boutique de quartier : doubles de clés en 5 minutes, badges, clés de voiture, serrures anciennes restaurées.",['#1A1512', '#D9733F', '#EFE6D8'],"serrurerie/03-ironhaven/",True),
  ("haven-hour","Serrurier de Garde","Urgence 24 h/24 · Lyon","Pensé pour l'appel de 3 h du matin : un humain répond, le tarif de nuit est annoncé, un serrurier arrive en 40 minutes.",['#1B2A4A', '#E4B35A', '#E7EAF2'],"serrurerie/04-haven-hour/",True),
  ("aperio","Aperio Accès","Contrôle d'accès · Île-de-France","Pour les syndics et les entreprises : interphones, badges Vigik, contrôle d'accès, astreinte 24 h/24.",['#0A0E14', '#4C93FF', '#E6ECF6'],"serrurerie/05-aperio/",True),
 ]),
 ("Taxis & chauffeurs", "VTC, taxi conventionné, course immédiate : chacun répond à une question précise du voyageur.", None, [
  ("onyx-chauffeur","Onyx Chauffeurs","Chauffeur privé · Paris","VTC haut de gamme : prix fixe confirmé à la réservation, suivi de vol, pancarte à l'arrivée. Réservation en deux minutes.",['#0A0A0A', '#C9A24B', '#EAE8E3'],"taxis/01-onyx-chauffeur/",True),
  ("vector-taxi","Vecteur Taxi","Taxi à prix fixe · Marseille","Aéroport, gare, croisières : le prix est annoncé avant de monter. L'argument qui convertit les voyageurs méfiants.",['#101216', '#E4C04A', '#F0EDE0'],"taxis/02-vector-taxi/",True),
  ("checker-cab","Taxis Damier","Taxi conventionné · Bordeaux","Transport médical sans avance de frais, chauffeur attitré pour les séances régulières. Depuis 1947.",['#111111', '#F2C200', '#F1EEE4'],"taxis/03-checker-cab/",True),
  ("lumen-ride","Lumen Trajets","Taxi calme · Tours","Accompagnement porte à porte des seniors, SMS aux proches au départ et à l'arrivée, trajets longue distance.",['#243B55', '#E9A857', '#EDE6DB'],"taxis/04-lumen-ride/",True),
  ("pulse-taxi","Pulse Taxi","Taxi 24 h/24 · Lille","Course immédiate en 10 minutes en moyenne, jour et nuit. L'appel en premier, la réservation ensuite.",['#0A0D12', '#00D97E', '#E3EDEA'],"taxis/05-pulse-taxi/",True),
 ]),
 ("Dentistes", "Nouveaux patients, patients anxieux, implants, esthétique : chaque cabinet parle à ses patients.", None, [
  ("eclat-dental","Éclat","Dentiste esthétique · Paris 16e","Facettes, blanchiment, alignement : le patient voit son futur sourire en simulation avant de décider.",['#0F3A36', '#D9A690', '#F2EBE1'],"dentistes/01-eclat-dental/",True),
  ("arcline-dental","Cabinet Arcline","Implants · Lyon 6e","Implants dentaires expliqués étape par étape, avec la part remboursée écrite sur le devis. Rassure sur un gros budget.",['#0B1526', '#5B8CFF', '#E7EDF7'],"dentistes/02-arcline-dental/",True),
  ("hollyfield-dental","Cabinet dentaire du Parc","Dentistes de famille · Angers","« Nouveaux patients acceptés » en tête de page : la réponse à la pénurie de dentistes, des enfants aux seniors.",['#1E3B2C', '#D1AE5E', '#EEE8D8'],"dentistes/03-hollyfield-dental/",True),
  ("still-point-dental","Cabinet Sérénade","Patients anxieux · Bordeaux","Pour ceux qui repoussent le dentiste depuis des années : premier rendez-vous sans soin, gaz relaxant, aucun jugement.",['#1B2E2E', '#8CC3BE', '#E4EFEE'],"dentistes/04-still-point-dental/",True),
  ("nova-smile","Nova Sourire","Orthodontie adulte · Nice","Gouttières transparentes et simulation 3D offerte : le résultat visible avant de s'engager.",['#0F0C24', '#9B85FF', '#EAE7F7'],"dentistes/05-nova-smile/",True),
 ]),
 ("Ophtalmologie", "De l'opticien créateur à la chirurgie de la vue, des rendez-vous qui ne se font plus attendre.", None, [
  ("iris-prive","Iris Privé","Opticien créateur · Paris 6e","Essayage privé d'une heure, montures de créateurs, verres ajustés à vos usages. Tiers payant.",['#1C3F5A', '#C9A24B', '#EEE9DE'],"ophtalmologie/01-iris-prive/",True),
  ("meridian-eye","Institut Méridien","Chirurgie de la vue · Lyon","Opération de la myopie et de la cataracte : un bilan complet d'abord, aucune pression, devis écrit.",['#0B1420', '#4FA3F0', '#E4EDF6'],"ophtalmologie/02-meridian-eye/",True),
  ("hawthorne-eye","Cabinet de l'Aubépine","Ophtalmologistes · Rouen","Un rendez-vous en quatre semaines, pas en six mois : l'argument qui compte le plus pour les patients.",['#2E4A3A', '#C9A96A', '#EDE8DC'],"ophtalmologie/03-hawthorne-eye/",True),
  ("serene-vision","Vision Douce","Yeux secs et enfants · Nantes","Deux spécialités qui demandent du temps : la sécheresse oculaire et l'ophtalmologie de l'enfant.",['#183642', '#8FC6D8', '#E3F0F3'],"ophtalmologie/04-serene-vision/",True),
  ("vizn-lab","VIZN","Dépistage de la rétine · Toulouse","DMLA, glaucome, diabète : dépistage par OCT et résultats expliqués au patient le jour même.",['#05070D', '#33CFFF', '#E2EAF2'],"ophtalmologie/05-vizn-lab/",True),
 ]),
 ("Paysagistes", "Création, entretien, élagage, jardin sec : quatre paysagistes, quatre questions de clients différentes.", None, [
  ("seve-pierre","Sève & Pierre","Paysagistes · Yvelines","Création et entretien de jardins, crédit d'impôt de 50 % mis en avant : un jardin dont on profite au lieu d'y travailler.",['#1B3A2B', '#D08A55', '#ECE6D8'],"paysagistes/01-seve-pierre/",True),
  ("allees-vertes","Allées Vertes","Entretien de jardins · Orléans","Tonte, haies, désherbage : le crédit d'impôt de 50 % déduit directement de la facture, l'argument qui déclenche l'appel.",["#1F3A1C","#9ACD4E","#E7F0DD"],"paysagistes/02-allees-vertes/",True),
  ("cime-racine","Cime & Racine","Élagueurs grimpeurs · Morbihan","Élagage, abattage par démontage au-dessus des toits, urgence après tempête : rassurer sur un travail risqué.",["#16241C","#E0A43A","#E6E9DE"],"paysagistes/03-cime-racine/",True),
  ("jardins-de-garrigue","Jardins de Garrigue","Jardins secs · Vaucluse","Des jardins beaux en août malgré les restrictions d'eau : une réponse directe à la question que se posent les propriétaires du Sud.",["#2F3A26","#D9895A","#F1E7D6"],"paysagistes/04-jardins-de-garrigue/",True),
 ]),
 ("Avocats", "Particuliers, entrepreneurs, victimes, urgences pénales : quatre cabinets, quatre façons de rassurer avant le premier appel.", None, [
  ("roussel-associes","Roussel & Associés","Avocats · Montpellier","Divorce, licenciement, bail, succession : comprendre ses droits dès le premier rendez-vous, honoraires écrits.",['#101A2E', '#C4A15A', '#ECE8DD'],"avocats/01-roussel-associes/",True),
  ("castel-avocats","Castel Avocats","Avocats des entrepreneurs · Lyon","Création de société, contrats, impayés : des forfaits annoncés et une réponse en 48 h, le langage que comprennent les dirigeants.",["#14213D","#F4B942","#E7EAF0"],"avocats/02-castel-avocats/",True),
  ("delmas-victimes","Delmas Avocats","Défense des victimes · Toulouse","« L'assureur a ses avocats, vous avez droit au vôtre » : capter les victimes d'accidents avant qu'elles signent une offre trop basse.",["#2B2330","#E3A07D","#F0E9E2"],"avocats/03-delmas-victimes/",True),
  ("leroy-defense","Leroy Défense","Avocate pénaliste · Paris, 24 h/24","Pensé pour l'appel de la famille pendant une garde à vue : joignable la nuit, honoraires annoncés, l'appel en premier.",["#0D0D0D","#E55B5B","#E8E8E8"],"avocats/04-leroy-defense/",True),
 ]),
 ("Médecins généralistes", "Six cabinets, six façons d'installer la confiance dès la page d'accueil.", None, [
  ("cabinet-des-cedres","Cabinet des Cèdres","Médecine de famille · Lyon","Le suivi d'un médecin de famille, sans l'attente. Prise de rendez-vous mise en avant.",["#1B3A2B","#C9A24B","#F2EFE7"],"medecins/01-cabinet-des-cedres/",True),
  ("praxis","Praxis","Cabinet de groupe · Bordeaux","Plusieurs praticiens, un seul parcours limpide : choisir, réserver, être reçu.",["#0E1B2E","#3E82E0","#EEF2F7"],"medecins/02-praxis/",True),
  ("maison-bariol","Maison Bariol","Cabinet familial · Toulouse","Le cabinet qui voit grandir les enfants : un ton chaleureux qui fidélise les familles.",["#2C211A","#E4A79A","#F5ECE2"],"medecins/03-maison-bariol/",True),
  ("maison-vernier","Maison Vernier","Suivi privilégié · Paris","La médecine avec les égards d'une conciergerie, pour une patientèle exigeante.",["#14120E","#C9B48A","#EDE7DA"],"medecins/04-maison-vernier/",True),
  ("racine-sante","Racine Santé","Approche globale · Annecy","Soigner la cause, pas seulement le symptôme. Pour une patientèle en quête de sens.",["#2E3320","#B79A67","#EDE7D6"],"medecins/05-racine-sante/",True),
  ("cabinet-des-tilleuls","Cabinet des Tilleuls","Cabinet apaisé · Nantes","Un cabinet où l'on respire : l'antidote à la salle d'attente anxiogène.",["#12403E","#E8765A","#EAF1F0"],"medecins/06-cabinet-des-tilleuls/",True),
 ]),
 ("Santé — spécialistes", "Des spécialités où la réassurance fait la prise de rendez-vous.", None, [
  ("vision-etoile-paris","Vision Étoile","Ophtalmologie · Paris","Retrouver une vue nette, durablement. Tarifs, équipe et réponses aux craintes.",["#0E1A2B","#C9A24B","#EDE7DA"],"sante/01-vision-etoile/",True),
  ("verveine","Verveine","Sage-femme · Nantes","Accompagnées du premier jour au dernier : grossesse, naissance et post-partum.",["#26331F","#C98A9B","#F0EBE0"],"sante/02-verveine/",True),
  ("les-petits-pas","Les Petits Pas","Pédiatrie · Bordeaux","De la première visite aux grands pas : un parcours par âge qui parle aux parents.",["#123A56","#F0A6B0","#F5EFE6"],"sante/03-les-petits-pas/",True),
 ]),
 ("Artisanat & services à domicile", "Les métiers où l'on gagne l'appel avant même le devis.", None, [
  ("braise-chauffage","Braise","Chauffagiste · 24/7","Installation, dépannage et entretien. L'urgence traitée comme un argument de vente.",["#16110E","#FF5A1F","#F3E9E1"],"artisanat/01-braise/",True),
  ("boreal-climatisation","Boréal","Climatisation & pompes à chaleur","Température, pureté de l'air et silence : trois promesses chiffrées, donc crédibles.",["#0E1620","#4FB0DB","#EAF1F6"],"artisanat/02-boreal/",True),
  ("aupres-domicile","Auprès","Aide à domicile","Rester chez soi, entouré. Un ton juste qui s'adresse aux proches autant qu'aux aînés.",["#1B3628","#C08457","#F3EEE6"],"artisanat/03-aupres/",True),
  ("plombier-bleu-confiance","Bleu Confiance","Plombier chauffagiste","Le plombier qu'on rappelle : zones d'intervention, avis clients et devis en deux clics.",["#0F172A","#38B6EF","#F8FAFC"],"artisanat/04-bleu-confiance/",True),
  ("serrurier-acier-laiton","Acier & Laiton","Serrurier · urgence","Votre porte rouverte en trente minutes. Pensé pour capter la recherche d'urgence locale.",["#16181D","#C1902C","#F6F5F2"],"artisanat/05-acier-laiton/",True),
 ]),
 ("Bâtiment & métiers de proximité", "Des sites construits autour de la question du client : qui peut venir, quand, pour quoi, et comment le joindre en un geste.", None, [
  ("morel-platrerie","Morel Plâtrerie","Plâtrier plaquiste · Lyon","Cloisons, plafonds, enduits. Six situations concrètes qui préremplissent le devis : le visiteur se reconnaît et demande sa visite.",["#1E2A33","#D98B3A","#F4F1EA"],"platriers/01-morel-platrerie/",True),
  ("garnier-isolation","Garnier Isolation","Isolation · Nantes","Combles, murs, planchers. Le confort et les aides expliqués simplement, pour transformer la facture de chauffage en demande de devis.",["#12343B","#F2A541","#E9F1EF"],"isolation/01-garnier-isolation/",True),
  ("lebrun-terrassement","Lebrun Terrassement","Terrassier · Gironde","Terrassement, viabilisation, assainissement. Pour capter les particuliers qui ont leur permis en poche et cherchent qui prépare le terrain.",["#2A2118","#F2C230","#EFE9DD"],"terrassiers/01-lebrun-terrassement/",True),
  ("atelier-delorme","Atelier Delorme","Tapissier · Paris","Réfection de fauteuils, canapés et chaises. Devis sur photo et enlèvement à domicile : on retire tout frein avant la demande.",["#3B1520","#D9A79E","#F2E8DE"],"tapissiers/01-atelier-delorme/",True),
  ("ferrer-cuisines-stores","Ferrer Cuisines & Stores","Cuisines et stores · Aix","Pose de cuisines toutes marques, même en kit, et stores. Le site répond au client qui a déjà acheté et cherche un poseur fiable.",["#26301F","#E3B964","#EFEBDD"],"cuisinistes/01-ferrer-cuisines-stores/",True),
  ("cordonnerie-saint-clair","Cordonnerie Saint-Clair","Cordonnier · Toulouse","Ressemelage, talons minute, maroquinerie. Horaires, adresse et délais en évidence pour faire venir en boutique.",["#1F2B24","#D0935A","#F2E8D8"],"cordonniers/01-cordonnerie-saint-clair/",True),
  ("maconnerie-rocher","Maçonnerie Rocher","Maçon · Rennes","Extension, mur porteur, dalle. Démarches et planning expliqués pour rassurer sur un gros budget avant le premier appel.",["#26282B","#E4683F","#ECEAE6"],"macons/01-maconnerie-rocher/",True),
  ("carrosserie-dumas","Carrosserie Dumas","Carrossier · Lille","Sinistre, rayures, grêle. Le libre choix du garage et la gestion de l'assurance mis en avant : l'argument qui fait venir l'automobiliste.",["#15171C","#FF5A45","#E8EBF0"],"carrossiers/01-carrosserie-dumas/",True),
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
               else f'<span class="idx">{len(sites)} site{"s" if len(sites) > 1 else ""}</span>')
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
    .lede b{color:var(--fg);font-weight:600}
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

    .geo{border-top:1px solid var(--border);padding:5.5rem 0 1rem;position:relative}
    .geo h2{font-family:'Sentient',serif;font-weight:200;font-size:clamp(2rem,4.4vw,3.1rem);max-width:820px;line-height:1.1}
    .geo-lede{font-family:var(--mono);font-size:.88rem;color:var(--muted);max-width:62ch;margin-top:1.4rem;line-height:1.85}
    .shift{display:grid;gap:1.3rem;margin-top:3.2rem;grid-template-columns:repeat(auto-fit,minmax(275px,1fr))}
    .shift-card{border:1px solid var(--border);border-radius:16px;padding:1.9rem;background:var(--panel);position:relative}
    .shift-card.now{border-color:rgba(255,199,0,.5);background:linear-gradient(180deg,rgba(255,199,0,.07),transparent 60%),var(--panel)}
    .shift-card .when{font-family:var(--mono);font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(--primary);display:block;margin-bottom:1rem}
    .shift-card h3{font-family:'Sentient',serif;font-weight:200;font-size:1.45rem;margin-bottom:.7rem;line-height:1.2}
    .shift-card p{font-size:.88rem;color:var(--muted);line-height:1.7}
    .ask{margin-top:2.6rem;border:1px solid var(--border);border-radius:16px;padding:1.6rem 1.8rem;background:#060606;display:flex;align-items:flex-start;gap:1rem;flex-wrap:wrap}
    .ask .q{font-family:var(--mono);font-size:.82rem;color:var(--fg);line-height:1.7;flex:1 1 320px}
    .ask .q span{color:var(--primary)}
    .ask .verdict{font-family:var(--mono);font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;color:#000;background:var(--primary);border-radius:999px;padding:.5rem .95rem;font-weight:700;white-space:nowrap}
    .geo-band{margin-top:2.6rem;padding:1.5rem 1.8rem;border-radius:16px;border:1px solid rgba(255,199,0,.35);background:linear-gradient(90deg,rgba(255,199,0,.1),transparent 70%);font-family:var(--mono);font-size:.84rem;color:var(--fg);line-height:1.8}
    .geo-band b{color:var(--primary);font-weight:700}
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
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>ZYAGENCY — Être la réponse que les IA recommandent</title>
  <meta name="description" content="Vos clients demandent désormais à une IA qui appeler. Les moteurs d'IA ne citent que ce qu'ils ont lu : sans site, vous n'êtes pas une réponse possible. {total} sites vitrines ZYAGENCY, optimisés pour Google et pour les IA (GEO), prêts à porter votre nom.">
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
        <p class="eyebrow">Visibilité web · Référencement · GEO</p>
        <h1>Quand une IA recommandera<br>un professionnel,<br><i class="em">il faudra que ce soit vous.</i></h1>
        <p class="lede">Vos clients ne tapent plus seulement sur Google : ils demandent à une IA qui appeler. Et ces moteurs ne citent que ce qu'ils ont lu et compris. Sans site, vous n'êtes pas mal classé — vous êtes absent de la réponse. {total} sites vitrines prêts à porter votre nom, construits pour être trouvés par Google <b>et</b> repris par les IA.</p>
        <div class="cta-row">
          <a class="btn btn-white" href="#geo">Pourquoi c'est urgent</a>
          <a class="btn btn-yellow" href="#contact">Parlons de vos objectifs</a>
        </div>
      </div>
    </section>

    <section class="container">
      <div class="stats">
        <div class="stat"><b>{total}</b><span>Sites prêts à l'emploi</span></div>
        <div class="stat"><b>0</b><span>Chance d'être cité par une IA sans site</span></div>
        <div class="stat"><b>+8 ans</b><span>D'expérience</span></div>
        <div class="stat"><b>98%</b><span>Clients satisfaits</span></div>
      </div>
    </section>

    <section class="geo container" id="geo">
      <p class="eyebrow">Ce qui vient de changer</p>
      <h2>On ne cherche plus un professionnel.<br><i class="em">On en demande un.</i></h2>
      <p class="geo-lede">Pendant vingt ans, un site servait à exister, à rassurer et à capter les recherches Google. Ce rôle reste. Mais une deuxième porte d'entrée vient de s'ouvrir, et elle se referme sur ceux qui n'ont rien à lire en ligne.</p>

      <div class="shift">
        <div class="shift-card">
          <span class="when">Hier</span>
          <h3>On vous cherchait</h3>
          <p>L'annuaire, le bouche-à-oreille, puis Google. Le client comparait lui-même dix résultats. Être présent suffisait à être dans la liste.</p>
        </div>
        <div class="shift-card now">
          <span class="when">Aujourd'hui</span>
          <h3>On demande à une IA</h3>
          <p>« Quel est le meilleur artisan près de chez moi ? » L'IA ne renvoie plus dix liens : elle donne deux ou trois noms. Vous en faites partie, ou le client ne saura jamais que vous existez.</p>
        </div>
        <div class="shift-card">
          <span class="when">Demain</span>
          <h3>Être la réponse</h3>
          <p>Les IA ne recommandent que ce qu'elles ont lu, compris et recoupé. Un site clair, structuré et à jour, c'est votre dossier d'admission dans leurs réponses.</p>
        </div>
      </div>

      <div class="ask">
        <p class="q">Posez la question vous-même : <span>« Quel est le meilleur plombier à Bordeaux ? »</span> Comptez les noms cités. S'il n'y a pas le vôtre, ce n'est pas une question de prix ni de qualité de travail : l'IA n'avait simplement rien à lire sur vous.</p>
        <span class="verdict">Le test qui décide</span>
      </div>

      <p class="geo-band"><b>SEO</b> pour être trouvé sur Google. <b>SEA</b> pour capter la recherche au bon moment. <b>GEO</b> pour devenir la réponse que les IA recommandent. Les trois travaillent le même objectif : des demandes entrantes, donc du chiffre d'affaires.</p>
    </section>

{secs}
    <section class="how container">
      <p class="eyebrow">Comment ça se passe</p>
      <h2>De la réalisation qui vous plaît<br>à votre site <i class="em">en ligne.</i></h2>
      <div class="steps">
        <div class="step"><b>01</b><h3>Vous choisissez</h3><p>Parcourez les réalisations et retenez celle dont l'univers correspond à votre métier et à votre clientèle.</p></div>
        <div class="step"><b>02</b><h3>Nous l'habillons</h3><p>Votre nom, vos couleurs, vos textes, vos photos et vos prestations. Le site devient le vôtre, pas une copie.</p></div>
        <div class="step"><b>03</b><h3>Nous le rendons lisible</h3><p>Nom de domaine, référencement local et informations structurées pour que Google vous classe et que les IA puissent vous citer.</p></div>
        <div class="step"><b>04</b><h3>Nous le faisons vivre</h3><p>Contenus, avis et campagnes : vous restez la réponse recommandée, et les demandes continuent d'arriver mois après mois.</p></div>
      </div>
    </section>

    <section class="final" id="contact">
      <div class="container">
        <p class="eyebrow" style="margin-bottom:1.2rem">Votre partenaire digital</p>
        <h2>Faites en sorte que l'IA <i class="em">ait votre nom.</i></h2>
        <p>Sites vitrines, e-commerce, référencement Google, campagnes et visibilité auprès des IA. Dites-nous où vous voulez aller, nous construisons le chemin.</p>
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
