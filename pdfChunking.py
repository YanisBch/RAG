from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

document = PdfReader(open('coursePDF/Theme_5_Equa_diff-20.pdf', 'rb'))
pdftext = ""
for page in range(len(document.pages)):
    pageObj = document.pages[page]
    pdftext += pageObj.extract_text()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(pdftext)