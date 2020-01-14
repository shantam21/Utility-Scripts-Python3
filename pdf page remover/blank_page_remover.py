#A simple script to remove extra pages from a PDF doc.
#Requires python3 and PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("The_Life_Changing_Magic_of_Tidying_Up_by_Marie_Kondo.pdf", "rb"))



# print how many pages input1 has, because why not:
print ("Input has %d pages." % input1.getNumPages())


skip_pages = []
for i in range(0,input1.getNumPages()):
    
    if input1.getPage(i).getContents() == None :
        print(input1.getPage(i).getContents())
        skippages.append(i)
        

for idx,x in enumerate(input1.pages):
	if(idx in skip_pages):
		print("Skipping page"+str(idx))
	else:
		output.addPage(input1.getPage(idx))
		
print ("Output has %d pages." % input1.getNumPages())
outputStream = open("PyPDF2-output.pdf", "wb")
output.write(outputStream)