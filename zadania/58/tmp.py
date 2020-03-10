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

    min = None
    rec = None
    rec_days = 0
    start_hour = None
    skok = {
        "min_value": None,
        "min_index": None,
        "max_value": None,
        "max_index": None,
        "max": None
    }

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
            elif time != start_hour + 24 * in_line and (in_line in wrong_index or s == 1):
                wrong_index.append(in_line)

            if skok["min_index"] is not None:
                if temp < skok["max_value"]:
                    skok["min_value"] = temp
                    skok["min_index"] = in_line
                r = (min - rec) ** 2
                r2 = (skok["min_index"] - in_line)
                r2 = r2 if r2 > 0 else 0 - r2
                if r2 > 0:
                    if skok["max"] > r / r2:
                        skok["max_index"] = in_line
                        skok["max_value"] = temp
                        skok["max"] = r / r2

    print("Min temp.: " + str(bin(min).replace("0b", "")))
    print("Rec temp.: " + str((rec)))
    print("Rec days.: " + str((rec_days)))
print("Liczba nieudanych pomiarów: " + str(len(wrong_index)))
# print(amount)
