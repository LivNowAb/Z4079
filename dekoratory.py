# print()
# def vyprintuj_a_pust(func):
#     def nova_funkce(a,b):
#         print(f"poustime funkci {func.__name__} s parametry {a}, {b}")
#         return func(a, b)
#     return nova_funkce
#
# @vyprintuj_a_pust
# def soucet(a, b):
#     return a + b
#
# @vyprintuj_a_pust
# def rozdil (a,b):
#     return a-b
#
# print(soucet(3, 5))
# print(rozdil(3, 5))


def with_password(func):
    pozadovane_heslo = "zadavamheslo42+"
    def nova_funkce():
        heslo = input(f"Zadejte spravne heslo: \n")
        if heslo == pozadovane_heslo:
            print(f"Zadali jste spravne heslo, kod pro Vas je nyni dostupny.")
            return func()
        else:
            print(f"Zadali jste spatne heslo.")
            return None
    return nova_funkce


@with_password
def vloz_heslo():
    print("Kod je nyni dostupny")

vloz_heslo()

