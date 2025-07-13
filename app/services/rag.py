import os
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# Define persist path relative to project root (located in data folder)
chroma_client = chromadb.PersistentClient(path="app/data/chroma")

collection = chroma_client.get_or_create_collection("cre_data")

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def load_excel_as_chunks(file_path: str) -> list[str]:
    """Read an Excel spreadsheet and convert rows to text chunks."""
    df = pd.read_csv(file_path)
    text_chunks = []

    for i, row in df.iterrows():
        row_text = " | ".join(str(cell) for cell in row.values)
        text_chunks.append(row_text)

    return text_chunks


def embed_text(text: str) -> list[float]:
    """Embed a single text string using sentence-transformers."""
    embedding = embedder.encode(text)
    return embedding.tolist()


def load_chunks_into_chroma(chunks: list[str]):
    """Take a list of text chunks and store them in ChromaDB."""
    for i, chunk in enumerate(chunks):
        embedding = embed_text(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"doc-{i}"]
        )
    print("Persisting ChromaDB to disk...")


def get_relevant_context(query: str, top_k: int = 3) -> str:
    """Embed the query and retrieve top-k matching documents from Chroma."""
    query_embedding = embed_text(query)
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    documents = result.get("documents", [[]])[0]
    return "\n\n".join(documents)
