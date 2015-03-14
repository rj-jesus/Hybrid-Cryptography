TPDFC = pdflatex
TPDFFLAGS = -shell-escape
TOBJ = $(shell find . -type f -iname '*.tex')
BC = biber
BOBJ = $(subst .tex, .bcj, $(TOBJ))

all : 
	$(TPDFC) $(TPDFFLAGS) $(TOBJ)
	$(TPDFC) $(TPDFFLAGS) $(TOBJ)
	$(BC) $(BOBJ)
	$(TPDFC) $(TPDFFLAGS) $(TOBJ)

BOBJ : 
	$(shell find . -type f -iname '*.bcf')
