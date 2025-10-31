"""
Pipeline Ingest & Ekstraksi Dokumen
- Membaca file PDF, TXT, HTML dari data/raw/
- Jika PDF hasil scan, lakukan OCR
"""
import os
from pathlib import Path
from typing import List, Dict

import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from bs4 import BeautifulSoup

RAW_DIR = Path("data/raw/")


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Ekstrak teks dari PDF, gunakan OCR jika perlu."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            page_text = page.get_text()
            if page_text.strip():
                text += page_text
            else:
                # OCR jika halaman kosong (kemungkinan hasil scan)
                images = convert_from_path(str(pdf_path), first_page=page.number+1, last_page=page.number+1)
                for img in images:
                    text += pytesseract.image_to_string(img)
        doc.close()
    except Exception as e:
        print(f"Gagal ekstrak PDF {pdf_path}: {e}")
    return text

def extract_text_from_txt(txt_path: Path) -> str:
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_text_from_html(html_path: Path) -> str:
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return soup.get_text(separator=' ')

def ingest_documents(raw_dir: Path = RAW_DIR) -> List[Dict]:
    """Membaca semua dokumen di raw_dir dan ekstrak teksnya."""
    docs = []
    for file in raw_dir.glob("**/*"):
        if file.suffix.lower() == '.pdf':
            text = extract_text_from_pdf(file)
        elif file.suffix.lower() == '.txt':
            text = extract_text_from_txt(file)
        elif file.suffix.lower() == '.html':
            text = extract_text_from_html(file)
        else:
            continue
        docs.append({
            'filename': file.name,
            'source_path': str(file.resolve()),
            'text': text
        })
    return docs

if __name__ == "__main__":
    docs = ingest_documents()
    print(f"Total dokumen terproses: {len(docs)}")
    for d in docs:
        print(f"{d['filename']}: {len(d['text'])} karakter")
