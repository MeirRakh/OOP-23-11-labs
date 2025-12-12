class Employee:
    def work(self):
        print("Қызметкер күнделікті жұмысын орындайды.")
class Manager(Employee):
    def work(self):
        print("Менеджер команданы басқарады және шешім қабылдайды.")
e = Employee()
m = Manager()
print("work() әдісін шақыру")
print("Қызметкер объектісі:")
e.work()
print("\nМенеджер объектісі:")
m.work()