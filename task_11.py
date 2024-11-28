class Iterator_mocnin:

    def __init__(self, seznam):
        self.seznam = seznam
        self.pozice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pozice >= self.seznam:
            raise StopIteration
        self.pozice += 1
        return self.pozice ** 2


mocniny = Iterator_mocnin(5)

for mocnina in mocniny:
    print(mocnina)

