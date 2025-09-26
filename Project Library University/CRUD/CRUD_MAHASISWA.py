
def main():
    class mahasiswa:
        def __init__(self,nama,nim):
            self.nama = nama
            self.nim = nim

        def tambah_mahasiswa(self):
            print(f"| {"No":^5} | {"Nama":^20} | {"Nim":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_mahasiswa, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['nim']:^20} |")

        def hapus_mahasiswa(self,hapus_mahasiswa):
            if hapus_mahasiswa >= 1 <= len(daftar_mahasiswa):
                daftar_mahasiswa.pop(hapus_mahasiswa - 1)
            else:
                print('Nomor mahasiswa tidak sesuai')
            print(f"| {"No":^5} | {"Nama":^20} | {"Nim":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_mahasiswa, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['nim']:^20} |")

        def ubah_mahasiswa(self,ubah_mahasiswa):
            if ubah_mahasiswa >= 1 <= len(daftar_mahasiswa):
                daftar_mahasiswa.pop(ubah_mahasiswa - 1)
                dict_mahasiswa_baru = {}
                dict_mahasiswa_baru["nama"] = input("Masukkan nama mahasiswa Baru disini : ")
                dict_mahasiswa_baru["nim"]  = input("Masukkan nim mahasiswa Baru disini  : ")
                daftar_mahasiswa.append(dict_mahasiswa_baru)
            else:
                print('Nomor mahasiswa tidak sesuai')

            print(f"| {"No":^5} | {"Nama":^20} | {"Nim":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_mahasiswa, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['nim']:^20} |")

        def info_mahasiswa(self):
            print(f"| {"No":^5} | {"Nama":^20} | {"Nim":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_mahasiswa, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['nim']:^20} |")


    daftar_mahasiswa = []

    while True:
        import os
        os.system('cls')

        print(f"{"="*100:^100}")
        print(f"{"Selamat Datang Dipelajaran OOP saya":^100}")
        print(f"{"="*100:^100}")

        opsi_tindakan = int(input('''Pilih tindakan dibawah ini
        1. Tambahkan mahasiswa
        2. Hapus mahasiswa
        3. Ubah mahasiswa
        4. Info mahasiswa
    Pilih tindakan (1/2/3/4) : '''))
        
        if opsi_tindakan == 1:
            dict_mahasiswa = {}
            dict_mahasiswa['nama'] = input("Masukkan nama mahasiswa : ")
            dict_mahasiswa['nim']  = input("Masukkan nim mahasiswa  : ")
            daftar_mahasiswa.append(dict_mahasiswa)
            print(f"{"="*100:^100}")
            mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
            print(mahasiswa_baru.tambah_mahasiswa())
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 2:
            print(f"{"="*100:^100}")
            mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
            print(mahasiswa_baru.info_mahasiswa())
            print(f"{"="*100:^100}")

            hapus_mahasiswa = int(input('Masukkan Nomer Yang Ingin kamu Hapus : '))
                
            print(f"{"="*100:^100}")
            mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
            print(mahasiswa_baru.hapus_mahasiswa(hapus_mahasiswa))
            print(f"{"="*100:^100}")


        elif opsi_tindakan == 3:
            print(f"{"="*100:^100}")
            mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
            print(mahasiswa_baru.info_mahasiswa())
            print(f"{"="*100:^100}")

            ubah_mahasiswa = int(input('Masukkan Nomer Yang Ingin kamu ubah : '))

            print(f"{"="*100:^100}")
            mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
            print(mahasiswa_baru.ubah_mahasiswa(ubah_mahasiswa))
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 4:
            try:
                print(f"{"="*100:^100}")
                mahasiswa_baru = mahasiswa(dict_mahasiswa["nama"], dict_mahasiswa["nim"])
                print(mahasiswa_baru.info_mahasiswa())
                print(f"{"="*100:^100}")
            except:
                print("Belum ada data silahkan tambahkan data terlebih dahulu")


        opsi_lanjutan = input("Apakah anda ingin melanjutkan program (y/n) : ")
        if opsi_lanjutan == 'n':
            break

    print(f"{"="*100:^100}")
    print(f"{"Selamat Jalan Dipelajaran OOP saya":^100}")
    print(f"{"="*100:^100}")