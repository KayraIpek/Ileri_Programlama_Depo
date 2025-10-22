class Kutuphane:
    def __init__(self):
        self.veriler = []

    @staticmethod
    def karsilama(program_adi):
        print(f"{program_adi} isimli programa hoş geldiniz!\n")

    def kitap_ekle(self):
        ad = input("Kitap adı: ")
        yazar = input("Yazar: ")
        tur = input("Türü: ")
        self.veriler.append({"ad": ad, "yazar": yazar, "tur": tur})
        print(f"'{ad}' eklendi!\n")

    def kitap_ara(self):
        kelime = input("Aramak istediğiniz eser bilgisini giriniz: ").lower()
        sonuc = [ktp for ktp in self.veriler if kelime in ktp["ad"].lower() or kelime in ktp["yazar"].lower()]
        if not sonuc:
            print("Aradığınız eser bulunamadı.\n")
        else:
            for ktp in sonuc:
                print(f"{ktp['ad']} - {ktp['yazar']} ({ktp['tur']})")
                print()

    def kitaplari_listele(self):
        if not self.veriler:
            print("Henüz kayıtlı eser yok.\n")
            return
        for i, kitap in enumerate(self.veriler, 1):
            print(f"{i}. {kitap['ad']} - {kitap['yazar']} ({kitap['tur']})")
            print()

    def baslat(self):
        self.karsilama("Kayra'nın Kitaplığı")

        while True:
            print("1. Yeni eser ekle")
            print("2. Eser ara")
            print("3. Listele")
            print("4. Çıkış")

            secim = input("Seçim: ")

            if secim == "1":
                self.kitap_ekle()
            elif secim == "2":
                self.kitap_ara()
            elif secim == "3":
                self.kitaplari_listele()
            elif secim == "4":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim! Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    kutuphane = Kutuphane()
    kutuphane.baslat()
