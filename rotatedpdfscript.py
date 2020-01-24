#script is creating from one pdf file to other (rotated file)
import PyPDF2

with open('onepage.pdf', 'rb') as file:  #r(read),b(binary),w(write)
	reader = PyPDF2.PdfFileReader(file)
	# print(reader.numPages) #return number of sites in file pdf

##channging text by 90 degrees
	page = reader.getPage(0) 
	#print(page.rotateCounterClockwise(90))
	page.rotateCounterClockwise(90)

##saving new file pdf
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('rotatedpage.pdf', 'wb') as new_file:
		writer.write(new_file)
	