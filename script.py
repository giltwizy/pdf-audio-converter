import PyPDF2,pyttsx3

# PDF File 
path = open('file.pdf','rb')

# Creating a pdffilereader object
pdfReader = PyPDF2.PdfFileReader(path)

# Get an engine instance for speech synthesis 
speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
speak.stop()
