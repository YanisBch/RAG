import chromadb
from dotenv import load_dotenv
import os

load_dotenv()
dbDirectory = os.getenv("DB_DIRECTORY")
client = chromadb.PersistentClient(dbDirectory)

collection = client.create_collection("documents")

