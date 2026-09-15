#!/usr/bin/env python3
"""Create a source-only Overleaf ZIP without archived documents or build files."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'dist' / 'replication-erasure-coding-overleaf.zip'
files = [ROOT / name for name in (
    'replication-erasure-coding.tex', 'preamble.tex', 'macros.tex', 'metadata.tex', 'OVERLEAF.md', 'sample_code.py', 'calc.py')]
files += sorted((ROOT / 'sections').glob('*.tex'))
files += sorted((ROOT / 'fig').glob('*.tex'))
DEST.parent.mkdir(exist_ok=True)
with ZipFile(DEST, 'w', ZIP_DEFLATED) as archive:
    for path in files:
        archive.write(path, path.relative_to(ROOT))
    # Overleaf manages its own output directory. Do not copy the local .latexmkrc.
    archive.writestr('latexmkrc', "$pdf_mode = 1;\n")
print(DEST)
