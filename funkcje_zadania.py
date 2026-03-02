#Zad 0.3
#a)
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]
wynik = suma_v(u, v)
print(wynik)


#b)
def iloczyn_v(u, v):
    il = []
    for i in range(len(u)):
        iloczyn = u[i] * v[i]
        il.append(iloczyn)
    return sum(il)


wynik2 = iloczyn_v(u, v)
print(wynik2)


#c) SPRAWDZ CZY GIT
'''def iloczyn_vik(v, k):
    ilo = []
    for i in range(len(v)):
        iloczyn = v[i] * k
        ilo.append(iloczyn)
    return sum(ilo)

k = 5
wynik3 = iloczyn_vik(v, k)
print(wynik3)'''


# Zad 2.1

def czy_anagramy(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

#print(cz_anagramy('nosek', 'keson'))
s1 = 'nosek'
s2 = "keson"
print(sorted(s1) == sorted(s2))

#Zadanie 2.2
def jaki_trojkat(a, b, c):
    if a + b + c > 2*max([a, b, c]):
        if a ** 2 + b ** 2 + c ** 2 == 2*max([a, b, c]) ** 2:
            print('prostokątny')
        elif a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]) ** 2:
            print('ostrokątny')
        elif a ** 2 + b ** 2 + c ** 2 < 2*max([a, b, c]) ** 2:
            print('rozwartokątny')
    else:
        print('To nie jest trójkąt')
jaki_trojkat(5, 5, 12)
