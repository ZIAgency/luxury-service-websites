#!/bin/zsh
# Export statique de démonstration de Vision Étoile (source : ~/Claude/vision-etoile-paris).
# La source garde son vrai formulaire (API Resend) ; l'export se fait depuis une copie sans route API,
# avec NEXT_PUBLIC_STATIC_DEMO=1 (le formulaire valide et confirme sans rien envoyer).
# Usage : export-vision-etoile.sh   (monte dans sante/01-vision-etoile)
set -e
mount=sante/01-vision-etoile
dest=${0:A:h:h}/$mount
src=~/Claude/vision-etoile-paris
W=$(mktemp -d)
rsync -a --exclude .next --exclude .git --exclude out $src/ $W/
cd $W
rm -rf src/app/api
cat > next.config.ts <<'C'
import type { NextConfig } from "next";
const nextConfig: NextConfig = { output: "export", trailingSlash: true, basePath: process.env.NEXT_PUBLIC_BASE_PATH, images: { unoptimized: true } };
export default nextConfig;
C
NEXT_PUBLIC_STATIC_DEMO=1 NEXT_PUBLIC_BASE_PATH=/$mount npx next build > /tmp/build-vision-etoile.log 2>&1 || { tail -30 /tmp/build-vision-etoile.log; exit 1; }
[ -d out ] || { echo "ERREUR : pas de dossier out/"; exit 1; }
rm -rf $dest && mkdir -p $dest && cp -R out/. $dest/
rm -rf $W
echo "exporté -> $mount"
