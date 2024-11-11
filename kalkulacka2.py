try:
    prvni_cislo = float(input("Zadejte prvni cislo: "))
    znamenko = input("Zadejte znamenko (+, -, *, /): ")

    if znamenko not in ["+", "-", "*", "/"]:
        print("Chyba: Pouzijte pouze '+', '-', '*' nebo '/'")
    else:
        druhe_cislo = float(input("Zadejte druhe cislo: "))

        if znamenko == "+":
            vysledek = prvni_cislo + druhe_cislo
        elif znamenko == "-":
            vysledek = prvni_cislo - druhe_cislo
        elif znamenko == "*":
            vysledek = prvni_cislo * druhe_cislo
        elif znamenko == "/":
            if druhe_cislo == 0:
                print("Chyba: Nulou nelze delit!")
            else:
                vysledek = prvni_cislo / druhe_cislo

        if znamenko in ["+", "-", "*", "/"] and druhe_cislo != 0:
            print(f"Vysledek je {vysledek}.")

except ValueError:
    print("Chyba: Zadejte platne cislo.")