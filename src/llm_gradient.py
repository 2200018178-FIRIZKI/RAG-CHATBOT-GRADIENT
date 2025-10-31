"""
Integrasi ke LLM (Gradient.io) - Kirim hasil retrieval (top-k chunk) sebagai konteks ke LLM via API
"""
import os
import requests
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

load_dotenv()

# Konfigurasi Gradient API
GRADIENT_API_URL = os.getenv("GRADIENT_API_URL", "https://api.gradient.ai/v1/llm/generate")
GRADIENT_API_KEY = os.getenv("GRADIENT_API_KEY", "your_gradient_api_key")
MODEL_NAME = "all-MiniLM-L6-v2"
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "rag_chunks"

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

def build_prompt(query, retrieved_chunks):
    context = "\n---\n".join([chunk.payload['text'] for chunk in retrieved_chunks])
    prompt = f"Berikut adalah beberapa kutipan dokumen:\n{context}\n\nJawablah pertanyaan berikut berdasarkan kutipan di atas.\nPertanyaan: {query}\nJawaban:"
    return prompt

def ask_gradient_llm(prompt):
    headers = {
        "Authorization": f"Bearer {GRADIENT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0.2
    }
    response = requests.post(GRADIENT_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("result") or response.json().get("text")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    pertanyaan = input("Masukkan pertanyaan: ")
    retrieved = search_qdrant(pertanyaan, top_k=5)
    prompt = build_prompt(pertanyaan, retrieved)
    print("\nPrompt ke LLM:\n", prompt)
    jawaban = ask_gradient_llm(prompt)
    print("\nJawaban LLM:")
    print(jawaban)
