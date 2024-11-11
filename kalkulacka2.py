try:
    prvni_cislo = float(input("Zadejte prvni cislo: "))

    znamenko = input("Zadejte znamenko (+, -, *, /): ")

    if znamenko not in ["+", "-", "*", "/"]:
        raise ValueError("Zadali jste nespravny znak. Pouzijte '+', '-', '*' nebo '/'")

    druhe_cislo = float(input("Zadejte druhe cislo: "))

    if znamenko == "+":
        vysledek = prvni_cislo + druhe_cislo
    elif znamenko == "-":
        vysledek = prvni_cislo - druhe_cislo
    elif znamenko == "*":
        vysledek = prvni_cislo * druhe_cislo
    elif znamenko == "/":
        if druhe_cislo == 0:
            raise ZeroDivisionError("Chyba: Nulou nelze delit!")
        vysledek = prvni_cislo / druhe_cislo

    print(f"Vysledek je {vysledek}.")

except ValueError:
    print(f"Chyba: Zadali jste nespravny znak. Pouzijte '+', '-', '*' nebo '/'")
except ZeroDivisionError:
    print(f"Chyba: Nulou nelze delit!")