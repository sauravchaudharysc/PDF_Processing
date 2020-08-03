import PyPDF2

with open('Cs.pdf','rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	writer = PyPDF2.PdfFileWriter()
	pg = reader.getNumPages();
	for x in range(pg):
		page = reader.getPage(x)
		page.rotateCounterClockwise(90)
		writer.addPage(page)
		with open('tilt.pdf','wb') as new_file:
			writer.write(new_file)

		


