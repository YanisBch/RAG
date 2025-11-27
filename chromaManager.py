import chromadb
import pdfChunking as pdf


client = chromadb.Client()
collection = client.create_collection("document")


def addDocumentDB(filePath):
    """
    Add document into chromaDB.
    
    Args:
        filePath (str): Path of the document to insert into the db
        
    Returns:
        None: The function modifies the database but return nothing
    """
    document = pdf.pdfChunking(filePath)
    
    collection.add(
        documents=[chunk for chunk in document], 
        ids=["doc"+str(i) for i in range(len(document))],
    )

def searchQuery(retrieve):
    """
    Find similar text between an input of the user and the vectorial db.

    Args:
        retrieve (str): Retrieved string of the user
        
    Returns:
        QueryResult: The rows from the db that are similar to the retrieved string
            class QueryResult(TypedDict):
            ids: List[IDs]
            embeddings: Optional[List[Embeddings]],
            documents: Optional[List[List[Document]]]
            metadatas: Optional[List[List[Metadata]]]
            distances: Optional[List[List[float]]]
            included: Include
    """
    results = collection.query(
        query_texts=[retrieve],
        n_results=3 
    )
    return results
