import os
import CRUD.CRUD_BUKU as CRUD_BUKU
import CRUD.CRUD_MAHASISWA as CRUD_MAHASISWA
import CRUD.CRUD_PEGAWAI as CRUD_PEGAWAI
from pyfiglet import Figlet
from rich.console import Console
from rich.style import Style

while True:
    os.system('cls')
    f = Figlet(font="slant")
    art = f.renderText("Antekasinc").splitlines()
    console = Console()

    colors = ["cyan", "magenta", "green", "yellow", "blue"]
    for i, line in enumerate(art):
        console.print(line, style=Style(color=colors[i % len(colors)], bold=True))
    print("="*100)
    print(f"{'WELCOME TO LIBRARY UNIVERSITY':^100}")
    print("="*100)

    opsi_tindakan = int(input('''Pilihlah Tindakan Dibawah
    1. Program CRUD Buku
    2. Program CRUD Mahasiswa
    3. Program CRUD Pegawai
    4. Exit
Pilihlah Opsi Dibawah Ini : '''))

    match opsi_tindakan:
        case 1:
            CRUD_BUKU.main()
        case 2:
            CRUD_MAHASISWA.main()
        case 3:
            CRUD_PEGAWAI.main()
        case 4:
            exit()
        case _:
            print("Pilihan hanya 1/2/3")

    opsi_lanjutan = input("\nApakah kamu ingin kembali ke halaman utama (y/n) : ").lower()
    if opsi_lanjutan == 'n':
        break

print("="*100)
print(f"{'SEE YOU NEXT TIME!':^100}")
print("="*100)
