#!/bin/zsh
# Usage : export-astro.sh <dossier source> <chemin de montage, ex. artisanat/04-bleu-confiance>
set -e
src=$1; mount=$2
dest=${0:A:h:h}/$mount
cd $src
rm -rf dist
npx astro build --base /$mount > /tmp/build-$(basename $src).log 2>&1 || { tail -30 /tmp/build-$(basename $src).log; exit 1; }
out=dist/client; [ -d $out ] || out=dist
rm -rf $dest && mkdir -p $dest && cp -R $out/. $dest/
rm -rf dist
# Liens bruts "/..." des pages vers le chemin de montage
find $dest -name "*.html" -print0 | xargs -0 perl -pi -e "s#(href|src)=\"/(?!/|$mount)#\\1=\"/$mount/#g"
echo "exporté -> $mount"
