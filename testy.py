'''lista = [2, 5, 6, 8, 9, 11]
suma = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        suma = suma + lista[i]
print(suma)'''

a = int(input('Podaj liczbę'))
b = int(input('Podaj kolejną liczbę'))
x = 1
y = 1


for i in range(a * b):
    if x <= a and y <= b:
        print(f'({x}, {y})')
        #x = x + 1
        y = y +1


    if x <= a and y <= b:
        print(f'({x}, {y})')
        x = x + 1

'''elif x < a and y <= b:
print(f'({x - 1}, {y})')
y = y + 1'''