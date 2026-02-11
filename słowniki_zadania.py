lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]

zbior_caly = set()   #pusty zbior
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior_caly.add(element)
print(zbior_caly)

for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)
print(zbior_caly)

#1.2
lista1d = []
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        lista1d.append(element)