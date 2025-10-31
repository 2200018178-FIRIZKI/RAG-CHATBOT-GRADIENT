# RAG Chatbot with Gradient.io

## Deskripsi
Chatbot berbasis Retrieval-Augmented Generation (RAG) menggunakan model LLM yang dilatih di Gradient.io.

## Struktur Folder
- `data/` : Dataset mentah & terproses
- `models/` : Model terlatih/checkpoint
- `src/` : Kode sumber utama
- `notebooks/` : Eksperimen & eksplorasi
- `tests/` : Unit test

## Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Training: `python src/train.py`
3. Inferensi: `python src/inference.py`

## Kebutuhan
- Python 3.8+
- Akun Gradient.io

## Catatan
- Pastikan data sudah tersedia di folder `data/`
- Konfigurasi dapat diubah di `src/config.py`
