

def mais_proximo(rex, oli, bob):
    distanciaRex = abs(oli - rex)
    distanciaBob = abs(oli - bob)

    if distanciaRex > distanciaBob:
        for x in range(3):
            print(str(x+1)+".  ", end="")
            for i in range(20):
                print("-", end="")
                if i == rex:
                    print("R", end="")
                elif i == oli:
                    print("O", end="")
                elif i == bob:
                    print("B", end="")

            if rex > oli:
                rex -= 1
            else:
                rex += 1

            if bob > oli:
                bob -= 1
            else:
                bob += 1

            print("\n")
        return print("Bob chegará primeiro!")
    elif distanciaRex < distanciaBob:
        for x in range(3):
            print(str(x + 1) + ".  ", end="")
            for i in range(20):
                print("-", end="")
                if i == rex:
                    print("R", end="")
                elif i == oli:
                    print("O", end="")
                elif i == bob:
                    print("B", end="")

            if rex > oli:
                rex -= 1
            else:
                rex += 1

            if bob > oli:
                bob -= 1
            else:
                bob += 1
            print("\n")
        return print("Rex chegará primeiro!")
    else:
        for x in range(3):
            print(str(x + 1) + ".  ", end="")
            for i in range(20):
                print("-", end="")
                if i == rex:
                    print("R", end="")
                elif i == oli:
                    print("O", end="")
                elif i == bob:
                    print("B", end="")

            if rex > oli:
                rex -= 1
            else:
                rex += 1

            if bob > oli:
                bob -= 1
            else:
                bob += 1
            print("\n")
        return print("Rex e Bob chegarão ao mesmo tempo e vão brigar!")


rex = abs(int(input("Informe a posição que Rex está: ")))
oli = abs(int(input("Informe a posição que Oli está: ")))
bob = abs(int(input("Informe a posição que Bob está: ")))

mais_proximo(rex, oli, bob)