import sqlite3


def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250),
        category_code VARCHAR(2),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES store(store_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100)
    )
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)
    ''', [
        ('FD', 'Food products'),
        ('CL', 'Clothes'),
        ('EL', 'Electronics'),
    ])

    cursor.executemany('''
    INSERT OR IGNORE INTO store (store_id, title) VALUES (?, ?)
    ''', [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar'),
    ])

    cursor.executemany('''
    INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Chocolate', 'FD', 10.5, 129, 1),
        (2, 'Adidas_x', 'CL', 2700, 10, 1),
        (3, 'Macbook_m3_pro', 'EL', 240000, 9, 2),
        (4, 'Iphone_15_promax', 'EL', 120000, 22, 3),
        (5, 'Dime_jeans', 'CL', 3300, 26, 2)
    ])

    conn.commit()
    conn.close()


def show_stores(cursor):
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")


def show_products_in_store(cursor, store_id):
    query = """
    SELECT p.title, c.title, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print()
    else:
        print("В этом магазине нет продуктов.")


def main():
    setup_database()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    while True:
        show_stores(cursor)
        store_id = input("Введите id магазина: ")
        if store_id == "0":
            print("Выход....")
            break

        if not store_id.isdigit():
            print("Вы ввели неправльный id.")
            continue

        show_products_in_store(cursor, int(store_id))

    conn.close()


if __name__ == "__main__":
    main()
