""" Kullanıcıyı sürekli konsolda tutarak istediği kadar işlem yapmasını sağlayacak bir hesap makinesi
programlayacağız. Hesaplama işlemlerinin her biri ayrı fonksiyon olmalıdır.
Kullanıcı klavyeden ilk olarak istediği işlemi ( + - / * %) girmelidir. Dört işleme ek olarak mod operatörü de dahil. Daha 
sonra gireceği iki sayının kullanıcının istediği işleme yönlendirilmesini eğer kullanıcıdan alınan değer yukarıdaki beş sembolden 
biri değilse programın hata vermesini sağlayalım.
Kullanıcı işlem seçmek yerine "q" harfi girişi yaparsa programı sonlandıralım aksi takdirde program her hesaplama sonrası tekrar işlem
yapabiliyor olmalıdır. """

def cikartmaIslemi(sayi1,sayi2):
    return sayi1-sayi2

def toplamaIslemi(sayi1,sayi2):
    return sayi1+sayi2

def bolmeIslemi(sayi1,sayi2):
    return sayi1/sayi2

def carpmaIslemi(sayi1,sayi2):
    return sayi1*sayi2

def modIslemi(sayi1,sayi2):
    return sayi1%sayi2

while True:
    sayi1 = int(input("sayi1 giriniz"))
    sayi2 = int(input("sayi2 giriniz"))
    islem = input("islem")

    if islem=="+":
        print(toplamaIslemi(sayi1,sayi2))

    elif islem=="-":
         print(cikartmaIslemi(sayi1,sayi2))

    elif islem=="/":
        print(bolmeIslemi(sayi1,sayi2))

    elif islem=="*":
        print(carpmaIslemi(sayi1,sayi2))

    elif islem=="%":
        print(modIslemi(sayi1,sayi2))

    elif islem=="q":
        break

    else:
        print("hatalı giriş yaptınız")