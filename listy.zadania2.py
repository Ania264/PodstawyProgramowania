#Zadanie 2
'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]
x_max = max(lista)
x_min = min(lista)

print(lista)
lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''

#Zadanie 3
#sposób1
''''lista2 = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
lista2 = [x for x in lista2 if x < 1000 or x > 9999]
print(lista2)

#sposób2
lista2 = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
lista2 = [x for x in lista2 if not (x >= 1000 and x <= 9999)]
print(lista2)'''''



#Zadanie 4

#sposób 1
tekst = "LITWOOJCZYZNOMOJATYJESTESZJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILDZISPIEKNOSCTWACALEJOZDOBIEWIDZEIOPISUJEBOTESKNIEPOTOBIEPANNOSWIETACOJASNEJBRONISZCZESTOCHOWYIOSTREJSWIECISZBRAMIETYCOGRODZAMKOWYNOWOGRODZKIOCHRANIASZZJEGOWIERNMLUDEMJAKMNIEDZIECKODOZDROWIAPOWROCILASCUDYMGDYODPLACZACEJMATKIPODTWOJAOPIEKEOFIAROWANYMARTWAPODNIOSELMOJEPOWIEKEIZARAZMOGLEMPIESZODOTWYCZSWIATYNPROGUISTZAWROCONEZYCIEPODZIEKOWACBOGUTAKNASPOWROCISCUDYMNADOJCZYZNYLONOTYMCZASEMPRENOSMOJADUSZEUTESKNIONADOTYCHPAGORKOWLESNYCHDOTYCHLAKZIELONYCHSZEROKONADBLEKITNYMNIEMNEMROZCIAGNIONYCHDOTYCHPOLMALOWANYCHZBOZEMROZMAITEMWYZLACANYCHPSZENICAPOSREBRZANYCHZYTEMGDZIEBURSZTYNOWYSWIERZOPGRYKAJAKSNIEGBIALAGDZIEPANIENSKIMRUMIENCEMDZIECIELINAPALAAWSZYSTKOPRZEPASANEJAKBYWSTEGAMIEDZAZIELONANANIJZZADKACICHEGRUSZESIEDZA"
suma = 0
for x in tekst:
    ord(x)
    suma += ord(x)
print(suma)

#sposób 2
print(sum(list(map(ord, tekst))))

#sposób 3
kod_ascii_map = map(ord, tekst)
kod_ascii_lista = list(kod_ascii_map)
suma2 = sum(kod_ascii_lista)
print(suma2)


#ZADANIE 5 DO DOMU
lista = ['informatyka', 'matematyka', 'fizyka', 'geografia', 'biologia', 'chemia']

#sposób 1
b = 'biologia'
if b in lista:
    print('Jest')
else:
    print('Nie ma')

#sposób 2
l = 0
for x in lista:
    if x == 'biologia':
        print('Jest')
        l += 1
if l == 0:
        print('Nie ma')

#sposób 3
lista.index('biologia')
if lista.index('biologia') >= 0:
    print('Jest')

#sposób 4
lista.count('biologia')
if lista.count('biologia') > 0:
    print('Jest')
else:
    print('Nie ma')

#sposób 5
#??????
