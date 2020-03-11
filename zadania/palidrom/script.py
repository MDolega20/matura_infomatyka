def palidron(a, b):
    if a == b[::-1]:
        return True
    return False


print(palidron("kot", "tok"))
