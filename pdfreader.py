from pyPdf import PdfFileWriter, PdfFileReader

output     = PdfFileWriter()
input_data = PdfFileReader(file("doc.pdf", "rb"))

for page in input.pages:
    print page.extractText()
    
# outputStream = file("document-output.pdf", "wb")
# output.write(outputStream)
# outputStream.close()