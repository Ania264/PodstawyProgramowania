#Pętla while - przykłady
liczba = 120
licznik = 0

while liczba > 0:   #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba = licznik // 2
    licznik = licznik + 1
print(licznik)

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