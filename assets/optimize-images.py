#!/usr/bin/env python3
"""Génère les versions WebP responsives des photos des sites métiers.

Pour chaque site : hero-640/1024/1440.webp et job-N-480/800.webp (jamais plus larges que
l'original). Les JPEG d'origine restent en place (Open Graph, structured data).
Usage : python3 assets/optimize-images.py [filtre de chemin]
"""
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
HERO_W = (640, 1024, 1440)
JOB_W = (480, 800)


def convert(src, stem, widths):
    im = Image.open(src).convert("RGB")
    out = []
    for w in widths:
        last = w >= im.width
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        dst = src.parent / f"{stem}-{w}.webp"
        im.resize((w, h), Image.LANCZOS).save(dst, "WEBP", quality=72, method=6)
        out.append((dst.name, dst.stat().st_size))
        if last:
            break
    return out


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ""
    n = 0
    for hero in sorted(ROOT.glob("*/*/hero.jpg")):
        if flt not in str(hero.relative_to(ROOT)) or hero.parts[-3] in ("medecins", "sante", "artisanat"):
            continue
        convert(hero, "hero", HERO_W)
        for i in (1, 2, 3):
            j = hero.parent / f"job-{i}.jpg"
            if j.exists():
                convert(j, f"job-{i}", JOB_W)
        n += 1
    print(n, "sites traités")


if __name__ == "__main__":
    main()
