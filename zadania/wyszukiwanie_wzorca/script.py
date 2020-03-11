def wyszukaj(wzor, string):
    for index, x in enumerate(string):
        if wzor[0] == x:
            p = True
            for index2, y in enumerate(wzor):
                if y != string[index + index2]:
                    return False
    return True


wyszukaj("ala", "ala ma kota")
