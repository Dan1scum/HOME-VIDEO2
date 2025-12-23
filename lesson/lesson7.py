# Базы данных и СУБД. Работа с БД в Python. Основы SQL, создание таблиц и типы данных, CRUD операции.


import sqlite3


connect = sqlite3.connect("products.db")
cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    title TEXT,
    price INTEGER,
    quantity INTEGER
)
""")
connect.commit()


def add_product(title, price, quantity):
    cursor.execute(
        "INSERT INTO products (title, price, quantity) VALUES (?, ?, ?)",
        (title, price, quantity)
    )
    connect.commit()
    print("Товар добавлен")


def get_all_products():
    cursor.execute("SELECT rowid, * FROM products")
    products = cursor.fetchall()
    return products


def get_by_rowid(row_id):
    cursor.execute(
        "SELECT rowid, * FROM products WHERE rowid = ?",
        (row_id,)
    )
    product = cursor.fetchone()
    return product


def update_product(row_id, title, price, quantity):
    cursor.execute(
        """
        UPDATE products
        SET title = ?, price = ?, quantity = ?
        WHERE rowid = ?
        """,
        (title, price, quantity, row_id)
    )
    connect.commit()
    print("Товар обновлён")


def delete_product(row_id):
    cursor.execute(
        "DELETE FROM products WHERE rowid = ?",
        (row_id,)
    )
    connect.commit()
    print("Товар удалён")


if __name__ == "__main__":
    add_product("Ноутбук", 70000, 5)
    add_product("Мышь", 1500, 20)

    print("\n Все товары:")
    for product in get_all_products():
        print(product)

    print("\n Товар с rowid = 1:")
    print(get_by_rowid(1))

    update_product(1, "Игровой ноутбук", 90000, 3)

    delete_product(2)

    print("\n Итоговый список:")
    for product in get_all_products():
        print(product)

    connect.commit()




# import sqlite3
#
# # A4
# connect = sqlite3.connect('users.db')
# # Рука с карандашом
# cursor = connect.cursor()
#
#
# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             name VARCHAR (50) NOT NULL,
#             age INTEGER NOT NULL,
#             hobby TEXT
#         )
# ''')
# connect.commit()
#
#
# # CRUD - Create Read Update Delete
#
# def create_user(name, age, hobby=None):
#     # cursor.execute(
#     #     f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")'
#     # ))
#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
#         (name, age, hobby)
#     )
#     connect.commit()
#     print(f'Пользователь добавлен {name}!!')
#
# # create_user('Danis', 25, 'GOD')
#
#
# def get_users():
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchmany(3)
#     # print(users)
#     for i in users:
#         print(f"NAME: {i[0]} AGE: {i[1]} HOBBY: {i[2]}")
#
# # get_users()
#
#
# def update_users_name(row_id, name):
#     cursor.execute(
#         'UPDATE users SET hobby = ? WHERE rowid = ?',
#         (name, row_id)
#     )
#     connect.commit()
#     print('Пользователь обнавлен')
#
# # update_users_name(2, 'Любит горы летом')
#
#
# def delete_user(row_id):
#     cursor.execute(
#         'DELETE FROM users WHERE rowid = ?',
#         (row_id,)
#     )
#     connect.commit()
#     print('Пользователь удален!!')
#
# delete_user(2)