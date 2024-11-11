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
    if druhe_cislo != 0:
        vysledek = prvni_cislo / druhe_cislo
    else:
        vysledek = "Chyba: Nulou nelze delit."
else:
    vysledek = "Chyba."


print(f"Vysledek je {vysledek}.")