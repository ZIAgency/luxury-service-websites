#!/usr/bin/env python3
"""Génère les sites métiers orientés client (isolation, terrassement, tapisserie,
cuisines et stores, cordonnerie, maçonnerie, carrosserie).

Le modèle de référence est platriers/01-morel-platrerie (écrit à la main) :
même logique (hero avec photo du métier, situations qui préremplissent le devis,
services, étapes, chantiers, engagements, FAQ, formulaire court, barre mobile),
mais chaque site a sa palette, ses polices, sa mise en page de hero et ses textes.

Usage : python3 assets/build-metiers.py
Les photos (hero.jpg) sont téléchargées à part, depuis Pexels (voir PHOTO dans chaque site).
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "platriers/01-morel-platrerie"

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1Z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 16.2-3.5-3.5L4 14.2l5 5 11-11-1.4-1.4Z"/></svg>'
TOP_ICONS = [
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm1 10.4V6h-2v7.6l5 3 1-1.7Z"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5Z"/></svg>',
]

# ─────────────────────────────── Sites ───────────────────────────────

SITES = [
  {
    "dir": "isolation/01-garnier-isolation",
    "photo": ("6124239", "unrecognizable-worker-insulating-with-stone-wool-6124239", "introspectivedsgn"),
    "name": "Garnier Isolation", "tagline": "Isolation thermique à Nantes",
    "schema": "HomeAndConstructionBusiness",
    "city": "Nantes", "cp": "44300", "street": "8 rue de la Fonderie",
    "phone": "02 61 91 42 17", "tel": "+33261914217",
    "hours": "Du lundi au vendredi, 8 h à 18 h", "hours_schema": "Mo-Fr 08:00-18:00",
    "zone_short": "Nantes et Loire-Atlantique",
    "zone": ["Nantes", "Saint-Herblain", "Rezé", "Orvault", "Carquefou", "Vertou", "Sainte-Luce-sur-Loire", "La Chapelle-sur-Erdre", "Bouguenais"],
    "top3": "Artisan RGE",
    "title": "Isolation combles, murs et planchers à Nantes | Garnier Isolation",
    "desc": "Isolation des combles, des murs par l'intérieur ou l'extérieur et des planchers à Nantes. Artisan RGE : vos travaux peuvent ouvrir droit aux aides. Visite thermique et devis gratuits.",
    "fonts": ("Sora", "Sora:wght@500;600;700;800", "Karla", "Karla:wght@400;500;600"),
    "pal": dict(paper="#F7FAF9", chalk="#E9F1EF", ink="#12343B", muted="#51666A", line="#D3E0DD", accent="#F2A541", deep="#A8620C"),
    "layout": "split-right",
    "icon": '<path d="M5 26 16 6l11 20" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path class="blade" d="M10 22h12l-2-4h-8z"/>',
    "eyebrow": "Isolation thermique · Artisan RGE",
    "h1": ("Une maison chaude l'hiver,", "et des factures qui baissent."),
    "lead": "Combles, murs, planchers : on repère d'abord par où votre maison perd sa chaleur, puis on isole ce qui compte vraiment. Artisan RGE, nous vous aidons à monter vos dossiers d'aides.",
    "proofs": ["Visite thermique et devis gratuits", "Artisan RGE : travaux éligibles aux aides", "Combles isolés en une journée le plus souvent"],
    "cta": "Faire isoler ma maison", "note": "Réponse sous 24 h, visite sur place dans la semaine.",
    "badge": ("RGE", "artisan reconnu<br>garant de l'environnement"),
    "alt": "Un artisan pose des rouleaux de laine isolante entre les montants d'un mur",
    "sit_title": "Vous reconnaissez votre maison ?",
    "sits": [
      ("Il fait froid à l'étage malgré le chauffage", "La chaleur monte et s'échappe par le toit : les combles sont souvent le premier chantier.", "Isolation des combles perdus"),
      ("Mes murs sont froids au toucher", "Doublage isolant par l'intérieur, pièce par pièce, ou isolation par l'extérieur.", "Isolation des murs"),
      ("Mes pieds ont froid au rez-de-chaussée", "Isolation du plancher par le dessous, depuis le garage ou le vide sanitaire.", "Isolation du plancher bas"),
      ("Je veux aménager mes combles", "Isolation sous rampants, pare-vapeur et finition prête à peindre.", "Isolation des combles aménagés"),
      ("J'ai étouffé sous le toit cet été", "Un isolant épais et dense ralentit aussi la chaleur en été.", "Confort d'été"),
      ("Je veux savoir à quelles aides j'ai droit", "On vous explique les aides possibles selon vos revenus et vos travaux.", "Aides et financement"),
    ],
    "serv_eyebrow": "Nos travaux", "serv_h2": "On isole là où votre maison perd vraiment sa chaleur.",
    "servs": [
      ("Combles perdus", "Soufflage de laine minérale ou de ouate de cellulose sur toute la surface. Chantier rapide, sans toucher à vos pièces de vie."),
      ("Combles aménagés", "Isolation sous rampants avec pare-vapeur, pour transformer un grenier en chambre agréable été comme hiver."),
      ("Murs par l'intérieur", "Doublage isolant pièce par pièce, finition plaques prêtes à peindre. Idéal lors d'une rénovation."),
      ("Murs par l'extérieur", "Isolant fixé en façade puis enduit : vous gardez toute votre surface habitable et rafraîchissez la façade."),
      ("Planchers bas", "Panneaux isolants posés sous le plancher, depuis le garage, la cave ou le vide sanitaire."),
      ("Visite thermique", "Avant tout devis, on regarde votre maison, votre chauffage et vos factures pour prioriser les travaux."),
    ],
    "steps_h2": "De la visite aux travaux terminés, sans mauvaise surprise.",
    "steps": [
      ("Vous nous contactez", "Téléphone ou formulaire : dites-nous ce qui vous gêne, froid, humidité ou factures."),
      ("Visite thermique gratuite", "On inspecte combles, murs et planchers et on vous dit ce qui rapportera le plus."),
      ("Devis et aides", "Devis détaillé avec les aides possibles. On vous accompagne pour les dossiers."),
      ("Travaux propres et rapides", "Combles souvent faits en une journée. Nettoyage complet avant notre départ."),
    ],
    "job_labels": ("Travaux", "Durée"),
    "jobs": [
      ("Rezé · Maison des années 70", "Combles perdus isolés en ouate de cellulose", "Soufflage 90 m²", "1 jour"),
      ("Nantes · Longère rénovée", "Combles aménagés en deux chambres", "Rampants et pare-vapeur", "5 jours"),
      ("Orvault · Pavillon", "Plancher isolé depuis le garage", "Panneaux sous dalle", "2 jours"),
    ],
    "pledges_h2": "Ce que nous vous garantissons.",
    "pledges": [
      ("Un conseil honnête.", "Si un poste n'apporte rien chez vous, on vous le dit, même si cela réduit le devis."),
      ("Des aides bien montées.", "Nous vérifions avec vous les conditions avant la signature, pas après."),
      ("Un chantier propre.", "Protection des accès, aspiration des résidus, trappe refermée proprement."),
      ("Des garanties écrites.", "Qualification RGE et assurance décennale jointes au devis."),
    ],
    "reviews": [
      ("« L'étage était glacial l'hiver. Depuis l'isolation des combles, on a baissé le chauffage d'un cran et il fait bon partout. »", "Sophie L. · Rezé · Combles perdus"),
      ("« Ils nous ont aidés pour le dossier d'aides de A à Z. Chantier fini en une journée, rien à nettoyer derrière eux. »", "Thomas R. · Orvault · Combles et plancher"),
    ],
    "faq": [
      ("Par quoi commencer pour isoler sa maison ?", "Le plus souvent par la toiture : la chaleur monte, et des combles mal isolés sont une des premières sources de pertes. La visite thermique permet de confirmer l'ordre des travaux chez vous."),
      ("Quelles aides pour isoler en 2026 ?", "Selon vos revenus et vos travaux, des aides nationales et des primes énergie peuvent réduire la facture, à condition de passer par un artisan RGE comme nous. Nous vérifions votre éligibilité lors de la visite."),
      ("Combien de temps durent les travaux ?", "Des combles perdus s'isolent le plus souvent en une journée. Des combles aménagés ou une isolation de murs prennent quelques jours à deux semaines selon la surface."),
      ("Isolation par l'intérieur ou par l'extérieur ?", "L'intérieur coûte moins cher mais réduit un peu la surface des pièces. L'extérieur préserve la surface et traite les ponts thermiques, mais demande souvent une déclaration en mairie. On compare les deux chez vous."),
      ("Faut-il quitter la maison pendant les travaux ?", "Non. Pour les combles et les planchers, nous travaillons sans entrer dans vos pièces de vie. Pour les murs intérieurs, on avance pièce par pièce."),
      ("Quel isolant choisir ?", "Laine de verre, laine de roche, ouate de cellulose ou fibre de bois : chacun a ses atouts selon l'endroit, le budget et le confort d'été recherché. Nous vous conseillons selon votre maison."),
    ],
    "quote_h2": "Parlez-nous de votre maison.", "quote_p": "Deux minutes pour nous décrire votre logement. On vous rappelle pour fixer la visite thermique, gratuite et sans engagement.",
    "work_label": "Travaux envisagés",
    "works": ["Isolation des combles perdus", "Isolation des combles aménagés", "Isolation des murs", "Isolation du plancher bas", "Confort d'été", "Aides et financement", "Je ne sais pas encore"],
    "extra": ("year", "Année de construction", "Ex. : 1975", True),
    "details_ph": "Ex. : maison de 110 m², chauffage au gaz, étage froid l'hiver",
    "success_end": "fixer la visite thermique de votre maison",
    "nav": ["Nos travaux", "Comment ça se passe", "Chantiers", "Questions"],
  },
  {
    "dir": "terrassiers/01-lebrun-terrassement",
    "photo": ("36657008", "excavator-at-construction-site-with-earth-mound-36657008", "Vadym Alyekseyenko"),
    "name": "Lebrun Terrassement", "tagline": "Terrassement et VRD en Gironde",
    "schema": "HomeAndConstructionBusiness",
    "city": "Mérignac", "cp": "33700", "street": "27 avenue de l'Industrie",
    "phone": "05 36 49 18 62", "tel": "+33536491862",
    "hours": "Du lundi au vendredi, 7 h à 18 h", "hours_schema": "Mo-Fr 07:00-18:00",
    "zone_short": "Bordeaux et Gironde",
    "zone": ["Bordeaux", "Mérignac", "Pessac", "Talence", "Le Haillan", "Saint-Médard-en-Jalles", "Eysines", "Bègles", "Gradignan", "Villenave-d'Ornon"],
    "top3": "Engins et camions en propre",
    "title": "Terrassement, viabilisation, assainissement à Bordeaux | Lebrun Terrassement",
    "desc": "Terrassier à Mérignac et en Gironde : terrassement de maison et d'extension, viabilisation de terrain, assainissement individuel, fouilles de piscine, démolition. Visite et devis gratuits.",
    "fonts": ("Barlow Condensed", "Barlow+Condensed:wght@600;700;800", "Barlow", "Barlow:wght@400;500;600"),
    "pal": dict(paper="#FAF8F3", chalk="#EFE9DD", ink="#2A2118", muted="#6A5E50", line="#E0D7C6", accent="#F2C230", deep="#8A6508"),
    "layout": "overlay",
    "icon": '<path d="M4 24h24" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path class="blade" d="M6 20l6-10h6l-3 6h9l-3 4z"/>',
    "eyebrow": "Terrassier · Bordeaux et Gironde",
    "h1": ("Votre terrain prêt à construire,", "creusé, raccordé et remis propre."),
    "lead": "Terrassement de maison ou d'extension, viabilisation, assainissement, fouilles de piscine et démolition. Nos engins, nos camions, nos équipes : un seul interlocuteur du premier coup de pelle à l'évacuation des terres.",
    "proofs": ["Visite de terrain et devis gratuits", "Évacuation des terres comprise dans le devis", "Démarches réseaux faites par nos soins"],
    "cta": "Demander une visite de terrain", "note": "Réponse sous 24 h. Mini-pelle disponible pour les accès étroits.",
    "badge": ("18 ans", "de chantiers<br>en Gironde"),
    "alt": "Une pelleteuse jaune déplace de la terre sur un chantier",
    "sit_title": "Où en est votre projet ?",
    "sits": [
      ("J'ai mon permis, il faut préparer le terrain", "Décapage, fouilles des fondations, plateforme : prêt pour le maçon.", "Terrassement pour maison"),
      ("Mon terrain n'est pas raccordé", "Tranchées et branchements eau, électricité, télécom, eaux usées jusqu'à la maison.", "Viabilisation"),
      ("Ma fosse septique n'est plus aux normes", "Remplacement par une installation conforme, adaptée à votre sol.", "Assainissement individuel"),
      ("Je veux une piscine", "Fouille aux dimensions, évacuation ou régalage des terres sur place.", "Fouille de piscine"),
      ("Il faut démolir un vieux garage ou un abri", "Démolition, tri des gravats, terrain nivelé et propre.", "Démolition"),
      ("Mon terrain est en pente ou ravine", "Nivellement, talus, enrochement et drainage.", "Nivellement et drainage"),
    ],
    "serv_eyebrow": "Nos travaux", "serv_h2": "Tout ce qui se passe sous vos pieds avant de construire.",
    "servs": [
      ("Terrassement de maison et d'extension", "Décapage de la terre végétale, fouilles en rigole ou en pleine masse, plateforme compactée pour la dalle."),
      ("Viabilisation de terrain", "Tranchées et fourreaux pour l'eau, l'électricité, la fibre et le tout-à-l'égout, en lien avec les concessionnaires."),
      ("Assainissement individuel", "Fosse toutes eaux, filtre compact ou micro-station, selon l'étude de sol et les exigences du service de contrôle."),
      ("Fouilles de piscine", "Implantation, fouille aux cotes du pisciniste, évacuation ou régalage des déblais sur votre terrain."),
      ("Démolition", "Petits bâtiments, dalles, murets : démolition, tri et évacuation des gravats vers les filières adaptées."),
      ("Aménagements extérieurs", "Nivellement, drainage, enrochement, préparation des allées et des accès pour les véhicules."),
    ],
    "steps_h2": "Un chantier de terrassement bien préparé, c'est un chantier sans surprise.",
    "steps": [
      ("Vous nous appelez", "Envoyez le plan de masse ou quelques photos du terrain si vous les avez."),
      ("Visite du terrain", "Accès, nature du sol, pente, réseaux : on regarde tout avant de chiffrer."),
      ("Devis clair sous 72 h", "Terrassement, évacuation, remblais : chaque poste chiffré, au mètre cube quand c'est possible."),
      ("Chantier et remise en état", "Démarches réseaux faites, date tenue, terrain laissé propre et nivelé."),
    ],
    "job_labels": ("Travaux", "Durée"),
    "jobs": [
      ("Pessac · Maison neuve", "Terrassement et plateforme pour une maison de plain-pied", "Fouilles et plateforme", "3 jours"),
      ("Saint-Médard-en-Jalles · Terrain à bâtir", "Viabilisation complète sur 40 mètres", "Eau, électricité, fibre, eaux usées", "4 jours"),
      ("Gradignan · Jardin", "Fouille de piscine 8 × 4 m", "Fouille et régalage des terres", "2 jours"),
    ],
    "pledges_h2": "Nos engagements sur chaque chantier.",
    "pledges": [
      ("Le bon engin pour votre accès.", "Mini-pelle pour un passage étroit, pelle de 20 tonnes pour une grosse plateforme."),
      ("Des terres gérées.", "Évacuation, régalage ou réemploi sur place : c'est écrit dans le devis."),
      ("Les réseaux sécurisés.", "Déclarations préalables aux travaux faites par nos soins avant le premier coup de pelle."),
      ("Des garanties.", "Assurance décennale et responsabilité civile, attestations fournies avec le devis."),
    ],
    "reviews": [
      ("« Le terrain était prêt le jour prévu pour le maçon. Terres évacuées, plateforme nickel, rien à redire. »", "Nicolas P. · Pessac · Terrassement de maison"),
      ("« Ils ont tout géré pour la viabilisation, y compris les échanges avec les concessionnaires. Un vrai soulagement. »", "Aurélie D. · Eysines · Viabilisation"),
    ],
    "faq": [
      ("Combien coûte un terrassement ?", "Le prix dépend du volume de terre, de la nature du sol, de l'accès pour les engins et de la gestion des déblais (évacuation ou réemploi). Après la visite, nous chiffrons chaque poste pour que vous compariez sur une base claire."),
      ("Que comprend la viabilisation d'un terrain ?", "Le raccordement aux réseaux : eau potable, électricité, télécom et fibre, eaux usées et pluviales. Nous réalisons les tranchées et les branchements en lien avec chaque concessionnaire."),
      ("Ma fosse septique doit-elle être remplacée ?", "Si le contrôle du service d'assainissement l'a déclarée non conforme, oui, dans un délai fixé. Nous installons une solution adaptée à votre sol et à la taille du logement, après étude."),
      ("Vos engins passent-ils par un portail étroit ?", "Oui dans la plupart des cas : nos mini-pelles passent par un accès d'environ un mètre. On vérifie l'accès lors de la visite."),
      ("Que deviennent les terres extraites ?", "Selon votre projet, elles sont régalées sur le terrain, réutilisées en remblai ou évacuées. C'est décidé avec vous et chiffré dans le devis."),
      ("Faut-il faire des démarches avant de creuser ?", "Oui, des déclarations préalables sont obligatoires près des réseaux enterrés. Nous nous en occupons avant le démarrage du chantier."),
    ],
    "quote_h2": "Parlez-nous de votre terrain.", "quote_p": "Quelques informations suffisent. On vous rappelle pour fixer la visite de terrain, gratuite et sans engagement.",
    "work_label": "Type de travaux",
    "works": ["Terrassement pour maison", "Terrassement pour extension", "Viabilisation", "Assainissement individuel", "Fouille de piscine", "Démolition", "Nivellement et drainage", "Autre"],
    "extra": ("city", "Commune du terrain", "Ex. : Pessac", True),
    "details_ph": "Ex. : maison de 120 m² de plain-pied, terrain en légère pente, accès par un portail de 3 m",
    "success_end": "fixer la visite de votre terrain",
    "nav": ["Nos travaux", "Comment ça se passe", "Chantiers", "Questions"],
  },
  {
    "dir": "tapissiers/01-atelier-delorme",
    "photo": ("29224637", "artisan-working-in-istanbul-s-workshop-29224637", "Mesut Yalcin"),
    "name": "Atelier Delorme", "tagline": "Tapissier d'ameublement · Paris 11e",
    "schema": "LocalBusiness",
    "city": "Paris", "cp": "75011", "street": "42 rue de Charonne",
    "phone": "01 99 00 37 25", "tel": "+33199003725",
    "hours": "Du mardi au samedi, 9 h 30 à 18 h 30", "hours_schema": "Tu-Sa 09:30-18:30",
    "zone_short": "Paris et petite couronne",
    "zone": ["Paris (tous arrondissements)", "Montreuil", "Vincennes", "Saint-Mandé", "Bagnolet", "Les Lilas", "Charenton-le-Pont", "Boulogne-Billancourt", "Neuilly-sur-Seine"],
    "top3": "Enlèvement et livraison à domicile",
    "title": "Tapissier à Paris · Réfection de fauteuils, chaises, canapés | Atelier Delorme",
    "desc": "Tapissier d'ameublement à Paris 11e : réfection de fauteuils et de chaises en garniture traditionnelle ou moderne, recouverture de canapés, rideaux et coussins. Devis sur photo, enlèvement et livraison.",
    "fonts": ("Cormorant Garamond", "Cormorant+Garamond:ital,wght@0,600;0,700;1,600", "Jost", "Jost:wght@400;500;600"),
    "pal": dict(paper="#FBF7F2", chalk="#F2E8DE", ink="#3B1520", muted="#6E5A5E", line="#E6D8CC", accent="#D9A79E", deep="#8E2F43"),
    "layout": "split-left",
    "icon": '<path class="blade" d="M8 14c0-4 3.6-7 8-7s8 3 8 7v4H8z"/><path d="M7 18h18v4H7zM9 22v4M23 22v4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "eyebrow": "Tapissier d'ameublement · Paris",
    "h1": ("Le fauteuil de votre grand-mère,", "refait pour trente ans de plus."),
    "lead": "Réfection de sièges en garniture traditionnelle ou moderne, recouverture de canapés, chaises, têtes de lit, rideaux. Envoyez-nous une photo : vous recevez un devis sous 48 h, et nous venons chercher le meuble chez vous.",
    "proofs": ["Devis gratuit sur simple photo", "Enlèvement et livraison à domicile", "Plus de 400 tissus à voir à l'atelier, ou le vôtre"],
    "cta": "Envoyer ma demande de devis", "note": "Vous pouvez aussi passer à l'atelier avec votre chaise, sans rendez-vous.",
    "badge": ("1987", "un atelier ouvert<br>rue de Charonne"),
    "alt": "Un artisan tapissier travaille un siège dans son atelier",
    "sit_title": "Qu'est-ce qu'on refait pour vous ?",
    "sits": [
      ("Mon fauteuil s'affaisse quand on s'assoit", "Sangles, ressorts et garniture refaits : l'assise retrouve sa tenue.", "Réfection de fauteuil"),
      ("Le tissu de mon canapé est usé ou démodé", "Recouverture complète, avec ou sans reprise des mousses.", "Recouverture de canapé"),
      ("J'ai une série de chaises à refaire", "Assises refaites à l'identique, même tissu pour toute la série.", "Chaises"),
      ("J'ai hérité d'un siège ancien", "Garniture traditionnelle au crin, dans le respect du style d'origine.", "Siège ancien, garniture traditionnelle"),
      ("Je veux une tête de lit sur mesure", "Capitonnée, droite ou cintrée, aux dimensions de votre lit.", "Tête de lit sur mesure"),
      ("Il me faut des rideaux qui tombent bien", "Prise de mesures chez vous, confection et pose.", "Rideaux et voilages"),
    ],
    "serv_eyebrow": "L'atelier", "serv_h2": "Des sièges refaits dans les règles, et des tissus qui vous ressemblent.",
    "servs": [
      ("Garniture traditionnelle", "Sangles de jute, ressorts guindés à la main, crin et toile : la méthode d'origine pour les sièges anciens et de style."),
      ("Garniture moderne", "Mousses haute résilience et ouatine pour les sièges contemporains, les banquettes et les chaises du quotidien."),
      ("Canapés et banquettes", "Recouverture, reprise des assises, coussins de dossier regarnis. Enlèvement et livraison compris."),
      ("Chaises et séries", "Refaire six chaises d'un coup, c'est notre quotidien : même tissu, même tenue, même rendu."),
      ("Têtes de lit et sur-mesure", "Têtes de lit capitonnées, bancs de pied de lit, coussins de banquette de fenêtre."),
      ("Rideaux et voilages", "Mesures chez vous, confection à l'atelier, pose des tringles et des rideaux."),
    ],
    "steps_h2": "Du premier message au siège livré chez vous.",
    "steps": [
      ("Vous envoyez une photo", "Face, profil et l'état de l'assise : cela suffit pour un premier devis."),
      ("Devis sous 48 h", "Prix de la main-d'œuvre, du tissu et des fournitures, délai annoncé."),
      ("Choix du tissu", "À l'atelier parmi nos échantillons, ou avec votre propre tissu."),
      ("Enlèvement et livraison", "On vient chercher le meuble et on vous le rapporte, refait, à la date prévue."),
    ],
    "job_labels": ("Travail", "Délai"),
    "jobs": [
      ("Paris 11e · Fauteuil Voltaire", "Garniture traditionnelle refaite au crin, velours côtelé", "Réfection complète", "4 semaines"),
      ("Vincennes · Six chaises de salle à manger", "Assises refaites et recouvertes en lin lavé", "Série de chaises", "3 semaines"),
      ("Paris 15e · Canapé trois places", "Recouverture et coussins regarnis", "Recouverture", "5 semaines"),
    ],
    "pledges_h2": "Notre façon de travailler.",
    "pledges": [
      ("Un devis complet.", "Main-d'œuvre, tissu au mètre et fournitures : vous savez exactement ce que vous payez."),
      ("Le respect du meuble.", "Un siège ancien est refait selon sa méthode d'origine, pas en mousse par facilité."),
      ("Un délai annoncé et tenu.", "La date de livraison est écrite sur le devis."),
      ("Zéro transport pour vous.", "Enlèvement et livraison à Paris et en petite couronne."),
    ],
    "reviews": [
      ("« Le fauteuil de ma grand-mère était fichu. Il est plus confortable qu'avant et le velours choisi est superbe. »", "Hélène V. · Paris 12e · Fauteuil Voltaire"),
      ("« Devis reçu le lendemain sur photo, enlèvement et livraison impeccables. Les six chaises sont comme neuves. »", "Marc T. · Vincennes · Série de chaises"),
    ],
    "faq": [
      ("Combien coûte la réfection d'un fauteuil ?", "Le prix dépend de la taille du siège, du type de garniture (traditionnelle ou moderne) et du tissu choisi. Envoyez-nous une photo : vous recevez un devis détaillé sous 48 h."),
      ("Combien de temps faut-il compter ?", "En général de trois à six semaines selon le travail et la disponibilité du tissu. Le délai exact figure sur le devis."),
      ("Puis-je fournir mon propre tissu ?", "Oui. Nous vous indiquons le métrage nécessaire avant l'achat, en tenant compte des raccords de motifs."),
      ("Garniture traditionnelle ou moderne : laquelle choisir ?", "La traditionnelle (ressorts, crin) convient aux sièges anciens et de style et dure très longtemps. La moderne (mousse) est adaptée aux sièges contemporains et coûte moins cher. Nous vous conseillons selon le meuble."),
      ("Venez-vous chercher le meuble ?", "Oui, à Paris et en petite couronne. Vous pouvez aussi le déposer à l'atelier, rue de Charonne."),
      ("Refaites-vous aussi les sièges de voiture ou de bateau ?", "Non, nous sommes spécialisés dans l'ameublement. Nous pouvons en revanche vous orienter vers un sellier."),
    ],
    "quote_h2": "Parlez-nous de votre meuble.", "quote_p": "Décrivez le meuble en quelques mots. On vous rappelle pour convenir de l'envoi des photos et vous remettre un devis sous 48 h.",
    "work_label": "Meuble ou travail",
    "works": ["Réfection de fauteuil", "Recouverture de canapé", "Chaises", "Siège ancien, garniture traditionnelle", "Tête de lit sur mesure", "Rideaux et voilages", "Autre"],
    "extra": ("qty", "Nombre de pièces", "Ex. : 1 fauteuil, 6 chaises", True),
    "details_ph": "Ex. : fauteuil Louis XVI, assise affaissée, je voudrais un velours vert",
    "success_end": "organiser l'envoi des photos de votre meuble",
    "nav": ["L'atelier", "Comment ça se passe", "Réalisations", "Questions"],
  },
  {
    "dir": "cuisinistes/01-ferrer-cuisines-stores",
    "photo": ("15124970", "men-working-inside-a-house-under-repairs-15124970", "Thoinamcao"),
    "name": "Ferrer Cuisines & Stores", "tagline": "Pose de cuisines et stores · Aix-en-Provence",
    "schema": "HomeAndConstructionBusiness",
    "city": "Aix-en-Provence", "cp": "13090", "street": "5 chemin de la Blanque",
    "phone": "04 65 71 86 30", "tel": "+33465718630",
    "hours": "Du lundi au samedi matin, 8 h à 18 h", "hours_schema": "Mo-Fr 08:00-18:00",
    "zone_short": "Aix, Marseille et le pays d'Aix",
    "zone": ["Aix-en-Provence", "Marseille", "Gardanne", "Vitrolles", "Les Milles", "Venelles", "Bouc-Bel-Air", "Trets", "Éguilles", "Pertuis"],
    "top3": "Poseurs salariés, pas de sous-traitance",
    "title": "Pose de cuisine et stores à Aix-en-Provence | Ferrer Cuisines & Stores",
    "desc": "Installateur à Aix-en-Provence et Marseille : pose de cuisines (y compris achetées en grande surface), plans de travail, électroménager encastré, stores bannes, stores intérieurs et volets roulants motorisés.",
    "fonts": ("DM Serif Display", "DM+Serif+Display", "DM Sans", "DM+Sans:wght@400;500;600;700"),
    "pal": dict(paper="#FAF8F2", chalk="#EFEBDD", ink="#26301F", muted="#5E6655", line="#DEDACB", accent="#E3B964", deep="#7D5E17"),
    "layout": "split-right",
    "icon": '<rect x="6" y="8" width="20" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2.4"/><path class="blade" d="M6 13h20v3H6z"/>',
    "eyebrow": "Pose de cuisines et stores · Pays d'Aix",
    "h1": ("Votre cuisine posée au millimètre,", "vos stores installés dans la foulée."),
    "lead": "Vous avez acheté votre cuisine, en magasin ou en ligne ? On la monte, on l'ajuste et on la raccorde. Et pour l'été, stores bannes et volets roulants motorisés, posés par les mêmes équipes.",
    "proofs": ["Cuisines de toutes marques, même en kit", "Plomberie et électricité raccordées", "Devis gratuit sous 48 h après métré"],
    "cta": "Demander mon devis de pose", "note": "Une cuisine standard est posée en 2 à 4 jours.",
    "badge": ("2 à 4 j", "pour poser<br>une cuisine standard"),
    "alt": "Un poseur installe des meubles de cuisine dans une maison en rénovation",
    "sit_title": "Qu'est-ce qu'on installe chez vous ?",
    "sits": [
      ("J'ai acheté ma cuisine en kit", "Montage, mise à niveau, découpes, fixation murale et raccordements.", "Pose de cuisine en kit"),
      ("Je veux changer seulement le plan de travail", "Dépose de l'ancien, découpes évier et plaque, pose du nouveau.", "Plan de travail"),
      ("Il faut encastrer four, plaque et lave-vaisselle", "Découpes, raccordements eau et électricité, mise en service.", "Électroménager encastré"),
      ("Ma terrasse est brûlante l'après-midi", "Store banne sur mesure, manuel ou motorisé avec capteur de vent.", "Store banne"),
      ("Je veux motoriser mes volets", "Volets roulants motorisés, commandés à distance ou programmés.", "Volets roulants"),
      ("Je cherche des stores intérieurs", "Stores enrouleurs, vénitiens ou plissés, occultants ou tamisants.", "Stores intérieurs"),
    ],
    "serv_eyebrow": "Nos poses", "serv_h2": "La cuisine et les protections solaires, posées par la même équipe.",
    "servs": [
      ("Pose de cuisine complète", "Montage des caissons, réglage des portes, fixation des meubles hauts, fileurs et plinthes ajustés."),
      ("Plans de travail", "Stratifié, bois, quartz : découpes d'évier, de plaque et de crédence faites sur place, joints propres."),
      ("Raccordements", "Évier, lave-vaisselle, hotte, plaque et four raccordés et testés avant notre départ."),
      ("Stores bannes", "Stores sur mesure pour terrasses et balcons, motorisation et capteur vent-soleil en option."),
      ("Volets roulants", "Remplacement ou motorisation de volets existants, commande murale, télécommande ou smartphone."),
      ("Stores intérieurs", "Enrouleurs, vénitiens, plissés ou bateaux, mesurés et posés dans toutes les pièces."),
    ],
    "steps_h2": "Une pose préparée, une cuisine utilisable le jour prévu.",
    "steps": [
      ("Vous nous contactez", "Envoyez le plan de votre cuisine ou la référence de vos stores."),
      ("Métré chez vous", "On vérifie les murs, les niveaux, les arrivées d'eau et d'électricité."),
      ("Devis sous 48 h", "Pose, découpes, raccordements : tout est détaillé, prix ferme."),
      ("Pose et mise en service", "Tout est testé avec vous avant notre départ, emballages évacués."),
    ],
    "job_labels": ("Pose", "Durée"),
    "jobs": [
      ("Aix-en-Provence · Appartement", "Cuisine en kit de 4 mètres linéaires avec îlot", "Montage et raccordements", "3 jours"),
      ("Venelles · Villa", "Store banne motorisé de 5 mètres sur terrasse", "Pose et motorisation", "1 jour"),
      ("Marseille 8e · Maison", "Plan de travail en quartz et électroménager encastré", "Découpes et raccordements", "1 jour"),
    ],
    "pledges_h2": "Ce que vous pouvez attendre de nous.",
    "pledges": [
      ("Des poseurs salariés.", "Les personnes qui viennent chez vous font partie de l'équipe, pas d'un sous-traitant du jour."),
      ("Un prix ferme.", "Le devis signé est le prix payé, découpes et raccordements compris."),
      ("Une cuisine qui fonctionne.", "Eau, électricité, électroménager : tout est testé avec vous."),
      ("Un chantier rangé.", "Cartons et emballages évacués, sols protégés et nettoyés."),
    ],
    "reviews": [
      ("« Cuisine achetée en ligne, posée en trois jours. Les portes sont parfaitement alignées, et ils ont tout raccordé. »", "Laura S. · Aix-en-Provence · Pose de cuisine"),
      ("« Le store banne a changé notre été. Pose propre, motorisation expliquée, rien à reprocher. »", "Philippe G. · Venelles · Store banne"),
    ],
    "faq": [
      ("Posez-vous des cuisines achetées en grande surface ou en ligne ?", "Oui, c'est une grande partie de notre activité. Nous montons et posons les cuisines de toutes marques, livrées en kit ou déjà montées."),
      ("Combien coûte la pose d'une cuisine ?", "Le prix dépend du nombre de meubles, des découpes du plan de travail et des raccordements. Après le métré, vous recevez un devis ferme et détaillé."),
      ("Combien de temps dure la pose ?", "Entre deux et quatre jours pour une cuisine standard. Un îlot ou un plan de travail en pierre peut ajouter un jour."),
      ("Faites-vous la plomberie et l'électricité ?", "Oui pour les raccordements de la cuisine : évier, lave-vaisselle, hotte, plaque, four. Si une arrivée doit être déplacée, nous vous le signalons au métré."),
      ("Un store banne est-il soumis à autorisation ?", "Sur une maison, une déclaration en mairie peut être demandée selon votre commune. En copropriété, l'accord du syndic est souvent nécessaire. On vous aide à vérifier."),
      ("Peut-on motoriser des volets roulants existants ?", "Souvent oui, en remplaçant le treuil par un moteur tubulaire. On vérifie le coffre et le tablier lors du métré."),
    ],
    "quote_h2": "Parlez-nous de votre projet.", "quote_p": "Cuisine, stores ou les deux : décrivez-nous votre besoin. On vous rappelle pour fixer le métré, gratuit et sans engagement.",
    "work_label": "Type de pose",
    "works": ["Pose de cuisine en kit", "Pose de cuisine montée", "Plan de travail", "Électroménager encastré", "Store banne", "Volets roulants", "Stores intérieurs", "Autre"],
    "extra": ("brand", "Marque ou magasin de la cuisine", "Ex. : acheté en ligne, en grande surface…", True),
    "details_ph": "Ex. : cuisine en L de 3,5 m avec colonne four, livraison prévue le 15",
    "success_end": "fixer le métré chez vous",
    "nav": ["Nos poses", "Comment ça se passe", "Réalisations", "Questions"],
  },
  {
    "dir": "cordonniers/01-cordonnerie-saint-clair",
    "photo": ("14832520", "shoemaker-repairing-shoes-in-his-workshop-14832520", "Zeynep Sude Emek"),
    "name": "Cordonnerie Saint-Clair", "tagline": "Cordonnier · Toulouse centre",
    "schema": "LocalBusiness",
    "city": "Toulouse", "cp": "31000", "street": "19 rue Saint-Rome",
    "phone": "05 36 49 72 05", "tel": "+33536497205",
    "hours": "Du mardi au samedi, 9 h à 19 h", "hours_schema": "Tu-Sa 09:00-19:00",
    "zone_short": "Boutique rue Saint-Rome",
    "zone": ["Toulouse", "Envoi postal partout en France"],
    "top3": "Talons et patins en 15 minutes",
    "title": "Cordonnier à Toulouse · Ressemelage, talons, cuir | Cordonnerie Saint-Clair",
    "desc": "Cordonnier au centre de Toulouse : ressemelage cuir et gomme, talons minute, couture, teinture, réparation de sacs et de ceintures, doubles de clés. Devis gratuit en boutique ou sur photo.",
    "fonts": ("Young Serif", "Young+Serif", "Work Sans", "Work+Sans:wght@400;500;600"),
    "pal": dict(paper="#FBF7F0", chalk="#F2E8D8", ink="#1F2B24", muted="#5F6760", line="#E4D9C6", accent="#D0935A", deep="#8C5424"),
    "layout": "split-left",
    "icon": '<path class="blade" d="M5 20c4 0 7-2 9-6l3 2c2 1 5 2 9 2v4H5z"/><path d="M5 24h21" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "eyebrow": "Cordonnier · Toulouse centre",
    "h1": ("Vos chaussures préférées,", "remises en état au lieu d'être jetées."),
    "lead": "Ressemelage, talons, coutures, teinture, sacs et ceintures. Déposez vos pièces en boutique rue Saint-Rome : devis immédiat, talons et patins faits pendant que vous attendez.",
    "proofs": ["Devis immédiat en boutique, gratuit", "Talons et patins faits en 15 minutes", "Ressemelage cuir cousu à l'atelier"],
    "cta": "Demander un devis", "note": "Sans rendez-vous. Pour un envoi postal, décrivez vos pièces dans le formulaire.",
    "badge": ("15 min", "pour des talons<br>ou des patins neufs"),
    "alt": "Un cordonnier répare une chaussure dans son atelier",
    "sit_title": "Qu'est-ce qui ne va pas ?",
    "sits": [
      ("Mes talons sont usés jusqu'au bois", "Talons refaits en 15 minutes, en gomme ou en cuir.", "Talons"),
      ("La semelle est trouée ou décollée", "Ressemelage complet ou demi-semelle, cuir ou gomme.", "Ressemelage"),
      ("Mes chaussures neuves glissent", "Patins antidérapants posés pendant que vous attendez.", "Patins"),
      ("Une couture a lâché", "Reprise à la machine ou à la main, fil assorti.", "Couture"),
      ("Mon sac ou ma ceinture est abîmé", "Anses, fermetures, doublures, bords teintés, trous de ceinture.", "Maroquinerie"),
      ("Le cuir est terne ou taché", "Nettoyage, rénovation et teinture du cuir.", "Rénovation et teinture"),
    ],
    "serv_eyebrow": "L'atelier", "serv_h2": "Tout ce qu'on peut réparer, plutôt que racheter.",
    "servs": [
      ("Ressemelage", "Semelles cuir cousues ou gomme collée, demi-semelles, bouts renforcés. Les chaussures de qualité se ressemellent plusieurs fois."),
      ("Talons et patins", "Talons homme et femme, bonbouts de talons aiguilles, patins antidérapants : faits en 15 minutes."),
      ("Coutures et renforts", "Reprise des coutures, pose de contreforts, élargissement et mise en forme."),
      ("Rénovation du cuir", "Nettoyage, nourrissage, teinture et cirage pour redonner couleur et souplesse."),
      ("Maroquinerie", "Sacs, ceintures, portefeuilles : anses, fermetures éclair, doublures, bords, trous supplémentaires."),
      ("Clés et petits services", "Doubles de clés, lacets, semelles intérieures et embauchoirs."),
    ],
    "steps_h2": "Simple, rapide, et vous savez le prix avant.",
    "steps": [
      ("Vous passez en boutique", "Sans rendez-vous, du mardi au samedi. Ou vous nous écrivez avec une photo."),
      ("Devis immédiat", "On regarde la pièce avec vous et on vous donne le prix et le délai."),
      ("Réparation à l'atelier", "Minute pour les talons et patins, quelques jours pour un ressemelage."),
      ("Vous récupérez vos pièces", "On vous prévient par SMS quand c'est prêt."),
    ],
    "job_labels": ("Travail", "Délai"),
    "jobs": [
      ("Richelieus en cuir · Homme", "Ressemelage cuir cousu et talons neufs", "Ressemelage complet", "6 jours"),
      ("Bottines · Femme", "Demi-semelles gomme et bonbouts", "Réparation", "2 jours"),
      ("Sac cabas en cuir", "Anses remplacées et bords reteintés", "Maroquinerie", "5 jours"),
    ],
    "pledges_h2": "Nos engagements.",
    "pledges": [
      ("Le prix avant la réparation.", "Pas de mauvaise surprise au moment de récupérer vos chaussures."),
      ("Un avis honnête.", "Si une réparation ne vaut pas le coût, on vous le dit."),
      ("Des matériaux de qualité.", "Cuirs et gommes choisis pour durer, pas pour tenir trois mois."),
      ("Un délai tenu.", "La date est notée sur votre ticket, et vous êtes prévenu par SMS."),
    ],
    "reviews": [
      ("« Mes boots préférées ressemelées en cuir, elles ont retrouvé une seconde vie. Délai annoncé respecté. »", "Julien M. · Toulouse · Ressemelage"),
      ("« Talons refaits pendant que je faisais une course à côté. Accueil adorable et bons conseils d'entretien. »", "Camille F. · Toulouse · Talons"),
    ],
    "faq": [
      ("Combien coûte un ressemelage ?", "Le prix dépend du type de chaussure et de la semelle choisie, cuir ou gomme. Passez en boutique ou envoyez-nous une photo : le devis est gratuit et immédiat."),
      ("Faut-il prendre rendez-vous ?", "Non, venez directement en boutique aux heures d'ouverture, du mardi au samedi de 9 h à 19 h."),
      ("Combien de temps pour une réparation ?", "Talons et patins : 15 minutes. Ressemelage : quelques jours à une semaine. Le délai exact est noté sur votre ticket."),
      ("Toutes les chaussures peuvent-elles être ressemelées ?", "Les chaussures cousues ou collées de bonne qualité, oui. Certaines baskets à semelle moulée ne peuvent pas l'être : on vous le dit franchement."),
      ("Réparez-vous les sacs et les ceintures ?", "Oui : anses, fermetures, doublures, bords, trous supplémentaires sur une ceinture."),
      ("Peut-on vous envoyer des chaussures par la poste ?", "Oui. Décrivez-nous la réparation via le formulaire, nous vous envoyons un devis puis les instructions d'envoi."),
    ],
    "quote_h2": "Une réparation à faire ?", "quote_p": "Décrivez-nous vos pièces. On vous rappelle avec un prix indicatif, ou passez directement en boutique.",
    "work_label": "Réparation",
    "works": ["Ressemelage", "Talons", "Patins", "Couture", "Rénovation et teinture", "Maroquinerie", "Autre"],
    "extra": ("item", "Pièce à réparer", "Ex. : bottines en cuir, sac à main", True),
    "details_ph": "Ex. : richelieus en cuir, semelle trouée à l'avant, talons usés",
    "success_end": "vous donner un prix et un délai",
    "nav": ["L'atelier", "Comment ça se passe", "Réparations", "Questions"],
    "shop": True,
  },
  {
    "dir": "macons/01-maconnerie-rocher",
    "photo": ("12276522", "a-man-constructing-a-hallow-blacks-wall-12276522", "Fausto Hernandez"),
    "name": "Maçonnerie Rocher", "tagline": "Maçon · Rennes et Ille-et-Vilaine",
    "schema": "HomeAndConstructionBusiness",
    "city": "Rennes", "cp": "35200", "street": "3 rue du Bas Village",
    "phone": "02 61 91 55 84", "tel": "+33261915584",
    "hours": "Du lundi au vendredi, 7 h 30 à 18 h", "hours_schema": "Mo-Fr 07:30-18:00",
    "zone_short": "Rennes et 40 km autour",
    "zone": ["Rennes", "Cesson-Sévigné", "Saint-Grégoire", "Bruz", "Chantepie", "Pacé", "Betton", "Vern-sur-Seiche", "Chartres-de-Bretagne", "Le Rheu"],
    "top3": "Assurance décennale",
    "title": "Maçon à Rennes · Extension, ouverture de mur, dalle | Maçonnerie Rocher",
    "desc": "Maçon à Rennes et en Ille-et-Vilaine : extension de maison, ouverture de mur porteur, dalles et fondations, murs de clôture, rénovation de façade et de pierre. Visite et devis gratuits.",
    "fonts": ("Oswald", "Oswald:wght@500;600;700", "Source Sans 3", "Source+Sans+3:wght@400;500;600"),
    "pal": dict(paper="#F8F7F5", chalk="#ECEAE6", ink="#26282B", muted="#5E6166", line="#DCD9D3", accent="#E4683F", deep="#B0431F"),
    "layout": "overlay",
    "icon": '<path d="M5 10h22M5 16h22M5 22h22M12 10v6M20 16v6M16 22v4M16 4v6" stroke="currentColor" stroke-width="2.2"/><rect class="blade" x="12" y="16" width="8" height="6"/>',
    "eyebrow": "Maçon · Rennes et Ille-et-Vilaine",
    "h1": ("Agrandir, ouvrir, reconstruire :", "du solide, dans les délais annoncés."),
    "lead": "Extension de maison, ouverture de mur porteur, dalle, fondations, murs de clôture et rénovation de pierre. Une entreprise de maçonnerie qui vous explique chaque étape et tient son planning.",
    "proofs": ["Visite et devis gratuits sous une semaine", "Accompagnement pour le permis ou la déclaration", "Assurance décennale, attestation jointe"],
    "cta": "Demander une visite", "note": "Réponse sous 24 h. Nous indiquons une date de démarrage dès le devis.",
    "badge": ("25 ans", "de maçonnerie<br>autour de Rennes"),
    "alt": "Un maçon monte un mur en parpaings sur un chantier",
    "sit_title": "Quel est votre projet ?",
    "sits": [
      ("Il me faut une pièce de plus", "Extension en parpaing ou en brique, des fondations au hors d'eau.", "Extension de maison"),
      ("Je veux ouvrir la cuisine sur le salon", "Ouverture de mur porteur avec étaiement et poutre dimensionnée.", "Ouverture de mur porteur"),
      ("Je veux une terrasse ou une dalle", "Dalle béton armé pour terrasse, abri, garage ou carport.", "Dalle et fondations"),
      ("Mon muret ou mon mur de clôture est à refaire", "Mur en parpaing enduit, en pierre ou en brique, avec portail.", "Mur de clôture"),
      ("Ma façade est fissurée", "Diagnostic, reprise des fissures, enduit ou ravalement.", "Façade et fissures"),
      ("J'ai une maison en pierre à rénover", "Rejointoiement à la chaux, reprise de linteaux et d'appuis.", "Rénovation de pierre"),
    ],
    "serv_eyebrow": "Nos travaux", "serv_h2": "Le gros œuvre de votre maison, du terrassement au hors d'eau.",
    "servs": [
      ("Extensions", "Agrandissement de plain-pied ou à l'étage : fondations, murs, dalle, raccord à l'existant."),
      ("Ouverture de murs porteurs", "Étaiement, pose d'une poutre dimensionnée par un bureau d'études, reprise propre des tableaux."),
      ("Dalles et fondations", "Semelles, longrines et dalles armées pour maison, garage, abri ou terrasse."),
      ("Murs et clôtures", "Murs de clôture, murets, murs de soutènement, piliers et seuils de portail."),
      ("Façades", "Reprise de fissures, enduits, ravalement, habillage de soubassement."),
      ("Pierre et bâti ancien", "Rejointoiement à la chaux, remplacement de pierres, linteaux et appuis de fenêtre."),
    ],
    "steps_h2": "Un chantier de maçonnerie, étape par étape.",
    "steps": [
      ("Vous nous contactez", "Plans, photos ou simple description : on commence par vous écouter."),
      ("Visite et conseil", "On mesure, on vérifie le sol et la structure, on parle démarches administratives."),
      ("Devis et planning", "Chaque poste chiffré et une date de démarrage annoncée dès le devis."),
      ("Chantier suivi", "Un point avec vous chaque semaine, réception des travaux ensemble."),
    ],
    "job_labels": ("Travaux", "Durée"),
    "jobs": [
      ("Cesson-Sévigné · Maison des années 80", "Extension de 25 m² pour une suite parentale", "Fondations, murs, dalle", "5 semaines"),
      ("Rennes · Maison de ville", "Mur porteur ouvert entre cuisine et séjour", "Étaiement et poutre acier", "4 jours"),
      ("Bruz · Longère", "Façade en pierre rejointoyée à la chaux", "Rejointoiement 60 m²", "2 semaines"),
    ],
    "pledges_h2": "Ce qu'on s'engage à faire.",
    "pledges": [
      ("Un planning tenu.", "Date de démarrage écrite sur le devis, point hebdomadaire pendant le chantier."),
      ("La structure calculée.", "Pour un mur porteur ou une extension, les éléments sont dimensionnés par un bureau d'études."),
      ("Des démarches expliquées.", "Permis ou déclaration préalable : on vous aide à préparer le dossier."),
      ("Des garanties solides.", "Assurance décennale et responsabilité civile, attestations fournies."),
    ],
    "reviews": [
      ("« Extension livrée à la date prévue. Un point chaque semaine, on savait toujours où en était le chantier. »", "Gwenaëlle K. · Cesson-Sévigné · Extension"),
      ("« Mur porteur ouvert en quatre jours, travail propre, poutre posée impeccablement. »", "Yann L. · Rennes · Ouverture de mur"),
    ],
    "faq": [
      ("Combien coûte une extension de maison ?", "Le prix dépend de la surface, des fondations nécessaires, des matériaux et du raccord à l'existant. Après la visite, nous vous remettons un devis détaillé par poste."),
      ("Faut-il un permis de construire pour une extension ?", "Selon la surface créée et les règles de votre commune, il faut une déclaration préalable ou un permis de construire. Nous vérifions avec vous auprès de la mairie."),
      ("Peut-on ouvrir un mur porteur ?", "Oui, avec un étaiement provisoire et une poutre dimensionnée par un bureau d'études. En copropriété, l'accord de l'assemblée générale est nécessaire."),
      ("Combien de temps dure une extension ?", "Pour le gros œuvre d'une extension de 20 à 30 m², comptez généralement quelques semaines. Le planning précis figure sur le devis."),
      ("Les fissures de ma façade sont-elles graves ?", "Les microfissures d'enduit sont souvent superficielles. Une fissure large, traversante ou qui s'agrandit doit être examinée. Nous venons faire le diagnostic."),
      ("Travaillez-vous avec les autres corps de métier ?", "Oui, nous coordonnons au besoin avec le charpentier, le couvreur, le menuisier et le plaquiste pour que l'extension soit livrée complète."),
    ],
    "quote_h2": "Parlez-nous de votre projet.", "quote_p": "Décrivez vos travaux en quelques lignes. On vous rappelle pour fixer une visite, gratuite et sans engagement.",
    "work_label": "Type de travaux",
    "works": ["Extension de maison", "Ouverture de mur porteur", "Dalle et fondations", "Mur de clôture", "Façade et fissures", "Rénovation de pierre", "Autre"],
    "extra": ("surface", "Surface envisagée", "Ex. : 25 m²", True),
    "details_ph": "Ex. : extension de 25 m² côté jardin pour une chambre et une salle d'eau",
    "success_end": "fixer la visite de votre chantier",
    "nav": ["Nos travaux", "Comment ça se passe", "Chantiers", "Questions"],
  },
  {
    "dir": "carrossiers/01-carrosserie-dumas",
    "photo": ("6870314", "person-using-paint-spray-gun-6870314", "Gustavo Fring"),
    "name": "Carrosserie Dumas", "tagline": "Carrossier peintre · Lille",
    "schema": "AutoBodyShop",
    "city": "Lille", "cp": "59000", "street": "112 rue du Faubourg de Roubaix",
    "phone": "03 53 01 64 29", "tel": "+33353016429",
    "hours": "Du lundi au vendredi, 8 h à 18 h 30, samedi 9 h à 12 h", "hours_schema": "Mo-Fr 08:00-18:30",
    "zone_short": "Lille et métropole",
    "zone": ["Lille", "Roubaix", "Tourcoing", "Villeneuve-d'Ascq", "Marcq-en-Barœul", "Lambersart", "La Madeleine", "Mons-en-Barœul", "Hellemmes"],
    "top3": "Toutes assurances acceptées",
    "title": "Carrossier à Lille · Réparation, peinture, sinistre | Carrosserie Dumas",
    "desc": "Carrossier peintre à Lille : réparation après accident, gestion du sinistre avec votre assurance, débosselage sans peinture, rayures, pare-chocs, peinture complète. Véhicule de prêt, devis gratuit.",
    "fonts": ("Saira", "Saira:wght@600;700;800", "Figtree", "Figtree:wght@400;500;600"),
    "pal": dict(paper="#F6F7F9", chalk="#E8EBF0", ink="#15171C", muted="#5A5F69", line="#D8DCE3", accent="#FF5A45", deep="#C4291A"),
    "layout": "split-right",
    "icon": '<path class="blade" d="M4 20l3-7c.5-1.2 1.6-2 3-2h12c1.4 0 2.5.8 3 2l3 7z"/><circle cx="10" cy="22" r="3" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="22" cy="22" r="3" fill="none" stroke="currentColor" stroke-width="2.4"/>',
    "eyebrow": "Carrossier peintre · Lille",
    "h1": ("Un accrochage, une rayure, un sinistre ?", "On s'occupe de tout, assurance comprise."),
    "lead": "Réparation après accident, pare-chocs, rayures, bosses et peinture. Vous êtes libre de choisir votre carrossier : on gère le dossier avec votre assurance et on vous prête un véhicule pendant les travaux.",
    "proofs": ["Devis gratuit en 20 minutes sur place", "Gestion du sinistre avec votre assureur", "Véhicule de prêt pendant la réparation"],
    "cta": "Prendre rendez-vous", "note": "Réponse dans la journée. Venez aussi sans rendez-vous pour une estimation.",
    "badge": ("20 min", "pour estimer<br>votre réparation"),
    "alt": "Un carrossier peint une voiture au pistolet dans une cabine de peinture",
    "sit_title": "Que s'est-il passé ?",
    "sits": [
      ("J'ai eu un accident", "On gère la déclaration avec votre assurance et l'expert, du début à la fin.", "Réparation après sinistre"),
      ("Mon pare-chocs est rayé ou enfoncé", "Réparation ou remplacement, peinture à la teinte exacte.", "Pare-chocs"),
      ("J'ai une bosse sans rayure", "Débosselage sans peinture : plus rapide et moins cher.", "Débosselage sans peinture"),
      ("Ma carrosserie est rayée", "Polissage pour les rayures légères, retouche ou peinture pour les profondes.", "Rayures"),
      ("J'ai reçu de la grêle", "Débosselage des impacts, prise en charge par l'assurance selon votre contrat.", "Grêle"),
      ("Je veux rendre mon véhicule en LOA", "Remise en état avant restitution pour éviter les frais de retour.", "Remise en état avant restitution"),
    ],
    "serv_eyebrow": "Nos services", "serv_h2": "Réparer votre voiture, et vous simplifier la vie pendant ce temps.",
    "servs": [
      ("Réparation après sinistre", "Expertise, réparation, peinture : nous traitons directement avec votre assureur et l'expert."),
      ("Peinture", "Cabine de peinture, teinte contrôlée au spectrophotomètre pour un raccord invisible."),
      ("Débosselage sans peinture", "Pour les bosses et la grêle sans rayure : la peinture d'origine est conservée."),
      ("Rayures et pare-chocs", "Polissage, réparation plastique, remplacement et peinture des pare-chocs."),
      ("Vitrage", "Remplacement de pare-brise et de vitres, réparation d'impacts."),
      ("Véhicule de prêt", "Une voiture vous est prêtée pendant toute la durée des travaux, sur réservation."),
    ],
    "steps_h2": "Votre voiture réparée, sans courir après l'assurance.",
    "steps": [
      ("Vous prenez rendez-vous", "Par téléphone, formulaire ou directement à l'atelier."),
      ("Estimation en 20 minutes", "On regarde les dégâts avec vous et on vous explique les options."),
      ("On gère l'assurance", "Déclaration, expert, accord de prise en charge : on s'en charge."),
      ("Restitution lavée", "Votre voiture vous est rendue réparée, contrôlée et lavée."),
    ],
    "job_labels": ("Réparation", "Immobilisation"),
    "jobs": [
      ("Citadine · Choc arrière", "Pare-chocs et hayon remplacés, prise en charge assurance", "Sinistre", "4 jours"),
      ("Berline · Grêle", "35 impacts débosselés sans peinture", "Débosselage", "2 jours"),
      ("SUV · Portière rayée", "Reprise de la portière et raccord de teinte", "Peinture", "2 jours"),
    ],
    "pledges_h2": "Ce qu'on vous garantit.",
    "pledges": [
      ("Votre libre choix.", "Votre assureur ne peut pas vous imposer un garage : vous pouvez nous confier votre véhicule."),
      ("Un devis compréhensible.", "Pièces, main-d'œuvre et peinture détaillées, et ce que l'assurance prend en charge."),
      ("Une teinte parfaite.", "Couleur mesurée sur votre voiture, pas seulement d'après la référence constructeur."),
      ("Une mobilité assurée.", "Véhicule de prêt sur réservation pendant les travaux."),
    ],
    "reviews": [
      ("« Après mon accrochage, ils ont tout géré avec l'assurance. Voiture de prêt, réparation en quatre jours, rendue lavée. »", "Inès B. · Lille · Sinistre"),
      ("« Débosselage de la grêle sans repeindre, on ne voit plus rien. Très bon accueil et délai tenu. »", "Olivier C. · Villeneuve-d'Ascq · Grêle"),
    ],
    "faq": [
      ("Mon assurance peut-elle m'imposer un garage ?", "Non. Vous êtes libre de choisir votre réparateur, même si votre assureur vous en recommande un. Nous prenons en charge le dossier avec votre assurance et l'expert."),
      ("Combien de temps ma voiture sera-t-elle immobilisée ?", "De quelques heures pour un débosselage à quelques jours pour une réparation après sinistre, selon les pièces à commander. Le délai est annoncé sur le devis."),
      ("Combien coûte la réparation d'un pare-chocs ?", "Cela dépend de la réparation ou du remplacement, de la peinture et du modèle. Nous vous donnons un prix précis après une estimation de 20 minutes à l'atelier."),
      ("Qu'est-ce que le débosselage sans peinture ?", "Une technique qui remet la tôle en forme par l'arrière, sans poncer ni repeindre. Elle convient aux bosses sans rayure, comme la grêle ou les coups de portière."),
      ("Proposez-vous un véhicule de prêt ?", "Oui, sur réservation, pendant toute la durée des travaux. Selon votre contrat, il peut aussi être pris en charge par l'assurance."),
      ("Faut-il un rendez-vous pour une estimation ?", "Non, vous pouvez passer à l'atelier aux heures d'ouverture. Avec un rendez-vous, l'attente est plus courte."),
    ],
    "quote_h2": "Parlez-nous de votre véhicule.", "quote_p": "Décrivez les dégâts en quelques mots. On vous rappelle pour fixer l'estimation et réserver un véhicule de prêt si besoin.",
    "work_label": "Type de réparation",
    "works": ["Réparation après sinistre", "Pare-chocs", "Débosselage sans peinture", "Rayures", "Grêle", "Vitrage", "Remise en état avant restitution", "Autre"],
    "extra": ("car", "Marque et modèle", "Ex. : Peugeot 208, 2021", True),
    "details_ph": "Ex. : choc arrière gauche en stationnement, feu cassé, sinistre déclaré",
    "success_end": "fixer l'estimation de votre véhicule",
    "nav": ["Nos services", "Comment ça se passe", "Réparations", "Questions"],
  },
]

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
.hero h1 { font-size: clamp(2rem, 4vw, 3.1rem); }
.hero.split-left .hero-visual { order: -1; }
.hero.split-left .hero-badge { left: auto; right: -24px; }
.hero.overlay { position: relative; padding: 0; background: var(--ink); color: #fff; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; margin: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-bg::after { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, INKA.95) 0%, INKA.86) 55%, INKA.35) 100%); }
.hero.overlay .hero-grid { position: relative; grid-template-columns: minmax(0, 680px); min-height: min(720px, 88vh); align-content: center; padding: 72px 0; }
.hero.overlay .lead, .hero.overlay .proofs li { color: #fff; }
.hero.overlay .lead { color: ONINK; }
.hero.overlay h1 em { color: var(--ochre); }
.hero.overlay .eyebrow { color: var(--ochre); }
.hero.overlay .btn-ghost { border-color: rgba(255, 255, 255, .7); color: #fff; }
.hero.overlay .btn-ghost:hover { background: #fff; color: var(--ink); }
.hero.overlay .hero-note { color: ONINK2; }
.hero.overlay .hero-badge { position: static; display: inline-flex; margin-top: 28px; background: rgba(255, 255, 255, .08); border: 1px solid rgba(255, 255, 255, .2); box-shadow: none; }
.hero.overlay .hero-badge strong { color: var(--ochre); }
.hero.overlay .hero-badge span { color: ONINK; }
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
    copy = f'''        <div class="hero-copy">
          <p class="eyebrow">{e(s["eyebrow"])}</p>
          <h1>{e(h1a)} <em>{e(h1b)}</em></h1>
          <p class="lead">{e(s["lead"])}</p>
          <ul class="proofs">
{proofs}
          </ul>
          <div class="hero-ctas">
            <a class="btn btn-primary" href="#devis">{e(s["cta"])}</a>
            <a class="btn btn-ghost" href="tel:{s["tel"]}">
              {ICON_PHONE}
              {s["phone"]}
            </a>
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

    biz = {
        "@context": "https://schema.org", "@type": s["schema"], "name": s["name"],
        "description": s["desc"], "telephone": s["tel"],
        "address": {"@type": "PostalAddress", "streetAddress": s["street"], "postalCode": s["cp"], "addressLocality": s["city"], "addressCountry": "FR"},
        "areaServed": s["zone"], "openingHours": s["hours_schema"], "image": "hero.jpg",
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["serv_h2"], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d}} for t, d in s["servs"]]},
    }
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
    ld = lambda o: '  <script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=2) + "\n  </script>"

    zone_label = "Où nous trouver" if shop else "Nous intervenons à"
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
{ld(biz)}
{ld(faqld)}
</head>
<body>

  <a class="skip" href="#devis">Aller au formulaire</a>

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
        <p class="sit-hint">Cliquez sur votre situation : le formulaire se remplit tout seul.</p>
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
          <p class="eyebrow">{nav[2]} récent{"e" if nav[2].endswith("ions") else ""}s</p>
          <h2 id="jobs-title">Quelques exemples de ces derniers mois.</h2>
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
          </ul>
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
          <p class="eyebrow">Devis gratuit</p>
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

        <form class="quote-form" id="quoteForm" novalidate>
          <div class="hp" aria-hidden="true">
            <label for="website">Ne pas remplir</label>
            <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
          </div>

          <div class="field">
            <label for="work">{e(s["work_label"])}</label>
            <select id="work" name="work" required>
              <option value="">Choisissez</option>
{works}
            </select>
            <p class="err" data-for="work">Faites un choix dans la liste.</p>
          </div>

          <div class="row">
            <div class="field">
              <label for="{xid}">{e(xlabel)}{opt}</label>
              <input type="text" id="{xid}" name="{xid}" maxlength="80" placeholder="{e(xph)}">
            </div>
            <div class="field">
              <label for="zip">Code postal</label>
              <input type="text" id="zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" required>
              <p class="err" data-for="zip">5 chiffres, par exemple {s["cp"]}.</p>
            </div>
          </div>

          <div class="field">
            <label for="details">Précisez votre demande <span class="opt">(facultatif)</span></label>
            <textarea id="details" name="details" rows="3" maxlength="800" placeholder="{e(s["details_ph"])}"></textarea>
          </div>

          <div class="row">
            <div class="field">
              <label for="name">Nom</label>
              <input type="text" id="name" name="name" autocomplete="name" maxlength="80" required>
              <p class="err" data-for="name">Indiquez votre nom.</p>
            </div>
            <div class="field">
              <label for="phone">Téléphone</label>
              <input type="tel" id="phone" name="phone" autocomplete="tel" maxlength="20" required>
              <p class="err" data-for="phone">Un numéro à 10 chiffres pour vous rappeler.</p>
            </div>
          </div>

          <div class="field">
            <label for="email">E-mail <span class="opt">(facultatif)</span></label>
            <input type="email" id="email" name="email" autocomplete="email" maxlength="120">
            <p class="err" data-for="email">Cette adresse ne semble pas valide.</p>
          </div>

          <fieldset class="field">
            <legend>Quand vous rappeler ?</legend>
            <div class="chips">
              <label class="chip"><input type="radio" name="when" value="Matin" checked><span>Le matin</span></label>
              <label class="chip"><input type="radio" name="when" value="Midi"><span>Entre 12 h et 14 h</span></label>
              <label class="chip"><input type="radio" name="when" value="Après-midi"><span>L'après-midi</span></label>
            </div>
          </fieldset>

          <button class="btn btn-primary btn-block" type="submit">Envoyer ma demande</button>
          <p class="form-legal">Vos coordonnées servent uniquement à vous recontacter pour cette demande.</p>

          <div class="success" id="success" role="status" aria-live="polite" hidden>
            <svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22"/><path d="m14 24 7 7 13-14"/></svg>
            <h3>Demande bien reçue</h3>
            <p id="successMsg"></p>
          </div>
        </form>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap footer-inner">
      <p><strong>{e(s["name"])}</strong> · {e(s["tagline"])} · {e(s["street"])}, {s["cp"]} {e(s["city"])}</p>
      <p>SIRET 000 000 000 00000 · Assurance n° à préciser · <a href="#top">Retour en haut</a></p>
    </div>
  </footer>

  <!-- Barre d'action mobile -->
  <div class="mobile-bar">
    <a href="tel:{s["tel"]}" class="mb-call">
      {ICON_PHONE}
      Appeler
    </a>
    <a href="#devis" class="mb-quote">Devis gratuit</a>
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
    base = (BASE / "styles.css").read_text()
    for k, v in sorted(palette(s["pal"]).items(), key=lambda kv: -len(kv[0])):
        base = base.replace(k, v)
    head_font, _, body_font, _ = s["fonts"]
    base = base.replace('"Archivo"', f'"{head_font}"').replace('"Public Sans"', f'"{body_font}"')
    base = base.replace("/* Morel Plâtrerie · plâtre, ardoise et ocre */", f"/* {s['name']} */")
    ink = s["pal"]["ink"]
    v = (VARIANT_CSS.replace("INKA", rgba_prefix(ink) + " ")
         .replace("ONINK2", mix(ink, "#FFFFFF", .62)).replace("ONINK", mix(ink, "#FFFFFF", .8)))
    return base + v


def js(s):
    src = (BASE / "script.js").read_text()
    src = src.replace("/* Morel Plâtrerie · navigation", f"/* {s['name']} · navigation")
    src = src.replace("pour fixer la visite de votre chantier.", "pour " + s["success_end"] + ".")
    return src


def llms(s):
    lines = [f"# {s['name']}", "", f"> {s['desc']}", "",
             f"- Téléphone : {s['phone']} ({s['hours']})",
             f"- Adresse : {s['street']}, {s['cp']} {s['city']}",
             f"- Zone : {', '.join(s['zone'])}",
             "- Services : " + ", ".join(t for t, _ in s["servs"]),
             "- Devis : formulaire sur la page d'accueil, section « Devis gratuit »", ""]
    return "\n".join(lines)


def main():
    for s in SITES:
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
