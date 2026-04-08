#Zad 2.1
plik2 = open('liczby.txt')
dane2 = plik2.readlines()
for x in range(len(dane2)):
    dane2[x] = dane2[x].strip()

for x in dane2:
    if int(x[::-1]) % 17 == 0:
        print(x[::-1])

#Zad 2.2
print(len(set(dane2)))

podwojne = 0
potrojne = 0
for x in set(dane2):
    ilosc = dane2.count(x)
    if ilosc == 2:
        podwojne += 1
    elif ilosc == 3:
        potrojne += 1
print(podwojne, potrojne)