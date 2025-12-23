# import sqlite3
#
#
# connect = sqlite3.connect('shop.db')
# cursor = connect.cursor()
#
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR (50)
# )
# """)
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS orders(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product TEXT,
#     total INTEGER,
#     user_id INTEGER,
#     FOREIGN KEY (user_id) REFERENCE users(id)
# )
# ''')
# connect.commit()
#
#
# def create_user(name):
#     cursor.execute('INSERT INTO users(name) VALUE (?)',
#                    (name,))
#     connect.commit()
#     print(f'Пользователь создан {name}')
#
# def create_order(user_id, product_name, total):
#     cursor.execute('INSERT INTO orders(user_id, product_name, total) VALUE (?, ?, ?)',
#                    (user_id, product_name, total))
#     connect.commit()
#     print(f'Заказ создан {product_name}')
#
#
# # create_user('Danisalm')
# # create_user('GOD')
# # create_user('Arhangel')
# # create_order(1, 'APPLE Iphone 17 pro', 1200)
# # create_order(2, 'POCO Phone 13 pro', 400)
# # create_order(5, 'GOOGLE Phone 10 pro', 1000)
#
#
# def get_user_orders():
#     cursor.execute('''
#     SELECT users.name, order.product, order.total
#     FROM users FULL OUTER JOIN orders ON users.id = orders.user.id
#     ''')
#     users = cursor.fetchall()
#
#     for i in users:
#         print(f'NAME: {i[0]} PRODUCT: {i[1]} TOTAL: {i[2]}')


# get_user_orders()
# MAX() MIN() AVG() COUNT() SUM()


