with open("liczby.txt", "r") as f:
    l = f.readlines()

    numbers = []

    for x in range(0,12):
        numbers.append(3**x)
        
    found = 0

    for x in l:
        if int(x) in numbers:
            found += 1

    print(found)