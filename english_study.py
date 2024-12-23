import sqlite3
import random

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

s = 0
kontrol = 0
sorular = [0]
def menu():
    
    print("Yapmak istediginiz islemi secin...")

    secim = int(input("1-Kelime ekle 2-Kelime ara 3-Kelime Sil 4-Sinav Oyunu 0-Cikis \n"))

    if secim == 1:
        ekle()
    if secim == 2:
        ara()
    if secim == 0:
        exit()
    if secim == 3:
        sil()
    if secim == 4:
        global s
        s = int(input("Soru sayisini belirleyin: "))
        oyun(s) 
    

def ekle():
    
    ing = input("İngilizcesini gir: ")
    ing = ing.lower()
    tur = input("Turkcesini gir: ")
    tur = tur.lower()
    tel = input("Telafuz girin: ")
    tel = tel.lower()
    sev = int(input("Kelime seviyesini gir: "))
    sql = f"INSERT INTO sozluk(ingilizce,turkce,telafuz,seviye) VALUES('{ing}','{tur}','{tel}',{sev})"
    cursor.execute(sql)
    connection.commit()
    menu()

def ara():
    s = int(input("İngilizce ise 1 - Turkce ise 2 \n"))
    k = input("Kelimeyi gir: ")
    k = k.lower()
    if s == 1:
        cursor.execute(f"select turkce,telafuz from sozluk where ingilizce = '{k}'")
        sonuc = cursor.fetchall()
        if sonuc:
            print(f"Turkce: {sonuc[0][0]} Telafuz: {sonuc[0][1]}")
        else:
            print("Bulunamadi...")
    elif s == 2:
        cursor.execute(f"select ingilizce,telafuz from sozluk where turkce = '{k}'")
        sonuc = cursor.fetchall()
        if sonuc:
            print(f"Turkce: {sonuc[0][0]} Telafuz: {sonuc[0][1]}")
        else:
            print("Bulunamadi")

    menu()

def sil():
    s = input("Silmek istediginiz ingilizce kelimeyi girin: ")
    cursor.execute("delete from sozluk where ingilizce = ?",(s,))
    connection.commit()
    print(f"{s} kelimesi silindi")
    menu()

def oyun(s):
    print(s)
    cursor.execute("SELECT id FROM sozluk ORDER BY id DESC LIMIT 1")
    sonuc = cursor.fetchone()
    sonuc = int(sonuc[0])
    r = 0
    while True:

        r = random.randint(1,sonuc)
        if r in sorular:
            continue
        sorular.append(r)
        cursor.execute(f"select ingilizce from sozluk where id = ?",(r,))
        ing = cursor.fetchone()
        if ing:
            print(ing[0])
            break
        else:
            continue
    cursor.execute("select turkce from sozluk where id = ?", (r,))
    k = cursor.fetchone()
    c = input("Cevabi girin: ")
    c.lower()
    if c == k[0]:
        print("Dogru")
        global kontrol
        kontrol +=1
    else:
        print("yanlis")
    if s != 1:
        s -=1
        oyun(s)
    print(f"Dogru sayisi {kontrol}")
    
    menu()



menu()
cursor.close()


