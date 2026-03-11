# VISUALISASI DATA SEDERHANA DENGAN MATPLOTLIB

<p align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_secondary.svg" width="110" style="margin-right: 10px;">
  <img src="https://matplotlib.org/_static/images/logo2.svg" width="120">
</p>

Program ini adalah aplikasi Python sederhana berbasis **pandas**, **matplotlib** yang digunakan untuk mencatat, mengelola, dan memvisualisasikan dalam bentuk file CSV.  
Struktur project dibuat agar rapi dan mudah diperluas.

---

## 📂 Struktur Folder

```
Project/
│── Database_/              # Folder penyimpanan seluruh file CSV
│── Main_Folder/            # Folder utama program
│   │── Main_Program.py     # Main program (menu utama)
│   │── Visualisasi.py      # Modul Menampilkan Diagram data dari file CSV
│── requirements.txt        # Daftar library yang digunakan
└── README.md               # Dokumentasi project
```

---

## 🧰 Fitur Program

### 1. Main_Program.py (Program Utama)
Berisi 4 menu utama:
- Menambahkan Isi File CSV
- Menghapus Isi File CSV
- Mengubah Isi File CSV
- Melihat Isi File CSV

### 2. Visualisasi.py (Modul Visualisasi)
Berisi fitur visualisasi:
- Diagram Garis/PLOT
- Diagram Batang/BAR
- Diagram Lingkaran/PIE

---

## 📊 Cara Kerja Program
- Data dicatat dalam format CSV  
- Program membaca dan mengolah data menggunakan pandas  
- Semua operasi (tambah data, hapus data, ubah data, lihat data, visualisasi) dilakukan melalui menu interaktif  

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






