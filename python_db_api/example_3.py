"""Работа с DB-API в Python"""

import sqlite3


try:
    with sqlite3.connect('test.sqlite') as conn:
        cur = conn.cursor()

        users = [
            ("sidor", 11111, "sidor@mail.ru"),
            ("makar", 11111, "makar@mail.ru"),
        ]
        cur.executemany("INSERT INTO users(login, password, email) VALUES (?, ?, ?)", users)

        conn.commit()

except sqlite3.DatabaseError as e:
    print(f"Ошибка работы с базой данных: {e}")

finally:
    cur.execute('SELECT * FROM users')
    print(cur.fetchall())
