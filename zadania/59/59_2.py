f = open('liczby.txt', 'r')
lines = f.readlines()
liczby = []

for l in lines:
    if len(l) > 0:
        liczby.append(int(l))

def suma(l):
    return int(str(l)[::-1]) + l

def czy_polidron(l):
    if  int(str(l)[::-1]) == l:
        return True
    else: return False

ile_liczb = 0
for l in liczby:
    if czy_polidron(suma(l)):
        ile_liczb += 1

print(ile_liczb)