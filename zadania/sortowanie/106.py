
def find_index(el,tab):
    for index, i in enumerate(tab):
        if el == i:
            return index
    return -1

tablica = [12,13412,4213,54,23,5,2,345,23,41,43,12,54,324,6,45,632,5,34,25,4,32,4,23,52,345,2]

print(find_index(2, tablica))