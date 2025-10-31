"""
Script untuk menyimpan metadata chunk ke PostgreSQL
"""
import os
import json
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("PG_HOST", "localhost")
DB_PORT = os.getenv("PG_PORT", "5432")
DB_NAME = os.getenv("PG_DB", "ragdb")
DB_USER = os.getenv("PG_USER", "postgres")
DB_PASS = os.getenv("PG_PASS", "postgres")

EMBEDDING_DIR = Path("data/processed/embeddings/")

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS chunk_metadata (
    id SERIAL PRIMARY KEY,
    doc_id VARCHAR(255),
    filename VARCHAR(255),
    chunk_id INT,
    text TEXT,
    start_idx INT,
    end_idx INT,
    source_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

INSERT_SQL = """
INSERT INTO chunk_metadata (doc_id, filename, chunk_id, text, start_idx, end_idx, source_path)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

def save_metadata_to_postgres():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_SQL)
    conn.commit()
    for emb_file in EMBEDDING_DIR.glob("*_embeddings.json"):
        with open(emb_file, 'r', encoding='utf-8') as f:
            chunks = json.load(f)
        for chunk in chunks:
            doc_id = chunk.get('doc_id', None)
            filename = chunk.get('filename')
            chunk_id = chunk.get('chunk_id')
            text = chunk.get('text')
            start_idx = chunk.get('start_idx')
            end_idx = chunk.get('end_idx')
            source_path = chunk.get('source_path', filename)
            cur.execute(INSERT_SQL, (doc_id, filename, chunk_id, text, start_idx, end_idx, source_path))
        conn.commit()
        print(f"Metadata dari {emb_file.name} berhasil disimpan ke PostgreSQL.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    save_metadata_to_postgres()
