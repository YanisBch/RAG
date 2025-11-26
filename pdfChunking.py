from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def pdfChunking(filePath):
    """
    Split a pdf into chunk of similar size 

    Args:
        filePath (string): Path of the document to insert into the db

    Returns:
        texts: List of str representing all the chunks of the pdf

    """
    document = PdfReader(open(filePath, 'rb'))
    pdftext = ""
    
    for page in range(len(document.pages)):
        pageObj = document.pages[page]
        pdftext += pageObj.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_text(pdftext)
    
    return texts