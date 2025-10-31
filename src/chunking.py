"""
Modul chunking teks dokumen
- Membagi teks hasil ekstraksi PDF menjadi chunk per halaman
- Menyimpan metadata chunk (filename, chunk_id, page, text, start_idx, end_idx)
"""
from pathlib import Path
from typing import List, Dict
import json
import fitz  # PyMuPDF

CHUNK_SIZE = 700  # karakter per chunk (bisa diatur)
OVERLAP = 50      # overlap antar chunk (opsional)

def chunk_pdf_per_page(pdf_path: Path, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> List[Dict]:
    doc = fitz.open(pdf_path)
    chunks = []
    chunk_id = 0
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text()
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk_text = text[start:end]
            chunks.append({
                'chunk_id': chunk_id,
                'page': page_num + 1,
                'text': chunk_text,
                'start_idx': start,
                'end_idx': end
            })
            chunk_id += 1
            start += chunk_size - overlap
    doc.close()
    return chunks

def process_pdf_docs_to_chunks(raw_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for file in raw_dir.glob("*.pdf"):
        chunks = chunk_pdf_per_page(file)
        for chunk in chunks:
            chunk['filename'] = file.name
            chunk['source_path'] = str(file.resolve())
        with open(out_dir / f"{file.stem}_chunks.json", 'w', encoding='utf-8') as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
        print(f"{file.name}: {len(chunks)} chunk dibuat (per halaman).")

if __name__ == "__main__":
    raw_dir = Path("data/raw/")
    out_dir = Path("data/processed/chunks/")
    process_pdf_docs_to_chunks(raw_dir, out_dir)
