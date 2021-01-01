import sqlite3
from tipe_mobil import tipe_mobil

class mobil(tipe_mobil):
    def __init__(self):
        super().__init__()
        self.__nama_mobil = ''
        self.__warna = ''
        self.__harga_sewa = ''
        self.__jumlah_kursi = ''
        self.__id_tipe = ''

    def tambah_mobil(self):
        self.__nama_mobil = input('masukkan nama mobil: ')
        self.__warna = input('masukkan warna: ')
        self.__harga_sewa = int(input('masukkan harga_sewa: '))
        self.__jumlah_kursi = input('masukkan jumlah kursi: ')
        self.__id_tipe = input('masukkan id tipe: ')
        self.query = 'INSERT INTO mobil (nama_mobil, warna, harga_sewa, jumlah_kursi, id_tipe) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(self.query, [self.__nama_mobil, self.__warna, self.__harga_sewa, self.__jumlah_kursi, self.__id_tipe])
        self.con.commit()
        print('data berhasil dimasukkan')

    def get_data_mobil_fullset(self):
        self.query = '''SELECT mobil.id, mobil.nama_mobil, mobil.warna, mobil.harga_sewa, tipe_mobil.tipe, mobil.jumlah_kursi
                        FROM mobil JOIN tipe_mobil ON mobil.id_tipe = tipe_mobil.id'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print('ID:', result[0])
            print('nama mobil:', result[1])
            print('warna:', result[2])
            print('tipe mobil:', result[4])
            print('jumlah kursi: ', result[5])
            print('HARGA:', result[3])
            print()
        self.con.close()

    def get_just_mobil(self):
        self.query = 'SELECT * FROM mobil'
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def delete_mobil_byID(self):
        id = int(input('masukkan ID mobil: '))
        self.query = f'DELETE FROM mobil WHERE id = ?'
        self.cursor.execute(self.query, [id])
        self.con.commit()
        self.con.close()
        print('data berhasil dihapus')

    def update_mobil_byID(self):
        self.__id = int(input('masukkan id mobil: '))
        self.__nama_mobil = input('masukkan nama mobil: ')
        self.__warna = input('masukkan warna: ')
        self.__harga_sewa = int(input('masukkan harga_sewa: '))
        self.__jumlah_kursi = input('masukkan jumlah kursi: ')
        self.__id_tipe = input('masukkan id tipe: ')
        self.query = '''UPDATE mobil SET nama_mobil = ?, warna = ?, harga_sewa = ?, jumlah_kursi = ?, id_tipe = ? WHERE id = ?'''
        self.cursor.execute(self.query, [self.__nama_mobil, self.__warna, self.__harga_sewa, self.__jumlah_kursi,self.__id_tipe, self.__id])
        self.con.commit()
        self.con.close()
        print('data berhasil diubah')

# mobil = mobil()
# tipe_mobil = tipe_mobil()
# mobil.tambah_mobil()
# mobil.get_data_mobil_fullset()
# mobil.get_just_mobil()
# mobil.delete_mobil_byID()
# mobil.update_mobil_byID()
