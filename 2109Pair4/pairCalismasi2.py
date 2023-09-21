""" Kullanıcıdan vize ve final notları alacak. Vize %40 final %60 etkili olacak şekilde not ortalaması hesaplanacak. 
0-49 FF
50-59 DD
60-69 CC
70-79 BB
80-100 AA
Not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız. (Notlar ondalıklı sayı şeklinde olabilir)  """

final = int(input("final notunu giriniz"))
vize = int(input("vize notunu giriniz"))

notOrtalamasi = (final*0.6)+(vize*0.4)

if (final<0 or vize<0) or (final>100 or vize >100) :
    print("hatalı not girişi yaptınız")

else:
    print(f"not ortalaması:{notOrtalamasi} ")
    if notOrtalamasi>=80 :
        print("harf notu: AA")

    elif notOrtalamasi>=70:
        print("harf notu: BB")

    elif notOrtalamasi>=60:
        print("harf notu: CC")

    elif notOrtalamasi>=50:
        print("harf notu: DD")

    elif notOrtalamasi>=0:
        print("harf notu: FF")

    else:
        print("hatalı giriş yaptınız")