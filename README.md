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
scripts/package-overleaf.py    Source-only ZIP packager
```

## Build

Install a TeX distribution containing pdfLaTeX, latexmk, and the geometry package, such as [MacTeX](https://tug.org/mactex/) or [TeX Live](https://tug.org/texlive/). Packaging requires Python 3.

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

This project reorganizes `report6.tex`, dated July 19, 2013 within the manuscript. Its prose, equations, table, author affiliations, appendix code, section numbering, and four bibliography entries are preserved. Bibliographic entries remain in their original order in an editable `thebibliography` environment.

All 17 original files are preserved byte for byte in the local `Attic/`, verified by a SHA-256 manifest. Existing files within `Attic/` retain their paths; former root files and the `auto/` directory were moved into it. The archive includes two PDFs, older LaTeX drafts, editor files, `calc.py`, the workbook, author photos, and `r2014_july.rtf`. That later formatted RTF version has editorial differences and is not the source of this refactoring. Author photos are not used by the LaTeX manuscript.

The local archive, validation records, build intermediates, and distribution ZIP are excluded from Git. The final root PDF is tracked.

## Validation

- The final PDF has 13 pages, matching the archived `report6.pdf` page count.
- Every page has identical extracted text and an identical rendered image at 900 pixels on the longer edge compared with a fresh build of the unmodified `report6.tex` using the same installed TeX toolchain.
- The page overview was visually inspected. The original 4.92314-point overfull-box warning in Appendix A and three underfull-box warnings in the bibliography remain; text is not clipped. There are no unresolved references.
- The extracted Overleaf ZIP compiled locally and produced identical page text. The Overleaf service itself was not tested.
- The older archived PDF has text-extraction differences, including ligatures and spacing. Exact equivalence is established against a fresh original-source build, not that historical PDF binary.

## Historical limitations

This is a structural refactoring, not a technical or editorial revision. Original claims, URLs, spelling, and sample-code defects remain. In particular, Appendix A defines a binomial coefficient using `factorial(a + b)` where a choose operation is needed, and its `prob_fail` function returns inside the summation loop. The separately archived `calc.py` also returns inside that loop, imports a nonexistent `math.norm`, and uses Python 2 print syntax. Neither is presented as validated executable software. Correcting the numerical examples, code, and derivations requires a separate reviewed revision.
