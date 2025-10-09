#1. Co można wyświet;ić printem?
print(5)
print((2+2)*2)

x = 34

print(x)

print('informatyka')
print(round(2.234, 2))
print(2 == 3 and 1 > 0)
print([6, 1, 9, 4, 2])

#2. Formatowanie wyświetlenia tekstu

imie = input('Podaj imie')
nazwisko = input('Podaj nazwisko')
wiek = int(input('Podaj swój wiek'))

#sposób 1
'''print('Witaj ' + imie + ' ' + nazwisko + '. Masz ' + str(wiek) + 'lat. Za 5 lat będziesz mieć ' + str(wiek +5) + ' lat')'''


#sposób 2
'''print(f'Witaj {imie} {nazwisko}. Masz {wiek} lat. Za 5 lat będziesz mieć {wiek + 5} lat.')'''


liczba = 4.1234
#komenda {liczba: 0.2f} oznacza, że liczbę, która kryje się pod zmienną zaokrąglamy do 2 miejsc po przecinku.
print(f'Kwota = {liczba: 0.2f}')


#sposób 3.1.
print('Witaj {} {}. Masz {} lat. Za 5 lat będziesz mieć {} lat.'.format(imie, nazwisko, wiek, wiek + 5))


#sposób 3.2.
print('Witaj {1} {0}. Masz {3} lat. Za 5 lat będziesz mieć {2} lat.'.format(nazwisko, imie, wiek, wiek + 5))