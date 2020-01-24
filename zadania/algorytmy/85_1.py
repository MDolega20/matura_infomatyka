
nominaly = [50,20,10,5,2,1,0.5,0.20,0.10,0.05,0.02,0.01]

def wydaj_reszte(wartosc):
    reszta = []

    while wartosc > 0:
        for in_n, n in enumerate(nominaly):
            dziel = wartosc / n
            if dziel >= 0:
                for z in range(0,int(dziel)):
                    reszta.append(n)
                    wartosc -= n
    return reszta


test = [13,15.5,99]

for i in test:
    print(i)
    print(wydaj_reszte(i))
