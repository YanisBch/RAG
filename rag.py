from geminiApiManager import completionRequest
from chromaManager import searchQuery, addDocumentDB

def promptGeneration(retrieve):
    similarDocuments = searchQuery(retrieve)
    similarDocumentsText = ""
    
    for query in searchQuery:
        similarDocumentsText = query['ids'] + query['document'] + " "
    
    prompt = "Answer the question: " + retrieve + " Base your answer on these documents: " + similarDocumentsText
    
    return prompt

