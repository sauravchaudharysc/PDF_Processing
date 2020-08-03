import PyPDF2
import sys

#To Grab All The PDF File Written On Command Line Input As A List
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
	  merger.append(pdf+'.pdf')
	merger.write('merged.pdf')  
pdf_combiner(inputs)