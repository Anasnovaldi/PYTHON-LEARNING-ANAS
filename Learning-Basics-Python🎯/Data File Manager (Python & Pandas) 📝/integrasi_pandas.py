import os
import pandas as pd
import csv
import analisis as analis

while True:
    os.system('cls')
    print("="*70)
    print(f"{"== MINI PROJECT WITH PANDAS ==":^70}")
    print("="*70)

    opsi_awal = int(input('''Pilihlah Opsi Dibawah Ini : 
    1. Membuat File Baru
    2. Menambahkan Isi File Yang Tersedia
    3. Melihat File Yang Tersedia 
    4. Analisis Sederhana
Pilih Antara (1/2/3/4) : '''))
    
    if opsi_awal == 1:
        list_dataframe = []
        list_kolom = []
        
        nama_file    =     input("Masukkan Nama File    : ").lower()
        jumlah_kolom = int(input("Masukkan Jumlah Kolom : "))
        for i in range(jumlah_kolom):
            kolom = input(f"Masukkan Nama Kolom Ke {i+1} : ")
            list_kolom.append(kolom)
        list_dataframe.append(list_kolom)

        try:
            with open(nama_file, 'w', newline='') as file:
                content = csv.writer(file)
                for i in list_dataframe:
                    content.writerow(i)
                print(f"File Bernama {nama_file} Berhasil Dibuat")
                print("-"*70)
        except FileExistsError:
            print("File Sudah Dibuat")

    elif opsi_awal == 2:
        try:
            list_baris = []
            nama_file = input("Masukkan Nama File    : ").lower()
            with open(nama_file, 'r', encoding='utf-8') as file:
                content = csv.reader(file)
                header = next(content)
                jumlah_kolom = len(header)

            for i in range(jumlah_kolom):
                baris = input(f"Masukkan Isi Baris Pada Kolom '{header[i]}' : ")
                list_baris.append(baris)
            
            with open(nama_file, 'a', newline='', encoding='utf-8') as file:
                content = csv.writer(file)
                content.writerow(list_baris)
            print("-"*70)
            print("Berhasil Ditambahkan")
        
        except FileNotFoundError:
            print("File Tidak Ditemukan.")

    elif opsi_awal == 3:
        try:
            nama_file = input("Masukkan Nama File    : ").lower()
            os.system('cls')
            print('='*70)
            df = pd.read_csv(nama_file)
            print(df.to_string())
            print('='*70)

        except FileNotFoundError:
            print("File Tidak Ditemukan.")

    elif opsi_awal == 4:
        analis.analisis()

    opsi_akhir = input("Apakah anda ingn melanjutkan (y/n) : ").lower()
    if opsi_akhir == 'n':
        break

print("="*70)
print(f"{"== MINI PROJECT WITH PANDAS ==":^70}")
print("="*70)