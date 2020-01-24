# silnia

def silnia(b):
    wynik = 1
    for n in range(1,int(b)+1):
        wynik = wynik * n
    return wynik

print(silnia(10))

