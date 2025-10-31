# Makefile untuk RAG Chatbot


# Makefile untuk RAG Chatbot - pipeline lengkap

install:
	pip install -r requirements.txt

# 1. Ingest dokumen (PDF/TXT/HTML)
ingest:
	python src/ingest.py

# 2. Cleaning dokumen
clean:
	python src/cleaning.py

# 3. Chunking dokumen
chunk:
	python src/chunking.py

# 4. Embedding dokumen
embed:
	python src/embedding.py

# 5. Upload metadata ke PostgreSQL
pgmeta:
	python src/pg_metadata.py

# 6. Upload embedding ke Qdrant
qdrant-ingest:
	python src/qdrant_ingest.py

# 7. Cek data di Qdrant
qdrant-check:
	python src/qdrant_check.py

# 8. Search similarity dari Qdrant
search:
	python src/qdrant_search.py

# 9. Inference LLM (Gradient.io atau lain)
llm:
	python src/llm_gradient.py

# 10. Test pipeline
test:
	pytest tests/

# 11. Linting
lint:
	flake8 src/

# 12. Notebook
notebook:
	jupyter notebook notebooks/

# Pipeline otomatis dari awal hingga akhir (all)
all: ingest clean chunk embed pgmeta qdrant-ingest qdrant-check search llm

