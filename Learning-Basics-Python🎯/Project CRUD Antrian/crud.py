import os

FILE_NAME = "data.txt"

# ===== CREATE =====
def create(nama,keluhan,nomor):
    # buat id unik sederhana
    if not os.path.exists(FILE_NAME):
        pk = 1
    else:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            pk = len(lines) + 1
    
    with open(FILE_NAME, "a") as f:
        f.write(f"{pk},{nama},{keluhan},{nomor}\n")


# ===== READ =====
def read():
    if not os.path.exists(FILE_NAME):
        print("Belum ada data.")
        return
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    print(f"{"== DAFTAR ANTRIAN PASIEN ==":^100}")
    print(f'{"="*100:^100}')
    print(f"| {'ID':<5} | {'NAMA':<20} | {'KELUHAN':<20} | {'NOMOR':<10} |")
    print("-"*100)
    for line in lines:
        pk, nama, keluhan, nomor = line.strip().split(",")
        print(f"| {pk:<5} | {nama:<20} | {keluhan:<20} | {nomor:<10} |")


# ===== UPDATE =====
def update(pk, new_nama, new_keluhan, new_nomor):
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    
    with open(FILE_NAME, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == str(pk):
                f.write(f"{pk},{new_nama},{new_keluhan},{new_nomor}\n")
            else:
                f.write(line)


# ===== DELETE =====
def delete(pk):
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    
    with open(FILE_NAME, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] != str(pk):
                f.write(line)
