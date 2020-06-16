
def algorytm_euklidesa(a,b):
    def x(a,b):
        k = b
        b = a % b
        a = k
        if b != 0:
            x(a, b)
        else: 
            return a 
    return x(a, b)

print("50, 15  => "+str(algorytm_euklidesa(50,5)))

