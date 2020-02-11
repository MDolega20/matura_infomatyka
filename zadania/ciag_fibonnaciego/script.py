
def gen_ciag(max):
    ciag = [1,1]
    for i in range(2, max):
        ciag[i] = ciag[i-1]+ciag[i-2]

    print(ciag)

gen_ciag(100)