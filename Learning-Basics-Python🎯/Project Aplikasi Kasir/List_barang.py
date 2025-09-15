def header_list_barang():
    print(f'\n{'='*60:^60}')
    print(f'{'SELAMAT DATANG DI LIST BARANG':^60}')
    print(f'{'='*60:^60}')

barang = {
    "vanilla": {"harga": 10000, "stok": 21},
    "coklat": {"harga": 40000, "stok": 20},
    "moccacino": {"harga": 17000, "stok": 8},
    "capuccino": {"harga": 27000, "stok": 8},
}

def daftar_barang():
    for nama, info in barang.items():
        print(f"- {nama.capitalize():<10} | Harga: Rp{info['harga']:,} | Stok: {info['stok']}")
    print(f'{'='*60:^60}\n')

def tambah_barang(nama,harga,jumlah):
    if nama in barang:
        barang[nama]["stok"] += jumlah
        print(f"Stok {nama} berhasil ditambah {jumlah}. Total stok: {barang[nama]['stok']}")
    else:
        print(f"Barang {nama} belum ada, menambahkan baru...")
        barang[nama] = {"harga": harga, "stok": jumlah}