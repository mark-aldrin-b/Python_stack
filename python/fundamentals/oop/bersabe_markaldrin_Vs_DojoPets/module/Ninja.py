
class Ninja:

    def __init__(self, firstname, lastname, pet, treats, petfood):
        self.first_name = firstname
        self.last_name = lastname
        self.ninja_pet = pet
        self.treats = treats
        self.pet_food = petfood
    def walk(self):
        print(f"{self.first_name} and {self.ninja_pet.pet_name} are walking!")
        self.ninja_pet.play()
        return self
    def feed(self):
        print(f"{self.first_name} is feeding {self.ninja_pet.pet_name} with {self.pet_food}")
        self.ninja_pet.eat()
        return self
    def bathe(self):
        self.ninja_pet.noise()
        return self


