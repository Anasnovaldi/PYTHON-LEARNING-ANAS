import os
import pandas as pd
import csv
import Analysis

if __name__ == "__main__":
    class Main:
        def __init__(self):
            pass

        def Create(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*100)
            list_kolom = []
            nama_file = input("Masukkan Nama File Disini (Contoh: Datasiswa.csv) : ").lower()
            try:
                jumlah_kolom = int(input("Masukkan Jumlah Kolom Disini : "))
                for i in range(jumlah_kolom):
                    kolom = input(f"Masukkan Nama Kolom Ke-{i+1} : ")
                    list_kolom.append(kolom)
                lokasi_file = f"Database_/{nama_file}"

                with open(lokasi_file, "w", newline="") as file:
                    content = csv.writer(file)
                    content.writerow(list_kolom)
                    print(f"\n{"="*100}")
                    print(f"{"=== FILE CREATED SUCCESSFULLY ===":^100}")

            except ValueError:
                print("Number Only Options")
            except FileExistsError:
                print("File Sudah Tersedia")

        def Manipulation(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-" * 100)

            try:
                nama_file = input("Masukkan Nama File Disini (Contoh: Datasiswa.csv) : ").lower()
                lokasi_file = f'Database_/{nama_file}'
                df = pd.read_csv(lokasi_file)
                opsi_awal = int(input('''Pilihlah Opsi Dibawah :
    1. Menambahkan Isi File
    2. Menghapus Isi File
    3. Mengubah Isi File
    4. Melihat Isi File
Pilih Antara (1/2/3/4) : '''))

                if opsi_awal == 1:
                    list_baris = []
                    with open(lokasi_file, "r", encoding='utf-8') as file:
                        content = csv.reader(file)
                        kolom = next(content)
                    
                    for k in kolom:
                        baris = input(f"Masukkan Isi Kolom {k} : ")
                        list_baris.append(baris)

                    with open(lokasi_file, 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(list_baris)
                    print("== Berhasil Menambahkan Ke Dalam File ==")

                elif opsi_awal == 2:
                    opsi_hapus = int(input('''Pilihlah Opsi Dibawah Ini :
    1. Hapus Kolom
    2. Hapus Baris
Pilih Antara(1/2) : '''))       
                    if opsi_hapus == 1:
                        self.Lihat(nama_file)
                        print("="*100)
                        nomor_kolom = int(input("Pilih Nomor Kolom : "))
                        if 1 <= nomor_kolom <= len(df.columns):
                            nama_kolom = df.columns[nomor_kolom-1]
                            df = df.drop(nama_kolom, axis=1)
                            df.to_csv(lokasi_file, index=False)
                            df_view = df.copy()
                            df_view.index = df_view.index + 1
                            print(df_view.to_string())
                        else:
                            print(f"Kolom Hanya {df.columns}")
                    elif opsi_hapus == 2:
                        self.Lihat(nama_file)
                        print("="*100)
                        nomor_baris = int(input("Pilih Nomor Baris : "))
                        if 1 <= nomor_baris <= len(df.index):
                            index_baris = df.index[nomor_baris - 1]
                            df.drop(index_baris, axis=0, inplace=True)
                            df.to_csv(lokasi_file, index=False)
                            df_view = df.copy()
                            df_view.index = df_view.index + 1
                            print(df_view.to_string())
                        else:
                            print(f"Baris Hanya {df.index+1}")
                    else:
                        print("Pilihan Hanya (1/2) !!")

                elif opsi_awal == 3:
                    self.Lihat(nama_file)
                    print("="*100)
                    nomor_kolom = int(input("Pilih Nomor Kolom : "))
                    nomor_baris = int(input("Pilih Nomor Baris : "))
                    print("="*100)
                    df.iloc[(nomor_baris-1), (nomor_kolom-1)] = input(f"Masukkan Isi Dari Kolom {df.columns[nomor_kolom-1]} : ")
                    df.to_csv(lokasi_file, index=False)
                    df_view = df.copy()
                    df_view.index = df_view.index + 1
                    print(df_view.to_string())

                elif opsi_awal == 4:
                    self.Lihat(nama_file)

                else:
                    print("Choice Only (1/2/3/4)")

            except ValueError:
                print("Number Only Options")
                return
            except FileNotFoundError:
                print(f"Error: File '{nama_file}' tidak ditemukan di folder Database_!")
                print("-" * 100)
        
        def Lihat(self,nama_file):
            try:
                lokasi_file = f"Database_/{nama_file}"
                df = pd.read_csv(lokasi_file)
                print("="*100)
                df_view = df.copy()
                df_view.index = df_view.index + 1
                print(df_view.to_string())
                print(f"{"="*100}\n")
            except FileNotFoundError:
                print("FIle Tidak Ditemukan !!")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        print(f"{"== THIS PROJECT FOR TEACHER TO NOTE HER STUDENT ==":^100}")
        print("="*100)
        try:
            opsi_awal = int(input('''Choose Your Option
    1. Buat File
    2. Manipulasi Isi File
    3. Lihat Insight File
Choose between (1/2/3) : '''))
            if opsi_awal == 1:
                user = Main()
                user.Create()
            elif opsi_awal == 2:
                user = Main()
                user.Manipulation()
            elif opsi_awal == 3:
                Analysis.main()
            else:
                print("Choice Only (1/2/3)")
        except ValueError:
            print("Number Only Options")

        opsi_lanjutan = input("do you want to continue (y/n) : ").lower()
        if opsi_lanjutan == 'n':
            break
    print("="*100)
    print(f"{"== SEE YOU AGAIN !! ==":^100}")
    print("="*100)