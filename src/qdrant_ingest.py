"""
Script untuk menyimpan embedding ke Qdrant dan melakukan similarity search.
"""
import os
import json
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels
from dotenv import load_dotenv
import numpy as np

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "rag_chunks")
EMBEDDING_DIR = Path("data/processed/embeddings/")

# 1. Inisialisasi Qdrant
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# 2. Buat collection jika belum ada
VECTOR_SIZE = 384  # default all-MiniLM-L6-v2, sesuaikan dengan model Anda
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=qmodels.VectorParams(size=VECTOR_SIZE, distance=qmodels.Distance.COSINE)
)

# 3. Upload embedding ke Qdrant
points = []
idx = 0
for emb_file in EMBEDDING_DIR.glob("*_embeddings.json"):
    with open(emb_file, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    for chunk in chunks:
        points.append(qmodels.PointStruct(
            id=idx,
            vector=np.array(chunk['embedding'], dtype=np.float32),
            payload={
                "filename": chunk['filename'],
                "chunk_id": chunk['chunk_id'],
                "text": chunk['text'],
                "page": chunk.get('page'),
                "start_idx": chunk.get('start_idx'),
                "end_idx": chunk.get('end_idx'),
                "source_path": chunk.get('source_path')
            }
        ))
        idx += 1
if points:
    client.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"Berhasil upload {len(points)} embedding ke Qdrant.")
else:
    print("Tidak ada embedding yang ditemukan untuk diupload.")

# 4. Contoh similarity search (opsional)
def search_qdrant(query_vector, top_k=5):
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return hits

# Contoh penggunaan search:
# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer("all-MiniLM-L6-v2")
# query = "masukkan pertanyaan di sini"
# query_vec = model.encode(query)
# results = search_qdrant(query_vec)
# for hit in results:
#     print(hit.payload, hit.score)
