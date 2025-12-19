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
    # ))
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f'Пользователь добавлен {name}!!')

# create_user('Danis', 25, 'GOD')


def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchmany(3)
    # print(users)
    for i in users:
        print(f"NAME: {i[0]} AGE: {i[1]} HOBBY: {i[2]}")

# get_users()


def update_users_name(row_id, name):
    cursor.execute(
        'UPDATE users SET hobby = ? WHERE rowid = ?',
        (name, row_id)
    )
    connect.commit()
    print('Пользователь обнавлен')

# update_users_name(2, 'Любит горы летом')


def delete_user(row_id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('Пользователь удален!!')

delete_user(2)