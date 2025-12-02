import chromadb
from chromadb.config import Settings

# 1. Initialiser avec l'autorisation de reset
client = chromadb.PersistentClient(
    path="./chromaDB",
    settings=Settings(allow_reset=True) # <--- INDISPENSABLE
)

# 2. La commande de purge totale
#client.reset()
client.delete_collection(name="documents") 

print("Base de données vidée avec succès.")