.PHONY : cleanTeX clean
cleanTeX : 
	@find . -type f \( -iname '*.aux' -o -iname '*.bcf' -o -iname '*.lof' -o -iname '*.log' -o -iname '*.out' -o -iname '*.pdf' -o -iname '*.bcf' -o -iname '*.xml' -o -iname '*.gz' -o -iname '*.toc' -o -iname '*.bbl' -o -iname '*.blg' \) ! -iname 'ua.pdf' -delete
	@echo "Cleaning temporary files!"
clean : cleanTeX

all : 
	$(shell cd LaTeX;\
	pdflatex -shell-escape Crypto.tex;\
	pdflatex -shell-escape Crypto.tex;\
	biber Crypto.bcf;\
	pdflatex -shell-escape Crypto.tex)
