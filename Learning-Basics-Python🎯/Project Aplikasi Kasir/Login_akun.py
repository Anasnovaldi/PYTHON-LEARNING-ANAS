# Program Login
def header_login_akun():
    print(f'{'='*60:^60}')
    print(f'{'SELAMAT DATANG DIAPLIKASI KASIR':^60}')
    print(f'{'='*60:^60}')

def akun():
    data_login = {
        'legolas':'proxima',
        'thorin':'jupiter',
        'gandalf':'bima sakti',
        'baggins':'pluto'
    }

    nama  = input('Masukkan nama kamu disini  : ').lower()
    if nama in data_login:
        sandi = input('Masukkan sandi kamu disini : ').lower()
        if sandi == data_login[nama]:
            print(f'Hello {nama.capitalize()} selamat datang.\n')
        else:
            print('aduh sandi kamu salach nich\n')
            print('coba lagi ...')
            exit()
    else:
        print('nama kamu tidak terdaftar disini.\n')
        print('coba lagi ...')
        exit()