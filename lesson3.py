# Магические, статичные, классовые методы в классах, множественное наследование.







# from abc import ABC, abstractmethod
#
#
# # Абстрактный класс Animal
# class Animal(ABC):
#
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def voce(self):
#         pass
#
# class Dog(Animal):
#
#     def move(self):
#         return "Ходит"
#
#     def voce(self):
#         return "Гав Гав"
#
# my_dog = Dog()
#
# class User:
#
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country
#
# ardager2  =  User("Ardager", "KG")
# ardager3 = User("Ardager", "RU")
#
#
# class ABCSendOTP(ABC):
#     @abstractmethod
#     def send_otp(self, user):
#         pass
#
# class KGSendOTP(ABCSendOTP):
#     def send_otp(self, user):
#         sms = f"<Text>1234</Text><PhoneNumber>123123</PhoneNumber>"
#         print(sms)
#
# class RUSendOTP(ABCSendOTP):
#     def send_otp(self, user):
#         sms = {
#             'text': "1234",
#             'phoneNumber': "12312"
#         }
#         print(sms)
#
# kg = KGSendOTP()
# ru = RUSendOTP()
#
# class Register:
#     def __init__(self, country1, country2):
#         self.countryKG = country1
#         self.countryRU = country2
#
#     def register(self, user):
#
#         if user.country == "KG":
#             self.countryKG.send_otp(user)
#         elif user.country == "RU":
#             self.countryRU.send_otp(user)
#
# register = Register(kg, ru)
#
# user_name = input("Ввудите имя")
# user_country = input("Введите страну")
# my_user = User(user_name, user_country)
# register.register(my_user)




# class BankAccount:
#     def __init__(self, name, balance, password):
#          self.name = name
#          self._balance = balance
#          self.__password = password
#
#     def get_balance(self, password):
#         if password == self.__password:
#             return self._balance
#         else:
#             return 'Не верный пароль'
#
#     def get_money(self, amount):
#         if password == self.__password:
#             self._balance -= amount
#             return self._balance
#         else:
#             return 'Не верный пароль'
#
# danislam = BankAccount('Danislam', 100, 'Dastan')
# print(danislam.get_balance('Dastan'))