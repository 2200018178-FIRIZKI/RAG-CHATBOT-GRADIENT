"""
Script analisis jumlah halaman dan preview isi PDF
"""
import fitz

PDF_PATH = "data/raw/putusan_1878_pk_pid.sus_2025_20251031175537.pdf"


def cek_halaman_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    print(f"Jumlah halaman: {doc.page_count}")
    for i in range(doc.page_count):
        page = doc.load_page(i)
        text = page.get_text()
        print(f"\n--- Halaman {i+1} ---\n{text[:300]}...")  # Preview 300 karakter pertama
    doc.close()

if __name__ == "__main__":
    cek_halaman_pdf(PDF_PATH)
