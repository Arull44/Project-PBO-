import sqlite3
from database import data_manager

class tipe_mobil(data_manager):
    def tambah_tipe(self, tipe):
        self.query = 'INSERT INTO tipe_mobil(tipe) VALUES(\'%s\')'
        self.query = self.query % (tipe) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)
    def get_data_tipe(self):
        for row in self.con.execute('SELECT * FROM tipe_mobil'):
            print(row)
    
# add_tipe = tipe_mobil()
# add_tipe.tambah_tipe(input('masukkan tipe mobil: '))
# show_tipe = tipe_mobil()
# show_tipe.get_data_tipe()

# import sqlite3
# from tipe_mobil import tipe_mobil
# from database import data_manager

# class mobil(tipe_mobil):
#     nama_mobil = ""
#     warna = ""
#     harga_swa = ""
#     jumlah_kursi = ""
#     id_tipe = ""
#     def __init__(self, nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe):
#         self.__nama_mobil = nama_mobil
#         self.__warna = warna
#         self.__harga_sewa = harga_sewa
#         self.__jumlah_kursi = jumlah_kursi
#         self.__id_tipe = id_tipe

#     def tambah_mobil(self):
#         self.query = 'INSERT INTO mobil (nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'
#         self.query = self.query % (self.__nama_mobil, self.__warna, self.__harga_sewa, self.__jumlah_kursi, self.__id_tipe) 
#         print('data berhasil dimasukkan')
#         self.exe_query(self.query)
    
# class data_mobil(data_manager):
#     def get_data_mobil_fullset(self):
#         for row in self.con.execute('''SELECT mobil.nama_mobil, mobil.warna, mobil.harga_sewa, tipe_mobil.tipe, mobil.jumlah_kursi
#                             FROM mobil JOIN tipe_mobil ON mobil.id_tipe = tipe_mobil.id'''):
#             print(row)
#     def get_just_mobil(self):
#         for row in self.con.execute('SELECT * FROM mobil'):
#             print(row)
#     def delete_mobil_byID(self):
#         id = int(input('masukkan ID mobil: '))
#         self.query = f'DELETE FROM mobil WHERE id = "{id}"'
#         self.exe_query(self.query)

#     def update_mobil_byID(self):
#         id = int(input('masukkan ID mobil: '))
#         self.query = f'UPDATE mobil SET  WHERE id = "{id}"'
#         self.query = self.query % (self.__nama_mobil, self.__warna, self.__harga_sewa, self.__jumlah_kursi, self.__id_tipe) 
#         print('data berhasil dimasukkan')
#         self.exe_query(self.query)
            

# add_mobil = mobil(input('masukkan nama mobil: '), input('masukkan warna: '), input('masukkan harga sewa: '),  input('masukkan jumlah kursi: '), input('masukkan id tipe: '))
# add_mobil.tambah_mobil()
# car = data_mobil()
# car.get_data_mobil_fullset()
# car.get_just_mobil()
# car.delete_mobil_byID()