

from sqlalchemy import create_engine
from sqlalchemy.orm import (mapper, relationship, sessionmaker)
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey


class Data(object):
    def __init__(self, name='', age=None, weight=None, description='统计居民'):
        self.name = name
        self.age = age
        self.weight = weight
        self.description = description
        # print('DataPack:',description)

class DataBase(object):
    def __init__(self, ):
        # engine = create_engine('sqlite:///:memory:', echo=True) #内存形式
        self.engine = create_engine('sqlite:///test.db') #相对路径形式


    # def create_table(self):
    #
    #     metadata = MetaData() #元数据
    #     t_table = Table('People', metadata,
    #                         Column('id', Integer, primary_key=True),
    #                         Column('name', String),
    #                         Column('age', Integer),
    #                         Column('weight', Float),
    #                         Column('description', String)
    #                         )
    #     metadata.create_all(self.engine)
    #     mapper(Data, t_table) #映射



