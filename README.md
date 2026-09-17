# Collection de sites vitrines haut de gamme

Une vitrine de design : **des sites web complètement distincts, complets et haut de gamme** pour des commerces de services de proximité premium. Chaque site est une marque autonome avec sa propre palette, typographie, voix, animations et tunnels de conversion — développé **sans aucune dépendance** (HTML/CSS/JS purs, Google Fonts uniquement), prêt pour GitHub Pages. Tous les textes sont en français.

## 📁 Structure

```
luxury-service-websites/
├── plomberie/              ← ✅ Série 1 — Plomberie (5 sites + hub)
├── serrurerie/            ← ✅ Série 2 — Serrurerie (5 sites + hub)
├── taxis/                 ← ✅ Série 3 — Taxis (5 sites + hub)
├── dentistes/              ← ✅ Série 4 — Dentistes (5 sites + hub)
└── ophtalmologie/      ← ✅ Série 5 — Ophtalmologie (5 sites + hub)
```

Chaque dossier de catégorie contient `index.html` (page vitrine liant les cinq marques) et cinq dossiers de marques, chacun un site autonome : `index.html` + `styles.css` + `script.js`.

## 🚿 Plomberie — les cinq marques

| # | Site | Concept | Signature |
|---|------|---------|-----------|
| 01 | **Aqua Lumière** | Atelier plomberie privé, Art déco | Dégradés or chatoyants, éventails déco, voix conciergerie |
| 02 | **Meridian Plumbing Co.** | Discipline d'ingénieur suisse | Schéma de tuyauterie animé, fiche chantier en direct, ton fiche technique |
| 03 | **Copperline & Sons** | Héritage familial depuis 1962 | Typographie cuivre, chronologie générationnelle, « Garantie sans blague » |
| 04 | **Stillwater** | Bien-être / état d'esprit spa | Héros à ondulations respirantes, services-rituels, abonnements |
| 05 | **NEXA** | Systèmes d'eau connectés IoT | Dashboard de capteurs en direct, glassmorphism, récit IA |

## 🔐 Serrurerie — les cinq marques

| # | Site | Concept | Signature |
|---|------|---------|-----------|
| 01 | **Bastion & Clef** | Atelier onyx & laiton | Clef squelette en filigrane, panneau « Mécanisme № 7 » |
| 02 | **Keystone Lock Co.** | Fiche technique de précision, orange signal | Coupe de cylindre à goupilles animée, planning de contrôle qualité |
| 03 | **Ironhaven & Sons** | Héritage de forge depuis 1954 | Particules de braise, plaque du fondateur, chronologie qui se dessine |
| 04 | **Haven & Hour** | Réassurance calme, 3 h du matin | Lanterne et étoiles, horloge « quelqu'un est éveillé » en direct |
| 05 | **Aperio Systems** | Plateforme d'accès connecté | Journal d'accès en direct, hiérarchie des clés |

## 🚕 Taxis — les cinq marques

| # | Site | Concept | Signature |
|---|------|---------|-----------|
| 01 | **ONYX Chauffeurs** | Voiture de course noire de luxe | Bokeh & ligne d'horizon, sédan au trait qui se dessine |
| 02 | **Vector Taxi Co.** | Précision sans compteur | Tableau de tarifs forfaitaires en direct, horloge de dispatch |
| 03 | **Checker & Sons** | Héritage damier depuis 1947 | Badge « DEPUIS 1947 » rotatif, bandes damier animées |
| 04 | **Lumen Rides** | Le trajet calme | Héros crépusculaire respirant, carte « toujours à bord » |
| 05 | **PULSE** | Dispatch temps réel | Point de course animé sur grille urbaine, terminal auto-scripteur |

## 🦷 Dentistes — les cinq marques

| # | Site | Concept | Signature |
|---|------|---------|-----------|
| 01 | **Éclat Dental** | Studio cosmétique couture | Héros médaillon enso, dorure rose, porcelaine |
| 02 | **Arcline Dental Studio** | Clinique data-first | Schéma de scan intra-oral, ticker de spécifications |
| 03 | **Hollyfield Family Dental** | Cabinet familial depuis 1961 | Blason laiton, chronologie sur trois générations |
| 04 | **Still Point Dental** | Sans anxiété, bien-être | Anneaux respirants, Menu Confort, UI en pilules |
| 05 | **NOVA Smile Lab** | Smile design numérique, dark tech | Aperçu 3D filaire de dent, pastilles de teinte |

## 👁 Ophtalmologie — les cinq marques

| # | Site | Concept | Signature |
|---|------|---------|-----------|
| 01 | **Iris Privé** | Atelier de vision couture | Rotor d'iris rotatif avec parallaxe au curseur |
| 02 | **Meridian Eye Institute** | Chirurgical, piloté par les données | Échelle de Snellen en direct, grille blueprint |
| 03 | **Hawthorne Eye Care** | Cabinet familial depuis 1968 | Sceau fondateur à texte circulaire, registre des générations |
| 04 | **Serene Vision** | Spa œil sec & douceur pédiatrique | Ondulations respirantes, dégradés organiques |
| 05 | **VIZN Lab** | Imagerie rétinienne par IA | Dashboard OCT avec scanline et télémétrie des couches |

### Chaque site (les 25) comprend

- **Page d'accueil** avec un héros animé spectaculaire
- **Textes promotionnels premium** adaptés à la voix de chaque marque (en français)
- **Formulaire de contact** avec labels flottants + validation + état de succès animé
- **Formulaire de réservation** : assistant en 3 étapes (service → créneau horaire → coordonnées) avec confirmation animée
- Animations au défilement, compteurs animés, nav verre dépoli, menu mobile — le tout respectant `prefers-reduced-motion`

## 🔒 Sécurité

Sites 100 % statiques : aucune base de données, aucun envoi de données, donc **aucune surface d'attaque côté serveur**. Mesures en place :

- **Content-Security-Policy** stricte sur chaque page (balise `meta`) : scripts limités au domaine propre, `object-src 'none'`, `frame-src 'none'`, HTTPS forcé — bloque l'exécution de scripts tiers et le chargement de code distant
- **Anti-spam des formulaires** : champ *honeypot* invisible (rempli = robot → soumission ignorée silencieusement), piège temporel (soumission < 3 s après chargement = robot), limite de longueur sur chaque champ, protection anti double-soumission
- **Pas d'injection DOM** : toute saisie utilisateur est insérée via `textContent` (jamais `innerHTML`) — les récapitulatifs ne peuvent pas exécuter de code injecté
- **Zéro dépendance** : pas de jQuery ni de plugin tiers, donc pas de chaîne d'approvisionnement à attaquer ; HTTPS automatique + HSTS sur `*.github.io`

**Limites honnêtes** : GitHub Pages ne permet pas de définir des en-têtes HTTP personnalisés (`X-Frame-Options`, CSP en en-tête réel, `nosniff`) — pour des en-têtes complets, déployez sur Netlify ou Cloudflare Pages (simple fichier `_headers`). La limitation de débit sérieuse (anti-flood) et la validation finale exigent un backend : quand vous connecterez les formulaires à un service (Formspree, Netlify Forms, votre API), ajoutez-y validation serveur, vérification du honeypot côté serveur et rate-limiting.

## ▶ Lancer localement

Aucune étape de build :

```bash
open luxury-service-websites/plomberie/index.html        # macOS — n'importe quel hub
# ou servir :
cd luxury-service-websites/taxis && python3 -m http.server 8080
```

## 🐙 Publier sur GitHub Pages

1. Créez un dépôt, p. ex. `luxury-service-websites`, et poussez ce dossier.
2. **Dépôt → Settings → Pages → Source : Deploy from a branch → `main` / (root) → Save.**
3. Les sites sont en ligne sur `https://<user>.github.io/luxury-service-websites/<categorie>/` et chaque sous-dossier de marque — chemins relatifs, zéro configuration.

> Les formulaires sont des démonstrations front-end (état + validation + UI de confirmation). Reliez les handlers d'envoi à votre backend, Formspree, Netlify Forms ou similaire pour la mise en production.
