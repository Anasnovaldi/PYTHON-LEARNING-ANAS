import os
import numpy as np

class Weather:
    daftar_cuaca = []
    
    def __init__(self):
        print("Aplikasi Weather siap digunakan.")
        
    def Tambah(self):
        os.system('cls')
        print("="*100)
        data_wilayah = {}
        list_suhu = []
        list_nama_hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
        data_wilayah["nama_wilayah"] = input("Masukkan Nama Wilayah : ")
        for i in range(7):
            suhu_harian = int(input(f"Masukkan Suhu Hari Ke {i+1} : "))
            list_suhu.append(suhu_harian)

        suhu_awal = np.array(list_suhu)
        hari_suhu_tertinggi = np.argmax(suhu_awal)
        
        data_wilayah["rata_rata"] = np.mean(suhu_awal).round(2)
        data_wilayah["suhu_tertinggi"] = np.max(suhu_awal)
        data_wilayah["hari_suhu_tertinggi"] = list_nama_hari[hari_suhu_tertinggi]
        self.daftar_cuaca.append(data_wilayah)

        self.Lihat()

    def Lihat(self):
        os.system('cls')
        print("="*100)
        print(f"| {"NO":^5} | {"Wilayah":^14} | {"Suhu Tertinggi":^20} | {"Rata_Rata_Suhu":^20} | {"Hari":^20} |")
        print("-"*100)
        for i,data in enumerate(self.daftar_cuaca,start=1):
            print(f"| {i:^5} | {data['nama_wilayah']:^14} | {str(data['suhu_tertinggi']):^20} | {data['rata_rata']:^20} | {data['hari_suhu_tertinggi']:^20} |")
        print("="*100)

        suhu_tertinggi_global = -float('inf')
        kota_tertinggi = "N/A"
        hari_tertinggi = "N/A"

        for data in self.daftar_cuaca:
            if data['suhu_tertinggi'] > suhu_tertinggi_global:
                suhu_tertinggi_global = data['suhu_tertinggi']
                kota_tertinggi = data['nama_wilayah']
                hari_tertinggi = data['hari_suhu_tertinggi']

        print(f"Wilayah Dengan Suhu Tertinggi : {kota_tertinggi}")
        print(f"Suhu Tertinggi (Global)       : {suhu_tertinggi_global}")
        print(f"Hari Dengan Suhu Tertinggi    : {hari_tertinggi}")
        print("="*100)

    def Ubah(self):
        os.system('cls')
        self.Lihat()
        ubah = int(input("Masukkan Nomer Yang Ingin Dirubah : "))
        if ubah >= 1 <= len(self.daftar_cuaca):
            self.daftar_cuaca.pop(ubah - 1)
        else:
            print("Salah Input Bung")

        data_wilayah = {}
        list_suhu = []
        list_nama_hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
        data_wilayah["nama_wilayah"] = input("Masukkan Nama Wilayah : ")
        for i in range(7):
            suhu_harian = int(input(f"Masukkan Suhu Hari Ke {i+1} : "))
            list_suhu.append(suhu_harian)

        suhu_awal = np.array(list_suhu)
        hari_suhu_tertinggi = np.argmax(suhu_awal)
        
        data_wilayah["rata_rata"] = np.mean(suhu_awal).round(2)
        data_wilayah["suhu_tertinggi"] = np.max(suhu_awal)
        data_wilayah["hari_suhu_tertinggi"] = list_nama_hari[hari_suhu_tertinggi]
        self.daftar_cuaca.append(data_wilayah)

        self.Lihat()

    def Hapus(self):
        os.system('cls')
        self.Lihat()
        hapus = int(input("Masukkan Nomer Yang Ingin Dihapus : "))
        if hapus >= 1 <= len(self.daftar_cuaca):
            self.daftar_cuaca.pop(hapus - 1)
        else:
            print("Salah Input Bung")

        self.Lihat()