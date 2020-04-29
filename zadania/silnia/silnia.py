
def silnia(l):
    w = 1
    for x in range(1,l+1):
        w *= x
    return w

def symbol_newton(n, k):
    return silnia(n) / (silnia(k) * silnia(n - k))

print(symbol_newton(1,4))