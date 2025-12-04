# Simple Store Financial Report Analysis

Program ini adalah aplikasi Python sederhana berbasis **pandas** yang digunakan untuk mencatat, mengelola, dan menganalisis data penjualan toko kecil dalam bentuk file CSV.  
Struktur project dibuat agar rapi dan mudah diperluas.

---

## 📂 Struktur Folder

```
Project/
│── data/                   # Folder penyimpanan seluruh file CSV
│── program/                # Folder utama program
│   │── Halaman_Depan.py    # Main program (menu utama)
│   │── Perhitungan.py      # Modul analisis pendapatan/penjualan
│
│── requirements.txt        # Daftar library yang digunakan
└── README.md               # Dokumentasi project
```

---

## 🧰 Fitur Program

### 1. Halaman_Depan.py (Program Utama)
Berisi 4 menu utama:
- Membuat file CSV baru  
- Menambahkan isi file  
- Melihat isi file  
- Menghitung pendapatan toko  

### 2. Perhitungan.py (Modul Analisis)
Berisi fitur analisis:
- Menghitung total keuntungan setiap produk  
- Melihat produk yang terjual kurang/lebih dari 50%  

---

## 📊 Cara Kerja Program
- Data dicatat dalam format CSV  
- Program membaca dan mengolah data menggunakan pandas  
- Semua operasi (tambah data, lihat data, analisis) dilakukan melalui menu interaktif  

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
