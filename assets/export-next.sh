#!/bin/zsh
# Usage : export-next.sh <dossier source> <chemin de montage, ex. artisanat/01-braise>
set -e
src=$1; mount=$2
dest=${0:A:h:h}/$mount
cd $src
rm -rf out .next
STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/$mount npx next build > /tmp/build-$(basename $src).log 2>&1 || { tail -30 /tmp/build-$(basename $src).log; exit 1; }
rm -rf $dest && mkdir -p $dest && cp -R out/. $dest/
rm -rf out
echo "exporté -> $mount"
