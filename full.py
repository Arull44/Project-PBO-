import sqlite3

class data_manager:
    def __init__(self):
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()
    def exe_query(self, query):
        self.cursor.execute(query)
        self.con.commit()

class table(data_manager):
    def create_table_penyewa(self):
        self.query = """CREATE TABLE "penyewa"(
            "id" INTEGER NOT NULL UNIQUE,
            "nama_penyewa" TEXT NOT NULL,
            "username" TEXT NOT NULL,
            "password" TEXT NOT NULL,
            "tanggal_lahir" DATE NOT NULL,
            "nomor_telepon" INTEGER NOT NULL,
            "alamat" TEXT NOT NULL,
            "nama_kota" TEXT NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_tipemobil(self):
        self.query = """CREATE TABLE "tipe_mobil" (
            "id" INTEGER NOT NULL UNIQUE,
            "tipe" TEXT NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_mobil(self):
        self.query = """CREATE TABLE "mobil" (
            "id" INTEGER NOT NULL UNIQUE,
            "nama_mobil" TEXT NOT NULL,
            "warna" TEXT NOT NULL,
            "harga_sewa" INTEGER NOT NULL,
            "jumlah_kursi" INTEGER NOT NULL,
            "id_tipe" INTEGER NOT NULL,
            FOREIGN KEY ("id_tipe") REFERENCES "tipe_mobil"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_sewa(self):
        self.query = """CREATE TABLE "sewa" (
            "id" INTEGER NOT NULL UNIQUE,
            "id_penyewa" INTEGER NOT NULL,
            "id_mobil" INTEGER NOT NULL,
            "lama_sewa" INTEGER NOT NULL,
            FOREIGN KEY ("id_penyewa") REFERENCES "penyewa"("id"),
            FOREIGN KEY ("id_mobil") REFERENCES "mobil"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)
    
    def create_table_pengembalian(self):
        self.query = """CREATE TABLE "pengembalian"(
            "id" INTEGER NOT NULL UNIQUE,
            "tanggal_pengembalian" DATE NOT NULL,
            "denda" INTEGER,
            "id_sewa" INTEGER NOT NULL,
            FOREIGN KEY ("id_sewa") REFERENCES "sewa"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

# run the code to make the table
create_table = table()
# create_table.create_table_penyewa()
# create_table.create_table_tipemobil()
# create_table.create_table_mobil()
# create_table.create_table_pengembalian()
# create_table.create_table_sewa()

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
        self.query = '''SELECT penyewa.nama_penyewa, mobil.nama_mobil, mobil.harga_sewa, sewa.lama_sewa 
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


class register(data_manager):    
    def __init__(self, nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota):
        super().__init__()
        self.__nama_penyewa = nama_penyewa
        self.__username = username
        self.__password = password
        self.__tanggal_lahir = tanggal_lahir
        self.__nomor_telepon = nomor_telepon
        self.__alamat = alamat
        self.__nama_kota = nama_kota

    def register(self):
        self.query = 'INSERT INTO penyewa(nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota) VALUES (\'%s\',\'%s\',\'%s\',\'%s\', \'%s\', \'%s\',\'%s\')'
        self.query = self.query % (self.__nama_penyewa, self.__username, self.__password, self.__tanggal_lahir, self.__nomor_telepon, self.__alamat, self.__nama_kota) 
        self.exe_query(self.query)
        print('data berhasil didaftarkan')

# penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
# penyewa_add.register()


class login(data_manager):
    def input_login(self):
        self.username = input('masukkan username anda: ')
        self.password = input('masukkan password: ')
        for row in self.cursor.execute('SELECT * FROM penyewa WHERE username = username AND password = password'):
            if self.username and self.password in row:
                hal_utama = menu_utama()
                hal_utama.show_menu()
            else:
                print('data salah')
                return go.input_login()

    def hal_login(self):
        start = True
        while start:
            pilihan = interface_login()
            if pilihan == '1':
                go = login()
                go.hal_login()
            elif pilihan == '2':
                penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
                penyewa_add.register()

go = login()


def interface_login():
    print(('-----------------')*5)
    print('''*****Sewa Mobil Carents*****
    Pilih menu:
    sudah punya akun?
    1. Login
    belum punya akun?
    2. Registrasi''')
    pilihan = input('masukkan pilihan anda: ')
    return pilihan

# interface_login()