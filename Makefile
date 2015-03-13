.PHONY : cleanTeX clean
cleanTeX : 
	@find . -type f \( -iname '*.aux' -o -iname '*.bcf' -o -iname '*.lof' -o -iname '*.log' -o -iname '*.out' -o -iname '*.pdf' -o -iname '*.bcf' -o -iname '*.xml' -o -iname '*.gz' -o -iname '*.toc' \) ! -iname 'ua.pdf' -delete
	@echo "Cleaning temporary files!"
clean : cleanTeX
