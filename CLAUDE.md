# Portfolio ZYAGENCY — contexte du projet

Vitrine commerciale de **ZYAGENCY** (agence web) : 55 sites vitrines de démonstration,
présentés sur une landing page et destinés à être **vendus** à de futurs clients.
Tous les textes sont en français.

## État actuel

- **55 sites consultables**, tous en pages HTML lisibles directement par le navigateur.
- Branche de travail : `claude/recap-sites-produits-c5abux`.
- PR ouverte vers `main` : ZIAgency/luxury-service-websites#1, **à fusionner**.
- Déployé sur Vercel (portfolio non indexé) : https://luxury-service-websites.vercel.app/

## Arborescence

| Dossier | Contenu | Origine |
|---|---|---|
| `medecins/01..06` | 6 cabinets de médecine générale | **Générés** depuis le dépôt `ZIAgency/medecins-generalistes` |
| `sante/01..03` | Vision Étoile, Verveine, Les Petits Pas | **Générés** depuis `opt-premium-one`, `verveine`, `les-petits-pas` |
| `artisanat/01..05` | Braise, Boréal, Auprès, Bleu Confiance, Acier & Laiton | **Générés** depuis les dépôts `Site-*` |
| `plomberie/`, `serrurerie/`, `taxis/`, `dentistes/`, `ophtalmologie/` (5 chacun), `paysagistes/`, `avocats/`, `platriers/`, `isolation/`, `terrassiers/`, `tapissiers/`, `cuisinistes/`, `cordonniers/`, `macons/`, `carrossiers/` | 41 sites orientés client | **Générés** par `assets/build-metiers.py` à partir de `assets/sites/*.py` (une liste `SITES` par famille) et de `assets/metiers-base.css`. Ne jamais éditer leurs `index.html`, `styles.css`, `script.js`, `llms.txt` à la main. |
| `assets/previews/` | Une capture d'écran par site (1440×960, JPEG) | Capturées au navigateur |
| `assets/fonts/`, `assets/zy-logo.svg` | Police Sentient et logo ZY de l'agence | Dépôt `ZIAgency/zyagency` |

**Ne pas modifier à la main** `medecins/`, `sante/` et `artisanat/` : ce sont des exports.
Pour changer un de ces sites, modifier son dépôt source puis régénérer l'export.

Sources de `artisanat/` (clonées dans `~/Claude`) et commande d'export :

| Export | Dépôt source | Commande |
|---|---|---|
| `artisanat/01-braise` | `pros/braise-chauffage` (ZIAgency/Site-braise-chauffage) | `assets/export-next.sh ~/Claude/pros/braise-chauffage artisanat/01-braise` |
| `artisanat/02-boreal` | `pros/boreal-climatisation` | `assets/export-next.sh ~/Claude/pros/boreal-climatisation artisanat/02-boreal` |
| `artisanat/03-aupres` | `pros/aupres-domicile` | `assets/export-next.sh ~/Claude/pros/aupres-domicile artisanat/03-aupres` |
| `artisanat/04-bleu-confiance` | `client-plombier` (ZIAgency/Site-plombier-1, Astro) | `assets/export-astro.sh ~/Claude/client-plombier artisanat/04-bleu-confiance` |
| `artisanat/05-acier-laiton` | `client-serrurier` (ZIAgency/Site-serrurier-1, Astro) | `assets/export-astro.sh ~/Claude/client-serrurier artisanat/05-acier-laiton` |

Les projets Next lisent `STATIC_EXPORT` et `NEXT_PUBLIC_BASE_PATH` (helper `asset()` pour
les images de `/public`) ; les projets Astro utilisent `--base` et `withBase()`.
Depuis le 30/09/2026, ces 5 sites ont des photos du métier dans leurs sections
(étalonnées selon leur identité), les heros sont inchangés.

## La landing page

- `index.html` est **généré** par `assets/build-landing.py`. Ne pas éditer `index.html`
  directement : modifier le script, puis lancer `python3 assets/build-landing.py`.
- Une ligne par site dans `SECTIONS` : slug, nom, étiquette, description, 3 couleurs,
  lien, état.
- Chaque carte a un visuel, un lien « Voir le site » et un bouton **« Acheter ce site »**.

## Sites orientés client (depuis septembre 2026)

Direction voulue par Yacine, à appliquer à tout nouveau site métier : partir de la
question du client. Hero avec **une vraie photo du métier** (jamais un aplat avec une
phrase creuse), titre qui dit ce que le client obtient, téléphone et devis visibles
tout de suite, situations concrètes qui préremplissent le formulaire, FAQ des vraies
questions, barre mobile « Appeler / Devis ». Données structurées (entreprise, services,
FAQ) et `llms.txt` pour être lisible par les IA.

Photos : Pexels (licence libre, usage commercial), `hero.jpg` dans le dossier du site
(max ~300 Ko), téléchargées avec l'accord de Yacine. Crédits : clé `photo` de chaque site.

Générer : `python3 assets/build-metiers.py` (tout) ou `python3 assets/build-metiers.py taxis/`
(filtre sur le chemin). Formulaires : `form` = `devis` (défaut), `rdv` (santé, droit) ou
`taxi`. `urgent: True` met l'appel en bouton principal. Heros alternés : `layout` =
`overlay` (photo plein écran, texte par-dessus), `split-right` ou `split-left`.

Parallax : les heros `overlay` et la photo des heros `split` ont un parallax en CSS pur (`animation-timeline: scroll(root)`, dans `build-metiers.py`), sans bibliothèque ni code copié ; désactivé par `prefers-reduced-motion`. Inspiré de 21st.dev (Parallax Scrolling, licence inconnue : idée réécrite, pas copiée). Layout `expand` (photo qui s'agrandit au scroll, bureau uniquement, hero collant) : validé sur paysagistes/01-seve-pierre, aussi sur 03-cime-racine et taxis/01-onyx-chauffeur, à étendre au cas par cas. Autre piste : éventail de réalisations.

Éventail de réalisations : si un site définit `job_photos` (3 descriptions) et `job-1..3.jpg` dans son dossier, la section « réalisations » devient un éventail de cartes photo qui s'ouvre au scroll (CSS pur, bureau). Validé sur cuisinistes/01-ferrer-cuisines-stores ; crédits dans `job_photos_credit`.

SEO/GEO (appliqué via les fiches `~/.claude/skills/ai-seo.md` et `schema.md`) : H1 = métier + ville
(`seo_h1`), accroche en `p.headline`, JSON-LD `@graph` (entreprise + WebPage daté + FAQPage,
services, `knowsAbout`, fondateur), Open Graph, canonical sur `BASE_URL`, date « Page mise à
jour » en pied de page, `llms.txt` complet (services, engagements, FAQ). Pas d'avis en données
structurées (Google sanctionne les avis auto-déclarés). À la livraison d'un site : remplacer
`BASE_URL` par le domaine du client, retirer le `noindex`, créer la fiche Google Business Profile.

## Règles à respecter

1. **Direction artistique ZYAGENCY** : fond noir `#000`, accent jaune `#FFC700`,
   bordures `#424242`, titres en *Sentient* avec un mot en italique jaune,
   labels en monospace, boutons arrondis blanc et jaune.
2. **Ton de l'agence** : bénéfice client d'abord (« Votre partenaire digital »,
   « Parlons de vos objectifs »). Chaque carte dit à qui le site s'adresse et ce
   qu'il fait gagner.
3. **L'argumentaire GEO passe en premier** : les clients demandent désormais à une IA
   qui appeler ; les IA ne citent que ce qu'elles ont lu ; sans site, on est absent
   de la réponse. Triptyque SEO + SEA + GEO = des demandes entrantes, donc du chiffre
   d'affaires.
4. **Aucune mention de technologie** sur la landing (ni framework, ni outil de
   fabrication). Vérifier après chaque génération :
   `grep -icE 'next\.?js|astro|tailwind|framer' index.html` doit renvoyer 0.
5. **Pas de statistiques de marché inventées.** Un chiffre sourcé ou rien.
6. **Pas de thèmes Shopify dans la vitrine** (`ZIAgency/aurum-theme` est un thème
   Shopify : il reste hors de la landing pour l'instant).
7. Formulaires des sites : **démonstration uniquement**. Ils valident la saisie et
   affichent une confirmation, sans rien envoyer. Protections en place : honeypot,
   piège temporel (< 3 s = robot), limites de saisie, insertion par `textContent`.

## À faire

- [ ] Fusionner la PR #1, puis déployer sur Vercel.
- [ ] **Brancher les liens Shopify** : chaque bouton « Acheter ce site » a
      `data-site="<slug>"` et un `href="#contact"` provisoire. Le faire dans
      `assets/build-landing.py`, pas dans `index.html`.
- [ ] Optionnel : décliner d'autres marques pour les paysagistes et les avocats
      (les autres métiers en ont 5 chacun).

## Vérifier un changement

```bash
python3 -m http.server 8099     # puis ouvrir http://127.0.0.1:8099/
python3 assets/build-landing.py # régénère la landing
```

Pour les captures, Chromium doit accepter le certificat du proxy
(`ignoreHTTPSErrors: true`), sinon les polices Google ne se chargent pas et les
aperçus sortent avec des polices de repli.
