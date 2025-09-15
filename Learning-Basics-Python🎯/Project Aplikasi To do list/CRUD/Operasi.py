from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_list):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_list - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.replace("data_temp.txt",Database.DB_NAME)

def update(no_list,pk,data_add,tanggal,aktivitas,goals):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["goals"] = goals + Database.TEMPLATE["goals"][len(goals):]
    data["aktivitas"] = aktivitas + Database.TEMPLATE["aktivitas"][len(aktivitas):]
    data["tanggal"] = str(tanggal)

    data_str = f'{data["pk"]},{data["date_add"]},{data["aktivitas"]},{data["goals"]},{data["tanggal"]}\n'
    
    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_list-1))
            file.write(data_str)
    except:
        print("error dalam update data")

def create(tanggal,aktivitas,goals):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["goals"] = goals + Database.TEMPLATE["goals"][len(goals):]
    data["aktivitas"] = aktivitas + Database.TEMPLATE["aktivitas"][len(aktivitas):]
    data["tanggal"] = tanggal

    data_str = f'{data["pk"]},{data["date_add"]},{data["aktivitas"]},{data["goals"]},{data["tanggal"]}\n'

    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")

def create_first_data():
    aktivitas = input("Aktivitas: ")
    goals = input("Goals: ")
    while(True):
        try:
            tanggal = input("Tanggal\t: ")
            if len(tanggal) == 10:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy/mm/dd)")    
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy/mm/dd)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["goals"] = goals + Database.TEMPLATE["goals"][len(goals):]
    data["aktivitas"] = aktivitas + Database.TEMPLATE["aktivitas"][len(aktivitas):]
    data["tanggal"] = tanggal

    data_str = f'{data["pk"]},{data["date_add"]},{data["goals"]},{data["aktivitas"]},{data["tanggal"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_list = len(content)
            if "index" in kwargs:
                index_list = kwargs["index"]-1
                if index_list < 0 or index_list > jumlah_list:
                    return False
                else:    
                    return content[index_list]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    