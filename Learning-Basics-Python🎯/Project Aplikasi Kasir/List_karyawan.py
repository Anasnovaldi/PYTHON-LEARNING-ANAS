def header_karyawan():
    print(f'\n{'='*60:^60}')
    print(f'{'SELAMAT DATANG DI DAFTAR KARYAWAN':^60}')
    print(f'{'='*60:^60}')

data_karyawan = {
    "Legolas": {"umur" : 320, "jobdesk" : "Mencatat barang masuk dan keluar"},
    "Thorin": {"umur" : 70, "jobdesk" : "Membersihkan lingkungan pekerjaan"},
    "Gandalf": {"umur" : 160, "jobdesk" : "Menjaga Kasir"},
    "Baggins": {"umur" : 32, "jobdesk" : "Pengantar barang"}
}

def daftar_karyawan():
    for nama, info in data_karyawan.items():
        print(f'- {nama.capitalize():<10} | Umur: {info['umur']:} | Jobdesk:{info['jobdesk']}')
    print(f'{'='*60:^60}\n')

def tambah_karyawan(nama, umur, jobdesk):
    data_karyawan[nama] = {"umur": umur, "jobdesk": jobdesk}
    print(f"\nKaryawan {nama} berhasil ditambahkan.")

def hapus_karyawan(nama):
    if nama in data_karyawan:
        del data_karyawan[nama]
        print(f"\nKaryawan {nama} berhasil dihapus.")
    else:
        print(f"\nKaryawan {nama} tidak ditemukan.")