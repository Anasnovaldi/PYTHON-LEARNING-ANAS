import tkinter as tk
from tkinter import ttk

def tombol_kimia(input_frame, MODE_KIMIA, CELCIUS, KELVIN, FAHRENHEIT,HASIL_CELCIUS_FAHRENHEIT, HASIL_CELCIUS_KELVIN, HASIL_CELCIUS_REAMUR,HASIL_KELVIN_CELCIUS, HASIL_KELVIN_FAHRENHEIT, HASIL_KELVIN_REAMUR,HASIL_FAHRENHEIT_CELCIUS, HASIL_FAHRENHEIT_KELVIN, HASIL_FAHRENHEIT_REAMUR):
    def celcius():
        a = CELCIUS.get()
        HASIL_CELCIUS_FAHRENHEIT.set((9/5 * a) + 32)
        HASIL_CELCIUS_KELVIN.set(263.15 + a)
        HASIL_CELCIUS_REAMUR.set(4/5 * a)

    def fahrenheit():
        a = FAHRENHEIT.get()
        HASIL_FAHRENHEIT_CELCIUS.set((5/9) * (a - 32))
        HASIL_FAHRENHEIT_KELVIN.set((5/9 * (a - 32)) + 273.15)
        HASIL_FAHRENHEIT_REAMUR.set((4/9) * (a - 32))

    def kelvin():
        a = KELVIN.get()
        HASIL_KELVIN_CELCIUS.set(a - 273.15)
        HASIL_KELVIN_FAHRENHEIT.set((a * 9/5) - 459.67)
        HASIL_KELVIN_REAMUR.set((4/5) * (a - 273))


    def pilih_mode():
        for widget in input_frame.winfo_children():
            widget.destroy()

        if MODE_KIMIA.get() == "celcius":
            celcius_label = ttk.Label(input_frame,text="CELCIUS : ")
            celcius_label.pack(padx=10,fill="x",expand=True)

            celcius_entry = ttk.Entry(input_frame,textvariable=CELCIUS)
            celcius_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hasil = ttk.Button(input_frame,text="HITUNG",command=celcius)
            Tombol_hasil.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label_celcius_f = ttk.Label(input_frame,text="HASIL CELCIUS TO FAHRENHEIT: ")
            hasil_label_celcius_f.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_celcius_f = ttk.Label(input_frame,textvariable=HASIL_CELCIUS_FAHRENHEIT)
            hasil_entry_celcius_f.pack(padx=10,fill="x",expand=True)

            hasil_label_celcius_k = ttk.Label(input_frame,text="HASIL CELCIUS TO KELVIN: ")
            hasil_label_celcius_k.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_celcius_k = ttk.Label(input_frame,textvariable=HASIL_CELCIUS_KELVIN)
            hasil_entry_celcius_k.pack(padx=10,fill="x",expand=True)

            hasil_label_celcius_r = ttk.Label(input_frame,text="HASIL CELCIUS TO REAMUR: ")
            hasil_label_celcius_r.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_celcius_r = ttk.Label(input_frame,textvariable=HASIL_CELCIUS_REAMUR)
            hasil_entry_celcius_r.pack(padx=10,fill="x",expand=True)

        if MODE_KIMIA.get() == "fahrenheit":
            fahrenheit_label = ttk.Label(input_frame,text="FAHRENHEIT : ")
            fahrenheit_label.pack(padx=10,fill="x",expand=True)

            fahrenheit_entry = ttk.Entry(input_frame,textvariable=FAHRENHEIT)
            fahrenheit_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hasil = ttk.Button(input_frame,text="HITUNG",command=fahrenheit)
            Tombol_hasil.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label_fahrenheit_c = ttk.Label(input_frame,text="HASIL FAHRENHEIT TO CELCIUS: ")
            hasil_label_fahrenheit_c.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_fahrenheit_c = ttk.Label(input_frame,textvariable=HASIL_FAHRENHEIT_CELCIUS)
            hasil_entry_fahrenheit_c.pack(padx=10,fill="x",expand=True)

            hasil_label_fahrenheit_k = ttk.Label(input_frame,text="HASIL FAHRENHEIT TO KELVIN: ")
            hasil_label_fahrenheit_k.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_fahrenheit_k = ttk.Label(input_frame,textvariable=HASIL_FAHRENHEIT_KELVIN)
            hasil_entry_fahrenheit_k.pack(padx=10,fill="x",expand=True)

            hasil_label_fahrenheit_r = ttk.Label(input_frame,text="HASIL FAHRENHEIT TO REAMUR: ")
            hasil_label_fahrenheit_r.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_fahrenheit_r = ttk.Label(input_frame,textvariable=HASIL_FAHRENHEIT_REAMUR)
            hasil_entry_fahrenheit_r.pack(padx=10,fill="x",expand=True)

        if MODE_KIMIA.get() == "kelvin":
            kelvin_label = ttk.Label(input_frame,text="KELVIN : ")
            kelvin_label.pack(padx=10,fill="x",expand=True)

            kelvin_entry = ttk.Entry(input_frame,textvariable=KELVIN)
            kelvin_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hasil = ttk.Button(input_frame,text="HITUNG",command=kelvin)
            Tombol_hasil.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label_kelvin_c = ttk.Label(input_frame,text="HASIL KELVIN TO CELCIUS: ")
            hasil_label_kelvin_c.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_kelvin_c = ttk.Label(input_frame,textvariable=HASIL_KELVIN_CELCIUS)
            hasil_entry_kelvin_c.pack(padx=10,fill="x",expand=True)

            hasil_label_kelvin_f = ttk.Label(input_frame,text="HASIL KELVIN TO FAHRENHEIT: ")
            hasil_label_kelvin_f.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_kelvin_f = ttk.Label(input_frame,textvariable=HASIL_KELVIN_FAHRENHEIT)
            hasil_entry_kelvin_f.pack(padx=10,fill="x",expand=True)

            hasil_label_kelvin_r = ttk.Label(input_frame,text="HASIL KELVIN TO REAMUR: ")
            hasil_label_kelvin_r.pack(padx=10,fill="x",expand=True)
            
            hasil_entry_kelvin_r = ttk.Label(input_frame,textvariable=HASIL_KELVIN_REAMUR)
            hasil_entry_kelvin_r.pack(padx=10,fill="x",expand=True)

    mode_label = ttk.Label(input_frame, text="Pilih Perhitungan Suhu:")
    mode_label.pack(fill="x", pady=5)

    mode_box = ttk.Combobox(input_frame, textvariable=MODE_KIMIA,values=["celcius", "fahrenheit", "kelvin"],state="readonly")
    mode_box.pack(fill="x", pady=5)

    Tombol_pilih = ttk.Button(input_frame,text="PILIH",command=pilih_mode)
    Tombol_pilih.pack(fill='x',expand=True,padx=10,pady=10)