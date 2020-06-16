def nwd(a,b):
    while b:
        a, b = b, a%b
    return a

with open("przyklad.txt", "r") as f:
    l = f.readlines()

    max_len = 0
    max_frst = 0
    max_dzielnik = 0

    ciag_max = []
    ciag_now = []

    last_nwd = 1

    for x in range(0, len(l)-1):
        a, b = last_nwd, int(l[x])
        nwd_n = nwd(a,b)
        # print("Nwd: {}, liczb: {} i {}".format(nwd_n,a,b))

        if nwd_n > 1:
            ciag_now.append(b)
            last_nwd = nwd_n
        else:
            last_nwd = b
            ciag_now = []
            ciag_now.append(b)

        if len(ciag_now) > len(ciag_max):
            ciag_max = []
            ciag_max.extend(ciag_now)
            max_dzielnik = nwd_n
            max_frst = ciag_max[0]
            max_len = len(ciag_max)

    print("Pierwsza liczba ciągu: {}, długość: {}, największy wspólny dzielnik: {}".format(max_frst, max_len, max_dzielnik))

    f.close()