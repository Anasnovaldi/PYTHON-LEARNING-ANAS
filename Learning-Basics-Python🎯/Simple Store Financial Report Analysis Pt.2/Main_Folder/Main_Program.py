import pandas as pd
import os
import csv
import Analysis

if __name__ == "__main__":
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
        print("="*100)
        print(f"{"== PROJECT TOKO RETAIL PART 2 ==":^100}")
        print("="*100)

        try:
            opsi_awal = int(input('''Pilih Opsi Dibawah
    1. Membuat File
    2. Menambahkan Isi File
    3. Melihat Isi File
    4. Analisis Data
Pilih Antara (1/2/3/4) : '''))
            
            if opsi_awal == 1:
                list_dataframe = []
                list_kolom = []
                nama_file    = input("Masukkan Nama File CSV Disini : ")
                jumlah_kolom = int(input("Masukkan Jumlah Kolom Disini  : "))
                for i in range(jumlah_kolom):
                    kolom = input(f"Masukkan Nama Kolom Ke-{i+1} : ")
                    list_kolom.append(kolom)
                list_dataframe.append(list_kolom)
                
                lokasi_folder = f"Database_/{nama_file}"

                try:
                    with open (lokasi_folder, 'w', newline='') as file:
                        content = csv.writer(file)
                        for i in list_dataframe:
                            content.writerow(i)
                        print('='*100)
                        print(f"File Bernama {nama_file} Berhasil Dibuat")
                except FileExistsError:
                    print("File Sudah Dibuat.")

            elif opsi_awal == 2:
                try:
                    list_baris = []
                    nama_file = input("Masukkan Nama File CSV Disini : ")
                    lokasi_folder = f"Database_/{nama_file}"
                    with open (lokasi_folder, 'r', encoding='utf-8') as file:
                        content = csv.reader(file)
                        kolom = next(content)
                        jumlah_kolom = len(kolom)

                    for i in range(jumlah_kolom):
                        baris = input(f"Masukkan Isi Kolom {kolom[i]} : ")
                        list_baris.append(baris)

                    with open(lokasi_folder, 'a', newline='') as file:
                        content = csv.writer(file)
                        content.writerow(list_baris)
                        print("="*100)
                        print("Berhasil Menambahkan Baris")
                
                except FileNotFoundError:
                    print("File Tidak Ditemukan.")

            elif opsi_awal == 3:
                try:
                    nama_file = input("Masukkan Nama File CSV Disini : ")
                    lokasi_folder = f'Database_/{nama_file}'
                    df = pd.read_csv(lokasi_folder)
                    print(f"\n{"="*100}")
                    print(df.to_string())
                    print("="*100)
                except FileNotFoundError:
                    print("File Tidak Ditemukan.")

            elif opsi_awal == 4:
                Analysis.main_analisis()
            else:
                print("Pilihan Hanya Empat Pilihan.")

        except ValueError:
            print("Pilihan Hanya Berupa Angka .. !!")

        try:
            opsi_akhir = input("Apakah Anda Ingin Melanjutkan (y/n) : ").lower()
            if opsi_akhir == 'n':
                break
        except ValueError:
            print("Pilihan Hanya (y/n) .. !!")
            break

print("="*100)
print(f"{"== PROJECT TOKO RETAIL PART 2 ==":^100}")
print("="*100)