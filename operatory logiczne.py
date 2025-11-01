#Symbole logiczne

#Koniunkcja
print(2 == 3 and 3 > 1)

#Alternatywa
login = 'qwerty'
haslo = 'uiop'
print(login == 'admin' or haslo == 'uiop')

#Zaprzeczenie
print(not(login == 'admin' or haslo == 'uiop'))

#Alternatywa wykluczająca (1 prawda i 1 fałsz)
fryzjer = True
murarz = False

print(fryzjer == True ^ murarz == True)



# Priorytety operatorów logicznych
#1. (najpierw robi się and, później or)
print(2 == 3 and 3 > 1 or 2 > 6)

#2. (najpierw robimy not, później and a później or)
print(not(2 == 3 and 3 > 1 or 2 > 6))


# operatory standardowe
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

# potęgowanie
print(2 ** 5)


#pierwiastkowanie
print(36 ** 0.5)
print(125 ** (1/3))


#Dzielenie całkowite (div) - dzielimy i zaokrąglamy zawsze w dół do liczby całkowitej
print(12 // 5)

#Reszta z dzielenia liczby a przez liczbę b
print(12 % 5)



