def wyszukaj(wzor, string):
    for index, x in enumerate(string):
        if wzor[0] == x:
            s = True
            for index2, y in enumerate(wzor):
                if y != string[index + index2]:
                    s = False
            if s == True:
                return True
    return False


print(wyszukaj("ala", "sdghsdfgsrd ala ma kota"))