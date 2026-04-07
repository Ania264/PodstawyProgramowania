#Zad 2.1
plik2 = open('slowa.txt')
dane2 = plik2.readlines()
slowa = []
for s in dane2:
    slowo = s.strip()
    slowa.append(slowo)
print(slowa)
#print(dane2)
ilosc = 0
for x in range(len(slowa)):
    for y in range(len(slowa[x])):
        if slowa[x][y - 2] == 'k' and slowa[x][y] == 't':
            ilosc += 1
print(ilosc)

#Zad 2.2
takie_slowa = 0
wieksze_wystapienie = []
for z in range(len(slowa)):
    for w in slowa[z]:
        dlugosc = len(slowa[z])
        litera = slowa[z].count(w)
        if litera > dlugosc // 2:
            wieksze_wystapienie.append(slowa[z])
            takie_slowa += 1
print(wieksze_wystapienie)
print(takie_slowa)
