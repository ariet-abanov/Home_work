import sqlite3

db_name = 'hw_.db'

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(products):
    try:
        sql = '''INSERT INTO products
                 (product_title, price, quantity)
                 VALUES (?, ?, ?)'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)
def update_products(products):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)

def update_price_products(products):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)

def delete_products(id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_products():
    try:
        sql = '''SELECT * FROM products'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()  #fetchall - выводит из БД в консоль
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_salary(price_limit):
    try:
        sql = '''SELECT * FROM products WHERE price >= ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_product_title(search_term):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()

            cursor.execute(sql, ('%' + search_term + '%',))

            rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

# create_table(sql_to_create_products_table)

# insert_products(('cucumber', 44.06, 4))
# insert_products(('onion', 50.07, 5))
# insert_products(('potato', 39, 10))
# insert_products(('tomato', 25.08, 3))
# insert_products(('banana', 128.05, 6))
# insert_products(('pineapple', 151.3, 1))
# insert_products(('kiwi', 111.23, 7))
# insert_products(('carrot', 86, 6))
# insert_products(('watermelon', 321.89, 1))
# insert_products(('melon', 221.32, 1))
# insert_products(('orange', 150.01, 4))
# insert_products(('apple', 76, 12))
# insert_products(('shavel', 60.23, 12))
# insert_products(('peach', 93, 4))

# update_products((10, 2))
# update_price_products((102, 2))
# delete_products(2)
# select_all_products()
# select_products_by_salary(100)
select_products_by_product_title('onion')

