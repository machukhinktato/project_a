"""Работа с БД средствами Qt"""

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# имя_соединения = QtSql.QSqlDatabase.addDatabase(‘формат_базы_данных’)
# Для клиент-серверных баз данных есть методы для подключения к серверу

"""
conn.setDatabaseName("имя_базы_данных") 
conn.setHostName("имя_хоста")
conn.setUserName("имя_пользователя")
conn.setPassword("пароль")
conn.setPort("порт")

например,

conn.setDatabaseName("my_db") 
conn.setHostName("127.0.0.1")
conn.setUserName("postgres")
conn.setPassword("12345")
conn.setPort("5432")
"""

# Открываем базу данных
conn = QSqlDatabase.addDatabase('QSQLITE')

# Определяем путь до базы данных
conn.setDatabaseName('test.sqlite3')

if conn.open():
    # Выполняем действия с базой
    query = QSqlQuery()
    query.exec("select * from vendors")
    results = []
    if query.isActive():
        query.first()
        while query.isValid():
            results.append(query.value('name'))
            query.next()
        for el in results:
            print(el)
else:
    # Выводим текст ошибки
    print(conn.lastError().text())

conn.close()


bin()