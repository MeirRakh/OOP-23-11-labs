from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        return "Car drives"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle pedals forward"
class Airplane(Vehicle):
    def move(self):
        return "Airplane flies in the sky"
class Train(Vehicle):
    def move(self):
        return "Train moves on rails"
if __name__ == "__main__":
    vehicles = [Car(), Bicycle(), Airplane(), Train()]
    for v in vehicles:
        print(v.move())