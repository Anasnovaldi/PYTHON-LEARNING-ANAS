from . import Operasi
import os
DB_NAME = os.path.join(os.path.dirname(__file__),"data.txt")
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "aktivitas":255*" ",
    "goals":255*" ",
    "tanggal":"yyyy-mm-dd"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()