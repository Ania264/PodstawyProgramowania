# 'w' od write, pozwala nam zapisywać ciągi znaków w utworzonym pliku, jeśli jest 'r' od read, plik jest tylko do odczytu
plik = open('test.txt', 'a') #Tu było wcześniej open('test.txt', 'w') zobacz linijka 16

#jeśli możliwe jest edytowanie pliku, będzie True, czyli pętla będzie się wykonywać
#gdyby plik miałby 'r' czyli byłby tylko do odczytu, byłoby False, czyli pętla by się nie wykonała
if plik.writable():
    plik.write(input('Wprowadź tekst: ') + '\n')
plik.close()

#aby zobaczyć to co jest w pliku txt w konsoli, trzeba:
plik = open('test.txt', 'r')
'''if plik.readable():
    print('Zawartość pliku:')
    tekst = plik.read()
    print(tekst)'''
#tutaj widzimy że niestety to co jest w pliku txt automatycznie się usuwa rzy ponownym uruchomieniu programu
#by temu zapobiec zamieniamy skrót 'w' na 'a' od append, czyli dodawać


#sczytywanie wszystkich linii z pliku tworząc listę
'''if plik.readable():
    print('Zawartość pliku:')
    tekst = plik.readlines()
    print(tekst)
    for l in tekst:
        print(l)
'''

#Najłatwiejszy sposób na możliwość wyświetlenia zawartości pliku:
if plik.readable():
    print('Zawartość pliku:')
    for l in plik:
        print(l)