import sqlite3


def setup_database():
    conn = sqlite3.connect('HW-8.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO countries (title) VALUES (?)
    ''', [
        ('Kyrgyzstan',),
        ('Germany',),
        ('China',)
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO cities (title, area, country_id) VALUES (?, ?, ?)
    ''', [
        ('Bishkek', 127.0, 1),
        ('Karakol', 182.0, 1),
        ('Berlin', 891.8, 2),
        ('Munich', 310.7, 2),
        ('Beijing', 16411.0, 3),
        ('Shanghai', 6340.5, 3),
        ('Guangzhou', 7434.4, 3)
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
    ''', [
        ('Ariet', 'Abanov', 1),
        ('Agahan', 'Zhyrgalbaev', 1),
        ('Atay', 'Temirbekov', 2),
        ('Tariel', 'Almazbekov', 2),
        ('Hans', 'Schmidt', 3),
        ('Marta', 'Weber', 3),
        ('Lukas', 'Muller', 4),
        ('Anja', 'Fischer', 4),
        ('Li', 'Wang', 5),
        ('Mei', 'Zhang', 5),
        ('Wei', 'Chen', 6),
        ('Yuan', 'Li', 6),
        ('Chen', 'Lin', 7),
        ('Xiao', 'Hu', 7),
        ('Liu', 'Jin', 7)
    ])

    conn.commit()
    conn.close()


def show_cities(cursor):
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")


def show_students_in_city(cursor, city_id):
    query = """
    SELECT s.first_name, s.last_name, co.title, ci.title, ci.area
    FROM students s
    JOIN cities ci ON s.city_id = ci.id
    JOIN countries co ON ci.country_id = co.id
    WHERE s.city_id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()

    if students:
        for student in students:
            print(f"Имя: {student[0]}")
            print(f"Фамилия: {student[1]}")
            print(f"Страна: {student[2]}")
            print(f"Город проживания: {student[3]}")
            print(f"Площадь города: {student[4]}")
            print()
    else:
        print("В этом городе нет учеников.")


def main():
    setup_database()

    conn = sqlite3.connect('HW-8.db')
    cursor = conn.cursor()

    while True:
        show_cities(cursor)

        city_id = input("Введите id города: ")

        if city_id == "0":
            print("Выход из программы.")
            break

        if not city_id.isdigit():
            print("Введите корректный id города.")
            continue

        show_students_in_city(cursor, int(city_id))

    conn.close()


if __name__ == "__main__":
    main()

