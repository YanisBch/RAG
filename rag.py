from geminiApiManager import completionRequest
from chromaManager import searchQuery, addDocumentDB
from pdfChunking import pdfChunking

def promptGeneration(retrieve):
    similarDocuments = searchQuery(retrieve)
    similarDocumentsText = ""
    
    for i in range(len(similarDocuments['ids'][0])):
        similarDocumentsText += similarDocuments['ids'][0][i] + similarDocuments['documents'][0][i] + " "
    
    prompt = "Answer the question: " + retrieve + " Base your answer on these documents: " + similarDocumentsText
    return prompt

#addDocumentDB('documents/comOralC1.pdf')

#print(completionRequest(promptGeneration("Quel est le code secret pour ouvrir le coffre fort?")))

