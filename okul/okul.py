""" Bir okul kayıt sistemi kodlayalım;
Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım.
Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.  """

from ogrenci import Ogrenciler
from ogretmen import Ogretmen

liste = []
   
ogr = Ogrenciler("Bilge","Kavraz","ogrenci")
ogrList=[ogr.isim +""+ ogr.soyisim +" "+ ogr.meslek]
ogr2 = Ogrenciler("Bilge sena","Kavraz","ogrenci")
ogrList2=[ogr2.isim +""+ ogr2.soyisim +" "+ ogr2.meslek ]
liste.append(ogrList)
liste.append(ogrList2)

for i in range(len(liste)):
    print(f"{i+1}. " , liste[i])

ogr2.soruSor()