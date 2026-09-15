# Shared by make, latexmk, and editors invoked from the project root.
$pdf_mode = 1;
$out_dir = 'build';
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
@default_files = ('replication-erasure-coding.tex');
