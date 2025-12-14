import os
import pandas as pd
import csv

class Analysis_Class:
    def __init__(self):
        pass

    # Bagian Pembersihan Data ================================
    def Cleaning_Data(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"== Pembersihan Data ==":^100}")
        print("="*100)

        try:
            nama_file = input("Masukkan Nama File Kamu Disini : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            print(f'\n{"="*100}')
            print(df)
            print(f'{"="*100}\n')
            print(f"{"== KOLOM YANG INGIN DIHAPUS HARUS BERVALUE N/A ATAU KOSONG ... !!! =="}")

            kolom_analisa = int(input('Masukkan Nomor Kolom Untuk DiAnalisis : '))
            nama_kolom_analisa = df.columns[kolom_analisa-1]

            if 1 <= kolom_analisa <= len(df.columns):
                try:
                    opsi = int(input('''Pilihlah Opsi Dibawah :
        1. Membersihkan Data Dengan Menghapus Baris Sekaligus 
        2. Membersihkan Data Dengan Mengganti Nilai Yang Ditentukan
    Pilihlah Antara (1/2) : '''))
                    if opsi == 1:
                        df = df.dropna(subset=[nama_kolom_analisa])
                        df.to_csv(lokasi_file, index=False)
                        print(df.to_string())
                    elif opsi == 2:
                        nilai_baru = input("Masukkan Nilai Pengganti : ")
                        df[nama_kolom_analisa] = df[nama_kolom_analisa].fillna(nilai_baru)
                        df.to_csv(lokasi_file, index=False)
                        print(df.to_string())
                    else:
                        print('Pilihan Hanya (1/2) ...')
                except ValueError:
                    print("Pilihan Hanya Berupa Angka ...")
            else:
                print("Kolom Tidak Sesuai")
        except FileNotFoundError:
            print(f'File Bernama {nama_file} Tidak Ditemukan.')

    # Bagian Perhitungan Profit ================================
    def Calculate_Profit(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("="*100)
        print(f"{"== Hitung Laba Bersih Anda Disini =="}")
        print("="*100)

        try:
            nama_file = input('Masukkan Nama File Disini : ').lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            df_numerik = df.select_dtypes(include=['number'])
            print("="*100)
            print(df_numerik)
            print(f"{"="*100}\n")
            try:
                opsi = int(input('''Pilihlah Opsi Dibawah Ini
            1. Hitung Total Penjualan Dari Jumlah Produk Terjual X Harga Satuan
            2. Hitung Keuntungan Bersih
        Pilih Antara (1/2) : '''))
                if opsi == 1:
                    kolom_produk = int(input('Pilih Nomor Kolom Jumlah Produk Terjual : '))
                    harga_satuan = int(input('Pilih Nomor Kolom Harga Satuan          : '))
                    if 1 <= kolom_produk <= len(df_numerik.columns) and 1 <= harga_satuan <= len(df_numerik.columns):
                        df["Total_Keuntungan"] = df_numerik.iloc[:,(kolom_produk - 1)] * df_numerik.iloc[:,(harga_satuan - 1)]
                        df.to_csv(lokasi_file, index=False)
                        print("="*100)
                        print(df.to_string())
                        print("="*100)
                    else:
                        print(f"Kolom Hanya {len(df_numerik.columns)}")
                elif opsi == 2:
                    print("-"*100)
                    Total_Pemasukan   = int(input('Masukkan Total Pemasukkan  : '))
                    Total_Pengeluaran = int(input('Masukkan Total Pengeluaran : '))
                    laba_bersih = Total_Pemasukan - Total_Pengeluaran
                    print("-"*100)
                    print(laba_bersih)
                    print("-"*100)
                else:
                    print("Pilihan Hanya (1/2) ...")
            except ValueError:
                print("Pilihan Hanya Berupa Angka ...")    
        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan.")

    # Bagian Filter Keuntungan ================================
    def View_Product_above_50(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        print("="*100)
        print(f"{"== Produk Terjual Diatas 50 % ==":^100}")
        print("="*100)

        try:
            nama_file = input("Masukkan Nama File Disini : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)

            df_numerik = df.select_dtypes(include=['number'])
            print("="*100)
            print(df_numerik)
            print("="*100)
            pilihan_kolom1 = int(input("Pilihlah Nomer Kolom Stock Produk Awal    : "))
            pilihan_kolom2 = int(input("Pilihlah Nomer Kolom Stock Produk Terjual : "))

            if 1 <= pilihan_kolom1 <= len(df_numerik.columns) and 1 <= pilihan_kolom2 <= len(df_numerik.columns):
                Nilai_tengah = df_numerik.iloc[:,(pilihan_kolom1 - 1)] / 2
                print(f"\n{"="*100}")
                print(f"{"== Penjualan Produk Diatas 50 % ==":^100}")
                print(f"{"="*100}\n")
                df_filter_diatas_50 = df[(df_numerik.iloc[:,(pilihan_kolom2 - 1)] > Nilai_tengah)]
                print(df_filter_diatas_50)

                print(f"\n{"="*100}")
                print(f"{"== Penjualan Produk Dibawah 50 % ==":^100}")
                print(f"{"="*100}\n")
                df_filter_dibawah_50 = df[(df_numerik.iloc[:,(pilihan_kolom2 - 1)] < Nilai_tengah)]
                print(df_filter_dibawah_50)
            else:
                print(f"Kolom Hanya {len(df_numerik.columns)}")
        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan ...")
            

    # Bagian Kategori Produk ================================
    def View_Product_Category(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        print("="*100)
        print(f"{"== Hitung Rata_rata Produk Berdasarkan Jenis/Kategori Produk ==":^100}")
        print("="*100)

        try:
            nama_file = input("Masukkan Nama File Disini : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            print('-'*100)
            print(df)
            print('-'*100)
            kolom_jenis   = int(input('Pilih Nomor Kolom Jenis/Kategori Produk : '))
            kolom_Terjual = int(input('Pilih Nomor Kolom Jumlah Produk Terjual : '))
            if 1 <= kolom_jenis <= len(df.columns) and 1 <= kolom_Terjual <= len(df.columns):
                group = df.groupby(df.columns[kolom_jenis -1])[df.columns[kolom_Terjual -1]].mean().sort_values(ascending=False)
                print('-'*100)
                print(group.to_string())
                print('-'*100)
            else:
                print(f"Kolom Hanya {len(df.columns)}")
        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan ...")

def main_analisis():
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("="*100)
        print(f"{"== Analisis Data Kamu Disini ==":^100}")
        print("="*100)

        try:
            opsi_awal = int(input('''Pilihlah Opsi Dibawah Untuk Memulai Analisa
    1. Pembersihan Data
    2. Hitung Keuntungan Penjualan
    3. Lihat Produk Terjual Diatas Dan Dibawah 50%
    4. Lihat Rata-Rata Keuntungan Produk Dari Kategori/Jenis Produk
Pilihlah Antara (1/2/3/4) : '''))
            
            if opsi_awal == 1:
                user = Analysis_Class()
                user.Cleaning_Data()

            elif opsi_awal == 2:
                user = Analysis_Class()
                user.Calculate_Profit()

            elif opsi_awal == 3:
                user = Analysis_Class()
                user.View_Product_above_50()

            elif opsi_awal == 4:
                user = Analysis_Class()
                user.View_Product_Category()

            else:
                print("Pilihan Hanya Berupa (1/2/3/4) ...")

        except ValueError:
            print("Pilihan Hanya Berupa Angka ...")

        try:
            opsi_akhir = input("Apakah anda ingin melanjutkan (y/n) : ").lower()
            if opsi_akhir == 'n':
                break
        except ValueError:
            print("Pilihan Hanya (y/n) ...")
            break

    print("="*100)
    print(f"{"== Goodbye ==":^100}")
    print("="*100)