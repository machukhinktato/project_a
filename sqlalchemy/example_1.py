"""Традиционный подход к созданию таблиц, классов и отображений в SQLALchemy"""

# Иллюстрирует классический пример использования SQLAlchemy,
# в которой очень ценится разделение задач.

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker

# Создаем объект подключения
engine = create_engine('sqlite:///test.sqlite3')

# Создаем экземпляр каталога MetaData
metadata = MetaData()

# Описываем таблицу
vendors_table = Table('vendors', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('phone', String),
    Column('address', String)
)

# Создаем структуру таблиц
metadata.create_all(engine)

# Создаем класс-шаблон записи БД
class Vendor:

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Vendor({self.name}, {self.phone}, {self.address})>"

# Связываем шаблон записи с таблицей
mapper(Vendor, vendors_table)

# Создаем экземпляр записи с реальными параметрами
vendor = Vendor("ООО ‘Компани’ ", "8(495)77-77-77", "г. Москва, ул. Бажова, д. 9")

print(vendor)
# None. Как так? мы же создали объект записи и передали значения???
print(vendor.id)

# Оказывается мы еще ничего не сохранили. это нужно делать через сессии



#-------------------Cоздание сессии--------------------#
# С помощью конструктора sessionmaker создаем класс-сессия
SESSION = sessionmaker(bind=engine)

# создаем объект сессии
SESS_OBJ = SESSION()

# вот теперь все хорошо
SESS_OBJ.add(vendor)
SESS_OBJ.commit()
print(vendor.id)
