def silnia(x):
    s = 1
    for c in range(1,x+1):
        s *= c
    return s

def czy_silnia(x):
    sum = 0
    for s in str(x):
        sum += silnia(int(s))
    if sum == x:
        print("Liczba: {}, suma silni: {}".format(x, sum))
        return True
    else:
        return False



with open("liczby.txt", "r") as f:
    l = f.readlines()

    found = []

    for x in l:
        if czy_silnia(int(x)):
            found.append(int(x))

    print(found)

    f.close()