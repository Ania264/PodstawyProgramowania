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

# zadanie 14

a = float(input('podaj liczbe a rozna od 0'))
b = float(input('podaj liczbe b'))
c = float(input('podaj liczbe c'))

if a == 0:
    print('wspolczynnik powinien byc rozny od 1')

if b == c == 0:
    print('𝑥0 = 0')

if b == 0 and c != 0:
    if -(c / a) > 0:
        x1 = (-(c / a) ** 0.5)
        x2 = -(-(c / a) ** 0.5)
        print(f'x1 = {x1} v x2 = {x2}')
    if -(c / a) < 0:
        print('nie ma rozwiązań')

if c == 0 and b != 0:
    x1 = 0
    x2 = -(b / a)
    print(f'x1 = {x1} v x2 = {x2}')

if b != 0 and c != 0:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    if delta == 0:
        x0 = (-b) / (2 * a)
    if delta < 0:
        print('nie ma rozwiązań')

else:
    print('nie ma rozwiązań')