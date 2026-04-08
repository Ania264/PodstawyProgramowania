plik = open('bin.txt')
dane = plik.readlines()
lista =[]
for x in dane:
    x = int(x.strip())
    lista.append(x)
print(lista)