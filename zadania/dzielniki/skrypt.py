import math

def znajdz_dzielniki(liczba):
    dzielniki = []
    for i in range(2, math.ceil(math.sqrt(liczba))):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki;


print(znajdz_dzielniki(5880))
