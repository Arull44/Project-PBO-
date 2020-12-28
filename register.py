import sqlite3
from database import data_manager

class register(data_manager):    
    def __init__(self, nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota):
        super().__init__()
        self.__nama_penyewa = nama_penyewa
        self.__username = username
        self.__password = password
        self.__tanggal_lahir = tanggal_lahir
        self.__nomor_telepon = nomor_telepon
        self.__alamat = alamat
        self.__nama_kota = nama_kota

    def register(self):
        self.query = 'INSERT INTO penyewa(nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota) VALUES (\'%s\',\'%s\',\'%s\',\'%s\', \'%s\', \'%s\',\'%s\')'
        self.query = self.query % (self.__nama_penyewa, self.__username, self.__password, self.__tanggal_lahir, self.__nomor_telepon, self.__alamat, self.__nama_kota) 
        self.exe_query(self.query)
        print('data berhasil didaftarkan')

# penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
# penyewa_add.register()