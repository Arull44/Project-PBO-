import sqlite3
from penyewa import penyewa
from mobil import mobil
from tipe_mobil import tipe_mobil


data_mobil = mobil()
tipe_mobil = tipe_mobil()
penyewa = penyewa()

class sewa():
    def __init__(self):
        self.__lama_sewa = None
        self.__id_mobil = None
        self.__id_penyewa = None
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def set_data_sewa(self):
        self.__id_penyewa = int(input('ID anda: '))
        self.__id_mobil = int(input('masukkan id mobil yang disewa: '))
        self.__lama_sewa = int(input('berapa lama anda menyewa mobil: '))
        self.query = 'INSERT INTO sewa (id_penyewa, id_mobil, lama_sewa) VALUES (?, ?, ?)'
        self.cursor.execute(self.query, [self.__id_penyewa, self.__id_mobil, self.__lama_sewa])
        self.con.commit()
        print ('berhasil menyewa')

    def get_harga_sewa(self):
        id = int(input('masukkan ID mobil yang disewa: '))
        self.query = 'SELECT harga_sewa FROM sewa JOIN mobil ON sewa.id_mobil = mobil.id WHERE id = ?'
        self.cursor.execute(self.query, [id])
        self.con.commit()
        return self.__harga_sewa

    def get_lama_sewa(self):
        self.id_sewa = int(input('masukkan id sewa: '))
        self.query = 'SELECT lama_sewa FROM sewa WHERE = ?'
        self.cursor.execute(self.query, [self.id_sewa])
        self.con.commit()
        return self.get_lama_sewa()

    def get_harga_total(self):
        return self.get_lama_sewa() * get_harga_sewa()

# sewa_mobil = sewa()
# sewa_mobil.set_data_sewa()

