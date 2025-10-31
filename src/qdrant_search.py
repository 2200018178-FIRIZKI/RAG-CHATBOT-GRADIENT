"""
Script similarity search ke Qdrant dari query user
"""
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Konfigurasi
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "rag_chunks"
MODEL_NAME = "all-MiniLM-L6-v2"

# Inisialisasi model dan client
model = SentenceTransformer(MODEL_NAME)
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def search_qdrant(query, top_k=5):
    query_vec = model.encode(query)
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vec,
        limit=top_k
    )
    return hits

if __name__ == "__main__":
    pertanyaan = input("Masukkan pertanyaan: ")
    results = search_qdrant(pertanyaan, top_k=5)
    print("\nHasil similarity search:")
    for i, hit in enumerate(results):
        print(f"\nRank {i+1} (score={hit.score:.4f}):")
        print(f"Text: {hit.payload['text']}")
        print(f"Filename: {hit.payload['filename']}, Chunk: {hit.payload['chunk_id']}, Page: {hit.payload.get('page')}")
