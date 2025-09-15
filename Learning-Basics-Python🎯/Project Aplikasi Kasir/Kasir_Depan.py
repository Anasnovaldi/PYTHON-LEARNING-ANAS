# sales.py
from List_barang import barang

def jual_barang(nama, jumlah):
    """Mengurangi stok saat barang terjual"""
    if nama not in barang:
        print(f"Barang {nama} tidak ditemukan.")
        return
    
    if barang[nama]["stok"] >= jumlah:
        barang[nama]["stok"] -= jumlah
        total = barang[nama]["harga"] * jumlah
        print(f"Berhasil menjual {jumlah} {nama}. Total: Rp{total:,}")
    else:
        print(f"Stok {nama} tidak mencukupi! Sisa stok: {barang[nama]['stok']}")
