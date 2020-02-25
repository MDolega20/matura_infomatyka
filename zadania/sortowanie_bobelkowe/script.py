def sort_boble(tablica):
    for index in range(0, len(tablica) - 1):
        for index in range(0, len(tablica) - 1 - index):
            if index <= len(tablica) - 1:
                if tablica[index + 1] < tablica[index]:
                    c = tablica[index + 1]
                    tablica[index + 1] = tablica[index]
                    tablica[index] = c
    return tablica


print(sort_boble([1, 5, 6, 3222, 3333, 3, 3, 8, 9, 10, 11]))
