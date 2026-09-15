LATEXMK ?= latexmk

.PHONY: all pdf clean clean-all distclean overleaf help

all: pdf

# latexmk discovers dependencies (including figures) and resolves references.
pdf:
	$(LATEXMK) replication-erasure-coding.tex
	cp build/replication-erasure-coding.pdf replication-erasure-coding.pdf

# Restrict cleanup to generated files in build/; retain the finished PDF.
clean:
	$(LATEXMK) -c replication-erasure-coding.tex

clean-all: distclean

distclean:
	$(LATEXMK) -C replication-erasure-coding.tex

overleaf:
	python3 scripts/package-overleaf.py

help:
	@echo 'make            Build and refresh replication-erasure-coding.pdf with pdfLaTeX'
	@echo 'make clean      Remove build intermediates; keep the PDF'
	@echo 'make distclean  Remove build outputs; keep the top-level PDF'
	@echo 'make overleaf   Package editable sources in dist/replication-erasure-coding-overleaf.zip'
