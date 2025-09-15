import tkinter as tk
from tkinter import ttk
from CALC_TKINTER import tombol_matematika, tombol_fisika, tombol_kimia

window = tk.Tk()
window.configure(bg="white")
window.geometry("450x550")
window.resizable(False, False)
window.title("SCIENTIFIC CALCULATIONS")

# Variabel utama
MODE = tk.StringVar()
MODE_FISIKA = tk.StringVar()
MODE_KIMIA = tk.StringVar()
MODE_MATEMATIKA = tk.StringVar()

# Variabel Matematika
ANGKA1 = tk.IntVar()
ANGKA2 = tk.IntVar()
HASIL_TAMBAH = tk.IntVar()
HASIL_KURANG = tk.IntVar()
HASIL_KALI = tk.IntVar()
HASIL_BAGI = tk.IntVar()

# Variabel Fisika
MASSA = tk.IntVar()
VOLUME = tk.IntVar()
PERCEPATAN = tk.IntVar()
KECEPATAN = tk.IntVar()
WAKTU = tk.IntVar()
JARAK = tk.IntVar()
HASIL_KECEPATAN = tk.IntVar()
HASIL_JARAK = tk.IntVar()
HASIL_GAYA = tk.IntVar()
HASIL_MASSA_JENIS = tk.IntVar()

# Variabel Suhu
CELCIUS = tk.IntVar()
KELVIN = tk.IntVar()
FAHRENHEIT = tk.IntVar()
HASIL_CELCIUS_FAHRENHEIT = tk.IntVar()
HASIL_CELCIUS_KELVIN = tk.IntVar()
HASIL_CELCIUS_REAMUR = tk.IntVar()
HASIL_KELVIN_CELCIUS = tk.IntVar()
HASIL_KELVIN_FAHRENHEIT = tk.IntVar()
HASIL_KELVIN_REAMUR = tk.IntVar()
HASIL_FAHRENHEIT_CELCIUS = tk.IntVar()
HASIL_FAHRENHEIT_KELVIN = tk.IntVar()
HASIL_FAHRENHEIT_REAMUR = tk.IntVar()

# Frame utama
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

def tombol_click():
    for widget in input_frame.winfo_children():
        widget.destroy()

    if MODE.get() == "Matematika dasar":
        tombol_matematika(input_frame, ANGKA1, ANGKA2, HASIL_TAMBAH, HASIL_KURANG, HASIL_KALI, HASIL_BAGI, MODE_MATEMATIKA)

    elif MODE.get() == "Fisika dasar":
        tombol_fisika(input_frame, MASSA, VOLUME, KECEPATAN, JARAK, WAKTU, PERCEPATAN,HASIL_JARAK, HASIL_MASSA_JENIS, HASIL_KECEPATAN, HASIL_GAYA, MODE_FISIKA)

    elif MODE.get() == "Hitung suhu":
        tombol_kimia(input_frame, MODE_KIMIA, CELCIUS, KELVIN, FAHRENHEIT,HASIL_CELCIUS_FAHRENHEIT, HASIL_CELCIUS_KELVIN, HASIL_CELCIUS_REAMUR,HASIL_KELVIN_CELCIUS, HASIL_KELVIN_FAHRENHEIT, HASIL_KELVIN_REAMUR,HASIL_FAHRENHEIT_CELCIUS, HASIL_FAHRENHEIT_KELVIN, HASIL_FAHRENHEIT_REAMUR)

# Pilih mode awal
mode_label = ttk.Label(input_frame, text="Pilih Mode:")
mode_label.pack(fill="x", pady=5)

mode_box = ttk.Combobox(input_frame, textvariable=MODE,values=["Matematika dasar", "Fisika dasar", "Hitung suhu"],state="readonly")
mode_box.pack(fill="x", pady=5)

tombol_pilih = ttk.Button(input_frame, text="PILIH", command=tombol_click)
tombol_pilih.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()
