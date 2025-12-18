from random import randint
from time import sleep

#Pętla while - przykłady
'''liczba = 120
licznik = 0

while liczba > 0:   #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba = licznik // 2
    licznik = licznik + 1
print(licznik)
'''
import time

#Zadanie 1:
'''x = input('Podaj liczbę lub q aby zakończyć')
licznik =0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć')
print(f'Liczb mniejszych od 2 jest {licznik}')'''


#Zadanie 2 - Logowanie:
#nieskończone próby:
'''popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
while haslo != popr_haslo:
    print('Błędne hasło. Spróbuj ponownie')
    haslo = input('Podaj hasło')
print('Witaj w systemie!')
'''
#5 pób:
'''popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('Błędne hasło. Spróbuj ponownie')
    haslo = input('Podaj hasło')
    proba = proba + 1
if haslo == popr_haslo:
    print('Witaj w systemie!')
else:
    print('Nie ma hasła - nie ma dostępu!')'''


#ZAD DOM - Zad 3 i 4

#Zadanie 3:
'''n = 20
wynik = 0
while n >= 0:
    n -= 1
    if n % 2 == 1:
        continue
    wynik += n

print(wynik)'''

#Odp: Efektem wykonania tego kodu będzie wypisanie przez program liczby 90.
#Dzieje się tak, gdyż na początku program wpada w pętlę while, która wykouje się póki n >= 0.
#Na początku od n odejmujemy 1 czyli będzie 19. Reszta z dzielenia n przez 2 wynosi 1,
#więc program wraca do góry i się kontynuuje. Dalej znowu odejmujemy od n 1 i wychodzi 18.
#Reszta z dzielenia 18/2 wynosi 0, więc do wyniku dodajemy wartość n.
#Tu zauważamy, że do wyniku będą dodawane wszystkie parzyste liczby,
#bo co 2 odejmowanie reszta z dzielenia będzie wynosić 0.
#Czyli dodajemy: 18, 16, 14, 12, 10, 8, 6, 4, 2 i 0. Suma tych liczb to 90.


#Zadanie 4:
'''i = 10

while i >= 1:
    print(i)
    i -= 1

for x in range(i):
    print(i)
    i -= 1'''


#ZAD.5 DO DOMU
'''x, y = 0, 0
ruchy = ['p'] * 10 + ['d'] * 5 + ['l'] * 5 + ['g'] * 10 + ['q']


while True:
    #ruch = input("podaj ruch")
    ruch = ruchy[randint(0, len(ruchy) - 1)]
    if ruch == 'q':
        print('Koniec gry')
        break
    elif ruch == 'g':
        if y < 9:
            y += 1
        else:
            print("Niemożliwe")
    elif ruch == 'd':
        if y > 0:
            y -= 1
        else:
            print('Niemożliwe')
    elif ruch == 'l':
        if x > 0:
            x -= 1
        else:
            print('Niemożliwe')
    elif ruch == 'p':
        if x < 9:
            x += 1
        else:
            print('Niemożliwe')
    else:
        print('Nieznany ruch')
    print(f'({x}, {y})')
    sleep(1)'''

#Zad. 6:
wynik1 = 0
wynik2 = 0
akcja = 0

'''while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2):
    akcja += 1
    wygrana = int(input('Podaj drużynę wygraną'))
    if wygrana == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Akcja {akcja}')
    print('Podaj nr drużyny która wygrała')
    print(wygrana)
    print(f'Wynik {wynik1}:{wynik2}')
if wynik1 > wynik2 :
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')'''


#Symulacja gry z użyciem "RANDOM":



'''while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2):
    akcja += 1
    wygrana = randint(1,2)
    if wygrana == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Akcja {akcja}')
    print(wygrana)
    print(f'Wynik {wynik1}:{wynik2}')
    sleep(1)
if wynik1 > wynik2 :
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')'''


#Zadanie 7:
'''liczba = int(input('Podaj liczę'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')
'''

#Zadanie 8:
'''liczba = int(input('Podaj liczbę'))
d = 2
ile_czyn = 0
ile_r_czyn = 0

while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)'''