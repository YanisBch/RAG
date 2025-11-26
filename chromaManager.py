import chromadb
import pdfChunking as pdf


client = chromadb.Client()
collection = client.create_collection("document")


def addDocumentDB(filePath):
    """
    Add document into chromaDB.
    Args:
        filePath (string): Path of the document to insert into the db
    """
    document = pdf.pdfChunking(filePath)
    
    collection.add(
        documents=[chunk for chunk in document], 
        ids=["doc"+str(i) for i in range(len(document))],
    )

def searchQuery(retrieve):
    """
    Find similar text between an input of the user and the vectorial db

    Args:
        retrieve (string): Retrieved string of the user
        arg2 (type): Description de l'argument arg2.

    Returns:
        QueryResult: The rows from the db that are similar to the retrieved string

    """
    results = collection.query(
        query_texts=[retrieve],
        n_results=3 
    )
    return results
