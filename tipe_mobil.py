import sqlite3

class tipe_mobil():
    def __init__(self):
        self.__tipe = ''
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()

    def tambah_tipe(self):
        self.__tipe = input('masukkan tipe mobil: ')
        self.query = 'INSERT INTO tipe_mobil (tipe) VALUES (?)'
        self.cursor.execute(self.query, [self.__tipe])
        self.con.commit()
        print('data berhasil dimasukkan')

    def get_data_tipe(self):
        for row in self.con.execute('SELECT * FROM tipe_mobil'):
            print(row)

tipe = tipe_mobil()
# tipe.tambah_tipe()
# tipe.get_data_tipe()