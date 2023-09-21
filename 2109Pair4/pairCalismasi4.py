""" İlk iki elamanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturun.
Fibonacci Serisi : Serideki her bir sayı kendisinden önceki iki sayısının toplamına eşittir """

fibonacci = [1,1]
for i in range(25):
    fibonacci.append(fibonacci[-1]+ fibonacci[-2])

print(fibonacci) 