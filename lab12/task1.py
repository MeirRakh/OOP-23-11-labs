from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass
class Car(Vehicle):
    def move(self):
        return "Car is driving on the road"
    def fuel_type(self):
        return "Petrol or Diesel"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is moving using pedals"
    def fuel_type(self):
        return "No fuel — Human power"
if __name__ == "main":
    car = Car()
    bike = Bicycle()
    print(car.move(), "|", car.fuel_type())
    print(bike.move(), "|", bike.fuel_type())