"""Работа с DB-API в Python"""

import sqlite3


try:
    with sqlite3.connect('test.sqlite') as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO users VALUES(?, ?, ?)", ("petr", 11111, "petr@mail.ru"))

        conn.commit()

except sqlite3.DatabaseError as e:
    print(f"Ошибка работы с базой данных: {e}")

finally:
    cur.execute('SELECT * FROM users')
    print(cur.fetchall())  # -> [('ivan', '11111', 'ivan@mail.ru'),
    # ('petr', 11111, 'petr@mail.ru')]
