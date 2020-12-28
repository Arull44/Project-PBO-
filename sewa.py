import sqlite3
from database import data_manager
from penyewa import penyewa
# from mobil import mobil

class sewa(data_manager):
    global username
    def set_lama_sewa(self, lama_sewa):
        self.query = 'INSERT INTO sewa (lama_sewa) VALUES (\'%s\')'
        self.query = self.query % (lama_sewa) 
        return ('data berhasil dimasukkan')
        self.exe_query(self.query)

    def get_lama_sewa(self):
        return self.lama_sewa

    def sewa_mobil(self):
        self.query = '''SELECT penyewa.nama_penyewa, petugas.nama_petugas, mobil.nama_mobil, mobil.harga_sewa, sewa.lama_sewa 
                    FROM sewa INNER JOIN penyewa ON sewa.id_penyewa = penyewa.id_penyewa
                    ON sewa.id_petugas = petugas.id_petugas
                    ON sewa.id_mobil = mobil.id_mobil'''
        self.exe_query(self.query)

    # def set_datasewa(self, id_penyewa, id_mobil):
    #     self.query = 'INSERT INTO sewa (id_penyewa, id_mobil) VALUES (\'%s\',\'%s\')
    #     self.query = self.query % (id_penyewa, id_mobil) 
    #     print ('data berhasil dimasukkan')
    #     self.exe_query(self.query)

    def cancel_sewa(self):
        id = input('masukkan id: ')
        self.query = f'DELETE FROM sewa WHERE id = {id}'
        print('sewa mobil berhasil dibatalkan')
        self.exe_query(self.query)

    @staticmethod
    def get_harga_total():
        return self.lama_sewa * get_harga_sewa()

# add_lama_sewa = sewa()
# add_lama_sewa.tambah_lama_sewa(int(input('masukkan lama sewa mobil: ')))

# add_datasewa = sewa()
# add_datasewa.set_datasewa()

# batalkan_sewa  = sewa()
# batalkan_sewa.cancel_sewa()
