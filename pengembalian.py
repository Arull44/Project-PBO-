import sqlite3
import datetime
from sewa import sewa

class pengembalian(sewa):
    def __init__(self, tanggal):
        super().__init__()
        self.denda_per_hari = 100000
        self.year, self.month, self.day = map(int, tanggal.split('-'))

    def hitung_denda(self):
        tgl_sewa = datetime.date(self.year, self.month, self.day)
        today = datetime.date.today()
        selisih = tgl_sewa - today
        print('selisih hari: '+str(selisih.days))
        if(selisih.days < sewa.get_lama_sewa()):
            denda = self.denda_per_hari * (selisih.days+3) * -1
        else:
            denda = 0
        return denda
