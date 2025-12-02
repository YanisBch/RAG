import chromadb
from chromadb.utils import embedding_functions
import pdfChunking as pdf
from dotenv import load_dotenv
import os

huggingface = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-m3",
    device="cpu",
    normalize_embeddings=True
)

load_dotenv()
dbDirectory = os.getenv("DB_DIRECTORY")
client = chromadb.PersistentClient(dbDirectory)

collection = client.get_or_create_collection(name="documents", embedding_function=huggingface)


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
        metadatas = [{"categorie": filePath} for i in range(len(document))]
        
    )
    print("The document " + filePath + " is in the database")

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
        n_results=50
    )
    return results

#addDocumentDB('documentsPDF/CCTP-GROS-OEUVRE.pdf')

#print(searchQuery("Quelles sont les postures à adopter")['ids'][0][1])
