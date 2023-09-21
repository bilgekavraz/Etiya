""" Bir hesap makinesi kodladığımızı varsayalım, kullanıcı ilk olarak sırayla 2 adet sayı girecek ve bu sayılar arasında yapmak istediği dört işlemi seçecek.
Seçerken verdiği değerler dört işlemden birisi değil ise kullanıcı uyarılıcak (+ - * /).
Girilen işleme göre bu iki sayı arasında ilgili işlem yapılarak kullanıcıya sonuç gösterilecek. """

sayi1 = input("1.sayıyı giriniz")
sayi2 = input("2.sayıyı giriniz")
islem = input("yapmak istediğiniz işlemi giriniz")

if islem == "+" :
    print(int(sayi1)+int(sayi2))

elif islem == "-" :
    print(int(sayi1)-int(sayi2))

elif islem == "/" :
    print(int(sayi1)/int(sayi2))

elif islem == "*" :
    print(int(sayi1)*int(sayi2))

else:
    print("Hatalı işlem")
