"""Работа с DB-API в Python"""

import sqlite3


DATA = [('0055.AAAA.CCCC', 'sw5', 'Cisco 3750', 'London, Green Str'),
        ('0066.BBBB.CCCC', 'sw6', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw7', 'Cisco 2960', 'London, Green Str'),
        ('0088.AAAA.CCCC', 'sw8', 'Cisco 3750', 'London, Green Str')]


try:
    with sqlite3.connect('test.sqlite') as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE switch (mac TEXT NOT NULL PRIMARY KEY, HOSTNAME text, MODEL text, LOCATION text)
        """)

        cur.executemany("INSERT INTO switch VALUES (?, ?, ?, ?)", DATA)

        conn.commit()

except sqlite3.DatabaseError as e:
    print(f"Ошибка работы с базой данных: {e}")

    print("Тогда попытаемся добавить новую запись")

    try:

        with sqlite3.connect('test.sqlite') as conn:

            cur = conn.cursor()

            obj_to_insert = (
                '0055.AAAA.CCCC',
                'sw5',
                'Cisco 3750',
                'London, Green Str')

            cur.execute(
                "INSERT INTO switch VALUES (?, ?, ?, ?)",
                obj_to_insert)

            conn.commit()

    except sqlite3.IntegrityError as e:
        print(f"Ошибка работы с базой данных: {e}")

        print("И здесь провал! такая запись уже существует")
