import sqlite3
from login import login
from register import register
from penyewa import penyewa
# from mobil import mobil
from pengembalian import pengembalian

# main
def show_menu():
    print(('-----------------')*5)
    print('''*****Sewa Mobil Carents*****
    Pilih menu:
    1. Tampilkan daftar data diri
    2. Tampilkan daftar mobil
    3. Batalkan sewa mobil
    4. Tampilkan total denda (jika terlambat mengembalikan)
    5. Log out''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

show_menu()

    # def interface_login(self):
    #     print(('-----------------')*5)
    #     print('''*****Sewa Mobil Carents*****
    #     Pilih menu:
    #     sudah punya akun?
    #     1. Login
    #     belum punya akun?
    #     2. Registrasi''')
    #     pilihan = input('masukkan pilihan anda: ')
    #     return pilihan

# jalan = menu_utama()

# start = True
# while start:
#     pilihan = jalan.interface_login()
#     if pilihan == '1':
#         login.input_login()
#     elif pilihan == '2':
#         penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
#         penyewa_add.register()
    
