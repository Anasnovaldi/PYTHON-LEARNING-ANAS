
def main():
    class buku:
        def __init__(self,judul,penulis,tahun):
            self.judul = judul
            self.penulis = penulis
            self.tahun = tahun

        def tambah_buku(self):
            print(f"| {"No":^5} | {"Judul":^20} | {"Penulis":^20} | {"Tahun":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_buku, start=1):
                print(f"| {i:^5} | {data['judul']:^20} | {data['penulis']:^20} | {data['tahun']:^20} |")

        def hapus_buku(self,hapus_buku):
            if hapus_buku >= 1 <= len(daftar_buku):
                daftar_buku.pop(hapus_buku - 1)
            else:
                print('Nomor buku tidak sesuai')
            print(f"| {"No":^5} | {"Judul":^20} | {"Penulis":^20} | {"Tahun":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_buku, start=1):
                print(f"| {i:^5} | {data['judul']:^20} | {data['penulis']:^20} | {data['tahun']:^20} |")

        def ubah_buku(self,ubah_buku):
            if ubah_buku >= 1 <= len(daftar_buku):
                daftar_buku.pop(ubah_buku - 1)
                dict_buku_baru = {}
                dict_buku_baru["judul"]   = input("Masukkan Judul Buku Baru disini   : ")
                dict_buku_baru["penulis"] = input("Masukkan Penulis Buku Baru disini : ")
                dict_buku_baru["tahun"]   = input("Masukkan Tahun Buku Baru disini   : ")
                daftar_buku.append(dict_buku_baru)
            else:
                print('Nomor buku tidak sesuai')

            print(f"| {"No":^5} | {"Judul":^20} | {"Penulis":^20} | {"Tahun":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_buku, start=1):
                print(f"| {i:^5} | {data['judul']:^20} | {data['penulis']:^20} | {data['tahun']:^20} |")

        def info_buku(self):
            print(f"| {"No":^5} | {"Judul":^20} | {"Penulis":^20} | {"Tahun":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_buku, start=1):
                print(f"| {i:^5} | {data['judul']:^20} | {data['penulis']:^20} | {data['tahun']:^20} |")


    daftar_buku = []


    while True:
        import os
        os.system('cls')

        print(f"{"="*100:^100}")
        print(f"{"Selamat Datang Dipelajaran OOP saya":^100}")
        print(f"{"="*100:^100}")

        opsi_tindakan = int(input('''Pilih tindakan dibawah ini
        1. Tambahkan Buku
        2. Hapus Buku
        3. Ubah Buku
        4. Info Buku
    Pilih tindakan (1/2/3/4) : '''))
        
        if opsi_tindakan == 1:
            dict_buku = {}
            dict_buku['judul']   = input("Masukkan judul buku   : ")
            dict_buku['penulis'] = input("Masukkan Nama Penulis : ")
            dict_buku['tahun']   = input("Masukkan Tahun Terbit : ")
            daftar_buku.append(dict_buku)
            print(f"{"="*100:^100}")
            buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
            print(buku_baru.tambah_buku())
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 2:
            print(f"{"="*100:^100}")
            buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
            print(buku_baru.info_buku())
            print(f"{"="*100:^100}")

            hapus_buku = int(input('Masukkan Nomer Yang Ingin kamu Hapus : '))
                
            print(f"{"="*100:^100}")
            buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
            print(buku_baru.hapus_buku(hapus_buku))
            print(f"{"="*100:^100}")


        elif opsi_tindakan == 3:
            print(f"{"="*100:^100}")
            buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
            print(buku_baru.info_buku())
            print(f"{"="*100:^100}")

            ubah_buku = int(input('Masukkan Nomer Yang Ingin kamu ubah : '))

            print(f"{"="*100:^100}")
            buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
            print(buku_baru.ubah_buku(ubah_buku))
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 4:
            try:
                print(f"{"="*100:^100}")
                buku_baru = buku(dict_buku["judul"], dict_buku["penulis"], dict_buku["tahun"])
                print(buku_baru.info_buku())
                print(f"{"="*100:^100}")
            except:
                print("Belum ada data silahkan tambahkan data terlebih dahulu")


        opsi_lanjutan = input("Apakah anda ingin melanjutkan program (y/n) : ")
        if opsi_lanjutan == 'n':
            break

    print(f"{"="*100:^100}")
    print(f"{"Selamat Jalan Dipelajaran OOP saya":^100}")
    print(f"{"="*100:^100}")