import sqlite3

class data_manager:
    def __init__(self):
        self.con = sqlite3.connect("sewamobil.sqlite")
        self.cursor = self.con.cursor()
    def exe_query(self, query, ret_value = False):
        self.cursor.execute(query)
        self.all_results = self.cursor.fetchall()
        self.con.commit()
        if ret_value:
            return self.all_results
        # self.con.close()

class table(data_manager):
    # def create_table_kota(self):
    #     self.query = """CREATE TABLE kota (
    #         "id" INTEGER PRIMARY KEY NOT NULL,
    #         "nama_kota" TEXT NOT NULL)"""
    #     self.exe_query(self.query)

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

    # def create_table_petugas(self):
    #     self.query = """CREATE TABLE "petugas" (
    #         "id" INTEGER NOT NULL UNIQUE,
    #         "nama_petugas" TEXT NOT NULL,
    #         "id_kerja" INTEGER NOT NULL,
    #         "role" TEXT NOT NULL,
    #         PRIMARY KEY ("id" AUTOINCREMENT))"""
    #     self.exe_query(self.query)

    def create_table_tipemobil(self):
        self.query = """CREATE TABLE "tipe_mobil" (
            "id" INTEGER NOT NULL UNIQUE,
            "tipe" TEXT NOT NULL,
            "jumlah_kursi" INTEGER NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_mobil(self):
        self.query = """CREATE TABLE "mobil" (
            "id" INTEGER NOT NULL UNIQUE,
            "nama_mobil" TEXT NOT NULL,
            "warna" TEXT NOT NULL,
            "harga_sewa" INTEGER NOT NULL,
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

    # def create_table_denda(self):
    #     self.query = """CREATE TABLE "denda"(
    #         "id" INTEGER NOT NULL UNIQUE,
    #         "total_denda" INTEGER NOT NULL,
    #         "id_pengembalian" INTEGER NOT NULL,
    #         FOREIGN KEY ("id_pengembalian") REFERENCES "pengembalian"("id"),
    #         PRIMARY KEY ("id" AUTOINCREMENT))"""
    #     self.exe_query(self.query)

# run the code to make the table
create_table = table()
# create_table.create_table_kota()
# create_table.create_table_penyewa()
# create_table.create_table_tipemobil()
# create_table.create_table_mobil()
# create_table.create_table_petugas()
# create_table.create_table_pengembalian()
# create_table.create_table_denda()
# create_table.create_table_sewa()

# class kota():
#     def __init__(self, nama_kota):
#         self.__nama_kota = nama_kota
#     def tambah_kota(self):
#         con = sqlite3.connect("sewamobil.sqlite")
#         cursor = con.cursor()
#         query = f'INSERT INTO kota(nama_kota) VALUES (?)'
#         cursor.execute(query, [self.__nama_kota])
#         con.commit()
#         con.close()

# class kota(data_manager):
#     def tambah_kota(self, nama_kota):
#         self.query = 'INSERT INTO kota(nama_kota) VALUES (\'%s\')'
#         self.query = self.query % (nama_kota) 
#         print('data berhasil dimasukkan')
#         self.exe_query(self.query)
#     def get_data_kota(self):
#         self.query = 'SELECT * FROM kota'
#         self.exe_query(self.query)
#         for result in self.all_results:
#             print(result)

        
# add_kota = kota()
# add_kota.tambah_kota(input("masukkan nama kota: "))
# add_kota.get_data_kota()

# class penyewa(data_manager):
#     def __init__(self, nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota):
#         super().__init__()
#         self.__nama_penyewa = nama_penyewa
#         self.__username = username
#         self.__password = password
#         self.__tanggal_lahir = tanggal_lahir
#         self.__nomor_telepon = nomor_telepon
#         self.__alamat = alamat
#         self.__nama_kota = nama_kota
#     def tambah_penyewa(self):
#         self.query = 'INSERT INTO penyewa(nama_penyewa, username, password, tanggal_lahir, nomor_telepon, alamat, nama_kota) VALUES (\'%s\',\'%s\',\'%s\',\'%s\', \'%s\', \'%s\',\'%s\')'
#         self.query = self.query % (self.__nama_penyewa, self.__username, self.__password, self.__tanggal_lahir, self.__nomor_telepon, self.__alamat, self.__nama_kota) 
#         print('data berhasil dimasukkan')
#         self.exe_query(self.query)

# add_penyewa = penyewa(input("masukkan nama anda: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), int(input("masukkan kota anda: ")))
# add_penyewa.tambah_penyewa()

class petugas(data_manager):
    def __init__(self, nama_petugas, id_kerja, role):
        super().__init__()
        self.__nama_petugas = nama_petugas
        self.__id_kerja = id_kerja
        self.__role = role
    def tambah_petugas(self):
        self.query = 'INSERT INTO petugas(nama_petugas, id_kerja, role) VALUES (\'%s\',\'%s\',\'%s\')'
        self.query = self.query % (self.__nama_petugas, self.__id_kerja, self.__role) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)

class show_table(data_manager):
    def get_data_penyewa(self):
        self.query = 'SELECT * FROM penyewa'
        self.exe_query(self.query)
        for result in self.all_results:
            print(result)

    def get_data_petugas(self):
        self.query = 'SELECT * FROM petugas'
        self.exe_query(self.query)
        for result in self.all_results:
            print(result)

    def get_data_tipe(self):
        self.query = 'SELECT * FROM tipe_mobil'
        self.exe_query(self.query)
        for result in self.all_results:
            print(result)        

    def get_data_mobil(self):
        self.query = '''SELECT mobil.nama_mobil, mobil.warna, mobil.harga_sewa, tipe_mobil.tipe, tipe_mobil.jumlah_kursi
                        FROM mobil JOIN tipe_mobil ON mobil.id_tipe = tipe_mobil.id'''
        self.exe_query(self.query)
        for result in self.all_results:
            print(result)  

# add_petugas = petugas(input('masukkan nama petugas: '), input('masukkan id kerja: '), input('masukkan role: '))
# add_petugas.tambah_petugas()
# show_petugas = show_table()
# show_petugas.get_data_petugas()
# show_penyewa = show_table()
# show_penyewa.get_data_penyewa()

class tipe_mobil(data_manager):
    def tambah_tipe(self, tipe, jumlah_kursi):
        self.query = 'INSERT INTO tipe_mobil (tipe, jumlah_kursi) VALUES (\'%s\',\'%s\')'
        self.query = self.query % (tipe, jumlah_kursi) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)

# # add_tipe = tipe_mobil()
# # add_tipe.tambah_tipe(input('masukkan tipe mobil: '), input('masukkan jumlah kursi: '))
# # show_tipe = show_table()
# # show_tipe.get_data_tipe()

class mobil(tipe_mobil):
    def __init__(self, nama_mobil, warna, harga_sewa, id_tipe):
        super().__init__()
        self.__nama_mobil = nama_mobil
        self.__warna = warna
        self.__harga_sewa = harga_sewa
        self.__id_tipe = id_tipe
    def tambah_mobil(self):
        self.query = 'INSERT INTO mobil (nama_mobil, warna, harga_sewa, id_tipe) VALUES (\'%s\',\'%s\',\'%s\', \'%s\')'
        self.query = self.query % (self.__nama_mobil, self.__warna, self.__harga_sewa, self.__id_tipe) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)
   
# add_mobil = mobil(input('masukkan nama mobil: '), input('masukkan warna: '), input('masukkan harga sewa: '), input('masukkan id tipe: '))
# add_mobil.tambah_mobil()
# show_mobil = show_table()
# show_mobil.get_data_mobil()

class sewa(data_manager):
    def tambah_lama_sewa(self, lama_sewa):
        self.query = 'INSERT INTO sewa (lama_sewa) VALUES (\'%s\')'
        self.query = self.query % (lama_sewa) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)

    def sewa_mobil(self):
        self.query = '''SELECT penyewa.nama_penyewa, petugas.nama_petugas, mobil.nama_mobil, mobil.harga_sewa, sewa.lama_sewa 
                    FROM sewa INNER JOIN penyewa ON sewa.id_penyewa = penyewa.id_penyewa
                    ON sewa.id_petugas = petugas.id_petugas
                    ON sewa.id_mobil = mobil.id_mobil'''
        self.exe_query(self.query)

    def set_datasewa(self, id_penyewa, id_mobil, id_petugas):
        self.query = 'INSERT INTO sewa (id_penyewa, id_mobil, id_petugas) VALUES (\'%s\',\'%s\',\'%s\')'
        self.query = self.query % (id_penyewa, id_mobil, id_petugas) 
        print('data berhasil dimasukkan')
        self.exe_query(self.query)

    def cancel_sewa(self):
        self.query = 'DELETE FROM sewa'
        print('sewa mobil berhasil dibatalkan')
        self.exe_query(self.query)

    @staticmethod
    def get_harga_total():
        return lama_sewa * self.__harga_sewa

# add_lama_sewa = sewa()
# add_lama_sewa.tambah_lama_sewa(int(input('masukkan lama sewa mobil: ')))

# add_datasewa = sewa()
# add_datasewa.set_datasewa()

# batalkan_sewa  = sewa()
# batalkan_sewa.cancel_sewa()

# class pengembalian(sewa):
#     denda = 100000
#     def __init__(self, tanggal_pengembalian):
#         super().__init__(self.lama_sewa)
#         self.tanggal_pengembalian = tanggal_pengembalian


#     def date_pengembalian(self):
#         self.tanggal_pengembalian = #ambil tanggal sekarang
#         self.keterlambatan = 

#     @staticmethod
#     def hitung_denda(self):
#         return self.keterlambatan * self.denda


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

class login(data_manager):
    def input_login(self):
        print(data)
        username = input('masukkan username anda: ')
        password = input('masukkan password: ')
        self.query = ('SELECT * FROM penyewa WHERE username = username AND password = password')
        self.exe_query(self.query)
        # if username and password not in :
        #     print('data salah')
        # else:
        #     print('data benar')
        # for result in self.all_results:
        #     print(result)  
    
# penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
# penyewa_add.register()

login = login()
# login.input_login()

# #main
# def show_menu():
#     print(('-----------------')*5)
#     print('''*****Sewa Mobil Carents*****
#     Pilih menu:
#     1. Tampilkan daftar mobil
#     2. Batalkan sewa mobil
#     3. Tampilkan total denda (jika terlambat mengembalikan)
#     4. Log out''')
#     pilih_menu = input('masukkan pilihan anda: ')
#     return pilih_menu

# def interface_login():
#     print(('-----------------')*5)
#     print('''*****Sewa Mobil Carents*****
#     Pilih menu:
#     sudah punya akun?
#     1. Login
#     belum punya akun?
#     2. Registrasi''')
#     pilihan = input('masukkan pilihan anda: ')
#     return pilihan

# start = True
# while start:
#     pilihan = interface_login()
#     # interface_login()
#     if pilihan == '1':
#         login.input_login()
#         if 
#             menu = show_menu()
#             if pilihan == '1':
#                 show_mobil.get_data_mobil()
#             elif pilihan == '2':
#                 pass
#             elif pilihan == '3':
#                 pass
#             elif pilihan == '4':
#                 pass
#     elif pilihan == '2':
#         penyewa_add = register(input("masukkan nama anda: "), input("masukkan username: "), input("masukkan password: "), input("masukkan tanggal lahir anda (YYYY-MM-DD): "), input("masukkan nomor telepon: "), input("masukkan alamat anda: "), (input("masukkan kota anda: ")))
#         penyewa_add.register()

# interface_login()