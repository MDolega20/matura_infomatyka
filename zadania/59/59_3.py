f = open('liczby.txt', 'r')
lines = f.readlines()
liczby = []

for l in lines:
    if len(l) > 0:
        liczby.append(int(l))

def oblicz_iloczyn(l):
    i = 1
    for x in str(l):
        i *= int(x)
    return i

def jaka_moc(l):
    m = 0
    n = l
    while n >= 10:
        n = oblicz_iloczyn(n)
        m += 1
    return m

moce = [
    0,0,0,0,0,0,0,0,0
]
min_1 = None
max_1 = None

for l in liczby:
    moce[jaka_moc(l)] += 1

    if min_1 == None:
        if jaka_moc(l) == 1:
            min_1 = l
    else:
        if jaka_moc(l) == 1 and min_1 > l:
            min_1 = l
    if max_1 == None:
        if jaka_moc(l) == 1:
            max_1 = l
    else:
        if jaka_moc(l) == 1 and max_1 < l:
            max_1 = l

                    # print(jaka_moc(l))
    # if czy_polidron(suma(l)):
    #     ile_liczb += 1

for in_m, m in enumerate(moce):
    print(str(in_m)+" "+str(m))
print("Min: "+str(min_1))
print("Max: "+str(max_1))