#Pętla while - przykłady
'''liczba = 120
licznik = 0

while liczba > 0:   #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba = licznik // 2
    licznik = licznik + 1
print(licznik)
'''
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
i = 10

'''while i >= 1:
    print(i)
    i -= 1'''

for x in range(i):
    print(i)
    i -= 1
