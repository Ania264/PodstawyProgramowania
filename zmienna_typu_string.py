napis = 'informatyka'

#każdy znak napisu ma swój indeks. Indeksy zaczynają się od 0, a NIE od 1

#I. Fragment tekstu:
#1) wycinanie od ... do
print(napis[2:5]) #czyli tak naprawdę od 2 do 4

#2) wycinanie od ... do co ileś
print(napis[2:10:2])    #czyli program będzie wypisywał znaki od 2 do 9 co 2

#3) wycinanie od początku
print(napis[:3])    #czyli program wypisze znaki od początku do 2

#4) wycinanie do końca
print(napis[7:])    #czyli program wypisze wszystkie znaki od 7 do końca

#5) czytanie od końca
print(napis[::-2])  #program napisze napis od końca, co drugi znak

#II. Zawieranie się znaku w słowie
if 'x' in napis:
    print('należy')
else:
    print('nie należy')

#III. Łączenie napisów (konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

#IV. Funkcje zmiennych typu string

#1) poszukiwanie danego fragmentu w tekście
napis3 = 'matematyka'
index_gdzie_jest1 = napis3.find('tem')
print(index_gdzie_jest1)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
#program wypisze indeks znaku, na którym zaczyna się szukany fragment
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
#program wypisze indeks znaku, na którym zaczyna się szukany fragment za drugim razem
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz jest w napisie')
else:
    print('xyz nie jest w napisie')

#2.)Podział tekstu na fragmenty
'''c_liczb = input('Podaj pięć liczb. Oddziel je przecinkiem')
piec_liczb_po_podziale = piec_liczb.split(',')
#ta funkcja tworzy listę. Elementy, które wcześniej były oddzielone ",", teraz są osobnymi elementami listy
#po funkcji .split() w nawiasie podajemy znak, którym oddzielone mają być znaki podane przez użytkownika
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
#w nawiasie kwadratowym po nazwie zmiennej podajemy indeks liczby, której akurat potrzebujemy
print(trzecia_liczba + 33)'''

#3.) Łączenie napisów
lista_napisow = ['Windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '@'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
# \n oznacza znak nowej linii, więc każdy z elementów listy_napisow_2 będzie zapisany od nowej linii
print(cale_zdanie2)

#4.) Zliczanie danego znaku w tekście
napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)


#5.) "Mutowalność" stringów
napis6 = "fiwyka"
'''napis6[2] = "z"
print(napis6)'''
#Wniosek: Stringi są niemutowalne, czyli nie można podmieniać pojedynczych liter

#Sposób na zmutowanie stringa
napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = "z"
print(napis6_lista)
napis6 = ''.join(napis6_lista)
print(napis6)


#6.) Długość napisu
napis7 = 'językpolski'
print(len(napis7))

#7.) Powielanie stringa
napis8 = 'informatyka'
print(napis8 * 3)


#8.) Funkcje testujące cyfry i litery
napis9 = 'qwerty'
if napis9.isalpha() == True:
    print('słowo składa się z liter')
else:
    print('słowo nie składa się z liter')


napis10 = '1410'
if napis10.isdigit() == True:
    print('słowo składa się z cyfr')
else:
    print('słowo nie składa się z cyfr')

napis11 = '1410w'
if napis11.isalnum() == True:
    print('słowo składa się tylko z cyfr lub liter')
else:
    print('słowo nie składa się tylko z cyfr lub liter')


#9.) Kody ASCII

#9.1 ze znaku na kod ASCII
print(ord('A'))

#9.2 z kodu ASCII na znak
print(chr(66))

#Zagadka co wyjdzie:
print(chr(ord('Z')))
#wyjdzie Z, bo najpierw robimy kod ASCII z Z czyli 90, a poóźniej znak z kodu 90 czyli z powrotem Z.


#10.) Funkcja translate
slownik = str.maketrans('ąęćóżśźłń', 'aecozszln')
napis12 = 'ińfórmątyką'
napis_poprawny = napis12.translate(slownik)
print(napis_poprawny)


#11.) Funkcje dużych i małych literek
napis13 = 'KoNgO'
napis13_tylko_duże = napis13.upper()
print(napis13_tylko_duże)

napis13_tylko_małe = napis13.lower()
print(napis13_tylko_małe)


#12.) Podstawianie ciągu znaków
napis14 = 'chleb kosztuje 15 zł, a bułka 5 zł.'
napis14_w_euro = napis14.replace('zł', '€')
print(napis14_w_euro)


#13.) Sortowanie i odwracanie napisu
#13.1 odwracanie napisu
napis15 = 'kemot'
napis15_odwrotnie = napis15[::-1]

#13.2 sortowanie napisu
napis16 = 'dbca'
napis16_posortowany_lista = sorted(napis16)
napis16_posortowany = ''.join(napis16_posortowany_lista)
print(napis16_posortowany)