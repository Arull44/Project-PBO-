import sqlite3
import os

from register import register
from mobil import mobil
from penyewa import penyewa
from sewa import sewa
from petugas import petugas
from pengembalian import pengembalian

con = sqlite3.connect("sewamobil.sqlite")
cursor = con.cursor()

akun = []

class set_login:
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password

    def set_login_penyewa(self):
        query = 'SELECT username, password FROM penyewa WHERE username = ? AND password = ?'
        cursor.execute(query, [self.username, self.password])
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
        query = 'SELECT username, password FROM petugas WHERE username = ? AND password = ?'
        cursor.execute(query, [self.username, self.password])
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
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Data diri
    2. Data mobil
    3. Log out''')
    print('')

def tampilkan_datadiri_by_petugas():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data diri petugas
    2. Lihat data diri penyewa
    3. Ubah data diri petugas
    4. Hapus data diri petugas
    5. Hapus data diri penyewa
    6. Back''')
    print('')

def tampilkan_datamobil_by_petugas():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data mobil
    2. Tambah data mobil
    3. Ubah data mobil
    4. Hapus data mobil
    5. Back''')
    print('')

def tampilkan_menu():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Data diri
    2. Sewa mobil
    3. Tampilkan total denda (jika terlambat mengembalikan)
    4. Log out''')
    print('')

def tampilan_menu_penyewa():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Lihat data diri
    2. Ubah data diri
    3. Back''')
    print('')

def tampilkan_mobil_penyewa():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Sewa mobil
    2. Back''')
    print('')

def sewa_mobil():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Back''')
    print('')

def tampilkan_denda():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    1. Denda
    2. Back''')
    print('')

def pilihan_login():
    print(('-')*80)
    print('''                           *****Sewa Mobil Carents*****
    sebagai:
    1. Petugas
    2. Penyewa''')
clear = lambda: os.system('cls')

def main():
    start = True
    while start:
        print('''                           *****Sewa Mobil Carents*****
    Pilih menu:
    sudah punya akun?
    1. Login
    belum punya akun?
    2. Registrasi''')
        pilihan = input('masukkan pilihan anda: ')
        if pilihan == '1':
            pilihan_login()
            pilih_role = input('masukkan pilihan: ')
            if pilih_role == '1':
                username = input('masukkan username anda: ')
                password = input('masukkan password: ')
                login = set_login(username, password).set_login_petugas()
                while True:
                    tampilkan_menu_by_petugas()
                    pilih_menu = input('masukkan pilihan anda: ')
                    if pilih_menu == '1':
                        tampilkan_datadiri_by_petugas()
                        pilih_menu = input('masukkan pilihan anda: ')
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
                            print('*****Hapus data petugas')
                            user = petugas().delete_petugas()

                        elif pilih_menu == '5':
                            print('*****Hapus data penyewa')
                            user = petugas().delete_penyewa()   

                        elif pilih_menu == '6':
                            tampilkan_menu_by_petugas()
                            clear()
                        else:
                            print('pilihan tidak ada')

                    elif pilih_menu == '2':
                        tampilkan_datamobil_by_petugas()
                        pilih_menu = input('masukkan pilihan anda: ')
                        if pilih_menu == '1':
                            print('*****Lihat data mobil*****')
                            data_mobil = mobil().get_data_mobil_fullset()
                        
                        elif pilih_menu == '2':
                            print('*****Tambah data mobil*****')
                            data_mobil = mobil().tambah_mobil()
                        
                        elif pilih_menu == '3':
                            print('*****Ubah data mobil*****')
                            data_mobil = mobil().update_mobil_byID()

                        elif pilih_menu == '4':
                            print('*****Hapus data mobil*****')
                            data_mobil = mobil().delete_mobil_byID()
                        
                        elif pilih_menu == '5':
                            tampilkan_menu_by_petugas()
                            clear()
                        else:
                            print('pilihan tidak ada')

                    elif pilih_menu == '3':
                        exit()
                    
                    else:
                        print('pilihan tidak ada')

            elif pilih_role == '2':
                username = input('masukkan username anda: ')
                password = input('masukkan password: ')
                login = set_login(username, password).set_login_penyewa()

                while True:
                    tampilkan_menu()
                    pilih_menu = input('masukkan pilihan anda: ')
                    if pilih_menu == '1':
                        tampilan_menu_penyewa()
                        pilih_menu = input('masukkan pilihan anda: ')
                        if pilih_menu == '1':
                            print('*****Lihat data penyewa*****')
                            user = penyewa().get_data_penyewa_by_penyewa()
                        elif pilih_menu == '2':
                            print('*****Update data penyewa*****')
                            user = penyewa().update_penyewa()
                        elif pilih_menu == '3':
                            tampilkan_menu()
                            clear()
                        else:
                            print('pilihan tidak ada')

                    elif pilih_menu == '2':
                        tampilkan_mobil_penyewa()
                        pilih_menu = input('masukkan pilihan anda: ')
                        if pilih_menu == '1':
                            print('*****Sewa Mobil*****')
                            data_mobil = mobil().get_data_mobil_fullset()
                            sewa_mobil = sewa()
                            sewa_mobil.set_data_sewa()
                            print("Total harga = Rp.", "{:,}".format(sewa_mobil.get_harga_total()))
                            sewa_mobil.close_database()

                        elif pilih_menu == '2':
                            tampilkan_menu()
                            clear()
                        else:
                            print('pilihan tidak ada')

                    elif pilih_menu == '3':
                        tampilkan_denda()
                        pilih_menu = input('masukkan pilihan anda: ')
                        if pilih_menu == '1':
                            print('*****Denda pengembalian*****')
                            total_denda = pengembalian(input('terlambat berapa hari: '), input('ID sewa: ')).get_denda()
                            print("Total denda = Rp.", "{:,}".format(total_denda))
                        elif pilih_menu == '2':
                            tampilkan_menu()
                            clear()
                        else:
                            print('pilihan tidak ada')

                    elif pilih_menu == '4':
                        exit()

                    else:
                        print('pilihan tidak ada')

        elif pilihan == '2':
            pilihan_login()
            pilih_role = input('masukkan pilihan: ')
            if pilih_role == '1':
                petugas_add = register()
                petugas_add.register_petugas()  
            elif pilih_role == '2':
                add_penyewa = register()
                add_penyewa.register_penyewa()

        else:
            print('menu tidak ada')
    return False

main()