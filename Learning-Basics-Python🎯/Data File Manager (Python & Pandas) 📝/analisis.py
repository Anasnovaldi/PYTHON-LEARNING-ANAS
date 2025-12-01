import os
import pandas as pd
import csv

def analisis():
    nama_file = input("Masukkan Nama File    : ").lower()
    try:
        os.system('cls')
        print('='*70)
        print(f'{'== ANALISIS SEDERHANA : ==':^70}')
        print('='*70)
        df = pd.read_csv(nama_file)
        print(df.to_string())
        print('='*70)
        print(df.info())
        print('='*70)
        df_numerik = df.select_dtypes(include=['number'])

        if df_numerik.empty:
            print("⚠️ TIDAK ADA KOLOM NUMERIK yang dapat dianalisis secara statistik.")
            return

        print(f'{'== ANALISIS STATISTIK  ==':^70}')
        print('='*70)
        statistik = df_numerik.describe()
        print(statistik)

    except FileNotFoundError:
        print("File Tidak Ditemukan.")