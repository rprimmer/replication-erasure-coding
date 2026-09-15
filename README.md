# Comparing cost and performance of replication and erasure coding

**John D. Cook, Robert Primmer, and Ab de Kwant · July 19, 2013**

A historical paper comparing replication and erasure coding for storage efficiency, data availability, data protection, latency, and reconstruction costs. It discusses placement across data centers, local reconstruction codes, and trade-offs for hot and cold data.

[Read the paper](replication-erasure-coding.pdf) · [Overleaf instructions](OVERLEAF.md)

## Source organization

```text
replication-erasure-coding.tex  Main document and reading order
metadata.tex                   Title, authors, affiliations, and date
preamble.tex                   Original packages and page geometry
macros.tex                     Reserved for macros (none in the original)
sections/
  00-abstract.tex
  01-introduction.tex
  02-data-availability.tex
  03-data-protection.tex
  04-efficiency-considerations.tex
  05-costs-of-disk-failures.tex
  06-trade-offs.tex
  07-recommendations.tex
  08-appendix-a-software.tex
  09-appendix-b-reliability.tex
  10-references.tex
fig/                           Reserved for figures; this manuscript has none
sample_code.py                 Runnable code included directly in Appendix A
calc.py                        Python 3 calculator and approximation comparison
tests/test_calc.py             Numerical regression tests
scripts/package-overleaf.py    Source-only ZIP packager
```

## Build

Install a TeX distribution containing pdfLaTeX, latexmk, and the geometry package, such as [MacTeX](https://tug.org/mactex/) or [TeX Live](https://tug.org/texlive/). Packaging and the calculator require Python 3.8 or newer.

```sh
make
make overleaf
```

| Command | Result |
| --- | --- |
| `make` | Build in `build/` and refresh the tracked root PDF |
| `make clean` | Remove build intermediates; retain PDFs |
| `make distclean` | Remove build outputs; retain the tracked root PDF |
| `make overleaf` | Create `dist/replication-erasure-coding-overleaf.zip` |

Upload the ZIP as a new [Overleaf](https://www.overleaf.com/) project. Select `replication-erasure-coding.tex` as the main document and pdfLaTeX as compiler. The ZIP includes editable sources and an Overleaf-specific `latexmkrc`. No shell escape is required.

## Preservation and provenance

This project reorganizes `report6.tex`, dated July 19, 2013 within the manuscript. Its prose, equations, table, author affiliations, section numbering, and four bibliography entries are preserved except for the sample-code corrections and their directly affected numerical example described below. Bibliographic entries remain in their original order in an editable `thebibliography` environment.

All 17 original files are preserved byte for byte in the local `Attic/`, verified by a SHA-256 manifest. Existing files within `Attic/` retain their paths; former root files and the `auto/` directory were moved into it. The archive includes two PDFs, older LaTeX drafts, editor files, `calc.py`, the workbook, author photos, and `r2014_july.rtf`. That later formatted RTF version has editorial differences and is not the source of this refactoring. Author photos are not used by the LaTeX manuscript.

The local archive, validation records, build intermediates, and distribution ZIP are excluded from Git. The final root PDF is tracked.

## Sample-code corrections

Appendix A now includes [sample_code.py](sample_code.py) directly with LaTeX's `verbatiminput`, so the printed and executable versions share one source. The corrected implementation uses `math.comb` for the binomial coefficient and sums every term in the failure tail with `math.fsum`. The parity search considers zero disks and enforces the strict probability threshold. Input validation rejects invalid probabilities, counts, and unattainable targets such as a per-disk failure probability of one.

[calc.py](calc.py) is a runnable Python 3 replacement for the archived calculator. It uses `statistics.NormalDist` instead of the invalid `math.norm` import, shares the corrected probability functions, and keeps example output behind a main guard. The Rodrigues-Liskov approximation remains available for comparison, with the paper's original caveats.

```sh
python3 calc.py
python3 -m unittest discover -s tests -v
```

For `p=0.005`, `m=8`, and a target below `1e-6`, the minimum parity count remains **3**, giving redundancy **1.375**. The corrected full-tail probability is **2.0054667412485275e-7**. The manuscript's directly affected value changes from `1.99e-7` to `2.01e-7` (three significant figures).

These floating-point calculations are intended for small erasure-code groups, as in the paper. They are not a general-purpose numerical library for very large groups or extreme probability tails.

## Validation

- Five tests cover exhaustive enumeration of small systems, the paper's example and minimum parity count, endpoint probabilities, zero parity, strict threshold equality, invalid inputs, and normal-approximation identities.
- The corrected PDF and extracted Overleaf package compile locally. The package includes both Python source files; Appendix A is typeset from the runnable source.
- The original Appendix A overfull-box warning is eliminated. Three original bibliography underfull-box warnings remain, with no unresolved references.
- The initial structural refactoring matched a fresh original-source build page for page in extracted text and rendered pixels. The current revision intentionally changes the sample code and its directly affected numerical example.
- Original files remain unchanged in the local archive. The Overleaf service itself was not tested.

## Historical limitations

Original claims, URLs, spelling, and mathematical derivations otherwise remain as written. The archived `calc.py` and original Appendix A preserve the historical errors for provenance. This correction is not a comprehensive technical review of the manuscript.
