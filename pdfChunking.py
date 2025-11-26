from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def pdfChunking(filePath):
    document = PdfReader(open(filePath, 'rb'))
    pdftext = ""
    
    for page in range(len(document.pages)):
        pageObj = document.pages[page]
        pdftext += pageObj.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_text(pdftext)
    
    return texts