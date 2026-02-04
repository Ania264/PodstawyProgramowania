#Zadanie 6:
'''for x in range(1, 21):
    if x % 3 == 0 and x % 5 == 0:
        print(f'{x}, Fizz Buzz')
    elif x % 3 == 0:
        print(f'{x}, Fizz')
    elif x % 5 == 0:
        print(f'{x}, Buzz')
    else:
        print(x)'''

#Zadanie 7:
'''for x in range(1, 51):
    if x % 2 != 0 and x % 3 != 0:
        print(x)'''


#Zadanie 3:
'''x = int(input('Podaj liczbę'))
dzielnik = 2
ilosc_dziel = 0

for y in range(x):
    if x % dzielnik == 0:
        ilosc_dziel += 1
        dzielnik += 2
print(f'Liczba {x} posiada {ilosc_dziel} dzielników parzystych')'''


#Zadanie 4:
'''liczba = 99

for x in range(901):
    liczba += 1
    if liczba % 11 != 0:
        continue
    print(liczba, end = ',')'''

for x in range(1, 101):
    print(f'{x ** 2} \t {x ** 3} \t {x ** 4}')
