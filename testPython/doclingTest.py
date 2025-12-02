from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from transformers import AutoTokenizer
from docling.chunking import HybridChunker

# C'est le modèle par défaut de ChromaDB
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

source = "./documentsPDF/Le-travail-et-la-technique-cours.pdf"  # file path or URL

from docling.document_converter import DocumentConverter

doc = DocumentConverter().convert(source=source).document

chunker = HybridChunker(
    tokenizer=tokenizer,
    max_tokens=384  # Attention : ce modèle par défaut est limité à 384 tokens (pas 512 !)
)
chunk_iter = chunker.chunk(dl_doc=doc)

for i, chunk in enumerate(chunk_iter):
    print(f"=== {i} ===")
    print(f"chunk.text:\n{f'{chunk.text[:300]}…'!r}")

    enriched_text = chunker.contextualize(chunk=chunk)
    print(f"chunker.contextualize(chunk):\n{f'{enriched_text[:300]}…'!r}")

    print()