# RAG Chatbot dengan Gradient.io

## 1️⃣ Tujuan Utama
Proyek ini membangun chatbot cerdas berbasis Retrieval-Augmented Generation (RAG) yang memanfaatkan Large Language Model (LLM) dari Gradient.io. Chatbot ini mampu menjawab pertanyaan pengguna dengan menggabungkan hasil pencarian dokumen dan kemampuan generatif LLM, sehingga jawaban lebih relevan dan berbasis data.

## 2️⃣ Teknologi yang Digunakan
- **Python 3.8+** — Bahasa pemrograman utama
- **PostgreSQL** — Penyimpanan metadata dokumen
- **Qdrant** — Vector database untuk similarity search
- **Gradient.io API** — Layanan LLM untuk inferensi jawaban
- **SentenceTransformers** — Untuk embedding teks
- **Docker** — Orkestrasi database (opsional)
- **Makefile** — Otomasi pipeline

## 3️⃣ Struktur Folder
- `src/` — Kode sumber utama (pipeline RAG)
- `data/` — Dataset mentah & hasil proses
- `models/` — Model terlatih/checkpoint (jika ada)
- `tests/` — Unit test
- `venv/` — Virtual environment (jika lokal)
- `Makefile` — Otomasi pipeline
- `.env` — Konfigurasi rahasia & environment

## 4️⃣ Cara Instalasi & Menjalankan
1. **Clone repository & masuk ke folder:**
   ```bash
   git clone <repo-url>
   cd rag-chatbot-gradient
   ```
2. **Buat virtual environment & install dependensi:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   make install
   ```
3. **Konfigurasi `.env`**  
   Edit file `.env` sesuai kebutuhan (lihat contoh di repo).

4. **Jalankan pipeline RAG:**
   - Pipeline lengkap:
     ```bash
     make all
     ```
   - Atau jalankan step per step sesuai kebutuhan (`make ingest`, `make clean`, dst).

## 5️⃣ Contoh Penggunaan Chatbot
Setelah pipeline selesai, jalankan:
```bash
make llm
```
Masukkan pertanyaan, misal:
```
Masukkan pertanyaan: Siapa presiden Indonesia saat ini?
```
Chatbot akan menampilkan jawaban berbasis dokumen dan LLM.

## 6️⃣ Panduan Pengembang
- Struktur kode modular di dalam folder `src/`
- Setiap tahap pipeline dapat dijalankan terpisah
- Testing: `make test`
- Linting: `make lint`

## 7️⃣ Catatan
- Pastikan database PostgreSQL & Qdrant sudah berjalan (bisa via Docker)
- API Gradient.io membutuhkan API key yang valid
- Data mentah diletakkan di folder `data/`

---

**README.md** ini menjadi referensi utama bagi pengguna dan pengembang untuk memahami, menginstal, dan menjalankan proyek RAG Chatbot ini.
