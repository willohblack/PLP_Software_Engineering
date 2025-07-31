# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Polymorphic behavior
vehicles = [Car(), Plane(), Boat()]

print("Vehicle Movements:")
for v in vehicles:
    v.move()
