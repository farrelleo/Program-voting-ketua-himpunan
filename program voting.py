#
import csv
#



def menu_utama():
    def calon():
        print("")
        print("DAFTAR CALON".center(100))
        print("")
        print('''
        1. Farrell / 2021
        2. Fari / 2021
        ''')

    def voting():
        in_nama = input("Masukkan nama lengkap anda : ")
        in_nim = input("Masukkan NIM anda : ")
        calon()
        pil_calon = int(input("Masukkan angka pilihan calon anda : "))
#input data ke csv
        data = in_nim.capitalize(), in_nama.capitalize(), pil_calon
        with open('log pemilih.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow(data)
        

    def pilihan_menu():
        print("-----------".center(100))
        print("DAFTAR MENU".center(100))
        print("-----------".center(100))
        print("")
        print("1. Melakukan Voting".center(100))
        print("2. Hasil voting    ".center(100))
        print("")
        pilihan = int(input("Masukkan menu pilihan anda : "))
        print("")
        if pilihan == 1:
            print("")
            voting()
        elif pilihan == 2:
            print("HASIL VOTING")
            #
            print("")
            keluar = input("Tekan ENTER untuk keluar")
            if keluar == "":
                pass
            else:
                pass
        else:
            print("PERIKSA PILIHAN ANDA KEMBALI !!!")
            print("*gunakan angka pada input")
    print("=========================".center(100))
    print("SELAMAT DATANG DI PROGRAM".center(100))
    print("PEMILIHAN KAHIM HMTI 2023".center(100))
    print("=========================".center(100))
    print("")
    pilihan_menu()


menu_utama()

# DAFTAR PERTANYAAN
# cara mengetahui apakah input sudah masuk ke file csv pada kolom sekian
# cara menghitung banyak data yang sama dalam 1 kolom file csv dari baris pertama-akhir

print("")
def hasil_voting():
    print("CALON 1")
    print("{}, JUMLAH SUARA : {}".format("NAMA", "<jumlah>"))
    print("CALON 2")
    print("{}, JUMLAH SUARA : {}".format("NAMA", "<jumlah>"))