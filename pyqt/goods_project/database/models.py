from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)
    category_description = Column(String(200), nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return self.category_name


class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit = Column(String(10), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Positions(Base):
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column(String(20), nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return self.position


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(50), nullable=False)
    good_unit = Column(Integer, ForeignKey('units.unit_id', ondelete='CASCADE'), nullable=False)
    good_cat = Column(Integer, ForeignKey('categories.category_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, good_name):
        self.good_name = good_name

    def __repr__(self):
        return self.good_name


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(50), nullable=False)
    employee_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, employee_fio):
        self.employee_fio = employee_fio

    def __repr__(self):
        return self.employee_fio


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50), nullable=False)
    vendor_owner_chip_form = Column(String(50), nullable=False)
    vendor_address = Column(String(200), nullable=False)
    vendor_phone = Column(String(20), nullable=False)
    vendor_email = Column(String(20), nullable=False)

    def __init__(self, vendor_name, vendor_owner_chip_form, vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_owner_chip_form = vendor_owner_chip_form
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return self.vendor_name
