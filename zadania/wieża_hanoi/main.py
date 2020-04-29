
palik_1 = ["1","2","3"]
palik_2 = []
palik_3 = []

def przenies():
    for i_x, x in enumerate(palik_1):
        deleted = False
        if len(palik_2) == 0:
            palik_2.insert(0,x)
            deleted = True
        elif palik_2[len(palik_2)-1] > x:
            palik_2.insert(0,x)
            deleted = True
        elif len(palik_3) == 0:
            palik_3.insert(0,x)
            deleted = True
        elif palik_3[len(palik_3) - 1] > x:
            palik_3.insert(0,x)
            deleted = True
        if deleted:
            palik_1.remove(x)

        break

while len(palik_1) > 0:
   przenies()

   print(palik_1)
   print(palik_2)
   print(palik_3)