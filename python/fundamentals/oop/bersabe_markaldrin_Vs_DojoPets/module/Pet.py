

class Pet:
    
    def __init__(self, name, type, tricks):
        self.pet_name = name
        self.pet_type = type
        self.pet_tricks = tricks
        self.pet_health = 70
        self.pet_energy = 70
    def sleep(self):
        self.pet_energy += 25
        return self
    def eat(self):
        self.pet_energy += 5
        self.pet_health += 10
        return self
    def play(self):
        self.pet_health += 5
        print(f"health: {self.pet_health}")
        return self
    def noise(self):
        print("woof woof")
        return self