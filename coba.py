import sqlite3
def insert_data():
    con = sqlite3.connect("sewamobil.sqlite")
    cursor = con.cursor()
    nama_kota = input("masukkan nama kota: ")
    query = 'INSERT INTO kota(nama_kota) VALUES (?)'
    cursor.execute(query, [nama_kota])
    con.commit()
    con.close()

def show_table():
    con = sqlite3.connect("sewamobil.sqlite")
    cursor = con.cursor()
    query = '''SELECT * FROM penyewa'''
    cursor.execute(query)
    all_results = cursor.fetchall()
    con.commit()
    for result in all_results:
        print(result)
    con.close()

def delete_data():
    con = sqlite3.connect("sewamobil.sqlite")
    cursor = con.cursor()
    id = int(input('id: '))
    query = f'DELETE FROM penyewa WHERE id = "{id}"'
    cursor.execute(query)
    con.commit()
    con.close()

def drop_table():
    con = sqlite3.connect("sewamobil.sqlite")
    cursor = con.cursor()
    query = 'DROP TABLE mobil'
    cursor.execute(query)
    con.commit()
    con.close()

# insert_data()
drop_table()
# delete_data()
# show_table()