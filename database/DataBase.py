
from sqlalchemy import create_engine
from sqlalchemy.orm import (mapper, relationship, sessionmaker)
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey

class Temperature(object):
    def __init__(self, type, item, time, value):
        self.type = type
        self.item = item
        self.time = time
        self.value = value

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.type, self.item, self.time)

class DataBase(object):
    def __init__(self, ):
        # engine = create_engine('sqlite:///:memory:', echo=True) #内存形式
        self.engine = create_engine('sqlite:///test2.db') #相对路径形式

        metadata = MetaData() #元数据
        temperature_table = Table('temperature', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('type', String),
                            Column('item', String),
                            Column('time', String),
                            Column('value', Float)
                            )
        metadata.create_all(self.engine)

        mapper(Temperature, temperature_table) #映射



