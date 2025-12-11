#Zadanie 2
lista = [4, 12, 8, 1, 5, 6, 3]
licznik = 0

#sposób 1:
'''for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] != lista[y] and (lista[x] + lista[y]) % 3 == 0:
            #print(f'({lista[x]},{lista[y]})')
            licznik += 1
print(licznik)'''

#sposób 2:
'''for x in lista:
    for y in lista:
        if x != y and (x + y) % 3 == 0:
            #print(x, y)
            licznik += 1
            print(licznik)'''

#Zadanie 3:
n = int(input('Podaj ile będzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)
