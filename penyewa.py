import sqlite3
from register import register

class penyewa(register):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def get_data_penyewa_by_penyewa(self):
        username = input('masukkan username anda: ')
        self.query = 'SELECT * FROM penyewa WHERE username = ?'
        self.cursor.execute(self.query, [username])
        self.con.commit()
        self.results = self.cursor.fetchall()
        for result in self.results:
            print('ID:', result[0])
            print('nama lengkap:', result[1])
            print('username:', result[2])
            print('password:', result[3])
            print('tanggal lahir:', result[4])
            print('nomor telepon:', result[5])
            print('alamat:', result[6])
            print('kota:', result[7])
            print()
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
        print('data berhasil diubah')
        self.con.close()

# penyewa = penyewa()
# penyewa.get_data_penyewa_by_penyewa()
# penyewa.delete_penyewa()
# penyewa.update_penyewa(input('masukkan id atau username: '))