#joining pdf files to one pdf file (write pdf files to join in argument)
import PyPDF2
import sys

inputs = sys.argv[1:]  #adding argumenst in comannd line

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('all_in_one.pdf') #creating a new pdf file from the files given as an argument
pdf_combiner(inputs)
