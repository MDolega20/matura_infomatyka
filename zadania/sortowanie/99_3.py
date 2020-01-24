
liczby = [10,5,6,4,3,2,1,100,67,465,46346,3464]

def sortowanie_bobelkowe(tab):
    for z in tab:
        for in_x, x in enumerate(tab):
            if in_x+1 != len(tab):
                if tab[in_x] > tab[in_x + 1]:
                    c = tab[in_x + 1]
                    tab[in_x + 1] = tab[in_x]
                    tab[in_x] = c
    return tab

print(liczby)
print(sortowanie_bobelkowe(liczby))