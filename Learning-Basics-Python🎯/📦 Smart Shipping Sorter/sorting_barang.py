import os

pengiriman = {
    'same day': 1,
    'next day': 2,
    'reguler': 3,
    'kargo': 7
}

data_barang = []

while True:
    os.system('cls')
    print(f'{'='*100:^100}')
    print(f'{'== SELAMAT DATANG DIAPLIKASI OLSHOP ==':^100}')
    print(f'{'='*100:^100}')

    jumlah_barang = int(input('Masukkan jumlah barang yang diterima : '))
    for i in range(jumlah_barang):
        nama_barang = input('\nMasukkan nama barang : ')
        jenis_ekspedisi = int(input('''Pilihlah jenis ekspedisi barang
    1. Same day
    2. Next day
    3. Reguler
    4. Kargo
Pilih (1/2/3/4) : '''))
        jenis_barang = int(input('''Pilihlah jenis barang
    1. Benda cair / mudah pecah
    2. Benda cair / tidak mudah pecah
    3. Benda padat / mudah pecah
    4. Benda padat / tidak mudah pecah
Pilih (1/2) : '''))
        
        if jenis_ekspedisi == 1:
            jenis_ekspedisi = pengiriman['same day']
        elif jenis_ekspedisi == 2:
            jenis_ekspedisi = pengiriman['next day']
        elif jenis_ekspedisi == 3:
            jenis_ekspedisi = pengiriman['reguler']
        elif jenis_ekspedisi == 4:
            jenis_ekspedisi = pengiriman['kargo']
        else:
            print('Pastikan angka sudah sesuai')
            break

        if jenis_barang == 1:
            jenis_barang = 'benda cair/mudah pecah'
        elif jenis_barang == 2:
            jenis_barang = 'benda cair/tidak mudah pecah'
        elif jenis_barang == 3:
            jenis_barang = 'benda padat/mudah pecah'
        elif jenis_barang == 4:
            jenis_barang = 'benda padat/tidak mudah pecah'
        else:
            print('Pastikan angka sudah sesuai')
            break

        data_baru = {}
        data_baru['nama']  = nama_barang
        data_baru['ekspedisi'] = jenis_ekspedisi
        data_baru['j_barang'] = jenis_barang
        data_barang.append(data_baru)

    sorted_by_value = sorted(data_barang, key=lambda item: item['ekspedisi'])

    print(f'\n{'-'*100:^100}')
    print(f'{'== BARANG DIURUTKAN BERDASARKAN WAKTU ==':^100}')
    print(f'{'-'*100:^100}')
    print(f'| {'NO':^4} | {'NAMA BARANG':^17} | {'JENIS EKSPEDISI':^17} | {'JENIS BARANG':^30} |')
    print(f'{'-'*100:^100}')
    for i,data in enumerate (sorted_by_value, start=1):
        print(f'| {i:^4} | {data["nama"]:^17} | {str(data["ekspedisi"]) + " Hari":^17} | {data["j_barang"]:^30} |')


    opsi_lanjutan = input('Apakah anda ingin melanjutkan (y/n) : ')
    if opsi_lanjutan == 'n':
        break

print(f'\n{'-'*100:^100}')
print(f'{'== SEE YOU AGAIN ==':^100}')
print(f'{'-'*100:^100}')