import tkinter as tk
from tkinter import ttk

def tombol_fisika(input_frame, MASSA, VOLUME, KECEPATAN, JARAK, WAKTU, PERCEPATAN,HASIL_JARAK, HASIL_MASSA_JENIS, HASIL_KECEPATAN, HASIL_GAYA, MODE_FISIKA):

    def jarak():
        a = KECEPATAN.get()
        b = WAKTU.get()
        HASIL_JARAK.set(a * b)

    def gaya():
        a = MASSA.get()
        b = PERCEPATAN.get()
        HASIL_GAYA.set(a * b)

    def massa_jenis():
        a = MASSA.get()
        b = VOLUME.get()
        HASIL_MASSA_JENIS.set(a / b)

    def kecepatan():
        a = JARAK.get()
        b = WAKTU.get()
        HASIL_KECEPATAN.set(a / b)

    def pilih_mode():
        for widget in input_frame.winfo_children():
            widget.destroy()

        if MODE_FISIKA.get() == "Massa jenis":
            massa_label = ttk.Label(input_frame,text="MASSA : ")
            massa_label.pack(padx=10,fill="x",expand=True)
            massa_entry = ttk.Entry(input_frame,textvariable=MASSA)
            massa_entry.pack(padx=10,fill="x",expand=True)

            volume_label = ttk.Label(input_frame,text="VOLUME: ")
            volume_label.pack(padx=10,fill="x",expand=True)
            volume_entry = ttk.Entry(input_frame,textvariable=VOLUME)
            volume_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=massa_jenis)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL MASSA JENIS: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_MASSA_JENIS)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_FISIKA.get() == "gaya":
            massa_label = ttk.Label(input_frame,text="MASSA : ")
            massa_label.pack(padx=10,fill="x",expand=True)
            massa_entry = ttk.Entry(input_frame,textvariable=MASSA)
            massa_entry.pack(padx=10,fill="x",expand=True)

            percepatan_label = ttk.Label(input_frame,text="PERCEPATAN: ")
            percepatan_label.pack(padx=10,fill="x",expand=True)
            percepatan_entry = ttk.Entry(input_frame,textvariable=PERCEPATAN)
            percepatan_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=gaya)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL GAYA: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_GAYA)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_FISIKA.get() == "jarak":
            kecepatan_label = ttk.Label(input_frame,text="KECEPATAN : ")
            kecepatan_label.pack(padx=10,fill="x",expand=True)
            kecepatan_entry = ttk.Entry(input_frame,textvariable=KECEPATAN)
            kecepatan_entry.pack(padx=10,fill="x",expand=True)

            waktu_label = ttk.Label(input_frame,text="WAKTU: ")
            waktu_label.pack(padx=10,fill="x",expand=True)
            waktu_entry = ttk.Entry(input_frame,textvariable=WAKTU)
            waktu_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=jarak)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL JARAK: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_JARAK)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_FISIKA.get() == "kecepatan":
            jarak_label = ttk.Label(input_frame,text="JARAK : ")
            jarak_label.pack(padx=10,fill="x",expand=True)
            jarak_entry = ttk.Entry(input_frame,textvariable=JARAK)
            jarak_entry.pack(padx=10,fill="x",expand=True)

            waktu_label = ttk.Label(input_frame,text="WAKTU: ")
            waktu_label.pack(padx=10,fill="x",expand=True)
            waktu_entry = ttk.Entry(input_frame,textvariable=WAKTU)
            waktu_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=kecepatan)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL KECEPATAN: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_KECEPATAN)
            hasil_entry.pack(padx=10,fill="x",expand=True)

    mode_label = ttk.Label(input_frame, text="Pilih Perhitugan Fisika:")
    mode_label.pack(fill="x", pady=5)

    mode_box = ttk.Combobox(input_frame, textvariable=MODE_FISIKA,values=["Massa jenis", "gaya", "jarak", "kecepatan"],state="readonly")
    mode_box.pack(fill="x", pady=5)

    Tombol_pilih = ttk.Button(input_frame,text="PILIH",command=pilih_mode)
    Tombol_pilih.pack(fill='x',expand=True,padx=10,pady=10)
