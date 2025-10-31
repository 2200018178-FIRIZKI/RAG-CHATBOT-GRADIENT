

### ⚙️ Checklist Wajib Proyek RAG Chatbot

- [x] Struktur folder dan file profesional
- [x] requirements.txt dan .gitignore
- [x] Template README.md
- [x] Script training dan inference
- [x] Unit test dasar
- [x] Folder data dan models
- [x] Konfigurasi terpisah (config.py)
- [x] Notebook eksplorasi
- [x] Makefile
- [x] Data internal sudah tersedia di `data/raw/`
- [ ] Pipeline ingest dokumen (PDF, TXT, HTML) dengan OCR jika perlu
- [ ] Pembersihan & validasi teks (header, footer, nomor halaman, spasi ganda)
- [ ] Chunking teks (700–1200 karakter/token) & validasi distribusi chunk
- [ ] Embedding dengan SentenceTransformers/open-source, dimensi konsisten
- [ ] Penyimpanan embedding di vector database (Qdrant/FAISS/Chroma)
- [ ] Penyimpanan metadata dokumen di PostgreSQL (doc_id, filename, title, page_number, chunk_index, text, source_path, created_at)
- [ ] Retrieval & similarity search (top-3/top-5 konteks relevan)
- [ ] Penyimpanan metadata penting (doc_id, page, chunk_id, url)
- [ ] (Opsional) Re-ranking (BM25/ColBERT)
- [ ] Prompt engineering anti-halusinasi, selalu tampilkan sumber
- [ ] Guardrail: chatbot tidak menjawab di luar konteks dokumen
- [ ] Integrasi API Gradient.io (endpoint & token aman di .env)
- [ ] Model LLM sesuai hasil training di Gradient.io, versi tercatat
- [ ] UI sederhana (Streamlit/Gradio) atau API endpoint (FastAPI)
- [ ] Semua parameter konfigurasi di config.yaml
- [ ] Logging & monitoring (query, respons, error, dsb)
- [ ] Uji fungsional minimal 20 pertanyaan uji
- [ ] Uji performa (P95 < 3–5 detik, error <1%)
- [ ] Tidak ada token/API key di repo, lisensi data & model jelas
- [ ] Lingkungan reproducible (requirements.txt/pyproject.toml, Makefile)
- [ ] Dokumentasi lengkap: README.md, API.md, ARCHITECTURE.md
- [ ] Sesi handover & demo ke klien
