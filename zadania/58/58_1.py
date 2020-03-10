amount = 0

def con_to_10(number, system):
    return int(number, system)
def con_to_dec(number):
    return bin(number)


for s in range(1, 4):
    print("Stacja " + str(s))
    if s == 1:
        system = 2
    elif s == 2:
        system = 4
    elif s == 3:
        system = 8

    min = None

    file = open('dane/dane_systemy' + str(s) + '.txt', 'r')
    lines = file.readlines()

    for in_line, line in enumerate(lines):
        if len(line) > 0:
            amount += 1

            time = con_to_10(line.split()[0], system)
            temp = con_to_10(line.split()[1], system)

            if min is None or min > temp:
                min = temp
            if rec is None or rec < temp:
                rec = temp
                rec_days += 1
            if start_hour is None:
                start_hour = time

    print("Min temp.: " + str(bin(min).replace("0b", "")))
# print(amount)