def wydaj_reszte(input_money):
    nom = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, .1, 0.05, 0.02, 0.01]
    ilosc = [1, 10, 2, 2, 2, 2, 2, 100, 2, 2, 2, 2, 200, 200, 100]

    output = []
    while (input_money >= 0.01):
        for indn, n in enumerate(nom):
            if input_money / n > 0 and input_money > n and input_money > 0:
                while int(input_money / n) > 0 and ilosc[indn] > 0:
                    output.append(n)
                    input_money -= n
                    ilosc[indn] -= 1
        print(input_money)
    return output


print(wydaj_reszte(280.75))
