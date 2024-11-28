class Iterator_mocnin:

    def __init__(self, seznam):
        self.seznam = seznam
        self.pozice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pozice >= len(self.seznam):
            raise StopIteration
        num = self.seznam[self.pozice]
        self.pozice += 1
        return num ** 2

numbers = [1, 2, 3, 4, 5]
mocniny = Iterator_mocnin(numbers)

for mocnina in mocniny:
    print(mocnina)

