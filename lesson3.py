# Магические, статичные, классовые методы в классах, множественное наследование.


class Product:
    def __init__(self, name, price):
        self.name = name  # публичный атрибут
        self._price = price  # защищённый атрибут
        self.__discount = 0  # приватный атрибут (0–50%)

    def get_price(self):
        """Возвращает цену с учётом скидки"""
        final_price = self._price * (1 - self.__discount / 100)
        return round(final_price, 2)

    def set_discount(self, percent):
        """Устанавливает скидку, если она <= 50"""
        if percent <= 50:
            self.__discount = percent
        else:
            print("Ошибка: скидка не может быть больше 50%")

    def apply_extra_discount(self, secret_code):
        """Приватный код: VIP123"""
        if secret_code == "VIP123":
            self.__discount += 5
            if self.__discount > 50:
                self.__discount = 50
        else:
            print("Неверный код")


p = Product("Iphone", 1000)

p.set_discount(20)
print("Цена со скидкой:", p.get_price())

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print({"type": "crypto", "amount": amount, "currency": "USDT"})

    def refund(self, amount):
        print({"status": "refund", "amount": amount, "currency": "USDT"})


class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)


processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)




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