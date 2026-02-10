#Zadanie 6.1
plansza = [
[3,  8,  1,  9],
[4,  6,  5,  2],
[7,  1,  8,  3],
[2,  9,  4,  6]
]


# Zadanie 6.1.
'''
#średnie w wierszach
for x in plansza:
    print(sum(x) / len(x))

#średnie w kolumnach
for i in range(len(plansza[0])):
    suma = 0
    for j in range(len(plansza)):
        suma += plansza[j][i]
    print(suma / len(plansza))'''

# Zadanie 6.2.
'''for i in range(len(plansza)):
    for j in range(len(plansza[0])):
        licznik = 0
        srodkowy = plansza[i][j]  # szary element'''
'''        if srodkowy < plansza[i - 1][j]:
            licznik += 1
        if srodkowy < plansza[i + 1][j + 1]:
            licznik += 1'''

'''        for x in range(i - 1, (i + 1) + 1):
            for y in range(j - 1, (j + 1) + 1):
                if i < 0:
                    x = len(plansza) - 1
                elif x > len(plansza) - 1:
                    x = 0
                if y < 0:
                    y = len(plansza[0]) - 1
                elif y > len(plansza[0]) - 1:
                    y = 0
                czerwony = plansza[x][y]
                if srodkowy < czerwony:
                    licznik += 1
        print(i, j, licznik)
'''

#6.3
#Suma liczb jest największa w wierszu 1 i 4
#Iloczyn liczb jest największy w kolumnie 2

#6.4
#???????????

#8.
lista = [1, 5, 1, 2, 2, 1, 6, 7, 3, 2, 2, 1, 1, 4]
zbior = []

for i in lista:
    if i not in zbior:
        zbior.append(i)
        lista.count(i)
        print(f'{i} wystąpiło {lista.count(i)} razy.')
print(zbior)


#9.
plecak = [
("książka", 1.2),
("zeszyt", 0.5),
("laptop", 2.5),
("piórnik", 0.3),
("butelka z wodą", 1.0),
("strój sportowy", 1.8)
]



'''rzeczy_w1 = []

for i in range(len(plecak)):
    for j in range(len(plecak[0])):
        j += 1
        if j > plecak[4][1]:
            rzeczy_w1.append(plecak[i][j-1])
print(rzeczy_w1)'''

#??????????

#10.
#????????????