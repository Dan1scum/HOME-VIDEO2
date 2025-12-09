# Закрепление пройденного материала - Использование ООП в проекте



class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} готов в бою!'

class MagicHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def cast_spell(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(Hero):
    def attack(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        if password == "absolute":
            print(f"Успешно вошли в систему {self.name}")
        else:
            print("пошел нх!!!!!!!")

    def full_info(self):



    def get_bank_name(self):



    def bonus_for_level(self):      # пока все сырое
        return 'fy'






mage1 = MagicHero("Merlin", 80, 500, 150)
mage2 = MagicHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234")
acc2 = BankAccount(mage2, 3000, "0000")
acc3 = BankAccount(warrior, 2500, "1111")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)

# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())



# class Test:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         print(self.x)
#         print(other.x)
#
# v1 = Vector(22,33)
# v2 = Vector(24, 33)

# v3 = v1 + v2