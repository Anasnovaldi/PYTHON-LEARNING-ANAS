import os
import crud

while True:
    print(f'{"="*100:^100}')
    print(f'{"== SELAMAT DATANG DIPUSKESMAS AMBA RUOK ==":^100}')
    print(f'{"="*100:^100}')

    tindakan = int(input('''Pilih Tindakan Dibawah
    1. Membuat Antrian
    2. Melihat Antrian
    3. Mengubah Antrian
    4. Menghapus Antrian
Pilih [1/2/3/4] : '''))
    
    if tindakan == 1:
        print(f'{"="*100:^100}')
        print(f'{"== Silahkan Tambahkan Antrian ==":^100}')
        print(f'{"="*100:^100}')

        nama    = input('Masukkan nama pasien    : ')
        keluhan = input('Masukkan keluhan pasien : ')
        nomor   = input('Masukkan nomor pasien   : ')
        crud.create(nama,keluhan,nomor)
        os.system('cls')
        print(f'{'Berikut data yang telah ditambahkan':^100}')
        crud.read()

    elif tindakan == 2:
        os.system('cls')
        crud.read()
        input("\nTekan Enter untuk lanjut...")

    elif tindakan == 3:
        crud.read()
        print(f'{"="*100:^100}')
        print(f'{"== Silahkan Ubah Antrian ==":^100}')
        print(f'{"="*100:^100}')
        pk      = input("Masukkan ID yang ingin diubah: ")
        nama    = input("Nama baru                    : ")
        keluhan = input('Masukkan keluhan pasien      : ')
        nomor   = input("Nomor baru                   : ")
        crud.update(pk, nama, keluhan, nomor)

    elif tindakan == 4:
        crud.read()
        print(f'{"="*100:^100}')
        print(f'{"== Silahkan Hapus Antrian ==":^100}')
        print(f'{"="*100:^100}')
        pk = input("Masukkan ID yang ingin dihapus: ")
        crud.delete(pk)

    elif tindakan == 5:
        break
    else:
        print("Pilihan tidak valid!")

    opsi_lanjutan = input("Apakah anda ingin melanjutkan (y/n) : ")
    if opsi_lanjutan == 'n':
        break

print(f'{"="*100:^100}')
print(f'{"== SELAMAT DATANG DIPUSKESMAS AMBA RUOK ==":^100}')
print(f'{"="*100:^100}')