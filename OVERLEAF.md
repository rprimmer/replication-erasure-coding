# Overleaf

Run `make overleaf`, then upload `dist/replication-erasure-coding-overleaf.zip` as a new project at [Overleaf](https://www.overleaf.com/). Select `replication-erasure-coding.tex` as the main document and pdfLaTeX as compiler.

Edit manuscript files in `sections/`, title/authors/date in `metadata.tex`, layout in `preamble.tex`, and macros in `macros.tex`. The ZIP contains editable sources and an Overleaf-specific `latexmkrc`; it excludes archived originals and build artifacts.

Appendix A reads `sample_code.py` directly. Keep this file in the project root; edit it to change both the runnable sample and the printed listing. The ZIP also includes the standalone `calc.py` calculator.
