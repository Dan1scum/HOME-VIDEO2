# Встроенный модули PYTHON, определенние собствееных модулей, внешние модули и их устоновка.

# print(randint(1, 10))

# import lesson1

# hero = lesson1.Phone('Apple', 'iPhone 13', 100)
#
# print(hero.name)


# Библиотека colorama предназначена для цветного вывода текста в консоль
# Она позволяет делать сообщения более наглядными и удобными для чтения

from colorama import Fore, Style, init

# Инициализация colorama (особенно важно для Windows)
init()

print(Fore.GREEN + "Успешно! Всё работает.")
print(Fore.YELLOW + "Предупреждение: это пример использования библиотеки.")
print(Fore.RED + "Ошибка: это просто демонстрация цвета.")

# Сброс стилей
print(Style.RESET_ALL + "Обычный текст без цвета")
