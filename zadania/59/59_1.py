f = open('liczby.txt', 'r')
lines = f.readlines()
liczby = []

for l in lines:
    if len(l) > 0:
        liczby.append(int(l))

def czynniki(n):
    c = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            c.append(k)
        k += 1
    return c

def czy_wystepuja_trzy_czynniki_nieparzyste(tab):
    c_n = []
    for in_x, x in enumerate(tab):
        if x % 2 != 0:
            ok = True
            for c in c_n:
                if c == x:
                    ok = False
            if ok: c_n.append(x)
    if c_n == 3:
        return True
    else:
        return False

def czynniki_2(l):
    ile = 0
    czynnik = 3
    if l % 2 == 0: return False
    while l > 0:
        if l % czynnik == 0:
            ile += 1
        while l % czynnik == 0:
            l = l / czynnik
        czynnik += 2
        if ile > 3: return False
    if ile == 3: return True
    else:  return False


ile_liczb = 0
for l in liczby:
    # if czy_wystepuja_trzy_czynniki_nieparzyste(czynniki(l)):
    #     ile_liczb += 1
    #     print("Aktualnie: "+str(ile_liczb)) # skrypt działa bardzo długo
    if czynniki_2(l): ile_liczb += 1

print(ile_liczb)