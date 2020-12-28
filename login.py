import sqlite3
from database import data_manager
from register import register

class login(data_manager):
    def input_login(self):
        self.username = input('masukkan username anda: ')
        self.password = input('masukkan password: ')
        for row in self.cursor.execute('SELECT * FROM penyewa WHERE username = username AND password = password'):
            if self.username and self.password in row:
                hal_utama = menu_utama()
                hal_utama.show_menu()
            else:
                print('data salah')
                return go.input_login()

    def hal_login(self):
        start = True
        while start:
            pilihan = interface_login()
            if pilihan == '1':
                go = login()
                go.hal_login()
            elif pilihan == '2':
                penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
                penyewa_add.register()

go = login()


def interface_login():
    print(('-----------------')*5)
    print('''*****Sewa Mobil Carents*****
    Pilih menu:
    sudah punya akun?
    1. Login
    belum punya akun?
    2. Registrasi''')
    pilihan = input('masukkan pilihan anda: ')
    return pilihan

# interface_login()