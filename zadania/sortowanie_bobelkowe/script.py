def sort_boble(tablica):
    change = False
    for index in range(0, len(tablica) - 1):
        for index in range(0, len(tablica) - 1 - index):
            change = False
            if index <= len(tablica) - 1:
                if tablica[index + 1] < tablica[index]:
                    c = tablica[index + 1]
                    tablica[index + 1] = tablica[index]
                    tablica[index] = c
                    change = True
        if change == False:
            break
    return tablica


print(sort_boble([1, 5, 6, 3222, 3333, 3, 3, 8, 9, 10, 888888888888888, 3423432, 2343254325, 31523523, 11]))
