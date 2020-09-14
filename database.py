from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_path = 'database.sqlite3'


class DataBase:

    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}', echo=True)
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    database = DataBase(db_path)
