import sqlite3
from register import register

class petugas(register):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def get_data_petugas(self):
        self.query = '''SELECT * FROM petugas'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def update_petugas(self):
        username = input("masukkan username: ")
        self.__nama_petugas = input("masukkan nama anda: ")
        self.__username = input("masukkan username: ")
        self.__password = input("masukkan password: ")
        self.query = '''UPDATE petugas SET nama_petugas = ?, username = ?, password = ? WHERE username = ?'''
        self.cursor.execute(self.query, [self.__nama_petugas, self.__username, self.__password])
        self.con.commit()
        self.con.close()
        print('data berhasil diubah')

    def get_data_penyewa(self):
        self.query = '''SELECT * FROM penyewa'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def delete_penyewa(self):
        id = input('masukkan id: ')
        self.query = f'DELETE FROM penyewa WHERE id = ?'
        self.cursor.execute(self.query, [id])
        self.con.commit()
        self.con.close()
        print('data berhasil dihapus')

