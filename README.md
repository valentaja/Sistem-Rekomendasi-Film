# 🎬 Sistem Rekomendasi Film Menggunakan User-Based Collaborative Filtering

## Deskripsi

Project ini merupakan implementasi Sistem Rekomendasi Film menggunakan metode **User-Based Collaborative Filtering** dengan algoritma **Jaccard Similarity**. Program dikembangkan menggunakan bahasa pemrograman Python sebagai implementasi konsep **Matematika Diskrit**, khususnya teori himpunan (Set Theory), graf bipartit (Bipartite Graph), dan pengukuran tingkat kemiripan antar pengguna.

Sistem menghitung tingkat kemiripan antar pengguna berdasarkan daftar film yang pernah ditonton, kemudian menghasilkan rekomendasi film yang belum pernah ditonton oleh pengguna tersebut.

---

## Kelompok 7

| No | Nama |
|----|-----------------------------|
| 1 | Fuad Wigo Wicaksono |
| 2 | Muhammad Syarofi Kunaedi |
| 3 | Valent Ichsanul Fitri |

> Repository ini dikelola menggunakan akun GitHub salah satu anggota kelompok sebagai media pengumpulan tugas.

---

## Mata Kuliah

**Matematika Diskrit (TB-B)**

Program Studi Teknik Informatika

Universitas Muhammadiyah Cirebon

---

## Fitur Program

- Menghitung Jaccard Similarity antar pengguna.
- Memberikan rekomendasi film berdasarkan pengguna yang memiliki preferensi serupa.
- Menampilkan visualisasi Graf Bipartit.
- Menampilkan Heatmap Similarity.
- Mengukur waktu eksekusi program.

---

## Teknologi yang Digunakan

- Python 3
- NetworkX
- Matplotlib
- NumPy

---

## Struktur Project

```
Sistem-Rekomendasi-Film/
│
├── modifikasi.py
├── README.md
└── LICENSE
```

---

## Cara Menjalankan Program

1. Clone repository

```bash
git clone https://github.com/valentaja/Sistem-Rekomendasi-Film.git
```

2. Masuk ke folder project

```bash
cd Sistem-Rekomendasi-Film
```

3. Install library

```bash
pip install networkx matplotlib numpy
```

4. Jalankan program

```bash
python modifikasi.py
```

---

## Konsep Matematika Diskrit

Project ini mengimplementasikan beberapa konsep Matematika Diskrit, yaitu:

- Teori Himpunan (Set Theory)
- Operasi Irisan (Intersection)
- Operasi Gabungan (Union)
- Kardinalitas Himpunan
- Graf Bipartit (Bipartite Graph)
- Jaccard Similarity

---

## Referensi

Project ini dikembangkan sebagai bagian dari tugas Mata Kuliah Matematika Diskrit.

Ide dasar implementasi mengacu pada repository berikut:

https://github.com/rayhandwipadli/Sistem-Rekomendasi

Selanjutnya dilakukan modifikasi dan pengembangan sesuai kebutuhan tugas kelompok, termasuk penyesuaian algoritma, penyempurnaan struktur program, serta penambahan visualisasi untuk mendukung proses rekomendasi.

---

## Lisensi

Project ini dibuat untuk keperluan pembelajaran dan tugas akademik. Hak cipta atas kode asli tetap dimiliki oleh pembuat repository yang menjadi referensi. Modifikasi dilakukan oleh Kelompok 7 sebagai bagian dari tugas Mata Kuliah Matematika Diskrit.
