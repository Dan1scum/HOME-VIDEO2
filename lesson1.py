# HeroMage
# hero_mage




class Phone:
    """
    Класс Phone — описывает мобильный телефон.
    """

    def __init__(self, brand, model, battery):
        self.brand = brand            # бренд телефона (Apple, Samsung и т.д.)
        self.model = model            # модель (iPhone 12, Galaxy S22...)
        self.battery = battery        # заряд батареи в процентах
        self.is_on = False            # включён ли телефон

    def power_on(self):
        """Включает телефон"""
        if self.battery <= 0:
            return f"{self.brand} {self.model} не может включиться — батарея разряжена!"
        self.is_on = True
        return f"{self.brand} {self.model} включён."

    def charge(self, amount):
        """Заряжает телефон на указанное количество процентов"""
        self.battery = min(100, self.battery + amount)
        return f"Телефон зарядился. Текущий заряд: {self.battery}%"

    def info(self):
        """Возвращает информацию о телефоне"""
        status = "включён" if self.is_on else "выключен"
        return f"{self.brand} {self.model} — батарея: {self.battery}%, статус: {status}"


# Создаём объекты класса Phone
phone1 = Phone("Apple", "iPhone 12", 50)
phone2 = Phone("Samsung", "Galaxy S23", 10)
phone3 = Phone("Xiaomi", "Redmi Note 11", 0)

# Проверяем методы
print(phone1.info())
print(phone1.power_on())
print(phone1.charge(30))
print(phone1.info())

print("\n" + phone2.info())
print(phone2.power_on())
print(phone2.charge(50))
print(phone2.info())

print("\n" + phone3.info())
print(phone3.power_on())
print(phone3.charge(100))
print(phone3.power_on())
print(phone3.info())



# class Hero:
#     def __init__(self, name, lvl, hp): # конструктор класса
#         # Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     # Методы
#     def base_action(self):
#         return f'base action {self.name}'
#
# kirito = Hero('Kirito', 100, 1000)
# asuna = Hero('Asuna', 101, 2000)
#
# print(kirito.name)
# print(asuna.name)

