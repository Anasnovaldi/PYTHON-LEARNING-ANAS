from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor rencana yang akan di delete")
        no_list = int(input("Nomor rencana: "))
        data_list = Operasi.read(index=no_list)

        if data_list:
            data_break = data_list.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            aktivitas = data_break[2]
            goals = data_break[3]
            tanggal = data_break[4].strip()

    
            # data yang ingin diupdate
            print("\n"+"="*120)
            print("Data yang ingin anda Hapus")
            print(f"1. aktivitas\t: {aktivitas:.40}")
            print(f"2. goals\t: {goals:.40}")
            print(f"3. Tanggal\t: {tanggal:10}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_list)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")

            
def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor rencana yang akan di update")
        no_list = int(input("Nomor rencana: "))
        data_list = Operasi.read(index=no_list)

        if data_list:
            break
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    
    data_break = data_list.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    aktivitas = data_break[2]
    goals = data_break[3]
    tanggal = data_break[4][:-1]
    
    while(True):
        # data yang ingin diupdate
        print("\n"+"="*120)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. aktivitas\t: {aktivitas:.40}")
        print(f"2. goals\t: {goals:.40}")
        print(f"3. tanggal\t: {tanggal:10}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*120)
        match user_option:
            case "1": aktivitas = input("aktivitas\t: ")
            case "2": goals = input("goals\t: ")
            case "3": 
                while(True):
                    try:
                        tanggal = input(f"{'Tanggal':16}: ")
                        if len(tanggal) == 10:
                            break
                        else:
                            print("silahkan masukan tahun lagi (yyyy/mm/dd)")    
                    except:
                        print("tanggal harus angka, silahkan masukan tahun lagi (yyyy/mm/dd)")
            case _: print("index tidak cocok")

        print("Data baru anda")
        print(f"1. aktivitas\t: {aktivitas:.40}")
        print(f"2. goals\t: {goals:.40}")
        print(f"3. Tanggal\t: {tanggal:10}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(no_list,pk,data_add,tanggal,aktivitas,goals)
            


def create_console():
    print("\n\n"+"="*120)
    print("Silahkan tambah rencana\n")
    aktivitas = input("Aktivitas\t: ")
    goals = input(f"{'Goals':16}: ")
    while(True):
        try:
            tanggal = input(f"{'Tanggal':16}: ")
            if len(tanggal) == 10:
                break
            else:
                print("tanggal harus angka, silahkan masukan tanggal lagi (yyyy/mm/dd)")    
        except:
            print("tanggal harus angka, silahkan masukan tanggal lagi (yyyy/mm/dd)")

    Operasi.create(tanggal,aktivitas,goals)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    aktivitas = "Aktivitas"
    goals = "Goals"
    tanggal = "Tanggal"

    # Header
    print("\n"+"="*120)
    print(f"{index:4} | {aktivitas:40} | {goals:40} | {tanggal:11}")
    print("-"*120)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        if len(data_break) < 5:
            print(f"⚠️ Data tidak valid di baris {index+1}: {data_break}")
            continue
        pk = data_break[0]
        date_add = data_break[1]
        aktivitas = data_break[2]
        goals = data_break[3]
        tanggal = data_break[4]
        print(f"{index+1:4} | {aktivitas:.40} | {goals:.40} | {tanggal:10}",end="")

    # Footer
    print("="*120+"\n")