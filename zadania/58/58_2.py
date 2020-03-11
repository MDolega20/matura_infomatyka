amount = 0
wrong_index = []


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

    start_hour = None

    file = open('dane/dane_systemy' + str(s) + '.txt', 'r')
    lines = file.readlines()

    for in_line, line in enumerate(lines):
        if len(line) > 0:
            amount += 1

            time = con_to_10(line.split()[0], system)

            if start_hour is None:
                start_hour = time
            elif time != start_hour + 24 * in_line and (in_line in wrong_index or s == 1):
                wrong_index.append(in_line)

print("Liczba nieudanych pomiarów: " + str(len(wrong_index)))
