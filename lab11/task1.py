class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"Көліктің маркасы: {self.brand}, Шыққан жылы: {self.year}")
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def display_info(self):
        print(f"Көліктің маркасы: {self.brand}, Моделі: {self.model}, Шыққан жылы: {self.year}")
car1 = Car("Audi", 2024, "A4")
print("Жеңіл көлік туралы ақпарат")
car1.display_info()
vehicle1 = Vehicle("Tesla", 2023)
print("\nЖалпы көлік туралы ақпарат")
vehicle1.display_info()