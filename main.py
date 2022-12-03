from form import *
from PyQt5.QtWidgets import *
from sql_envanter import *


class Dukkan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.envanter = Envanter()
        self.ui.setupUi(self)
        self.icerikList = str()
        self.bosList = []
        self.satir = 0
        self.alisverisTutar = 0
        self.alisverisKar = 0
        # temizleme ekranı
        self.temizle()
        self.listele()
        self.alisveris_ekran_liste()
        self.satisTemizle()
        # temizleme
        self.setWindowTitle("Programa Hoşgeldiniz SATIŞ")
        # Buton KomutlarıARALIK
        self.ui.tablo_Yenile.clicked.connect(self.alisverisil)
        self.ui.envanter_onay.clicked.connect(self.sorgu_fonk)
        self.ui.btn_envanterGetir.clicked.connect(self.urunBul)
        self.ui.btn_sepeteEkle.clicked.connect(self.sepetEkle)
        self.ui.btn_siparisiptal.clicked.connect(self.satisTemizle)
        self.ui.btn_siparisOnay.clicked.connect(self.satisONAY)
        self.ui.btn_tmizle.clicked.connect(self.yenisatisAc)
        # Buton KomutlarıARALIK

    def alisverisil(self):
        self.ui.tablo_analiz.clear()
        self.ui.tablo_analiz.setHorizontalHeaderLabels(
            ("AlisverisNO", "AlisverisTutarı", "İcerik", "EdilenKar", "Alisveris Tarihi"))
        self.alisveris_ekran_liste()

    def alisveris_ekran_liste(self):
        self.envanter.alisverisTablo()
        for indexSatir, kayitNo in enumerate(self.envanter.ekran):
            for indexSutun, kayitSutun in enumerate(kayitNo):
                self.ui.tablo_analiz.setItem(
                    indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def listele(self):
        self.envanter.liste()
        for indexSatir, kayitNo in enumerate(self.envanter.veri):
            for indexSutun, kayitSutun in enumerate(kayitNo):
                self.ui.envanter_ekran.setItem(
                    indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def sorgu_fonk(self):
        if self.ui.radio_ekle.isChecked() == True:
            try:
                self.envanter.ekle(self.ui.line_envanterId.text(), self.ui.line_envanterAd.text(
                ), self.ui.line_satisFiyat.text(), self.ui.line_gelisFiyat.text())
            except:
                self.ui.info.setText(self.envanter.info)
        elif self.ui.radio_sil.isChecked() == True:
            self.envanter.sil(self.ui.line_envanterId.text())
        elif self.ui.radio_update.isChecked() == True:
            self.envanter.update(self.ui.line_envanterId.text(
            ), self.ui.line_satisFiyat.text(), self.ui.line_gelisFiyat.text())
        self.temizle()
        self.listele()

    def temizle(self):

        self.ui.envanter_ekran.clear()
        self.ui.envanter_ekran.setHorizontalHeaderLabels(
            ("UrunID", "UrunAD", "UrunSatisFiyat", "UrunGelisFiyat"))

    def urunBul(self):
        self.temizle()
        self.envanter.getir(self.ui.line_envanterAra.text())
        for indexSatir, kayitNo in enumerate(self.envanter.gelen_veri):
            for indexSutun, kayitSutun in enumerate(kayitNo):
                self.ui.envanter_ekran.setItem(
                    indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def satisTemizle(self):
        self.alisverisKar = 0
        self.alisverisTutar = 0
        self.satir = 0
        self.ui.satis_ekran.clear()
        self.ui.satis_ekran.setHorizontalHeaderLabels(
            ("UrunID", "UrunAD", "Adet", "Fiyat"))

    def sepetEkle(self):

        try:

            self.envanter.getir(self.ui.line_satisKod.text())
            if len(self.envanter.gelen_veri) == 0:
                self.ui.lbl_kar.setText(str("HATA"))
            else:
                for i in self.envanter.gelen_veri:
                    self.urunID = i[0]
                    self.urunAD = i[1]
                    self.urunSatisF = i[2]
                    self.urunGelisF = i[3]

                self.icerikList += str(self.urunAD) + ","
                self.adet = int(self.ui.line_satisAdet.text())
                self.tutar = int(self.ui.line_satisAdet.text()
                                 ) * self.urunSatisF
                self.Kar = self.tutar - (self.urunGelisF * self.adet)
                self.ui.satis_ekran.setItem(
                    self.satir, 0, QTableWidgetItem(str(self.urunID)))
                self.ui.satis_ekran.setItem(
                    self.satir, 1, QTableWidgetItem(str(self.urunAD)))
                self.ui.satis_ekran.setItem(self.satir, 2, QTableWidgetItem(
                    str(self.ui.line_satisAdet.text())))
                self.ui.satis_ekran.setItem(self.satir, 3, QTableWidgetItem(
                    str(int(self.ui.line_satisAdet.text()) * self.urunSatisF)))
                self.satir += 1
                self.alisverisTutar += self.tutar
                self.alisverisKar += self.Kar
                self.ui.alisveris_tutar.setText(str(self.alisverisTutar))
        except:
            self.ui.alisveris_tutar.setText(
                "hata")

    def satisONAY(self):
        self.ui.alisveris_tutar.setText(str(self.alisverisTutar))
        self.envanter.alisverisEkle(
            self.icerikList, self.alisverisTutar, self.alisverisKar)
        self.ui.lbl_kar.setText(str(self.alisverisKar))
        self.icerikList = ""
        self.envanter.gelen_veri.clear()
        self.alisverisil()
        self.yenisatisAc()

    def yenisatisAc(self):
        self.ui.alisveris_tutar.clear()
        self.satisTemizle()


program = QApplication([])
yeni = Dukkan()
yeni.show()
program.exec()
