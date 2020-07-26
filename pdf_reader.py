import os
import pyttsx3
import PyPDF2

current_directory = os.getcwd()
file_name = os.path.join(current_directory,input("Enter pdf file name: "))

pdf_file = open(file_name,'rb')
parsed_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = parsed_pdf.numPages
print(number_of_pages)

reader = pyttsx3.init()

for page in range(9,number_of_pages):
    current_page = parsed_pdf.getPage(page)
    text = current_page.extractText()
    reader.say(text)
    reader.runAndWait()

pdf_file.close()