f = open('ciagi.txt', 'r')

f = f.readlines()
counter = 0
max_r = 0

for x in f:

    x = x.split()
    r = None
    rp = None
    ciag = True

    last = None

    for i_l, l in enumerate(x):
        if last is not None:
            r = l - last
            if r != rp:
                ciag = False
            rp = r
        else:
            last = l



    # for i_l, l in enumerate(x):
    #     if i_l < len(x)-1:
    #         if r is None:
    #             r = int(x[i_l+1]) - int(x[i_l])
    #         if r != int(x[i_l+1]) - int(x[i_l]):
    #             ciag = False
    if ciag:
        counter = counter + 1

        print(r)
        # if r > max_r:
        #     max_r = r

print(f)
print(max_r)
print(counter)