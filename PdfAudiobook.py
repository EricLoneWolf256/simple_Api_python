from pydoc import text
from tkinter.filedialog import Open
import pyttsx3
import PyPDF2

book = Open('operating_systems.pdf', 'rb')
pdfReeader = PyPDF2.PdfFileReader(book)
pages = pdfReeader.numpages
print(pages)

Speaker = pyttsx3.init()
for num in range(7,pages):
    page = pdfReeader.getPagez(7)
    text = page.extractText()
    Speaker.say(text)