#Zad 3
plik3 = open('liczby.txt')
dane3 = plik3.readlines()

liczby = []
for x in range(len(dane3)):
    l = dane3[x].strip()
    liczby.append(l)
print(liczby)

ilosc = 0
lista = []
for x in range(len(liczby)):
    if liczby[x][0] == liczby[x][-1]:
        ilosc += 1
        lista.append(liczby[x])
print(ilosc, lista[0])
