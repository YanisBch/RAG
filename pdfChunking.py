from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter



def pdfChunking(filePath):
    """
    Split a pdf into chunk of similar size 

    Args:
        filePath (str): Path of the document to insert into the db

    Returns:
        list[str]: List of string representing each chunk of the pdf
    """
    document = PdfReader(open(filePath, 'rb'))
    pdftext = ""
    
    for page in range(len(document.pages)):
        pageObj = document.pages[page]
        pdftext += pageObj.extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", "(?<=\. )", " ", ""])
    texts = text_splitter.split_text(pdftext)
    
    return texts