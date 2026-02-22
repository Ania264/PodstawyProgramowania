#Zad. 2 listy zestaw 1:
lista = ['kot', 'pies', 'żółw', [4, 6, 7, 1], 2.7, [[8, 9], [3, 5]]]
#d)
print(lista)
'''lista.extend([11, 17])
print(lista)'''

lista.append([11, 17])
print(lista)

#Zad 3
przeslanie = [[90, 65, 87, 83, 90, 69], [87, 65, 82, 84, 79], [66, 89, 67], [80, 82, 90, 89, 90, 87, 79, 73, 84, 89, 77]]
print(' '.join([''.join(map(chr, s)) for s in przeslanie]))


#Zad 6
tekst = 'NAUCZYCIELEMWSZYSTKIEGOJESTPRAKTYKA'
'''tekst2 = set(tekst)
for i in tekst2:
    w = tekst.count(i)
    print(f'litera {i} wystąpiła {w} razy')'''

tekst2 = set(tekst)
maks = 0
l = ''
for i in tekst2:
    w = tekst.count(i)
    if w > maks:
        maks = w
        l = i
print(f'litera {l} wystąpiła najwięcej, czyli {maks} razy')