# TEACHER NOTES PROJECT

<p align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_secondary.svg" width="110" style="margin-right: 10px;">
</p>

Program ini adalah aplikasi Python sederhana berbasis **pandas** yang digunakan untuk mencatat, mengelola, dan menganalisis data Siswa dalam bentuk file CSV.  
Struktur project dibuat agar rapi dan mudah diperluas.

---

## 📂 Struktur Folder

```
Project/
│── Database/            # Folder penyimpanan seluruh file CSV
│── Main_Folder/         # Folder utama program
│   │── Main_Program.py  # Main program (menu utama)
│   │── Analysis.py      # Modul analisis pendapatan/penjualan
│── requirements.txt     # Daftar library yang digunakan
└── README.md            # Dokumentasi project
```

---

## 🧰 Fitur Program

### 1. Main_Program.py (Program Utama)
Berisi 3 menu utama:
- Membuat File CSV
- Manipulation File CSV
   4 Menu Dalam Opsi Manipulation
      - Menambahkan Isi File CSV
      - Menghapus Isi File CSV
      - Mengubah Isi File CSV
      - Melihat Isi File CSV
- Lihat Insight File CSV <<-- Opsi Untuk Ke File Analysis

### 2. Analysis.py (Modul Analisis)
Berisi fitur analisis:
- Urutkan Siswa Berdasarkan Nilai Ataupun Abjad
- Hitung Rata-Rata Nilai Siswa
- Filter Kriteria Siswa

---

## 📊 Cara Kerja Program
- Data dicatat dalam format CSV  
- Program membaca dan mengolah data menggunakan pandas  
- Semua operasi (tambah data, hapus data, ubah data, lihat data, analisis) dilakukan melalui menu interaktif  

---

## ▶️ Cara Menjalankan Project

1. Pastikan Python sudah terinstal  
2. Install library yang diperlukan:
   ```
   pip install -r requirements.txt
   ```
3. Masuk ke folder `program/`
4. Jalankan program:
   ```
   python Halaman_Depan.py
   ```

---


