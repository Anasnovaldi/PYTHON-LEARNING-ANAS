import numpy as np
import os

class operasi:
    def __init__(self,nama,nilai_kkm,nilai_remed,nilai_keseluruan,nilai_rata_rata,nilai_tertinggi,nilai_terendah):
        self.nama = nama
        self.nilai_kkm = nilai_kkm
        self.nilai_remed = nilai_remed
        self.nilai_keseluruhan = nilai_keseluruan
        self.nilai_rata_rata = nilai_rata_rata
        self.nilai_tertinggi = nilai_tertinggi
        self.nilai_terendah = nilai_terendah

    def tambah_nilai(self):
        os.system('cls')
        print("="*130)
        print(f"| {'No':^5} | {"Nama":^14} | {"Nilai Diatas KKM":^17} | {"Nilai Remedial":^14} | {"Keseluruhan":^14} | {"Nilai Rata^2":^14} | {"Nilai Tertinggi":^15} | {"Nilai Terendah":^14} |")
        print("-"*130)
        for i,data in enumerate(daftar_data_siswa, start=1):
            print(f"| {i:^5} | {data['nama_siswa']:^14} | {str(data['nilai_diatas_kkm']):^17} | {str(data['nilai_remedial']):^14} | {str(data['nilai_keseluruhan']):^14} | {data['nilai_rata_rata']:^14} | {data['nilai_tertinggi']:^15} | {data['nilai_terendah']:^14} |")
        print("-"*130)

    def ubah_nilai(self,ubah):
        os.system('cls')
        if ubah >= 1 <= len(daftar_data_siswa):
            daftar_data_siswa.pop(ubah - 1)
        else:
            print('Salah Input Bung')

        data_siswa = {}
        list_nilai = []
        data_siswa['nama_siswa'] = input("Masukkan Nama Siswa Disini         : ")
        Total_Mapel          = int(input("Masukkan Jumlah total Mapel Disini : "))
        for i in range(Total_Mapel):
            Nilai = int(input("Masukkan Nilai Siswa Disini : "))
            list_nilai.append(Nilai)
        nilai_awal = np.array(list_nilai)
        nilai_rata = np.mean(nilai_awal)
        nilai_tertinggi = np.max(nilai_awal)
        nilai_terendah = np.min(nilai_awal)
        nilai_keseluruhan = np.sum(nilai_awal)
        nilai_bersih = nilai_awal >= 75
        nilai_kotor = nilai_awal < 75
        data_siswa['nilai_keseluruhan'] = nilai_keseluruhan
        data_siswa['nilai_remedial'] = nilai_awal[nilai_kotor]
        data_siswa['nilai_diatas_kkm'] = nilai_awal[nilai_bersih]
        data_siswa['nilai_rata_rata'] = nilai_rata
        data_siswa['nilai_tertinggi'] = nilai_tertinggi
        data_siswa['nilai_terendah'] = nilai_terendah
        daftar_data_siswa.append(data_siswa)

        print("="*130)
        print(f"| {'No':^5} | {"Nama":^14} | {"Nilai Diatas KKM":^17} | {"Nilai Remedial":^14} | {"Keseluruhan":^14} | {"Nilai Rata^2":^14} | {"Nilai Tertinggi":^15} | {"Nilai Terendah":^14} |")
        print("-"*130)
        for i,data in enumerate(daftar_data_siswa, start=1):
            print(f"| {i:^5} | {data['nama_siswa']:^14} | {str(data['nilai_diatas_kkm']):^17} | {str(data['nilai_remedial']):^14} | {str(data['nilai_keseluruhan']):^14} | {data['nilai_rata_rata']:^14} | {data['nilai_tertinggi']:^15} | {data['nilai_terendah']:^14} |")
        print("-"*130)

    def lihat_nilai(self):
        os.system('cls')
        print("="*130)
        print(f"| {'No':^5} | {"Nama":^14} | {"Nilai Diatas KKM":^17} | {"Nilai Remedial":^14} | {"Keseluruhan":^14} | {"Nilai Rata^2":^14} | {"Nilai Tertinggi":^15} | {"Nilai Terendah":^14} |")
        print("-"*130)
        for i,data in enumerate(daftar_data_siswa, start=1):
            print(f"| {i:^5} | {data['nama_siswa']:^14} | {str(data['nilai_diatas_kkm']):^17} | {str(data['nilai_remedial']):^14} | {str(data['nilai_keseluruhan']):^14} | {data['nilai_rata_rata']:^14} | {data['nilai_tertinggi']:^15} | {data['nilai_terendah']:^14} |")
        print("-"*130)

    def hapus_nilai(self,hapus):
        os.system('cls')
        if hapus >= 1 <= len(daftar_data_siswa):
            daftar_data_siswa.pop(hapus - 1)
        else:
            print("Salah Input Bung")

        print("="*130)
        print(f"| {'No':^5} | {"Nama":^14} | {"Nilai Diatas KKM":^17} | {"Nilai Remedial":^14} | {"Keseluruhan":^14} | {"Nilai Rata^2":^14} | {"Nilai Tertinggi":^15} | {"Nilai Terendah":^14} |")
        print("-"*130)
        for i,data in enumerate(daftar_data_siswa, start=1):
            print(f"| {i:^5} | {data['nama_siswa']:^14} | {str(data['nilai_diatas_kkm']):^17} | {str(data['nilai_remedial']):^14} | {str(data['nilai_keseluruhan']):^14} | {data['nilai_rata_rata']:^14} | {data['nilai_tertinggi']:^15} | {data['nilai_terendah']:^14} |")
        print("-"*130)

daftar_data_siswa = []
while True:
    os.system('cls')
    print("="*100)
    print(f'{"== PROGRAM NUMPY ==":^100}')
    print("="*100)

    opsi_pilihan = int(input('''Pilih Tindakan dibawah Ini : 
    1. Menambahkan Nilai Siswa
    2. Mengubah Nilai Siswa
    3. Melihat Nilai Siswa
    4. Menghapus Nilai siswa
Pilih antara (1/2/3/4) : '''))
    
    if opsi_pilihan == 1:
        data_siswa = {}
        list_nilai = []
        data_siswa['nama_siswa'] = input("Masukkan Nama Siswa Disini         : ")
        Total_Mapel          = int(input("Masukkan Jumlah total Mapel Disini : "))
        for i in range(Total_Mapel):
            Nilai = int(input("Masukkan Nilai Siswa Disini : "))
            list_nilai.append(Nilai)
        nilai_awal = np.array(list_nilai)
        nilai_rata = np.mean(nilai_awal)
        nilai_tertinggi = np.max(nilai_awal)
        nilai_terendah = np.min(nilai_awal)
        nilai_keseluruhan = np.sum(nilai_awal)
        nilai_bersih = nilai_awal >= 75
        nilai_kotor = nilai_awal < 75
        data_siswa['nilai_keseluruhan'] = nilai_keseluruhan
        data_siswa['nilai_remedial'] = nilai_awal[nilai_kotor]
        data_siswa['nilai_diatas_kkm'] = nilai_awal[nilai_bersih]
        data_siswa['nilai_rata_rata'] = nilai_rata
        data_siswa['nilai_tertinggi'] = nilai_tertinggi
        data_siswa['nilai_terendah'] = nilai_terendah
        daftar_data_siswa.append(data_siswa)
        siswa = operasi(data_siswa['nama_siswa'],data_siswa['nilai_diatas_kkm'],data_siswa['nilai_remedial'],data_siswa['nilai_keseluruhan'],data_siswa['nilai_rata_rata'],data_siswa['nilai_tertinggi'],data_siswa['nilai_terendah'])
        siswa.tambah_nilai()

    elif opsi_pilihan == 2:
        siswa.lihat_nilai()
        ubah = int(input('Masukkan Nomer Yang Ingin Anda Ubah : '))
        siswa.ubah_nilai(ubah)

    elif opsi_pilihan == 3:
        siswa.lihat_nilai()

    elif opsi_pilihan == 4:
        siswa.lihat_nilai()
        hapus = int(input('Masukkan Nomer Yang Ingin Anda Hapus : '))
        siswa.hapus_nilai(hapus)

    opsi_lanjutan = input("Apakah anda ingin melanjutkan program (y/n) : ").lower()
    if opsi_lanjutan == 'n':
        break