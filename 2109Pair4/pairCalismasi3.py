"""  Kullanıcıdan aldığı(input) 10 adet isim soyisim bilgisini bir diziye ekleyen ve işlemler sonunda bu diziyi ekrana yazdıran programı geliştiriniz. """

dizi = []

for i in range(10):
    isimSoyisim = input("isim soy isim giriniz")
    dizi.append(isimSoyisim)

for isim in dizi:
    print(isim)

