plik = open('sily.txt')
dane = plik.readlines()
print(dane)

for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i][0] = float(dane[i][0])
    dane[i][1] = float(dane[i][1])
print(dane)

max_sila = 0
max_F = []
for F in dane:
    sila = (F[0] ** 2 + F[1] ** 2) ** 0.5
    if sila > max_sila:
        max_sila = sila
        max_F = F
print(max_F, max_sila)
