def pierwiastek(liczba, dokladnosc):
    a = liczba
    b = 1
    area = a * b

    while abs(a - b) >= dokladnosc:
        a = (b + a) / 2
        b = area / a
    print(b)


pierwiastek(3, 0.0000001)
