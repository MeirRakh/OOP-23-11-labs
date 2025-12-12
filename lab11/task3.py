class Employee:
    def __init__(self, name):
        self.name = name
    def area(self):
        return "Жалпы Қызмет (General Duties)"
class MarketingStaff(Employee):
    def area(self):
        return "Нарықтық Зерттеу және Жарнама (Market Research and Ads)"
class TechStaff(Employee):
    def area(self):
        return "Техникалық Қолдау және Дамыту (Technical Support and Development)"
staff = [
    MarketingStaff("Айгүл"),
    TechStaff("Бекжан"),
    Employee("Сәуле")
]
print("Қызметкерлердің Жұмыс Аймақтарын Анықтау")
for person in staff:
    print(f"Қызметкер: {person.name} | Жұмыс Аймағы {person.area()}")