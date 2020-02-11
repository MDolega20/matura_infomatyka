def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a


def dec_to_bin(number):
    out = ""

    while(number > 0):
        out += str(number % 2)
        number = number // 2

    out = reverse(out)

    return out;

print(dec_to_bin(50))