# Базы данных и СУБД. Работа с БД в Python. Основы SQL, создание таблиц и типы данных, CRUD операции.


import sqlite3

# A4
connect = sqlite3.connect('users.db')
# Рука с карандашом
cursor = connect.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()


# CRUD - Create Read Update Delete

def create_user(name, age, hobby=None):
    # cursor.execute(
    #     f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")'
    # )
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f'Пользователь добавлен {name}!!')

# create_user('Danislam', 22, 'Everest')

