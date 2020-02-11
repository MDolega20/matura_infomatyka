import math

def znajdz_dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki;

def czy_liczba_doskonala(liczba):
    out = 0
    for x in znajdz_dzielniki(liczba):
        out += x

    print(znajdz_dzielniki(liczba))
    if out == liczba:
        return True
    else:
        return False

print(czy_liczba_doskonala(6))