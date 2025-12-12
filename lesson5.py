# Виртуальная среда, встроенные модули Python, определение собственных модулей, внешние модули и их установка, Основы GIT.


# Статик метод
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# print(Math.add(12,12))


# Класс метод
# class User:
#     default_role = 'guest'
#
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#     @classmethod
#     def create_from_name(cls, name):
#         return cls(name, cls.default_role)
#
#     @classmethod
#     def get_base_role(cls):
#         return cls.default_role
#
#     def get_name(self):
#         return self.name
#
# user_1 = User.create_from_name('User')
# danislam = User('Danislam', 'Conquest')
# print(user_1.role)
# print(danislam.role)


# Декоратор @property
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError('Цена не может быть меньше нуля')
#         self.__price = value
#
#     @property
#     def full_info(self):
#         return f'{self.name}, {self.__price}'
#
# iphone = Product('SAMSUNG', 1000)
#
# print(iphone.full_info)
# iphone.price = -10


# Свои декораторы
# def simple_decorator(func):
#     def wrapper():
#         print('До выполнения')
#         func()
#         print('После выполнения')
#     return wrapper()
#
# @simple_decorator
# def greeting():
#     print('Hello world!!')
#
#
# def greeting_decorator(func):
#     def wrapper(name):
#         print(f"Привет {name}")
#         func(name)
#     return wrapper
#
# @greeting_decorator
# def greeting_name(name):
#     print(f"Как дела {name}?")

# greeting_name('Danislam')


def class_decorator(cls):
    class NewClass(cls):

        def new_method(self):
            return 'Я новый метод'
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return 'Я старый метод'

obj_1 = OldClass

print(type(obj_1))










