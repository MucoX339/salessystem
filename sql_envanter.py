import sqlite3 as sql
import datetime


class Envanter:
    def __init__(self):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        sorgu = """CREATE TABLE IF NOT EXISTS 'EnvanterInformation' (UrunID integer primary key not null,
        UrunAd text,UrunSatısFiyat float,UrunGelisFiyat float)"""
        self.cursor.execute(sorgu)
        self.conn.commit()
        self.conn.close()
        self.e = datetime.datetime.now()
        self.alisverisDb()
        self.tarih = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)

    def ekle(self, id, ad, satisFiyat, gelisFiyat):
        Envanter.__init__(self)
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(
                "insert into EnvanterInformation (UrunID,UrunAd,UrunSatısFiyat,UrunGelisFiyat) Values (?,?,?,?)", (id, ad, satisFiyat, gelisFiyat))
        except:
            self.info = "Bu Ürün Stoklarda Kayıtlıdır Lütfen Dikkatli Olunuz"
            print(self.info)
        self.conn.commit()
        self.conn.close()

    def sil(self, id):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "delete from EnvanterInformation WHERE UrunID='{}'".format(id))
        self.conn.commit()
        self.conn.close()

    def update(self, id, satisFiyat, gelisFiyat):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("Update 'EnvanterInformation' Set UrunSatısFiyat={},UrunGelisFiyat={} Where UrunID={}".format(
            satisFiyat, gelisFiyat, id))
        self.conn.commit()
        self.conn.close()

    def getir(self, id):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "select * from EnvanterInformation WHERE UrunID='{}'".format(id))
        self.gelen_veri = self.cursor.fetchmany()
        self.conn.close()

    def liste(self):
        Envanter.__init__(self)
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from EnvanterInformation")
        self.veri = self.cursor.fetchall()
        self.conn.close()

    def alisverisDb(self):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS 'ALISVERISLER'(AlisverisID integer primary key,ICERIK text,AlisverisToplamTutar float,AlisverisKar float,AlisverisSaati date)")
        self.conn.commit()
        self.conn.close()

    def alisverisEkle(self, icerik, tutar, kar):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "INSERT INTO 'ALISVERISLER' (ICERIK,AlisverisToplamTutar,AlisverisKar,AlisverisSaati) VALUES (?,?,?,?)", (icerik, tutar, kar, self.tarih))
        self.conn.commit()
        self.conn.close()

    def aralik(self):
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "select * from ALISVERISLER WHERE AlisverisSaati BETWEEN '1/11/2022' AND '5/12/2022' ")
        self.bilgilendirme = self.cursor.fetchall()
        for i in self.bilgilendirme:
            print(i)

    def alisverisTablo(self):
        Envanter.__init__(self)
        self.conn = sql.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from ALISVERISLER")
        self.ekran = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()


