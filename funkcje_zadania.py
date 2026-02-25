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