plik3 = open('ruch.txt')
dane3 = plik3.readlines()
print(dane3)

for x in range(len(dane3)):
    dane3[x] = dane3[x].split()
    #dane3[x] = [float(dane3[x][0]), float(dane3[x][1])]
    dane3[x] = list(map(float, dane3[x]))
print(dane3)

def t(i):
    return (i - 1) / 100

def v_sr(rk, rp, dt):
    return [(rk[0] - rp[0]) / dt, (rk[1] - rp[1]) / dt]

def szyb_sr(v_sr):
    return (v_sr[0] ** 2 + v_sr[1] ** 2) ** 0.5

wynik = []
for i in range(1, len(dane3)):
    rp = dane3[0]
    rk = dane3[i]
    czas = t(i + 1)
    pr_sr = v_sr(rk, rp, czas)
    szybkosc_sr = szyb_sr(pr_sr)
    wynik.append((czas, szybkosc_sr))
print(wynik)