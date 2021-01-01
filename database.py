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

    def create_table_petugas(self):
        self.query = """CREATE TABLE "petugas" (
            "id_petugas" INTEGER NOT NULL UNIQUE,
            "nama_petugas" TEXT NOT NULL,
            "username" TEXT NOT NULL,
            "password" TEXT NOT NULL,
            PRIMARY KEY ("id_petugas" AUTOINCREMENT))"""
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
# create_table = table()
# create_table.create_table_penyewa()
# create_table.create_table_petugas()
# create_table.create_table_tipemobil()
# create_table.create_table_mobil()
# create_table.create_table_pengembalian()
# create_table.create_table_sewa()
