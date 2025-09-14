# Nama : Dliya Syahla Hariyanto
# Nim : 2509116095
# minpro 

daftar_reservasi=[]
while True:
    print("-----Sistem Reservasi Nail Art-----")
    print("1. tambah data")
    print("2. lihat data")
    print("3. edit data")
    print("4. hapus data")
    print("5. keluar")

    menu = input("pilih menu (1/2/3/4/5): ")

    if menu=="1":
        Nama=input("Nama: ")
        Layanan=input("layanan: ")
        Harga=input("harga: ")
        tanggal=input("Tanggal: ")
        jam=input("jam: ")
        daftar_reservasi=[(Nama,Layanan,Harga,tanggal,jam)]
        print("data berhasil di tambah")

    elif menu=="2":
        if daftar_reservasi:
            print("data sekarang:",daftar_reservasi)
        else:
            print("belum ada data")

    elif menu=="3":
        if daftar_reservasi:
            edit=input("edit data? y/n: ")
            if edit =="y":
                Nama=input("Nama: ")
                Layanan=input("layanan: ")
                Harga=input("harga: ")
                tanggal=input("Tanggal: ")
                jam=input("jam: ")
                daftar_reservasi=[(Nama,Layanan,Harga,tanggal,jam)]
                print("data berhasil diedit")
        else:
                print("belum ada data di edit")

    elif menu =="4":
        if daftar_reservasi:
            hapus=input("hapus data? y/n: ")
            if hapus=="y":
                daftar_reservasi=[]
                print("data berhasil di hapus")
        else:
                print("belum ada data di hapus")

    elif menu=="5":
        print("kelua")
        break
    else:
        print("menu tidak ada")





                    









    
        







