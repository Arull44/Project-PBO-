import sqlite3
from database import data_manager

class register():    
    def __init__(self):
        self.__nama_penyewa = ''
        self.__nama_petugas = ''
        self.__username = ''
        self.__password = ''
        self.__tanggal_lahir = ''
        self.__nomor_telepon = ''
        self.__alamat = ''
        self.__nama_kota = ''
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def register_penyewa(self):
        self.__nama_penyewa = input("masukkan nama anda: ")
        self.__username = input("masukkan username: ")
        self.__password = input("masukkan password: ")
        self.__tanggal_lahir = input("masukkan tanggal lahir anda (YYYY-MM-DD): ")
        self.__nomor_telepon = input("masukkan nomor telepon: ")
        self.__alamat = input("masukkan alamat anda: ")
        self.__nama_kota = input("masukkan kota anda: ")
        self.query = 'INSERT INTO penyewa(nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota) VALUES (?, ?, ?, ?, ?, ?, ?)'
        self.cursor.execute(self.query, [self.__nama_penyewa, self.__username, self.__password, self.__tanggal_lahir, self.__nomor_telepon, self.__alamat, self.__nama_kota])
        self.con.commit()
        self.con.close()
        print('data berhasil didaftarkan')
    
    def register_petugas(self):
        self.__nama_petugas = input("masukkan nama anda: ")
        self.__username = input("masukkan username: ")
        self.__password = input("masukkan password: ")
        self.query = 'INSERT INTO petugas(nama_petugas, username, password) VALUES (?, ?, ?)'
        self.cursor.execute(self.query, [self.__nama_petugas, self.__username, self.__password])
        self.con.commit()
        self.con.close()
        print('data berhasil didaftarkan')

# penyewa_add = register()
# penyewa_add.register()
# petugas_add = register()
# petugas_add.register_petugas()