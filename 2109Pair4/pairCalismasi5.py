""" Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu mükemmel sayıdır.
Kullanıcıdan aldığınız sayının mükemmel olup olmadığını söyleyen bir program yazınız. """

sayi = int(input("sayı giriniz"))
toplam = 0
if sayi <= 0:
    print("lütfen 0'dan büyük sayı giriniz")
else:
    for i in range(sayi-1):
        if sayi % (i+1) == 0 :
            toplam=toplam+(i+1)

    if toplam == sayi :
        print("mükemmel sayı")

    else:
        print("mükemmel sayı değil")