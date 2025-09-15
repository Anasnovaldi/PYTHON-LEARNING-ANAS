import os
import CRUD as CRUD

if __name__ == "__main__":
    os.system('cls')
    print(f'{'='*50:^60}')
    print(f'{'SELAMAT DATANG DIAPLIKASI TO DO LIST':^60}')
    print(f'{'='*50:^60}')

    password = {
        'anas':'proxima',
        'novaldi':'centuri',
        'jawir':'jupiter'
    }

    nama = input("Masukkan nama kamu disini  : ").lower()

    if nama in password:
        sandi = input("Masukkan sandi kamu disini : ").lower()
        if sandi == password['anas']:
            print(f"Hello {nama} selamat datang")
        else:
            print('sepertinya kamu salah tulis')
            exit()
    else:
        print('nama kamu tidak terdata disini.')
        exit()

    CRUD.init_console()

    while True:
        opsi_user = input('''Pilihlah Opsi dibawah ini :
    1. Membuat rencana
    2. Melihat rencana
    3. Mengubah rencana
    4. Menghapus rencana
Pilih disini : ''')

        match opsi_user:
            case "1": CRUD.create_console()
            case "2": CRUD.read_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            case '5' : 
                print("Aduh bung sepertinya kamu salah tulis nih.")
                exit()
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print(f'{'='*50:^60}')
    print(f'{'SELAMAT DATANG DIAPLIKASI TO DO LIST':^60}')
    print(f'{'='*50:^60}')