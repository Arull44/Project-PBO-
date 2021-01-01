import sqlite3
from register import register

class penyewa(register):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def get_data_penyewa_by_penyewa(self):
        username = input('masukkan username anda: ')
        self.query = 'SELECT nama_penyewa, username, password, tanggal lahir, nomor_telepon, alamat, nama_kota FROM penyewa WHERE username = ?'
        self.cursor.execute(self.query, [username])
        self.con.commit()
        self.result = self.cursor.fetchone()
        print (result)
        self.con.close()

    def update_penyewa(self):
        username = input("masukkan username: ")
        self.__nama_penyewa = input("masukkan nama anda: ")
        self.__username = input("masukkan username: ")
        self.__password = input("masukkan password: ")
        self.__tanggal_lahir = input("masukkan tanggal lahir anda (YYYY-MM-DD): ")
        self.__nomor_telepon = input("masukkan nomor telepon: ")
        self.__alamat = input("masukkan alamat anda: ")
        self.__nama_kota = input("masukkan kota anda: ")
        self.query = '''UPDATE penyewa SET nama_penyewa = ?, username = ?, password = ?, tanggal_lahir = ?, nomor_telepon = ?, alamat = ?, nama_kota = ? WHERE username = ?'''
        self.cursor.execute(self.query, [self.__nama_penyewa, self.__username, self.__password, self.__tanggal_lahir, self.__nomor_telepon, self.__alamat, self.__nama_kota, username])
        self.con.commit()
        self.con.close()
        print('data berhasil diubah')

# penyewa = penyewa()
# penyewa.get_data_penyewa()
# penyewa.delete_penyewa()
# penyewa.update_penyewa(input('masukkan id atau username: '))