try:
    prvni_cislo = float(input("Zadejte prvni cislo: "))
    znamenko = input("Zadejte znamenko (+, -, *, /): ")
    druhe_cislo = float(input("Zadejte druhe cislo: "))


    if znamenko == '+':
        vysledek = prvni_cislo + druhe_cislo
    elif znamenko == '-':
        vysledek = prvni_cislo - druhe_cislo
    elif znamenko == '*':
        vysledek = prvni_cislo * druhe_cislo
    elif znamenko == '/':
        try:
            vysledek = prvni_cislo / druhe_cislo
        except ZeroDivisionError:
            print("Nulou nelze delit.")
    else:
        vysledek = "Chyba."

    print(f"Vysledek je {vysledek}.")

except ValueError:
    print("Chyba: Zadejte cislo.")