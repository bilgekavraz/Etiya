""" Bir okul kayıt sistemi kodlayalım;
Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım.
Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.  """

from ogrenci import Ogrenciler
from ogretmen import Ogretmen

listeOgr = []

listeOgretmen = []


def listele(meslekNo):
    if meslekNo ==1:
        for i in range(len(listeOgr)):
            print(f"{i+1}. " , listeOgr[i])
    if meslekNo ==2:
        for i in range(len(listeOgretmen)):
            print(f"{i+1}. " , listeOgretmen[i])
   
def kisiEkle():
    #1 ve 2 dışında bir int değerde döngü durur ve liste yazdırılır

    while True:
        meslekNo = int(input("ogrenci girişi için 1\nöğretmen girişi için 2 \n listeyi yazdırmak için herhangi bir in değeri tuşlayınız"))
        if meslekNo==1:
            meslek = "Öğrenci"
            ogr = Ogrenciler(input("isim"),input("soyisim"))      
            ogrList= [ogr.isim,ogr.soyisim,meslek]
            listeOgr.append(ogrList)
           

        elif meslekNo==2:
            meslek = "Öğretmen"
            ogretmen = Ogrenciler(input("isim"),input("soyisim"))
            ogrList= [ogretmen.isim+" "+ogretmen.soyisim +" "+ meslek]
            listeOgretmen.append(ogrList)
            
        else:
            print("Öğrenci Listesi: ")
            listele(1)
            print("Öğretmen Listesi: ")
            listele(2)
            break

kisiEkle()
""" 
ogr = Ogrenciler("Bilge","Kavraz","ogrenci")
ogrList=[ogr.isim +""+ ogr.soyisim +" "+ ogr.meslek]
ogr2 = Ogrenciler("Bilge sena","Kavraz","ogrenci")
ogrList2=[ogr2.isim +""+ ogr2.soyisim +" "+ ogr2.meslek ]
liste.append(ogrList)
liste.append(ogrList2)
 """


#ogr2.soruSor()