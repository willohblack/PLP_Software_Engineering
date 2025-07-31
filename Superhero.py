# Parent class: Superhero
class Superhero:
    def __init__(self, name, power, origin, level):
        self.name = name
        self.power = power
        self.origin = origin
        self.level = level

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, with the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} at level {self.level}!")

# Child class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, level, flight_speed):
        super().__init__(name, power, origin, level)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} takes to the skies at {self.flight_speed} mph, using {self.power}!")

# Creating instances
hero1 = Superhero("ShadowStorm", "Invisibility", "Night City", 5)
hero2 = FlyingSuperhero("SkyBlade", "Wind Control", "Cloud Fortress", 8, 300)

# Using methods
hero1.introduce()
hero1.use_power()

print("----")

hero2.introduce()
hero2.use_power()
