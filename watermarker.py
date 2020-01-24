#adding watermarker to pdf file (joing pdf and watermark)
import PyPDF2

template = PyPDF2.PdfFileReader(open('all_in_one.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(open('watermarker.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

#function creating a pdf file with two files (one with for example some text, two with the watermarker)
for i in range (template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('pdf_watermark.pdf', 'wb') as file:
		output.write(file)
