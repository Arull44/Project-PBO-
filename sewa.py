import sqlite3
from penyewa import penyewa
from mobil import mobil


class sewa():
    def __init__(self):
        self.con = sqlite3.connect("sewamobil.sqlite")       
        self.cursor = self.con.cursor()
        self.__lama_sewa = 0
        self.__id_mobil = 0
        self.__id_penyewa = 0
        self.get_harga_total()
        self.__set_harga_total()   

    def set_data_sewa(self):
        self.__id_penyewa = int(input('ID anda: '))
        self.__id_mobil = int(input('masukkan id mobil yang disewa: '))
        self.__lama_sewa = int(input('berapa lama anda menyewa mobil: '))
        self.query = 'INSERT INTO sewa (id_penyewa, id_mobil, lama_sewa) VALUES (?, ?, ?)'
        self.cursor.execute(self.query, [self.__id_penyewa, self.__id_mobil, self.__lama_sewa])
        self.con.commit()
        print ('berhasil menyewa')

    def get_id_penyewa(self):
        return self.__id_penyewa

    def get_id_mobil(self):
        return self.__id_mobil

    def get_lama_sewa(self):
        return self.__lama_sewa

    def __set_harga_total(self):
        self.query = 'SELECT harga_sewa FROM sewa JOIN mobil ON sewa.id_mobil = mobil.id WHERE mobil.id = ?'
        self.cursor.execute(self.query, [self.get_id_mobil()])
        self.con.commit()
        result = self.cursor.fetchone()
        if(result):
            return self.get_lama_sewa() * int(result[0])

    def get_harga_total(self):
        return self.__set_harga_total()

    def close_database(self):
        self.con.close()

# sewa_mobil = sewa()
# sewa_mobil.set_data_sewa()
# print('TOTAL HARGA SEWA:', sewa_mobil.get_harga_total())

