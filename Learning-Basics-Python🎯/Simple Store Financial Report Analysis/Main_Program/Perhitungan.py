import os
import pandas as pd

class Analyst:
    def __init__(self):
        pass

    def Keuntungan_Produk(self):
        os.system('cls') or os.system('clear')
        print("="*100)
        print(f"{"== PERHITUNGAN ==":^100}")
        print("="*100)

        try:
            nama_file = input("Masukkan Nama File : ").lower()
            lokasi_folder = f'data/{nama_file}'
            
            df = pd.read_csv(lokasi_folder)
            df_numerik = df.select_dtypes(include=['number'])

            if df_numerik.empty:
                print("Tidak Ada Kolom Yang Bertipe Numerik.")
                return
            
            print(f'\n{"="*100}')
            print(df_numerik)
            print(f'{"="*100}\n')

            try:
                pilihan_kolom1 = int(input("Pilihlah Nomer Kolom Jumlah Produk Yang Terjual       : "))
                pilihan_kolom2 = int(input("Pilihlah Nomer Kolom Harga Satuan Produk Yang Terjual : "))

                if 1 <= pilihan_kolom1 <= len(df_numerik.columns) and 1 <= pilihan_kolom2 <= len(df_numerik.columns):
                    os.system('cls') or os.system('clear')
                    print("="*100)
                    df['Total_Keuntungan_Produk'] = df_numerik.iloc[:,(pilihan_kolom1 - 1)] * df_numerik.iloc[:,(pilihan_kolom2 - 1)]
                    df.to_csv(lokasi_folder, index=False)
                    print(df.to_string())
                    print("="*100)
                    print(f"Total Keuntungan Seluruh Produk = {df['Total_Keuntungan_Produk'].sum()}")
                    print("="*100)
                else:
                    print(f"Jumlah Kolom Hanya {len(df_numerik.columns)} !!!")
            except ValueError:
                print("Masukkan Hanya Berupa Angka")

        except FileNotFoundError:
            print(f"File Bernama {nama_file} Tidak Ditemukan.")
    def Produk_Statistik(self):
        os.system('cls') or os.system('clear')
        print("="*100)
        print(f"{"== PERHITUNGAN ==":^100}")
        print("="*100)
        
        try:
            nama_file = input("Masukkan Nama File : ").lower()
            lokasi_folder = f'data/{nama_file}'
            
            df = pd.read_csv(lokasi_folder)
            df_numerik = df.select_dtypes(include=['number'])

            if df_numerik.empty:
                print("Tidak Ada Kolom Yang Bertipe Numerik.")
                return
            
            print(f'\n{"="*100}')
            print(df_numerik)
            print(f'{"="*100}\n')

            try:
                pilihan_kolom1 = int(input("Pilihlah Nomer Kolom Stock Produk Awal    : "))
                pilihan_kolom2 = int(input("Pilihlah Nomer Kolom Stock Produk Terjual : "))

                if 1 <= pilihan_kolom1 <= len(df_numerik.columns) and 1 <= pilihan_kolom2 <= len(df_numerik.columns):
                    os.system('cls') or os.system('clear')
                    produk_persentase_50 = df_numerik.iloc[:,(pilihan_kolom1 - 1)] / 2
                    print("="*100)
                    print(f"{"== Produk Terjual Diatas 50% ==":^100}")
                    print("="*100)
                    df_filter = df[(df_numerik.iloc[:,(pilihan_kolom2 - 1)] > produk_persentase_50)]
                    print(df_filter.to_string())

                    print(f"\n{"="*100}")
                    print(f"{"== Produk Terjual Dibawah/Sama Dengan 50% ==":^100}")
                    print("="*100)
                    df_filter = df[(df_numerik.iloc[:,(pilihan_kolom2 - 1)] <= produk_persentase_50)]
                    print(df_filter.to_string())
                else:
                    print(f"Jumlah Kolom Hanya {len(df_numerik.columns)}")
            except ValueError:
                print("Masukkan Hanya Berupa Angka.")
        except FileNotFoundError:
            print(f"FIle Bernama {lokasi_folder} Tidak Ditemukan.")


def main_perhitungan():
    while True:
        os.system('cls') or os.system('clear')
        print("="*100)
        print(f"{"== PERHITUNGAN ==":^100}")
        print("="*100)

        try:
            opsi_awal = int(input('''Pilihlah Tindakan
    1. Hitung Total Keuntungan Setiap Produk
    2. Lihat Produk Yang Terjual Kurang/Lebih Dari 50% 
Pilih Antara (1/2) : '''))
        
            if opsi_awal == 1:
                hitung = Analyst()
                hitung.Keuntungan_Produk()
            elif opsi_awal == 2:
                hitung = Analyst()
                hitung.Produk_Statistik()
            else:
                print("Pilihan Hanya (1/2) !")
        except ValueError:
            print("Masukkan Hanya Berupa Angka.")

        opsi_akhir = input("Apakah anda ingin melanjutkan (y/n) : ").lower()
        if opsi_akhir == 'n':
            break

    print("="*100)
    print(f"{"== PERHITUNGAN ==":^100}")
    print("="*100)