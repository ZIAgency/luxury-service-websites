# Portfolio ZYAGENCY — contexte du projet

Vitrine commerciale de **ZYAGENCY** (agence web) : 41 sites vitrines de démonstration,
présentés sur une landing page et destinés à être **vendus** à de futurs clients.
Tous les textes sont en français.

## État actuel

- **41 sites consultables**, tous en pages HTML lisibles directement par le navigateur.
- Branche de travail : `claude/recap-sites-produits-c5abux`.
- PR ouverte vers `main` : ZIAgency/luxury-service-websites#1, **à fusionner**.
- Prochaine étape : déployer sur **Vercel** (Add New Project → Framework « Other » → Deploy).
  `vercel.json` gère déjà les URLs propres et les en-têtes de sécurité.

## Arborescence

| Dossier | Contenu | Origine |
|---|---|---|
| `plomberie/`, `serrurerie/`, `taxis/`, `dentistes/`, `ophtalmologie/` | 5 marques chacun + un `index.html` de série | Écrits à la main (`index.html` + `styles.css` + `script.js`) |
| `paysagistes/01-seve-pierre/` | Sève & Pierre, paysagiste concepteur | Écrit à la main |
| `avocats/01-roussel-associes/` | Roussel & Associés, cabinet d'avocats | Écrit à la main |
| `medecins/01..06` | 6 cabinets de médecine générale | **Générés** depuis le dépôt `ZIAgency/medecins-generalistes` |
| `sante/01..03` | Vision Étoile, Verveine, Les Petits Pas | **Générés** depuis `opt-premium-one`, `verveine`, `les-petits-pas` |
| `artisanat/01..05` | Braise, Boréal, Auprès, Bleu Confiance, Acier & Laiton | **Générés** depuis les dépôts `Site-*` |
| `assets/previews/` | Une capture d'écran par site (1440×960, JPEG) | Capturées au navigateur |
| `assets/fonts/`, `assets/zy-logo.svg` | Police Sentient et logo ZY de l'agence | Dépôt `ZIAgency/zyagency` |

**Ne pas modifier à la main** `medecins/`, `sante/` et `artisanat/` : ce sont des exports.
Pour changer un de ces sites, modifier son dépôt source puis régénérer l'export
(`output: "export"`, `trailingSlash: true`, `basePath` = chemin de montage, puis
préfixer les liens `href="/..."` bruts par ce chemin).

## La landing page

- `index.html` est **généré** par `assets/build-landing.py`. Ne pas éditer `index.html`
  directement : modifier le script, puis lancer `python3 assets/build-landing.py`.
- Une ligne par site dans `SECTIONS` : slug, nom, étiquette, description, 3 couleurs,
  lien, état.
- Chaque carte a un visuel, un lien « Voir le site » et un bouton **« Acheter ce site »**.

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
