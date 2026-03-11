import matplotlib.pyplot as plt
import pandas as pd
import os

class VISUALISASI:
    def __init__(self):
        pass

    def garis(self):
        try:
            nama_file = input("Masukkan Nama File Untuk Visualisasi Data : ").lower()
            lokasi_folder = f"Project_Visualisasi\Database_\{nama_file}"
            df = pd.read_csv(lokasi_folder)
            df_view = df.copy()
            print("="*100)
            print(df_view.to_string())
            print("="*100)
            nomor_kolom_x = int(input("Pilih Nomer Kolom Sebagai Sumbu X : "))
            nomor_kolom_y = int(input("Pilih Nomer Kolom Sebagai Sumbu Y : "))
            nama_kolom_x = df.columns[nomor_kolom_x - 1]
            nama_kolom_y = df.columns[nomor_kolom_y - 1]
            x = df[nama_kolom_x]
            y = df[nama_kolom_y]
            Judul = input("Masukkan Judul Diagram : ")
            plt.grid(linestyle="dashed")
            plt.title(Judul,fontsize=20)
            plt.plot(x,y,
                     marker=".",
                     markersize=20,
                     color="#45f54a",
                     linestyle="solid",
                     linewidth=2)
            plt.show()

        except FileNotFoundError:
            print("file tidak ditemukan")
            exit()

    def batang(self):
        try:
            nama_file = input("Masukkan Nama File Untuk Visualisasi Data : ").lower()
            lokasi_folder = f"Project_Visualisasi\Database_\{nama_file}"
            df = pd.read_csv(lokasi_folder)
            df_view = df.copy()
            print("="*100)
            print(df_view.to_string())
            print("="*100)
            nomor_kolom_x = int(input("Pilih Nomer Kolom Sebagai Sumbu X : "))
            nomor_kolom_y = int(input("Pilih Nomer Kolom Sebagai Sumbu Y : "))
            nama_kolom_x = df.columns[nomor_kolom_x - 1]
            nama_kolom_y = df.columns[nomor_kolom_y - 1]
            x = df[nama_kolom_x]
            y = df[nama_kolom_y]
            Judul = input("Masukkan Judul Diagram : ")
            plt.grid(linestyle="dashed")
            plt.title(Judul,fontsize=20)
            plt.bar(x,y,
                     color="#45f54a")
            plt.show()

        except FileNotFoundError:
            print("file tidak ditemukan")
            exit()

    def Lingkaran(self):
        try:
            nama_file = input("Masukkan Nama File Untuk Visualisasi Data : ").lower()
            lokasi_folder = f"Project_Visualisasi\Database_\{nama_file}"
            df = pd.read_csv(lokasi_folder)
            df_view = df.copy()
            print("="*100)
            print(df_view.to_string())
            print("="*100)
            x = int(input("Pilih Nomer Kolom Sebagai Kategori/Value : "))
            y = int(input("Pilih Nomer Kolom Sebagai Percentage/Index : "))
            nama_value = df.columns[x - 1]
            nama_index = df.columns[y - 1]
            value = df[nama_value]
            index = df[nama_index]
            Judul = input("Masukkan Judul Diagram : ")
            plt.grid(linestyle="dashed")
            plt.title(Judul,fontsize=20)
            plt.pie(index,labels=value,
                    autopct="%1.1f%%")
            plt.show()

        except FileNotFoundError:
            print("file tidak ditemukan")
            exit()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*100)
        print(f"{"=== VISUALISASI DATA DISINI ===":^100}")
        print("="*100)
        try:
            opsi_awal = int(input('''Pilih Diagram Dibawah : 
    1. Diagram Garis
    2. Diagram Batang
    3. Diagram Lingkaran
Pilih Antara (1/2/3) : '''))
            
            if opsi_awal == 1:
                user = VISUALISASI()
                user.garis()

            elif opsi_awal == 2:
                user = VISUALISASI()
                user.batang()

            elif opsi_awal == 3:
                user = VISUALISASI()
                user.Lingkaran()
            
        except ValueError:
            print("Pilihan Hanya Berupa Angka")
            exit()
        
        opsi_akhir = input("Apakah Anda Ingin Melanjutkan ? (y/n) : ").lower()
        if opsi_akhir == 'n':
            break

    print("="*100)
    print(f"{"=== VISUALISASI DATA DISINI ===":^100}")
    print("="*100)