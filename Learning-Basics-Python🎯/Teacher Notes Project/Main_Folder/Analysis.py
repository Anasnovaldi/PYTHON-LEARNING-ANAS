import pandas as pd
import csv
import os

class Analyst:
    def __init__(self):
        pass

    def Sort(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini (Contoh: Datasiswa.csv) : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            self.Lihat(nama_file)
            opsi_sort = int(input('''Pilihlah Jenis Urutan Data
    1. Berdasarkan Abjad (Example : Name A-Z)
    2. Berdasarkan Angka (Example : X >> X)
Pilih Antara (1/2) : '''))
            
            if opsi_sort == 1:
                nomor_kolom = int(input("Masukkan Nomor Kolom Untuk Diurutkan : "))
                df = pd.read_csv(lokasi_file)
                nama_kolom = df.columns[nomor_kolom-1]
                if 1 <= nomor_kolom <= len(df.columns):
                    df = df.sort_values(by=nama_kolom, ascending=True)
                    df_view = df.copy()
                    df_view.index = df_view.index + 1
                    print(df_view.to_string())
                else:
                    print(f"Kolom Hanya {len(df.columns)}")

            elif opsi_sort == 2:
                nomor_kolom = int(input("Masukkan Nomor Kolom Untuk Diurutkan : "))
                df = pd.read_csv(lokasi_file)
                if 1 <= nomor_kolom <= len(df.columns):
                    df = df.sort_values(by=df.columns[nomor_kolom-1], ascending=False)
                    df_view = df.copy()
                    df_view.index = df_view.index + 1
                    print(df_view.to_string())
                else:
                    print(f"Kolom Hanya {len(df.columns)}")

            else:
                print("Choice Only (1/2)")
        except ValueError:
            print("Number Only")
        except FileNotFoundError:
            print(f"File {nama_file} Not Found")

    def Mean_Values(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        try:
            nama_file = input("Masukkan Nama File Disini (Contoh: Datasiswa.csv) : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            self.Lihat(nama_file)
            list_kolom = []
            jumlah_kolom = int(input("Masukkan Jumlah Kolom Untuk Dihitung : "))
            for i in range(jumlah_kolom):
                kolom = int(input(f"Masukkan Nomor Kolom Ke {i+1} : "))-1
                list_kolom.append(kolom)

            kolom_dipilih = [df.columns[i] for i in list_kolom]
            df["Nilai_rata_rata"] = df[kolom_dipilih].mean(axis=1)
            df.to_csv(lokasi_file, index=False)
            print(df.to_string())
            
        except ValueError:
            print("Number Only")
        except FileNotFoundError:
            print(f"File {nama_file} Not Found")

    def Filterization(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='*100)
        try:
            nama_file = input("Masukkan Nama File Disini (Contoh: Datasiswa.csv) : ").lower()
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            opsi_filter = int(input('''Pilihlah Opsi Dibawah
    1. Filter Berdasarkan Kategori Tertentu (Example: Gender = Male)
    2. Filter Berdasarkan Nilai Tertentu (Example: X<90)
Pilih Antara (1/2) : '''))
            
            if opsi_filter == 1:
                print(f"\n{"="*100}")
                print(df.to_string())
                nomor_kolom = int(input("Masukkan Nomor Kolom : "))
                nama_kolom = df.columns[nomor_kolom-1]
                if 1 <= nomor_kolom <= len(df.columns):
                    kategori = input("Masukkan Kategori Yang Sesuai : ")
                    df_filter = df[(df[nama_kolom] == kategori)]
                    print(df_filter.to_string())
                else:
                    print(f"Kolom Hanya {len(df.columns)}")

            elif opsi_filter == 2:
                print(f"\n{"="*100}")
                print(df.to_string())
                nomor_kolom = int(input("Masukkan Nomor Kolom : "))
                nama_kolom = df.columns[nomor_kolom-1]
                if 1 <= nomor_kolom <= len(df.columns):
                    opsi_pembanding = int(input('''Pilihlah Opsi Pembanding
    1. Nilai Kurang Dari (<)
    2. Nilai Lebih Dari (>)
    3. Nilai Sama Dari (=)
Pilih Antara (1/2/3) : '''))
                    if opsi_pembanding == 1:
                        nilai_pembanding = int(input("Masukkan Nilai Pembanding : "))
                        df_filter = df[(df[nama_kolom] < nilai_pembanding)]
                        print(df_filter.to_string())
                    elif opsi_pembanding == 2:
                        nilai_pembanding = int(input("Masukkan Nilai Pembanding : "))
                        df_filter = df[(df[nama_kolom] > nilai_pembanding)]
                        print(df_filter.to_string())
                    elif opsi_pembanding == 3:
                        nilai_pembanding = int(input("Masukkan Nilai Pembanding : "))
                        df_filter = df[(df[nama_kolom] == nilai_pembanding)]
                        print(df_filter.to_string())
                    else:
                        print(f"Kolom Hanya {len(df.columns)}")

                else:
                    print(f"Kolom Hanya {len(df.columns)}")
            else:
                print("Choice Only (1/2)")

        except ValueError:
            print("Number Only")
        except FileNotFoundError:
            print(f"File {nama_file} Not Found")

    def Lihat(self,nama_file):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        try:
            lokasi_file = f'Database_/{nama_file}'
            df = pd.read_csv(lokasi_file)
            df_view = df.copy()
            df_view.index = df_view.index + 1
            print(df_view.to_string())
        except FileNotFoundError:
            print(f"File {nama_file} Not Found")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        print(f"{"== THIS PROJECT FOR TEACHER TO NOTE HER STUDENT ==":^100}")
        print("="*100)
        try:
            opsi_awal = int(input('''Choose Your Option
    1. Urutkan Siswa Berdasarkan Nilai Ataupun Abjad
    2. Hitung Rata-Rata Nilai Siswa
    3. Filter Kriteria Siswa
Choose between (1/2/3) : '''))
            if opsi_awal == 1:
                user = Analyst()
                user.Sort()
            elif opsi_awal == 2:
                user = Analyst()
                user.Mean_Values()
            elif opsi_awal == 3:
                user = Analyst()
                user.Filterization()
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