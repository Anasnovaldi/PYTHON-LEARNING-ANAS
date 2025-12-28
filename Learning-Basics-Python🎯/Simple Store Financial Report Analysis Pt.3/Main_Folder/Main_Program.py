import os
import pandas as pd
import csv
import Analysis

if __name__ == '__main__':
    class Pilihan():
        def __init__(self):
            pass
        
        def Membuat_File(self):
            list_kolom = []
            nama_file        = input("Masukkan Nama File CSV Disini : ").lower()
            jumlah_kolom = int(input("Masukkan Jumlah Kolom Disini  : "))
            for i in range(jumlah_kolom):
                kolom = input(f"Masukkan Nama Kolom Ke-{i+1} : ")
                list_kolom.append(kolom)
            lokasi_file = f"Database_/{nama_file}"

            try:
                with open(lokasi_file, 'w', newline='') as file:
                    content = csv.writer(file)
                    content.writerow(list_kolom)
                    print('='*100)
                    print(f"File Bernama {nama_file} Berhasil Dibuat")
            except FileExistsError:
                print("File Sudah Dibuat.")
                exit()

        def Manipulasi_File(self):
            try:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print(f"\n{"-"*100}")
                opsi_awal = int(input('''Pilihlah Opsi Untuk Manipulasi File CSV
    1. Menambahkan Isi File CSV
    2. Menghapus Isi File CSV
    3. Mengubah Isi File CSV
    4. Melihat Isi File CSV
Pilih Antara (1/2/3/4) : '''))
                
                if opsi_awal == 1 :
                    try:
                        list_baris = []
                        nama_file = input("Masukkan Nama File CSV Disini : ").lower()
                        lokasi_file = f"Database_/{nama_file}"

                        with open(lokasi_file, 'r', encoding='utf-8') as file:
                            content = csv.reader(file)
                            kolom = next(content)
                            panjang_kolom = len(kolom)

                        for i in range(panjang_kolom):
                            baris = input(f"Masukkan Isi Kolom {kolom[i]} : ")
                            list_baris.append(baris)

                        with open(lokasi_file, 'a', newline='') as file:
                            content = csv.writer(file)
                            content.writerow(list_baris)
                            print("="*100)
                            print("Isi File Berhasil Dibuat")
                    except FileNotFoundError:
                        print(f"File Bernama {nama_file} Tidak Ditemukan")
                        exit()
            
                elif opsi_awal == 2 :
                    try:
                        try:
                            nama_file = input("Masukkan Nama File CSV Disini : ").lower()
                            lokasi_file = f"Database_/{nama_file}"
                            df = pd.read_csv(lokasi_file)
                            print("="*100)
                            df_view = df.copy()
                            df_view.index = df_view.index + 1
                            print(df_view.to_string())
                            print(f"{"="*100}\n")
                        except FileNotFoundError:
                            print(f"File Bernama {nama_file} Tidak Ditemukan")
                            exit()
                        
                        pilihan = int(input('''Pilihlah Opsi Dibawah Ini
    1. Hapus Kolom
    2. Hapus Baris
Pilih Antara (1/2) : '''))
                        if pilihan == 1:
                            pilih_kolom = int(input("Pilih Nomor Kolom Untuk Dihapus : "))
                            nama_kolom = df.columns[pilih_kolom-1]
                            df = df.drop(nama_kolom,axis=1)
                            df.to_csv(lokasi_file, index=False)
                            print("="*100)
                            df_view = df.copy()
                            df_view.index = df_view.index + 1
                            print(df_view.to_string())
                        elif pilihan == 2:
                            pilih_baris = int(input("Pilih Nomor Baris Untuk Dihapus : "))
                            index_baris = df.index[pilih_baris - 1]
                            df.drop(index_baris, axis=0, inplace=True)
                            df.to_csv(lokasi_file, index=False)
                            print("="*100)
                            df_view = df.copy()
                            df_view.index = df_view.index + 1
                            print(df_view.to_string())
                        else:
                            print("Pilihan Hanya (1/2)...")
                    except ValueError:
                        print(f"Pilihan Berupa Angka !!")
                        exit()

                elif opsi_awal == 3 :
                    try:
                        nama_file = input("Masukkan Nama File CSV Disini : ").lower()
                        lokasi_file = f"Database_/{nama_file}"
                        df = pd.read_csv(lokasi_file)
                        print("="*100)
                        df_view = df.copy()
                        df_view.index = df_view.index + 1
                        print(df_view.to_string())
                        print(f"{"="*100}\n")

                        pilih_kolom = int(input("Pilih Nomor Kolom Untuk Diubah : "))
                        pilih_baris = int(input("Pilih Nomor Baris Untuk Diubah : "))
                        print("="*100)
                        df.iloc[(pilih_baris - 1) , (pilih_kolom - 1)] = input(f"Masukkan Isi Dari Kolom {df.columns[pilih_kolom - 1]} : ")
                        df.to_csv(lokasi_file, index=False)
                        print("="*100)
                        df_view = df.copy()
                        df_view.index = df_view.index + 1
                        print(df_view.to_string())
                        
                    except FileNotFoundError:
                        print(f"File Bernama {nama_file} Tidak Ditemukan")
                        exit()

                elif opsi_awal == 4 :
                    self.Lihat()

            except ValueError:
                print("Pilihan Hanya Berupa Angka !!!")
                exit()

        def Lihat(self):
            try:
                nama_file = input("Masukkan Nama File CSV Disini : ").lower()
                lokasi_file = f"Database_/{nama_file}"
                df = pd.read_csv(lokasi_file)
                print("="*100)
                df_view = df.copy()
                df_view.index = df_view.index + 1
                print(df_view.to_string())
                print(f"{"="*100}\n")
            except FileNotFoundError:
                print(f"File Bernama {nama_file} Tidak Ditemukan")
                exit()

    # Main Program =================================
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("="*100)
        print(f"{"== PROJECT TOKO RETAIL PART 3 ==":^100}")
        print("="*100)
        
        try:
            opsi_awal = int(input('''Pilihlah Opsi Dibawah Ini
    1. Membuat File
    2. Manipulasi Isi File
    3. Analisis Data
Pilh Antara (1/2/3) : '''))
            
            if opsi_awal == 1:
                user = Pilihan()
                user.Membuat_File()

            elif opsi_awal == 2:
                user = Pilihan()
                user.Manipulasi_File()

            elif opsi_awal == 3:
                Analysis.main_analisis()
            else:
                print("Pilihan Hanya (1/2/3) !!")
        
        except ValueError:
            print("Pilihan Berupa Angka !!")
            exit()

        opsi_lanjutan = input("Apakah Anda Ingin Melanjutkan ? (y/n) : ")
        if opsi_lanjutan == 'n':
            break
    
    print("="*100)
    print(f"{"== PROJECT TOKO RETAIL PART 3 ==":^100}")
    print("="*100)