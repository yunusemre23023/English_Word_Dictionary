import sqlite3

connection = sqlite3.connect("words.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sozluk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingilizce TEXT NOT NULL,
    turkce TEXT NOT NULL,
    telafuz  TEXT NOT NULL,
    seviye INTEGER NOT NULL
)
""")
connection.commit()
def menu():
    #naber lan tırrek
    print("Yapmak istediginiz islemi secin...")

    secim = int(input("1-Kelime ekle 2-Kelime ara 3-Kelime Sil 4-Sinav Oyunu 0-Cikis"))

    if secim == 1:
        ekle()
    if secim == 2:
        ara()

def ekle():
    
    ing = input("İngilizcesini gir: ")
    tur = input("Turkcesini gir: ")
    tel = input("Telafuz girin: ")
    sev = int(input("Kelime seviyesini gir: "))
    sql = f"INSERT INTO sozluk(ingilizce,turkce,telafuz,seviye) VALUES('{ing}','{tur}','{tel}',{sev})"
    cursor.execute(sql)
    connection.commit()
    menu()

def ara():
    s = int(input("İngilizce ise 1 - Turkce ise 2"))
    k = input("Kelimeyi gir: ")
    if s == 1:
        cursor.execute(f"select * from sozluk where ingilizce = '{k}'")
        sonuc = cursor.fetchall()
        print(sonuc)
    elif s == 2:
        cursor.execute(f"select * from sozluk where turkce = '{k}'")
        sonuc = cursor.fetchall()
        print(sonuc)
    menu()

menu()
cursor.close()


