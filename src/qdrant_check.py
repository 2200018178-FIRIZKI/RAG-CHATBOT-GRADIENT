"""
Script untuk cek collection dan data di Qdrant
"""
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

# Cek daftar collection
collections = client.get_collections()
print("Collections:", collections)

# Cek info collection rag_chunks
info = client.get_collection("rag_chunks")
print("Collection info:", info)

# Cek 5 data pertama
points, _ = client.scroll(collection_name="rag_chunks", limit=5)
print("\nContoh data:")
for point in points:
    print(point.payload)
