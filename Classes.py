class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def look(self):
        print(f"Looking at you...")

    def breath(self):
        print(f"Breathing normally when not active.")

class Fish(Animals):

    def swim(self):
        print("Swimming in the sea.")

    def look(self):
        print("Fish are looking underwater...")

class Bird(Animals):

    def look(self):
        print("Fish are looking underwater...")

    def fly(self):
        print("Flying high, feeling free...")

class Mammal(Animals):

    def run(self):
        print("Running fast when needed.")

class DomesticDog(Mammal):

    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print(f"Barking at a postman or just for fun.")

    def retrieve(self):
        print(f"Retrieving everything back to the owner.")

dd1 = DomesticDog(30, 7, "german shepherd", "brown")
dd1.bark()
print(dd1.breed)
dd1.look()
