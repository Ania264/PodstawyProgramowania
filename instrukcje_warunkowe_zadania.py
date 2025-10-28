#Rozwiązywania równania kwadratowego
'''
a = float(input('Podaj liczbę a =/= 0'))
b = float(input('Podaj liczbę b'))
c = float(input('Podaj liczbę c'))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print ('x1 = x2 = {}'.format(x))
else:
    print('Brak rozwiązań')
'''


#Zadanie 12
pisemny_j_polski = int(input('pisemny polski'))
pisemny_j_obcy = int(input('pisemny obcy'))
pisemny_dodatkowy = int(input('pisemny dodatkowy'))
ustny_j_polski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny polski'))


#Zadanie 14
a = float(input('Podaj liczbę a =/= 0'))
b = float(input('Podaj liczbę b'))
c = float(input('Podaj liczbę c'))

if b == 0 and c == 0:
    print(f'wynik = 0')
if b == 0 and c != 0:
    if -c/a > 0:
        x1 = (-c/a) ** 0.5
        x2 = -((-c/a) ** 0.5)
        print(f'x1 = {x1} v x2 = {x2}')
    if -c/a < 0:
        print(f'Równanie nie ma rozwiązań. (jest sprzeczne)')
if c == 0 and b != 0:
    x1 = 0
    x2 = -(b)/(a)
    print(f'x1 = {x1} v x2 = {x2}')
if b != 0 and c != 0 #zamiast tego mogłoby być else
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    elif delta == 0:
        x = (-b) / (2 * a)
        print('x1 = x2 = {}'.format(x))
    else:
        print('Brak rozwiązań')
