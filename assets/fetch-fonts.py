#!/usr/bin/env python3
"""Télécharge les polices Google de chaque site (sous-ensemble latin, woff2) pour les héberger.

Lit l'URL Google Fonts du <head> actuel de chaque site, récupère le CSS, garde les blocs
`latin`, télécharge les .woff2 dans <site>/fonts/ et écrit <site>/fonts.css (inliné par
build-metiers.py). Polices libres (licence OFL). Usage : python3 assets/fetch-fonts.py [filtre]
"""
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read()


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ""
    for page in sorted(ROOT.glob("*/*/index.html")):
        d = page.parent
        if flt not in str(d.relative_to(ROOT)) or d.parts[-2] in ("medecins", "sante", "artisanat"):
            continue
        spec = d / "fonts.spec"
        m = re.search(r'href="(https://fonts\.googleapis\.com/css2\?[^"]+)"', page.read_text(encoding="utf-8"))
        if m:
            spec.write_text(unescape(m.group(1)) + "\n", encoding="utf-8")
        if not spec.exists():
            print("pas de police Google :", d.name)
            continue
        url = spec.read_text(encoding="utf-8").strip()
        css = get(url).decode("utf-8")
        (d / "fonts").mkdir(exist_ok=True)
        blocks = re.findall(r"/\* (\S+) \*/\s*(@font-face \{.*?\})", css, re.S)
        # Google sert un même fichier (police variable) pour plusieurs graisses : un seul @font-face
        # par fichier, avec la plage de graisses couverte.
        files = {}
        for subset, block in blocks:
            if subset != "latin":
                continue
            u = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
            fam = re.search(r"font-family: '([^']+)'", block).group(1)
            style = re.search(r"font-style: (\w+)", block).group(1)
            wt = int(re.search(r"font-weight: (\d+)", block).group(1))
            files.setdefault(u, dict(fam=fam, style=style, weights=[], block=block))["weights"].append(wt)
        for old in (d / "fonts").glob("*.woff2"):
            old.unlink()
        out = []
        for u, f in files.items():
            name = f"{f['fam'].replace(' ', '')}-{f['style']}.woff2"
            n = 2
            while name in [o[1] for o in out]:
                name = f"{f['fam'].replace(' ', '')}-{f['style']}-{n}.woff2"
                n += 1
            (d / "fonts" / name).write_bytes(get(u))
            lo, hi = min(f["weights"]), max(f["weights"])
            block = f["block"].replace(u, f"fonts/{name}")
            block = re.sub(r"font-weight: \d+;", f"font-weight: {lo} {hi};" if lo != hi else f"font-weight: {lo};", block)
            block = re.sub(r"\s*font-display: \w+;", "", block).replace("}", "  font-display: swap;\n}")
            out.append((block, name, f["style"]))
        (d / "fonts.css").write_text("\n".join(b for b, _, _ in out) + "\n", encoding="utf-8")
        print(d.relative_to(ROOT), len(out), "polices")


if __name__ == "__main__":
    main()
