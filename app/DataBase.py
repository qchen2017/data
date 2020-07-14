import sqlite3
from app.DataType import Temperature
from sqlalchemy.orm import (mapper, relationship, sessionmaker)

class Temperature(object):
    def __init__(self, type, item, time):
        self.type = type
        self.item = item
        self.time = time

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.type, self.item, self.time)

class DataBase(object):
    def __init__(self, ):
        path = "/home/yin/PycharmProjects/Data/test.db"
        self.cx = sqlite3.connect(path)
        self.cu = self.cx.cursor()  # 游标

        from sqlalchemy import create_engine
        # engine = create_engine('sqlite:///:memory:', echo=True) #内存形式
        engine = create_engine('sqlite:///test2.db')

        from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
        metadata = MetaData()

        temperature_table = Table('temperature', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('type', String),
                            Column('item', String),
                            Column('time', String)
                            )

        metadata.create_all(engine)

        mapper(Temperature, temperature_table) #映射


#         t = Temperature()
#         # self.cu.execute('''create table temperature(id integer primary key autoincrement,type varchar(20) not null)''')
#         self.cu.execute('''insert into temperature(id,type) values(1,'xiaoqiang')''')
#         self.cu.execute('''select * from temperature where id=1''')
#         values = self.cu.fetchall()
#         print(values)
#         self.cu.execute('''delete from temperature where id=1''')
#
# db = DataBase()



