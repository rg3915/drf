pdf:
	latexmk -pdf person
	latexmk -c

pvc:
	latexmk -pdf -pvc person

clear:
	latexmk -c
	rm *.nav *.snm *.vrb

convert:
	mogrify -format jpg -density 300 *.pdf