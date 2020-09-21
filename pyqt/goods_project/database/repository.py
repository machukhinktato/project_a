from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from dz6.database.models import Base, Goods, Categories

path_db = 'database.sqlite3'


class Repository:

    def __init__(self, path_db):
        self.engine = create_engine(fr'sqlite:///{path_db}?check_same_thread=False')
        self.session = self.get_session()
        self.session.execute('PRAGMA foreign_keys=ON')
        self.create_base()

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def create_base(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    rep = Repository(path_db)
    print(Base.metadata.tables.keys())
    print(Goods.__table__.columns.keys())
    # rep.session.add(Goods('ddd'))
    # rep.session.commit()
    # print(rep.session.query(Goods).all()[0])
    # print(rep.session.query(Categories).all()[0])
    # rep.session.delete(rep.session.query(Categories).all()[0])
    # rep.session.commit()
    # print(rep.session.query(Goods).all()[0])
    # print(rep.session.query(Categories).all()[0])