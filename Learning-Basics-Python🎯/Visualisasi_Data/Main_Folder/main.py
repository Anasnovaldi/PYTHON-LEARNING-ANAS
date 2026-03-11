import csv
import pandas as pd
import os
import Visualisasi

if __name__ == "__main__":
    class PILIHAN:
        def __init__(self):
            pass

        def Create_File(self):
            os.system("cls" if os.name=='nt' else "clear")
            print("="*100)
            print(f"{"=== OPSI MEMBUAT FILE ===":^100}")
            print(f"{"="*100}\n")

            try:
                list_kolom = []
                nama_file = input("Masukkan Nama File Yang Ingin Dibuat (e.g = namafile.csv) : ").lower()
                jumlah_kolom = int(input(f"Masukkan Jumlah Kolom Dalam File {nama_file} : "))
                lokasi_folder = f"Project_Visualisasi\Database_\{nama_file}"
                for i in range(jumlah_kolom):
                    kolom = input(f"Masukkan Nama Kolom ke {i+1} : ").lower()
                    list_kolom.append(kolom)

                with open(lokasi_folder, 'w', newline='') as file:
                    content = csv.writer(file)
                    content.writerow(list_kolom)
                    print(f"File Bernama {nama_file} Berhasil Dibuat")
            except ValueError:
                print("Pilihan Berupa Angka")

        def Manipulasi(self):
            os.system("cls" if os.name=='nt' else "clear")
            print("="*100)
            print(f"{"=== OPSI MANIPULASI DATA ===":^100}")
            print(f"{"="*100}\n")

            try:
                nama_file = input("Masukkan Nama File Yang Tersedia (e.g = namafile.csv) : ").lower()
                lokasi_folder = f"Project_Visualisasi\Database_\{nama_file}"

                opsi_manipulasi = int(input('''Pilihlah Opsi Manipulasi Data :
    1. Tambahkan Data CSV
    2. Hapus Data CSV
    3. Ubah Data CSV
    4. Lihat Data CSV
Pilih Antara (1/2/3/4):'''))
                
                if opsi_manipulasi == 1:
                    list_baris = []
                    with open(lokasi_folder, 'r', encoding='UTF-8') as file:
                        content = csv.reader(file)
                        kolom = next(content)
                        panjang_kolom = len(kolom)

                    print("="*100)
                    for i in range(panjang_kolom):
                        nama_file = input(f'Masukkan Isi File Dari Kolom {kolom[i]} : ').lower()
                        list_baris.append(nama_file)

                    with open(lokasi_folder, 'a', newline='') as file:
                        content = csv.writer(file)
                        content.writerow(list_baris)
                        print("Baris Telah Berhasil Dibuat")
                    print("="*100)

                elif opsi_manipulasi == 2:
                    df = pd.read_csv(lokasi_folder)
                    df_view = df.copy()
                    df_view.index = df_view.index+1
                    print(df_view.to_string())
                    opsi_hapus = int(input('''Pilihlah Opsi Penghapusan:
    1. Hapus Baris
    2. Hapus Kolom
Pilih Antara (1/2): '''))
                    if opsi_hapus == 1:
                        nomor_baris = int(input("Masukkan Nomor Baris Yang Ingin Dihapus : "))
                        index_baris = df.index[nomor_baris - 1]
                        df.drop(index_baris, axis=0, inplace=True)
                        df.to_csv(lokasi_folder, index=False)
                        print("="*100)
                        df_view = df.copy()
                        df_view.index = df_view.index + 1
                        print(df_view.to_string())
                    elif opsi_hapus == 2:
                        nomor_kolom = int(input("Masukkan Nomor Kolom Yang Ingin Dihapus : "))
                        nama_kolom = df.columns[nomor_kolom - 1]
                        df = df.drop(nama_kolom, axis=1)
                        df.to_csv(lokasi_folder, index=False)
                        print("="*100)
                        df_view = df.copy()
                        df_view.index = df_view.index + 1
                        print(df_view.to_string())
                    else:
                        print("Pilihan Hanya (1/2)")

                elif opsi_manipulasi == 3:
                    df = pd.read_csv(lokasi_folder)
                    df_view = df.copy()
                    df_view.index = df_view.index+1
                    print(df_view.to_string())
                    nomor_baris = int(input("Masukkan Nomor Baris Yang Ingin Diubah : "))
                    nomor_kolom = int(input("Masukkan Nomor Kolom Yang Ingin Diuabh : "))
                    df.iloc[(nomor_baris - 1), (nomor_kolom - 1)] = input(f"Masukkan Data Baru Dari Kolom {df.columns[nomor_kolom - 1]} : ")
                    df.to_csv(lokasi_folder, index=False)
                    print("="*100)
                    df_view = df.copy()
                    df_view.index = df_view.index + 1
                    print(df_view.to_string())

                elif opsi_manipulasi == 4:
                    df = pd.read_csv(lokasi_folder)
                    df_view = df.copy()
                    df_view.index = df_view.index+1
                    print(df_view.to_string())

                else:
                    print("Pilihan Hanya (1/2/3/4)")

            except ValueError:
                print("Pilihan Hnaya Berupa Angka")
                exit()
            except FileNotFoundError:
                print("File Tidak Ditemukan")
                exit()

    while True:
        os.system("cls" if os.name=='nt' else "clear")
        print("="*100)
        print(f"{"=== PROGRAM VISUALISASI DATA ===":^100}")
        print(f"{"="*100}\n")
        try:
            opsi_awal = int(input('''Pilihlah Opsi Dibawah Ini:
        1. Membuat File CSV
        2. Manipulasi File CSV
        3. Visualisasi Data File CSV
    Pilih Antara (1/2/3) : '''))
            
            if opsi_awal == 1:
                user = PILIHAN()
                user.Create_File()

            elif opsi_awal == 2:
                user = PILIHAN()
                user.Manipulasi()

            elif opsi_awal == 3:
                Visualisasi.main()

            else:
                print("Pilihan Hanya (1/2/3)")
        except ValueError:
            print('Pilihan Hanya Berupa Angka')

        opsi_akhir = input("Apakah Anda Ingin Melanjutkan ? (y/n) : ").lower()
        if opsi_akhir == 'n':
            break

    print("="*100)
    print(f"{"=== PROGRAM VISUALISASI DATA ===":^100}")
    print(f"{"="*100}\n")