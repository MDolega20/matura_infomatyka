n = None
l = []

while n != "0":
    n = input("Wpisz liczbę: ")
    if int(n) > 0:
        l.append(int(n))
     

if len(l) > 0:
    x = []
    y = []
    for c in l:
        if c % 2:
            x.append(c)
        else:
            y.append(c)

print("Parzyste")
print(y)
print("Nie parzyste")
print(x)