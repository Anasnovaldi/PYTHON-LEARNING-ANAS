import os
import pandas as pd
import csv
import Perhitungan

if __name__ == "__main__":
    while True:
        os.system('cls') or os.system('clear')
        print("="*100)
        print(f"{"== SIMPAN DAN ANALISIS PENJUALAN ==":^100}")
        print("="*100)

        try:        
            opsi_awal = int(input('''| Pilih Tindakan Dibawah Ini |
    1. Membuat File
    2. Menambahkan Isi File
    3. Lihat Isi File
    4. Hitung Pendapatan
Pilih Opsi Antara (1/2/3/4) : '''))

            if opsi_awal == 1:
                list_dataframe = []
                list_kolom = []
                nama_file = input("Masukkan Nama File : ").lower()
                jumlah_kolom = int(input("Masukkan Jumlah Kolom : "))
                for i in range(jumlah_kolom):
                    kolom = input(f"Masukkan Nama Kolom Ke {i+1} : ")
                    list_kolom.append(kolom)
                list_dataframe.append(list_kolom)

                lokasi_folder = f'data/{nama_file}'

                try:
                    with open(lokasi_folder, 'w', newline='') as file:
                        content = csv.writer(file)
                        for i in list_dataframe:
                            content.writerow(i)
                        print('='*100)
                        print(f"File Bernama {nama_file} Berhasil Dibuat.")
                except FileExistsError:
                    print("File Sudah Dibuat")

            elif opsi_awal == 2:
                try:
                    list_baris = []
                    nama_file = input("Masukkan Nama File : ").lower()
                    lokasi_folder = f'data/{nama_file}'

                    with open(lokasi_folder, 'r', encoding='utf-8') as file:
                        content = csv.reader(file)
                        header = next(content)
                        jumlah_kolom = len(header)

                    for i in range(jumlah_kolom):
                        baris = input(f"Masukkan Isi Kolom '{header[i]}' : ")
                        list_baris.append(baris)

                    with open(lokasi_folder, 'a', newline='') as file:
                        content = csv.writer(file) 
                        content.writerow(list_baris)
                        print("="*100)
                        print(f"Berhasil Menambahkan Isi Pada File {nama_file}")

                except FileNotFoundError:
                    print(f"File Bernama '{nama_file}' Tidak Ditemukan.")

            elif opsi_awal == 3:
                try:
                    nama_file = input("Masukkan Nama File : ").lower()
                    lokasi_folder = f'data/{nama_file}'
                    
                    print(f'\n{"="*100}')
                    df = pd.read_csv(lokasi_folder)
                    print(df.to_string())
                    print(f'{"="*100}\n')

                except FileNotFoundError:
                    print(f"File Bernama '{nama_file}' Tidak Ditemukan.")

            elif opsi_awal == 4:
                Perhitungan.main_perhitungan()

            else:
                print("Opsi Hanya (1/2/3/4).")
        
        except ValueError:
            print("Masukkan Hanya Berupa Angka.")

        opsi_akhir = input("Apakah Anda Ingin Melanjutkan (y/n) : ")
        if opsi_akhir == 'n':
            break

    print("="*100)
    print(f"{"== SIMPAN DAN ANALISIS PENJUALAN ==":^100}")
    print("="*100)