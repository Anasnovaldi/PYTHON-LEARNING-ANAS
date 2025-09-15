import tkinter as tk
from tkinter import ttk

def tombol_matematika(input_frame, ANGKA1, ANGKA2, HASIL_TAMBAH, HASIL_KURANG, HASIL_KALI, HASIL_BAGI, MODE_MATEMATIKA):
    def hitung():
        a = ANGKA1.get()
        b = ANGKA2.get()
        HASIL_TAMBAH.set(a + b)
        HASIL_KURANG.set(a - b)
        HASIL_KALI.set(a * b)
        HASIL_BAGI.set(a / b)

    def pilih_mode():
        for widget in input_frame.winfo_children():
            widget.destroy()

        if MODE_MATEMATIKA.get() == "tambah":
            angka1_label = ttk.Label(input_frame,text="ANGKA 1 : ")
            angka1_label.pack(padx=10,fill="x",expand=True)
            angka1_entry = ttk.Entry(input_frame,textvariable=ANGKA1)
            angka1_entry.pack(padx=10,fill="x",expand=True)

            angka2_label = ttk.Label(input_frame,text="ANGKA 2 : ")
            angka2_label.pack(padx=10,fill="x",expand=True)
            angka2_entry = ttk.Entry(input_frame,textvariable=ANGKA2)
            angka2_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=hitung)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL TAMBAH: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_TAMBAH)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_MATEMATIKA.get() == "kurang":
            angka1_label = ttk.Label(input_frame,text="ANGKA 1 : ")
            angka1_label.pack(padx=10,fill="x",expand=True)
            angka1_entry = ttk.Entry(input_frame,textvariable=ANGKA1)
            angka1_entry.pack(padx=10,fill="x",expand=True)

            angka2_label = ttk.Label(input_frame,text="ANGKA 2 : ")
            angka2_label.pack(padx=10,fill="x",expand=True)
            angka2_entry = ttk.Entry(input_frame,textvariable=ANGKA2)
            angka2_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=hitung)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL KURANG: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_KURANG)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_MATEMATIKA.get() == "kali":
            angka1_label = ttk.Label(input_frame,text="ANGKA 1 : ")
            angka1_label.pack(padx=10,fill="x",expand=True)
            angka1_entry = ttk.Entry(input_frame,textvariable=ANGKA1)
            angka1_entry.pack(padx=10,fill="x",expand=True)

            angka2_label = ttk.Label(input_frame,text="ANGKA 2 : ")
            angka2_label.pack(padx=10,fill="x",expand=True)
            angka2_entry = ttk.Entry(input_frame,textvariable=ANGKA2)
            angka2_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=hitung)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL KALI: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_KALI)
            hasil_entry.pack(padx=10,fill="x",expand=True)

        elif MODE_MATEMATIKA.get() == "bagi":
            angka1_label = ttk.Label(input_frame,text="ANGKA 1 : ")
            angka1_label.pack(padx=10,fill="x",expand=True)
            angka1_entry = ttk.Entry(input_frame,textvariable=ANGKA1)
            angka1_entry.pack(padx=10,fill="x",expand=True)

            angka2_label = ttk.Label(input_frame,text="ANGKA 2 : ")
            angka2_label.pack(padx=10,fill="x",expand=True)
            angka2_entry = ttk.Entry(input_frame,textvariable=ANGKA2)
            angka2_entry.pack(padx=10,fill="x",expand=True)

            Tombol_hitung = ttk.Button(input_frame,text="HITUNG",command=hitung)
            Tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

            hasil_label = ttk.Label(input_frame,text="HASIL BAGI: ")
            hasil_label.pack(padx=10,fill="x",expand=True)
            hasil_entry = ttk.Label(input_frame,textvariable=HASIL_BAGI)
            hasil_entry.pack(padx=10,fill="x",expand=True)

    mode_label = ttk.Label(input_frame, text="Pilih Perhitungan Matematika:")
    mode_label.pack(fill="x", pady=5)

    mode_box = ttk.Combobox(input_frame, textvariable=MODE_MATEMATIKA,values=["tambah", "kurang", "kali", "bagi"],state="readonly")
    mode_box.pack(fill="x", pady=5)

    Tombol_pilih = ttk.Button(input_frame,text="PILIH",command=pilih_mode)
    Tombol_pilih.pack(fill='x',expand=True,padx=10,pady=10)