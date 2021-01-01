import sqlite3

from register import register
from mobil import mobil
from penyewa import penyewa
from sewa import sewa
from petugas import petugas

con = sqlite3.connect("sewamobil.sqlite")
cursor = con.cursor()

class set_login:
    def __init__(self,username = None, password = None):
        self.username = username
        self.password = password

    def set_login_penyewa(self):
        akun = []
        query = 'SELECT * FROM penyewa WHERE username = username AND password = password'
        cursor.execute(query)
        con.commit()
        result = cursor.fetchone()
        if(result):
            akun.append(result)
            print("Selamat datang")
        else:
            print("Username atau password salah")
            return result
        con.close()

    def set_login_petugas(self):
        akun = []
        query = 'SELECT * FROM petugas WHERE username = username AND password = password'
        cursor.execute(query)
        con.commit()
        result = cursor.fetchone()
        if(result):
            akun.append(result)
            print("Selamat datang")
        else:
            print("Username atau password salah")
            return result
        con.close()

def tampilkan_menu_by_petugas():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Data diri
    2. Data mobil
    3. Log out''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilkan_datadiri_by_petugas():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data diri petugas
    2. Lihat data diri penyewa
    3. Ubah data diri petugas
    4. Hapus data diri penyewa
    5. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilkan_datamobil_by_petugas():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data mobil
    2. Ubah data mobil
    3. Hapus data mobil
    4. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilkan_menu():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Data diri
    2. Sewa mobil
    3. Tampilkan total denda (jika terlambat mengembalikan)
    4. Log out''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilan_menu_penyewa():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data diri
    2. Ubah data diri
    3. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilkan_mobil_penyewa():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat mobil
    2. Sewa mobil
    3. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def lihat_mobil():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu

def tampilkan_denda():
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Denda
    2. Back''')
    pilih_menu = input('masukkan pilihan anda: ')
    return pilih_menu


start = True
while start:
    print(('-----------------')*10)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    sudah punya akun?
    1. Login
    belum punya akun?
    2. Registrasi''')
    pilihan = input('masukkan pilihan anda: ')
    if pilihan == '1':
        print(('-----------------')*10)
        print('''                       *****Sewa Mobil Carents*****
        sebagai:
        1. Petugas
        2. Penyewa''')
        pilih_role = input('masukkan pilihan: ')
        if pilih_role == '1':
            username = input('masukkan username anda: ')
            password = input('masukkan password: ')
            login = set_login(username, password).set_login_petugas()
            while True:
                pilih_menu = tampilkan_menu_by_petugas()
                if pilih_menu == '1':
                    pilih_menu = tampilkan_datadiri_by_petugas()
                    if pilih_menu == '1':
                        print('*****Lihat data petugas*****')
                        user = petugas().get_data_petugas()

                    elif pilih_menu == '2':
                        print('*****Lihat data penyewa*****')
                        user = petugas().get_data_penyewa()

                    elif pilih_menu == '3':
                        print('*****Update data penyewa*****')
                        user = petugas().update_petugas()
                    
                    elif pilih_menu == '4':
                        print('*****Hapus data penyewa')
                        user = petugas().delete_penyewa()
                    elif pilih_menu == '5':
                        tampilkan_menu_by_petugas()

                elif pilih_menu == '2':
                    pilih_menu = tampilkan_datamobil_by_petugas()
                    if pilih_menu == '1':
                        print('*****Lihat data mobil*****')
                        data_mobil = mobil().get_data_mobil_fullset()
                    
                    elif pilih_menu == '2':
                        print('*****Ubah data mobil*****')
                        data_mobil = mobil().update_mobil_byID()
                    
                    elif pilih_menu == '3':
                        print('*****Hapus data mobil*****')
                        data_mobil = mobil().delete_mobil_byID()

                    elif pilih_menu == '4':
                        tampilkan_menu_by_petugas()

                elif pilih_menu == '3':
                    exit()
        elif pilih_role == '2':
            username = input('masukkan username anda: ')
            password = input('masukkan password: ')
            login = set_login(username, password).set_login_penyewa()
            while True:
                pilih_menu = tampilkan_menu()
                if pilih_menu == '1':
                    pilih_menu = tampilan_menu_penyewa()
                    if pilihan == '1':
                        print('*****Lihat data penyewa*****')
                        user = penyewa().get_data_penyewa_by_penyewa()
                    elif pilihan == '2':
                        print('*****Update data penyewa*****')
                        user = penyewa().update_penyewa()
                    elif pilihan == '3':
                        tampilkan_menu()

                elif pilih_menu == '2':
                    pilih_menu = tampilkan_mobil_penyewa()
                    if pilihan == '1':
                        print('*****Lihat data Mobil*****')
                        data_mobil = mobil().get_data_mobil_fullset()
                    elif pilihan == '2':
                        print('*****Sewa mobil*****')
                        sewa_mobil = sewa().set_data_sewa()
                    elif pilihan == '3':
                        tampilkan_menu()

                elif pilih_menu == '3':
                    pilih_menu = tampilkan_denda()

                elif pilih_menu == '4':
                    exit()
    elif pilihan == '2':
        print(('-----------------')*10)
        print('''                          *****Sewa Mobil Carents*****
        sebagai:
        1. Petugas
        2. Penyewa''')
        pilih_role = input('masukkan pilihan: ')
        if pilih_role == '1':
            petugas_add = register()
            petugas_add.register_petugas()  
        elif pilih_role == '2':
            add_penyewa = register()
            add_penyewa.register_penyewa()

