import os
import numpy as np

def hitung_jam_tidur(jam_tidur, jam_bangun):
    """Hitung total jam tidur berdasarkan jam tidur dan bangun."""
    if jam_tidur >= 19:  # tidur malam lewat jam 19.00
        return (24 - jam_tidur) + jam_bangun
    elif jam_tidur <= 10:  # tidur pagi/siang
        return jam_bangun - jam_tidur
    return 0

total_tidur = []
daftar_tidur = []

while True:
    os.system('cls')
    print(f'{'='*100:^100}')
    print(f'{'YOU CAN TAKE CONTROL YOUR SLEEP !!':^100}')
    print(f'{'='*100:^100}')

    for hari in range(1, 8):
        tidur  = float(input(f"Masukkan jam tidur hari ke-{hari}   (contoh 21 / 21.30): "))
        bangun = float(input(f"Masukkan jam bangun hari ke-{hari}   (contoh 6 / 6.30) : "))
        total = hitung_jam_tidur(tidur, bangun)
        total_tidur.append(total)
        print("-"*100)

    data_baru = {}
    data_baru['hari1'] = total_tidur[0]
    data_baru['hari2'] = total_tidur[1]
    data_baru['hari3'] = total_tidur[2]
    data_baru['hari4'] = total_tidur[3]
    data_baru['hari5'] = total_tidur[4]
    data_baru['hari6'] = total_tidur[5]
    data_baru['hari7'] = total_tidur[6]
    daftar_tidur.append(data_baru)

    temps = np.array(total_tidur)

    print(f'\n{'-'*100:^100}')
    mean_sleep = temps.mean()
    print(f'Rata-rata waktu tidur harianmu      :  {mean_sleep:.2f} Jam')
    outliers = temps < mean_sleep
    hari_berantakan = np.where(outliers)[0] + 1
    hari_list = ", ".join([f"Hari ke-{h}" for h in hari_berantakan])

    if np.any(outliers) == True:    
        print('Apakah ada gangguan tidur           : ', np.any(outliers))
        print('Hari Tidur Yang berantakan          : ', hari_list)
        print('Laporan tidur buruk berdasarkan jam : ', ", ".join(map(str, temps[outliers])))
        print('\nKurangi screen time, hindari kafein malam hari, cobalah relaksasi seperti membaca atau minum susu hangat')

    elif np.any(outliers) == False:
        print('Apakah ada gangguan tidur           : ', np.any(outliers))
        print('\nPertahankan konsistensi, buat rutinitas tidur, hindari begadang.')

    print(f'\n{'-'*100:^100}')
    print(f'{'== LAPORAN WAKTU TIDUR KAMU ==':^100}')
    print(f'{'-'*100:^100}')
    print(f'| {'Hari ke 1':^10} | {'Hari ke 2':^10} | {'Hari ke 3':^10} | {'Hari ke 4':^10} | {'Hari ke 5':^10} | {'Hari ke 6':^10} | {'Hari ke 7':^10} |')
    print(f'{'-'*100:^100}')
    for data in daftar_tidur:
        print(f"| {data['hari1']:^10.2f} | {data['hari2']:^10.2f} | {data['hari3']:^10.2f} | {data['hari4']:^10.2f} | {data['hari5']:^10.2f} | {data['hari6']:^10.2f} | {data['hari7']:^10.2f} |")

    opsi_lanjutan = input('Yakin Sudah Beres (y/n)')
    if opsi_lanjutan == 'n':
        break

print(f'{'='*100:^100}')
print(f'{'YOU DID IT BUDDY !!':^100}')
print(f'{'='*100:^100}')