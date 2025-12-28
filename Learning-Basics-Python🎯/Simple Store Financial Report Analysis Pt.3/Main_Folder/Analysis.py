import os
import pandas as pd
import csv

class Analisis():
    def __init__(self):
        pass

    def Cleaning_Data(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"=== CLEANING DATA DISINI ===":^100}")
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini : ")
            lokasi_file = f"Database_/{nama_file}"
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print("="*100)
            print(df.to_string())
            print("="*100)
            print(f"{"=== DATA YANG DIBERSIHKAN HARUS BERNILAI N/A ATAU O ===":^100}")
            print(f"{"=== DATA YANG DIBERSIHKAN MENCAKUP SATU KOLOM JADI BERHATI-HATI ===":^100}")
            print("="*100)
            pilih_kolom = int(input("Pilih Nomer Kolom Yang Ingin Dibersihkan : "))
            nama_kolom = df.columns[pilih_kolom - 1]
            if 1 <= pilih_kolom <= len(df.columns):
                nilai_ganti = input(f"Masukkan Nilai Ganti Pada Kolom {nama_kolom} : ")
                df[nama_kolom] = df[nama_kolom].fillna(nilai_ganti)
                df.to_csv(lokasi_file, index=False)
                df_view = df.copy()
                df_view.index = df_view.index + 1
                print(df_view.to_string())
            else:
                print(f"Jumlah Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan")
            exit()

    def Analisis_Time_Series(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"=== ANALISIS TIME SERIES DISINI ===":^100}")
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini : ").lower()
            lokasi_file = f"Database_/{nama_file}"
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print(df_view.to_string())
            pilih_kolom_tanggal = int(input("Pilih Nomer Kolom Tanggal : "))
            pilih_kolom_total   = int(input("Pilih Nomer Kolom Total   : "))
            nama_kolom_tanggal = df.columns[pilih_kolom_tanggal - 1]
            nama_kolom_total = df.columns[pilih_kolom_total - 1]
            if (1 <= pilih_kolom_tanggal <= len(df.columns)) and (1 <= pilih_kolom_total <= len(df.columns)):
                df[nama_kolom_tanggal] = pd.to_datetime(df[nama_kolom_tanggal])
                df.set_index(nama_kolom_tanggal, inplace=True)
                df_mingguan = df[nama_kolom_total].resample("W").sum()
                print(df_mingguan.to_string())
            else:
                print(f"Jumlah Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan")
            exit()
    
    def Top_And_Worst_Sell(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"=== PRODUK TERLARIS(TOP SELLING) DAN PRODUK TERBURUK(WORST SELLING) ===":^100}")
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini : ")
            lokasi_file = f"Database_/{nama_file}"
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print(df_view.to_string())
            pilih_kolom_stock_awal    = int(input("Masukkan Kolom Stock Awal    : "))
            pilih_kolom_stock_terjual = int(input("Masukkan Kolom Stock Terjual : "))
            
            if (1 <= pilih_kolom_stock_awal <= len(df.columns)) and (1 <= pilih_kolom_stock_terjual <= len(df.columns)):
                nilai_tengah_stock_awal = df.iloc[:,(pilih_kolom_stock_awal - 1)] / 2
                print(nilai_tengah_stock_awal)
                print("="*100)
                print(f"{"=== Produk Top Selling ===":^100}")
                print("="*100)
                top_selling = df[(df.iloc[:,pilih_kolom_stock_terjual - 1] > nilai_tengah_stock_awal)]
                print(top_selling)
                print(f"\n{"="*100}")
                print(f"{"=== Produk Top Selling ===":^100}")
                print("="*100)
                worst_selling = df[(df.iloc[:,pilih_kolom_stock_terjual - 1] < nilai_tengah_stock_awal)]
                print(worst_selling)
            else:
                print(f"Jumlah Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f'File Bernama {nama_file} Tidak Ditemukan')
            exit()

    def Total_Harga(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"=== PRODUK TERLARIS(TOP SELLING) DAN PRODUK TERBURUK(WORST SELLING) ===":^100}")
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini : ")
            lokasi_file = f"Database_/{nama_file}"
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print(df_view.to_string())
            kolom_produk = int(input('Pilih Nomor Kolom Jumlah Produk Terjual : '))
            harga_satuan = int(input('Pilih Nomor Kolom Harga Satuan          : '))
            if (1 <= kolom_produk <= len(df.columns)) and (1 <= harga_satuan <= len(df.columns)):
                df["Total_Keuntungan"] = df.iloc[:,(kolom_produk - 1)] * df.iloc[:,(harga_satuan - 1)]
                df.to_csv(lokasi_file, index=False)
                print("="*100)
                df_view = df.copy()
                df_view.index = df_view.index + 1
                print(df_view.to_string())
                print("="*100)
            else:
                print(f"Jumlah Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f'File Bernama {nama_file} Tidak Ditemukan')
            exit()

    def Total_Harga_Kategori(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"=== HITUNG TOTAL HARGA PRODUK TERJUAL BERDASARKAN KATEGORI ===":^100}")
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini : ")
            lokasi_file = f"Database_/{nama_file}"
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print(df_view.to_string())
            pilih_kolom_total    = int(input('Pilih Nomor Kolom Total Harga Produk : '))
            pilih_kolom_kategori = int(input('Pilih Nomor Kolom Kategori Produk    : '))
            nama_kolom_total = df.columns[pilih_kolom_total - 1]
            nama_kolom_kategori = df.columns[pilih_kolom_kategori - 1]
            if (1 <= pilih_kolom_total <= len(df.columns)) and (1 <= pilih_kolom_kategori <= len(df.columns)):
                group = df.groupby(nama_kolom_kategori)[nama_kolom_total].sum()
                print("="*100)
                print(group)
                print("="*100)
            else:
                print(f"Jumlah Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f'File Bernama {nama_file} Tidak Ditemukan')
            exit()

def main_analisis():
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        print("="*100)
        print(f"{"=== Analisis Data Anda Disini ===":^100}")
        print("="*100)

        try:
            opsi_awal = int(input('''Pililah Opsi Dibawah Ini : 
    1. Cleaning Data
    2. Analisis Time Series (Mingguan)
    3. Produk Terlaris (Top Selling) Dan Produk Terburuk (Worst Selling)
    4. Hitung Total Harga Per Transaksi
    5. Hitung Total Harga Produk Terjual Berdasarkan Kategori
Pilih Antara (1/2/3/4) : '''))

            if opsi_awal == 1:
                user = Analisis()
                user.Cleaning_Data()

            elif opsi_awal == 2:
                user = Analisis()
                user.Analisis_Time_Series()

            elif opsi_awal == 3:
                user = Analisis()
                user.Top_And_Worst_Sell()

            elif opsi_awal == 4:
                user = Analisis()
                user.Total_Harga()

            elif opsi_awal == 5:
                user = Analisis()
                user.Total_Harga_Kategori()
            
            else:
                print("Pilihan Hanya (1/2/3/4/5) !!")

        except ValueError:
            print(f"Pilihan Hanya Berupa Angka !!")
            exit()

        opsi_lanjutan = input("Apakah Anda Ingin Melanjutkan (y/n) : ").lower()
        if opsi_lanjutan == 'n':
            break

    print("="*100)
    print(f"{"=== SAMPAI JUMPA LAGI !!! ===":^100}")
    print("="*100) 