-- SQLite
CREATE TABLE "kota" 
(
    "id_kota" INTEGER NOT NULL UNIQUE,
    "nama_kota" TEXT NOT NULL,
    PRIMARY KEY ("id_kota" AUTOINCREMENT)
)
DROP TABLE "kota"

CREATE TABLE "penyewa"
(
    "id_penyewa" INTEGER NOT NULL UNIQUE,
    "nama_penyewa" TEXT NOT NULL,
    "tanggal_lahir" DATETIME NOT NULL,
    "nomor_telepon" INTEGER NOT NULL,
    "alamat" TEXT NOT NULL,
    FOREIGN KEY ("id_kota") REFERENCES "kota"("id_kota")
    PRIMARY KEY ("id_penyewa" AUTOINCREMENT) 
)

CREATE TABLE "petugas" 
(
    "id_petugas" INTEGER NOT NULL UNIQUE,
    "nama_petugas" TEXT NOT NULL,
    PRIMARY KEY ("id_petugas" AUTOINCREMENT)
)
DROP TABLE "petugas"

CREATE TABLE "tipe_mobil" 
(
    "id_tipe_mobil" INTEGER NOT NULL,
    "tipe" TEXT NOT NULL,
    "jumlah_kursi" INTEGER NOT NULL,
    PRIMARY KEY ("id_tipe_mobil" AUTOINCREMENT)
)
DROP TABLE tipe_mobil

CREATE TABLE "mobil" 
(
    "id_mobil" INTEGER NOT NULL,
    "nama_mobil" TEXT NOT NULL,
    "warna" TEXT NOT NULL,
    "harga_sewa" INTEGER NOT NULL,
    FOREIGN KEY ("id_tipe_mobil") REFERENCES "tipe_mobil"("id_tipe_mobil"),
    PRIMARY KEY ("id_mobil" AUTOINCREMENT)
)

CREATE TABLE "sewa"
(
	"id_sewa" INTEGER NOT NULL,
	"tanggal" DATE DEFAULT GETDATE() NOT NULL,
	"lama_sewa" INTEGER NOT NULL,
	"tujuan" TEXT (100) NOT NULL,
	FOREIGN KEY ("id_mobil") REFERENCES "mobil"("id_mobil") NOT NULL,
    FOREIGN KEY ("id_petugas") REFERENCES "petugas"("id_petugas") NOT NULL,
	FOREIGN KEY ("id_penyewa") REFERENCES "penyewa"("id_penyewa") NOT NULL,
    PRIMARY KEY ("id_sewa") AUTOINCREMENT)
)

CREATE TABLE "pengembalian"
(
    "id_pengembalian" INTEGER NOT NULL,
    "tanggal_pengembalian" DATE NOT NULL,
    FOREIGN KEY ("id_sewa") REFERENCES "sewa"("id_sewa") NOT NULL,
    PRIMARY KEY ("id_pengembalian") AUTOINCREMENT) 
)

CREATE TABLE "denda"
(
    "id_denda" INTEGER NOT NULL,
    "total_denda" INTEGER NOT NULL,
    FOREIGN KEY ("id_pengembalian") REFERENCES "pengembalian"("id_pengembalian") NOT NULL,
    PRIMARY KEY ("id_denda" AUTOINCREMENT)
)

SELECT penyewa.nama_penyewa, petugas.nama_petugas, mobil.nama_mobil, mobil.harga_sewa, sewa.lama_sewa 
FROM (((sewa 
INNER JOIN penyewa ON sewa.id_penyewa = penyewa.id_penyewa),
ON sewa.id_petugas = petugas.id_petugas),
ON sewa.id_mobil = mobil.id_mobil)

SELECT sewa.id, sewa.lama_sewa, penyewa.nama_penyewa, mobil.nama_mobil, mobil.harga_sewa
FROM ((sewa
INNER JOIN penyewa ON sewa.id_penyewa = penyewa.id)
INNER JOIN mobil ON sewa.id_mobil = mobil.id)