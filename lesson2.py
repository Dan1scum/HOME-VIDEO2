# Другие принципы ООП - Инкапсуляция, Полиморфизм.


class Hero:
    def __init__(self, name, lvl, hp): # конструктор класса
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Методы
    def base_action(self):
        return f'base action {self.name}'

# Дочерный класс
class MagicHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def cast_spell(self):
        return f"{self.name} кастует огненый шар"

class WarriorHero(Hero):
    def attack(self):
        return f"{self.name} кот айрам"


gandalf = MagicHero('Gandalf', 77, 7777, 10000)
kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 101, 2000)
aragorn = WarriorHero('Aragotn', 88, 8888)

print(gandalf.base_action())
print(kirito.base_action())
print(asuna.base_action())
print(aragorn.base_action())
