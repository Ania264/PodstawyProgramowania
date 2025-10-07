#1. Wprowadzanie danych przez użytlownika do programu
#1) utworzenie zmiennej
#2) na ekranie pojawia się komunikat z inputa
#3) program się zatrzymuje i czeka na podanie danych oraz zatwierdzenie tego ENTEREM
#4) po wpisaniu i zatwierdzeniy ENTEREM to co wpiszemy trafia jako string do zmiennej
#5) i program wykonuje się dalej
imie = input('Podaj swoje imię')

liczba = int(input('Podaj liczbę'))
print(type(liczba))

liczba_z_przecinkiem = float(input('Podaj liczbę z przecinkiem'))
print(type(liczba_z_przecinkiem))

cos = list(input('Podaj coś'))
print(cos)
print(type(cos))