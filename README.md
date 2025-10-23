# Program Pengecekkan Proposal

Program desktop untuk validasi dan review proposal penelitian menggunakan konsep automata (NFA) dengan antarmuka GUI berbasis Tkinter.

## 📋 Fitur Utama

- ✅ Upload dan preview file proposal (PDF, DOCX, PNG)
- ✅ Validasi kelengkapan proposal menggunakan NFA
- ✅ Review sistematis untuk setiap bagian proposal
- ✅ Catatan review untuk setiap bagian
- ✅ Tampilan hasil review lengkap

## 🛠️ Teknologi

- **Python 3.x**
- **Tkinter** - GUI framework
- **PyMuPDF (fitz)** - PDF rendering
- **Pillow (PIL)** - Image processing
- **NFA (Nondeterministic Finite Automaton)** - State management

## 📦 Instalasi

### Prerequisites

Pastikan Python 3.x sudah terinstal di sistem Anda.

### Install Dependencies

```bash
pip install PyMuPDF Pillow
```

## 🚀 Cara Menggunakan

1. **Jalankan program:**
   ```bash
   python app.py
   ```

2. **Pilih File**
   - Klik tombol "Pilih file"
   - Pilih file proposal (PDF/DOCX/PNG)

3. **Upload File**
   - Klik tombol "Upload" setelah file dipilih

4. **Pemeriksaan Kelengkapan**
   - Pilih "Lengkap" jika proposal sudah lengkap
   - Pilih "Tidak Lengkap" untuk upload ulang

5. **Review Proposal** (5 bagian)
   - **Judul** - Periksa kesesuaian judul
   - **Pendahuluan** - Review latar belakang
   - **Tinjauan Pustaka** - Evaluasi referensi
   - **Metode Penelitian** - Analisis metodologi
   - **Format Proposal** - Cek format penulisan

6. **Kirim Review**
   - Klik "Kirim Review" setelah semua bagian selesai

7. **Lihat Hasil**
   - Klik "Review Notes" di halaman utama untuk melihat hasil lengkap

## 📁 Struktur Project

```
PROJECT_VALIDASI_PROPOSAL/
├── app.py              # Main application & GUI
├── nfa.py              # NFA implementation
└── README.md           # Documentation
```

## 🔄 Konsep NFA

Program menggunakan Nondeterministic Finite Automaton (NFA) untuk mengelola state transisi dalam proses review:

| State | Deskripsi | Input |
|-------|-----------|-------|
| **q1** | Initial state | File uploaded |
| **q2** | Completeness check | complete/incomplete |
| **q3** | Title review | title |
| **q4** | Introduction review | introduction |
| **q5** | Literature review | literature_review |
| **q6** | Methodology review | methodology |
| **q7** | Format review (Final) | format |

## 📝 Flow Diagram

```
q1 (Upload) → q2 (Kelengkapan) → q3 (Judul) → q4 (Pendahuluan) 
→ q5 (Tinjauan Pustaka) → q6 (Metode) → q7 (Format) → Selesai
```

## 💡 Fitur Tambahan

- Preview PDF dengan scrollbar
- Entry field untuk catatan setiap bagian
- Notifikasi status upload
- Window terpisah untuk setiap tahap review
- Hasil review tersimpan dan dapat dilihat kapan saja

## 🔧 Troubleshooting

**Error saat membuka PDF:**
- Pastikan PyMuPDF terinstal dengan benar
- Cek format file yang didukung (PDF, DOCX, PNG)

**GUI tidak muncul:**
- Pastikan Tkinter terinstal (sudah termasuk dalam Python standard)
- Jalankan sebagai administrator jika diperlukan

## 📄 Lisensi

Project ini dibuat untuk keperluan edukasi.

---

**Dibuat dengan ❤️ untuk Teori Bahasa dan Otomata**
