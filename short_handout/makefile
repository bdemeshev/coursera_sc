file_name = short_handout

$(file_name).pdf: $(file_name).tex
	# protection against biber error
	# http://tex.stackexchange.com/questions/140814/
	rm -rf `biber --cache`

	# create pdf
	# will automatically run pdflatex/biber if necessary
	# latexmk -xelatex $(file_name).tex
	arara -v $(file_name).tex

	# clean auxillary files
	# latexmk -c $(file_name).tex


clean:
	latexmk -c $(file_name).tex
	-rm *.nav
	-rm *.snm
	-rm *.xdv
	-rm *.blg
	-rm *.bbl
	-rm *.log
	-rm *.pdf

