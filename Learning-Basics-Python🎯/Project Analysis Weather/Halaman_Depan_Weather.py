import os
from CRUD.CalculationWeather import Weather 

while True:
    os.system("cls")
    try:
        weather_app
    except NameError:
        weather_app = Weather()
    
    print("="*100)
    print(f"{"== PROJECT ANALYSIS WEATHER ==":^100}")
    print("="*100)

    opsi_tindakan = int(input('''Pilihlah Salah Satu : 
    1. Tambah Wilayah
    2. Lihat Wilayah
    3. Ubah Wilayah
    4. Hapus Wilayah
Pilih (1/2/3/4) :  '''))
    
    try:
        if opsi_tindakan == 1:
            weather_app.Tambah()
        elif opsi_tindakan == 2:
            weather_app.Lihat()
        elif opsi_tindakan == 3:
            weather_app.Ubah()
        elif opsi_tindakan == 4:
            weather_app.Hapus()
        else:
            print("Pilih Antara (1/2/3/4)")
    except ValueError:
        print("input harus angka !!!")
        break

    opsi_lanjutan = input("Again ? (y/n) : ").lower()
    if opsi_lanjutan == "n":
        break

print("="*100)
print(f"{"== PROJECT ANALYSIS WEATHER ==":^100}")
print("="*100)