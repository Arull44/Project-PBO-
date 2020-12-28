import sqlite3
from tipe_mobil import tipe_mobil
from database import data_manager

class mobil(tipe_mobil):
    def __init__(self, nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe):
        self.__nama_mobil = nama_mobil
        self.__warna = warna
        self.__harga_sewa = harga_sewa
        self.__jumlah_kursi = jumlah_kursi
        self.__id_tipe = id_tipe

    def tambah_mobil(self):
        self.query = 'INSERT INTO mobil (nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'
        self.query = self.query % (self.__nama_mobil, self.__warna, self.__harga_sewa, self.__jumlah_kursi, self.__id_tipe) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)
        self.con.close()

    def get_harga_sewa(self):
        return self.__harga_sewa

class data_mobil(data_manager):
    def get_data_mobil_fullset(self):
        self.query = '''SELECT mobil.nama_mobil, mobil.warna, mobil.harga_sewa, tipe_mobil.tipe, mobil.jumlah_kursi
                        FROM mobil JOIN tipe_mobil ON mobil.id_tipe = tipe_mobil.id'''
        self.exe_query(self.query)
        self.all_results = self.cursor.fetchall()
        no = 1
        for result in self.all_results:
            print(no, result)
            no += 1
        self.con.close()

    def get_just_mobil(self):
        self.query = 'SELECT * FROM mobil'
        self.exe_query(self.query)
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def delete_mobil_byID(self):
        id = int(input('masukkan ID mobil: '))
        self.query = f'DELETE FROM mobil WHERE id = "{id}"'
        self.exe_query(self.query)
        print('data berhasil dihapus')

    def update_mobil_byID(self, id, nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe):
        self.query = (f'''UPDATE mobil SET nama_mobil = "{nama_mobil}", warna = "{warna}", harga_sewa = "{harga_sewa}", jumlah_kursi = "{jumlah_kursi}", id_tipe = "{id_tipe}" WHERE id = {id}''')
        self.exe_query(self.query)
        self.con.close()
        print('data berhasil diubah')


        

add_mobil = mobil(input('masukkan nama mobil: '), input('masukkan warna: '), input('masukkan harga_sewa: '), input('masukkan jumlah kursi: '), input('masukkan id tipe: '))
add_mobil.tambah_mobil()
# car = data_mobil()
# car.get_data_mobil_fullset()
# car.get_just_mobil()
# car.delete_mobil_byID()
# car.update_mobil_byID(int(input('masukkan id: ')),input('masukkan nama mobil: '), input('masukkan warna: '), input('masukkan harga_sewa: '), input('masukkan jumlah kursi: '), input('masukkan id tipe: '))