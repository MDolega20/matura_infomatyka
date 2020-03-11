def funkcja(x):
    return x ** 2


def oblicz(start, end, episolon):
    pole = 0
    step = (end - start) / episolon
    pos = 0

    while pos <= end:
        s = pos
        s1 = s + step
        s2 = (s1 + s) / 2
        p1 = funkcja(s2) * step
        pole += p1
        pos += step

    print(pole)


oblicz(1, 5, 10000000)
