import sqlite3
from sewa import sewa

class pengembalian(sewa):
    denda = 100000
    def __init__(self, tanggal_pengembalian):
        super().__init__(self.lama_sewa)
        self.tanggal_pengembalian = tanggal_pengembalian


    # def date_pengembalian(self):
    #     self.tanggal_pengembalian = #ambil tanggal sekarang
    #     self.keterlambatan = 

    @staticmethod
    def hitung_denda(self):
        return self.keterlambatan * self.denda
