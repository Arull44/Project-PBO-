import sqlite3
from database import data_manager

class penyewa(data_manager):
    def get_data_penyewa(self):
        self.query = 'SELECT * FROM penyewa'
        self.exe_query(self.query)
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        # self.con.close()
        
        print('''PILIH:
        1. hapus data penyewa
        2. edit data penyewa''')
        pilihan = (input('masukkan pilihan: '))
        if pilihan == '1':
            penyewa.delete_penyewa()
        elif pilihan == '2':
            penyewa.update_penyewa(int(input('masukkan id: ')),input('masukkan nama anda: '), input('masukkan username: '), input('masukkan password: '), input('masukkan tanggal lahir: '), input('masukkan nomor telepon: '),input('masukkan alamat: '),input('masukkan kota: '))

    def delete_penyewa(self):
        id = input('masukkan id: ')
        self.query = f'DELETE FROM penyewa WHERE id = {id}'
        self.exe_query(self.query)
        self.con.close()
        print('data berhasil dihapus')

    def update_penyewa(self, id, nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota):
        self.query = (f'''UPDATE penyewa SET nama_penyewa = "{nama_penyewa}", username = "{username}", password = "{password}", tanggal_lahir = "{tanggal_lahir}", nomor_telepon = "{nomor_telepon}", alamat = "{alamat}", nama_kota = "{nama_kota}" WHERE id = {id}''')
        self.exe_query(self.query)
        self.con.close()
        print('data berhasil diubah')
        
penyewa = penyewa()
# penyewa.get_data_penyewa()
# penyewa.delete_penyewa()
# penyewa.update_penyewa(int(input('masukkan id: ')),input('masukkan nama anda: '), input('masukkan username: '), input('masukkan password: '), input('masukkan tanggal lahir: '), input('masukkan nomor telepon: '),input('masukkan alamat: '),input('masukkan kota: '))