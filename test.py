import PyPDF2
import sys

#To Grab All The PDF File Written On Command Line Input As A List
inputs = sys.argv[1:]

def water_marker(pdf_list):
	for pdf in pdf_list:	
		template = PyPDF2.PdfFileReader(open(f'{pdf}.pdf','rb'))
		water_mark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
		output = PyPDF2.PdfFileWriter()
		for i in range(template.getNumPages()):

			page = template.getPage(i)
			page.mergePage(water_mark.getPage(0))
			output.addPage(page)
			with open(f'water_mark{pdf}.pdf','wb') as file:
				output.write(file)	
	
water_marker(inputs)	