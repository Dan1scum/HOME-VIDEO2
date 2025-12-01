# HeroMage
# hero_mage

class Hero:
    def __init__(self, name, lvl, hp): # конструктор класса
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Методы
    def base_action(self):
        return f'base action {self.name}'

kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 101, 2000)

print(kirito.name)
print(asuna.name)

