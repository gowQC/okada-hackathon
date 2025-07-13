# Should be run only once to get chunks. No need to run if chroma directory is available in data folder.
# Run with this command from "okada-hackathon" directory in terminal: python -m app.scripts.load_excel
from app.services.rag import load_excel_as_chunks, load_chunks_into_chroma

file_path = "app/data/mock_data.csv"

chunks = load_excel_as_chunks(file_path)
load_chunks_into_chroma(chunks)

print(f"✅ Loaded {len(chunks)} rows into ChromaDB.")