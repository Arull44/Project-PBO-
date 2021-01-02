import sqlite3
from sewa import sewa

class pengembalian(sewa):
    def __init__(self, hari, id_sewa):
        super(sewa, self).__init__()
        self.denda_per_hari = 100000
        self.hari = hari
        self.id_sewa = id_sewa
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor() # kaya objek/perintah buat akses databasenya

    def get_hari(self):
        return self.hari
    
    def get_id_sewa(self):
        return self.id_sewa

    def __set_data_pengembalian(self):
        self.query = 'INSERT INTO pengembalian (hari, id_sewa) VALUES (?, ?)'
        self.cursor.execute(self.query, [self.get_hari(), self.get_id_sewa()])
        self.con.commit()
        if int(self.hari) > 0:
            self.total_denda = self.denda_per_hari * int(self.get_hari())
        else:
            self.total_denda = 0
        return self.total_denda
        self.con.close()

    def get_denda(self):
        return self.__set_data_pengembalian()


# denda = pengembalian(input('terlambat berapa hari: '), input('ID sewa: '))
# print(denda.get_denda())
# denda.set_data_pengembalian()

