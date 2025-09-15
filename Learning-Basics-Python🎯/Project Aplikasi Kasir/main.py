from Login_akun import header_login_akun,akun
from List_karyawan import header_karyawan,daftar_karyawan,tambah_karyawan,hapus_karyawan
from List_barang import header_list_barang, daftar_barang, tambah_barang
from Kasir_Depan import jual_barang
import os

os.system('cls')
header_login_akun()
akun()


while True:
    opsi = input('''Hello bos pilih tindakan disini : 
        1. Lihat daftar karyawan
        2. Tambahkan karyawan 
        3. Keluarkan Karywan 
        4. Lihat daftar barang
        5. Tambahkan Barang 
        6. Pengeluaran barang 
    Pilih tindakan kamu disini : ''')

    if opsi == '1':
        header_karyawan()
        daftar_karyawan()

    elif opsi == '2':
        header_karyawan()
        daftar_karyawan()
        nama =    input('Masukkan nama karyawan disini    : ').lower()
        umur= int(input('Masukkan umur karyawan disini    : '))
        jobdesk = input('Masukkan Jobdesk karyawan disini : ')
        tambah_karyawan(nama,umur,jobdesk)

    elif opsi == '3':
        header_karyawan()
        daftar_karyawan()
        nama =    input('Masukkan nama karyawan disini    : ').lower()
        hapus_karyawan(nama)

    elif opsi == '4':
        header_list_barang()
        daftar_barang()

    elif opsi == '5':
        header_list_barang()
        daftar_barang()
        nama   =     input('Masukkan nama barang yang masuk   : ').lower()
        harga  = int(input('Masukkan harga barang disini      : '))
        jumlah = int(input('Masukkan jumlah barang yang masuk : '))
        tambah_barang(nama,harga,jumlah)

    elif opsi == '6':
        header_list_barang()
        daftar_barang()
        nama   =     input('Masukkan nama barang yang keluar   : ').lower()
        jumlah = int(input('Masukkan jumlah barang yang keluar : '))
        jual_barang(nama,jumlah)

    else:
        print('Aduh bung kamu salah pilih ni.')

    opsi_lanjutan = input('Apakah anda ingin melanjutkan (y/n) : ')
    if opsi_lanjutan == 'n':
        break

print('GOODBYE BOS')