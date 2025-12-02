'''lista = [1]

for i in lista:
    liczba = float(input("Podaj liczbę"))
    print(liczba)
    if liczba != 0:
        lista.append(11)

for i in lista:
    print(i)
    lista.append(i + 1)'''


#Zadanie 2. gr. B
#sposób 1:
lista = [12, 45, 78, 101, 9, -5, 9, 7, 23]
'''for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i])'''

#sposób 2:
'''for i in range(1, len(lista), 2):
    print(lista[i])'''


#sposób 3:
'''for i in lista[1::2]:   #[45, 101, -5, 7]
    print(i)'''

#sposób 4:
'''i = 1
while i < len(lista):
    print(lista[i])
    i = i + 2'''



#Zadanie 4. gr. B
lista3 = [100]

'''for x in lista3:
    print('xd')
    #jakbyśmy teraz skończyli, to by wydrukowało się tylko raz "xd" bo jest w liście 1 element
    lista3.append(100)  #w nawiasie można podać cokolwiek'''


    for x in lista3:
        liczba = float(input("Podaj liczbę"))
        print(liczba)
        if liczba != 0:
            lista3.append(1)