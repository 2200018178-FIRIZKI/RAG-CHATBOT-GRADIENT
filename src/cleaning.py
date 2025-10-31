"""
Modul pembersihan & validasi teks dokumen
- Menghapus header, footer, nomor halaman, spasi ganda, karakter tidak relevan
- Menyimpan snapshot sebelum & sesudah pembersihan
"""
import re
from pathlib import Path
from typing import List, Dict
import json

def clean_text(text: str) -> str:
    # Hilangkan nomor halaman (misal: 'Page 1', 'Halaman 2', dst)
    text = re.sub(r'(Page|Halaman)\s*\d+', '', text, flags=re.IGNORECASE)
    # Hilangkan header/footer umum (misal: 'Confidential', 'Draft', dst)
    text = re.sub(r'Confidential|Draft|Dokumen Rahasia', '', text, flags=re.IGNORECASE)
    # Hilangkan spasi ganda & baris kosong
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def process_and_save_cleaned_docs(docs: List[Dict], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for doc in docs:
        raw_text = doc['text']
        cleaned_text = clean_text(raw_text)
        # Simpan snapshot sebelum & sesudah
        snap = {
            'filename': doc['filename'],
            'source_path': doc['source_path'],
            'raw_text': raw_text[:1000],  # Simpan 1000 karakter pertama
            'cleaned_text': cleaned_text[:1000]
        }
        with open(out_dir / f"{doc['filename']}.json", 'w', encoding='utf-8') as f:
            json.dump(snap, f, ensure_ascii=False, indent=2)
        # Update doc untuk pipeline berikutnya
        doc['text'] = cleaned_text
    return docs

if __name__ == "__main__":
    from ingest import ingest_documents
    docs = ingest_documents(raw_dir=Path("data/raw/"))
    cleaned_docs = process_and_save_cleaned_docs(docs, Path("data/processed/snapshots/"))
    print(f"Total dokumen dibersihkan: {len(cleaned_docs)}")
