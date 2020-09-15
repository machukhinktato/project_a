"""Декларативный подход к созданию таблиц, классов и отображений в SQLALchemy"""

# Большое число приложений не требуют такого разделения, и для них SQLAlchemy
# предоставляет альтернативный, более лаконичный стиль: декларативный.

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Функция declarative_base() определяет новый класс,
# который мы назвали Base, от которого будет унаследованы все наши ORM-классы.
Base = declarative_base()

# Создаем объект подключения
engine = create_engine('sqlite:///test.sqlite3')

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    address = Column(String)

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Vendor({self.name}, {self.phone}, {self.address})>"


Base.metadata.create_all(engine)

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
