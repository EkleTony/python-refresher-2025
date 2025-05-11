# =========== Classes and object =====

class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

# derived class


class Car(Vehicle):
    def __init__(self, enginestype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginestype

# motor-cycle class


class Motorcycle(Vehicle):
    def __init__(self, engiinestype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
        self.enginetype = engiinestype


car1 = Car("gas")
car2 = Car("electric")
motorcycle1 = Motorcycle("gas", True)

print(motorcycle1.wheels)
print(car1.engine)
print(car2.bodystyle)
