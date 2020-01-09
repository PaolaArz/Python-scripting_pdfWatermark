import PyPDF2
import sys

original = sys.argv[1]
wtr = sys.argv[2]

with open(original, 'rb') as input_file:
	original_reader = PyPDF2.PdfFileReader(input_file)
	with open(wtr, 'rb') as wtr_file:
		wtr_reader = PyPDF2.PdfFileReader(wtr)
		wtr_page = wtr_reader.getPage(0)
		writer = PyPDF2.PdfFileWriter()

		for i in range(original_reader.getNumPages()):
			original_page = original_reader.getPage(i)			
			original_page.mergePage(wtr_page)
			writer.addPage(original_page)
	with open('final.pdf', 'wb') as output_file:
		writer.write(output_file)
