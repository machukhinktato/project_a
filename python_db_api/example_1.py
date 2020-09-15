"""Работа с DB-API в Python"""

import sqlite3


try:
    with sqlite3.connect('test.sqlite') as conn:
        cur = conn.cursor()

        cur.executescript("""
            create table users(
                login,
                password,
                email
            );
            insert into users(login, password, email)
            values ('ivan', '11111', 'ivan@mail.ru');
            """)

        conn.commit()

except sqlite3.DatabaseError as e:
    print(f"Ошибка работы с базой данных: {e}")

finally:

    cur.execute('SELECT * FROM users')
    # print(cur.fetchall())  # -> [('ivan', '11111', 'ivan@mail.ru')]

    print(cur.fetchone())  # -> ('ivan', '11111', 'ivan@mail.ru')
    # print(cur.fetchone())  # -> все элементы извлечены, поэтому ф-ция возвращает None

    # параметризованный запрос
    cur.execute("SELECT login FROM users WHERE password = ? AND email = ?", ('11111', 'ivan@mail.ru'))

    print(cur.fetchone())
