#1) listy a napis
napis = 'informatyka'

'''lista = []
for l in napis:
    lista.append(l)
print(lista)'''

#Zamiana napisu na listę
lista = list(napis)
print(lista)

#2) Zakres i lista
zakres = range(3, 10, 2)
lista2 = list(zakres)
print(lista2)


#3) Indeksowanie elementów listy
lista3 = ['osa', 99, 3.14, [5, 7, 8, 9]]
print(lista3[1:3])  #wycinanie fragmentu listy
print(lista3[3][2])   #obsługa listy zagnieżdżonej
print(lista3[3][::2])   #obsługa listy zagnieżdżonej


#4) Powielanie listy
#dodawanie list
lista4 = ['a', 45, 78]
lista5 = [[4, 8], 56, 12]
lista6 = lista5 + lista4
print(lista6)

#dodawanie list2
lista7 = ['a', 45, 78]
lista8 = [[4, 8], 56, 12]
lista8.extend(lista7)
print(lista8)


#"mnożenie" listy przez liczbę
lista9 = [0] * 1000
'''lista10 = [[0] * 10] * 10
lista10[0][0] = 5
print(lista10)'''
