
def main():
    class karyawan:
        def __init__(self,nama,id_anggota):
            self.nama = nama
            self.id_anggota = id_anggota

        def tambah_karyawan(self):
            print(f"| {"No":^5} | {"Nama":^20} | {"Id_anggota":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_karyawan, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['id_anggota']:^20} |")

        def hapus_karyawan(self,hapus_karyawan):
            if hapus_karyawan >= 1 <= len(daftar_karyawan):
                daftar_karyawan.pop(hapus_karyawan - 1)
            else:
                print('Nomor karyawan tidak sesuai')
            print(f"| {"No":^5} | {"Nama":^20} | {"Id_anggota":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_karyawan, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['id_anggota']:^20} |")

        def ubah_karyawan(self,ubah_karyawan):
            if ubah_karyawan >= 1 <= len(daftar_karyawan):
                daftar_karyawan.pop(ubah_karyawan - 1)
                dict_karyawan_baru = {}
                dict_karyawan_baru["nama"]       = input("Masukkan nama karaywan Baru disini : ")
                dict_karyawan_baru["id_anggota"] = input("Masukkan id_anggota Baru disini    : ")
                daftar_karyawan.append(dict_karyawan_baru)
            else:
                print('Nomor karyawan tidak sesuai')

            print(f"| {"No":^5} | {"Nama":^20} | {"Id_anggota":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_karyawan, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['id_anggota']:^20} |")

        def info_karyawan(self):
            print(f"| {"No":^5} | {"Nama":^20} | {"Id_anggota":^20} |")
            print(f"{"-"*100:^100}")
            for i,data in enumerate(daftar_karyawan, start=1):
                print(f"| {i:^5} | {data['nama']:^20} | {data['id_anggota']:^20} |")


    daftar_karyawan = []

    while True:
        import os
        os.system('cls')

        print(f"{"="*100:^100}")
        print(f"{"Selamat Datang Dipelajaran OOP saya":^100}")
        print(f"{"="*100:^100}")

        opsi_tindakan = int(input('''Pilih tindakan dibawah ini
        1. Tambahkan karyawan
        2. Hapus karyawan
        3. Ubah karyawan
        4. Info karyawan
    Pilih tindakan (1/2/3/4) : '''))
        
        if opsi_tindakan == 1:
            dict_karyawan = {}
            dict_karyawan['nama']       = input("Masukkan nama karyawan : ")
            dict_karyawan['id_anggota'] = input("Masukkan id_anggota    : ")
            daftar_karyawan.append(dict_karyawan)
            print(f"{"="*100:^100}")
            karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
            print(karyawan_baru.tambah_karyawan())
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 2:
            print(f"{"="*100:^100}")
            karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
            print(karyawan_baru.info_karyawan())
            print(f"{"="*100:^100}")

            hapus_karyawan = int(input('Masukkan Nomer Yang Ingin kamu Hapus : '))
                
            print(f"{"="*100:^100}")
            karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
            print(karyawan_baru.hapus_karyawan(hapus_karyawan))
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 3:
            print(f"{"="*100:^100}")
            karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
            print(karyawan_baru.info_karyawan())
            print(f"{"="*100:^100}")

            ubah_karyawan = int(input('Masukkan Nomer Yang Ingin kamu ubah : '))

            print(f"{"="*100:^100}")
            karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
            print(karyawan_baru.ubah_karyawan(ubah_karyawan))
            print(f"{"="*100:^100}")

        elif opsi_tindakan == 4:
            try:
                print(f"{"="*100:^100}")
                karyawan_baru = karyawan(dict_karyawan["nama"], dict_karyawan["id_anggota"])
                print(karyawan_baru.info_karyawan())
                print(f"{"="*100:^100}")
            except:
                print("Belum ada data silahkan tambahkan data terlebih dahulu")


        opsi_lanjutan = input("Apakah anda ingin melanjutkan program (y/n) : ")
        if opsi_lanjutan == 'n':
            break

    print(f"{"="*100:^100}")
    print(f"{"Selamat Jalan Dipelajaran OOP saya":^100}")
    print(f"{"="*100:^100}")