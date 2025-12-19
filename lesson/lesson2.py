# Другие принципы ООП - Инкапсуляция, Полиморфизм.




class Animal:
    def __init__(self, name: str, age: str, health: str):
        self.name = name
        self.age = age
        self.health = health

    def info(self) -> str:
        return f'{self.name}, {self.age} лет, здоровья {self.health}'

    def use_ability(self) -> str:
        return f'{self.name} использует базувую способность.'



class Flyable:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + ' летатет.'

class Swimmable:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + ' плавает.'

class Invisible:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + ' становиться невидимым.'



class Duck(Flyable, Swimmable, Animal):
    pass

class Bat(Flyable, Invisible, Animal):
    pass

class Frog(Swimmable, Animal):
    pass

class Phoenix(Flyable, Invisible, Animal):
    def reborn(self):
        self.health = 200
        return f"{self.name} возродился из пепла!"




class Zoo:
    def __init__(self):
        self.animal: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animal.append(animal)

    def show_all(self):
        for animal in self.animal:
            print(animal.info())

    def perform_show(self):
        for animal in self.animal:
            print(animal.use_ability())



if __name__ == '__main__':
    zoo = Zoo()

    duck = Duck('Дональд', 3, 80)
    bat = Bat('Бэтти', 5, 60)
    frog = Frog('Кермит', 2, 50)
    phoenix = Phoenix('Феникс', 100, 200)

    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print('=== Информация о животных ===')
    zoo.show_all()
    print('\n=== Шоу суперспособностей ===')
    zoo.perform_show()
    print("\nMRO для Duck:", Duck.__mro__)
    print("MRO для Phoenix:", Phoenix.__mro__)








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
# # Дочерный класс
# class MagicHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return f"{self.name} кастует огненый шар"
#
# class WarriorHero(Hero):
#     def attack(self):
#         return f"{self.name} кот айрам"
#
#
# gandalf = MagicHero('Gandalf', 77, 7777, 10000)
# kirito = Hero('Kirito', 100, 1000)
# asuna = Hero('Asuna', 101, 2000)
# aragorn = WarriorHero('Aragotn', 88, 8888)
#
# print(gandalf.base_action())
# print(kirito.base_action())
# print(asuna.base_action())
# print(aragorn.base_action())
