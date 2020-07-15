
"""
Storage objects - save data_frame to database
"""

from sqlalchemy.orm import sessionmaker
from database.DataBase import Temperature


class Storage(object):
    def __init__(self, db, station):
        self.db = db
        self.station = station

        self.session = None

    def save_data(self):
        DBsession = sessionmaker(bind=self.db.engine)
        session = DBsession()

        t_list = []
        for data in self.station.datas:
            t_list.append(Temperature(data['type'], data['item'], data['time'], data['value']))

        session.add_all(t_list)
        session.commit()
        self.session = session
        # session.close()


# sqlite test
if 1 == 11:
    import sqlite3

    path = "/home/yin/PycharmProjects/Data/test.db"
    cx = sqlite3.connect(path)
    cu = cx.cursor()  # 游标

    # 建表：
    cu.execute(
        'create table catalog (id integer primary key,pid integer,type varchar(10) UNIQUE)')  # 上面语句创建了一个叫catalog的表，它有一个主键id，一个pid，和一个name，name是不可以重复的。

    # 插入数据:
    cu.execute("insert into catalog values(0, 0, 'name1')")
    cu.execute(
        "insert into catalog values(1, 0, 'hello')")  # 简单的插入两行数据,不过需要提醒的是,只有提交了之后,才能生效.我们使用数据库连接对象cx来进行提交commit和回滚rollback操作.
    cx.commit()

    # 查询:
    cu.execute("select * from catalog")  # 要提取查询到的数据,使用游标的fetch***函数,如:
    print(cu.fetchall())  # 返回结果如下:
    # [(0, 0, u'name1'), (1, 0, u'hello')] #如果我们使用cu.fetchone(),则首先返回列表中的第一项,再次使用,则返回第二项,依次下去.

    # 修改:
    cu.execute("update catalog set type='name2' where id = 0")

    cx.commit()  # 注意,修改数据以后提交

    # 删除:
    cu.execute("delete from catalog where id = 1")
    cx.commit()  # 以上简单的操作反应的Python SQLITE数据库操作的基本要点,这里点到为止.然后,SQLite的强大,并不仅限于此,其对SQL高级特性的支持及其小巧灵活的特点,使得SQLite在众多领域受到开发者的青睐.
