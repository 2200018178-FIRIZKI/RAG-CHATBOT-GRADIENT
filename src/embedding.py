"""
Modul embedding chunk teks
- Melakukan embedding pada setiap chunk menggunakan SentenceTransformers
- Menyimpan hasil embedding dan metadata ke file JSON
"""
from pathlib import Path
import json
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"  # Bisa diganti sesuai kebutuhan
CHUNKS_DIR = Path("data/processed/chunks/")
EMBEDDING_DIR = Path("data/processed/embeddings/")


def embed_chunks(model, chunks_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    texts = [chunk['text'] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    for chunk, emb in zip(chunks, embeddings):
        chunk['embedding'] = emb.tolist()
    out_path = out_dir / chunks_path.name.replace('_chunks.json', '_embeddings.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Embedding selesai: {chunks_path.name} -> {out_path.name}")

if __name__ == "__main__":
    model = SentenceTransformer(MODEL_NAME)
    EMBEDDING_DIR.mkdir(parents=True, exist_ok=True)
    for chunk_file in CHUNKS_DIR.glob("*_chunks.json"):
        embed_chunks(model, chunk_file, EMBEDDING_DIR)
