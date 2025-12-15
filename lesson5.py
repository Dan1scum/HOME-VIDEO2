# Виртуальная среда, встроенные модули Python, определение собственных модулей, внешние модули и их установка, Основы GIT.


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняется действие: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Mage:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

    @classmethod
    def frieren(cls):
        return cls("Frieren", 1000)

    @staticmethod
    def is_legendary(mana):
        return mana >= 500

    @log_action
    def cast_spell(self):
        print(f"{self.name} использует магию (мана: {self.mana})")


mage1 = Mage.frieren()
mage2 = Mage("Fern", 300)

mage1.cast_spell()
mage2.cast_spell()

print(Mage.is_legendary(mage1.mana))  # True
print(Mage.is_legendary(mage2.mana))  # False






command = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]
}


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return f"{self.username} ({self.role})"


def command_access(command_name):
    def decorator(func):
        def wrapper(self, user: User, *args, **kwargs):
            if command_name not in command.get(user.role, []):
                print(f'Пользователь {user.username} не может выполнять команду "{command_name}"')
                return

            print(f'Пользователь {user.username} ({user.role}) выполняет команду {command_name}')
            return func(self, user, *args, **kwargs)

        return wrapper
    return decorator


class CommandHandler:

    @command_access("start")
    def start(self, user):
        print("Система запущена")

    @command_access("ban")
    def ban(self, user):
        print("Пользователь заблокирован")

    @command_access("stop")
    def stop(self, user):
        print("Система остановлена")

    @command_access("message")
    def message(self, user):
        print("Пользователь отправил сообщение")


if __name__ == "__main__":
    handler = CommandHandler()

    user1 = User("Alice", "admin")
    user2 = User("Bob", "user")

    # Админ
    handler.start(user1)
    handler.ban(user1)
    handler.stop(user1)

    print()

    # Обычный пользователь
    handler.start(user2)
    handler.ban(user2)
    handler.message(user2)





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


# def class_decorator(cls):
#     class NewClass(cls):
#
#         def new_method(self):
#             return 'Я новый метод'
#     return NewClass
#
# @class_decorator
# class OldClass:
#     def old_method(self):
#         return 'Я старый метод'
#
# obj_1 = OldClass
# print(type(obj_1))










