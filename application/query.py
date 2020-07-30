
import pandas as pd
import sqlite3

class Query(object):
    def __init__(self):
        # self.session = session
        self.data_frame = None

    def query(self):
        # 方式一: query容易写，读取出来的是字典
        # query_data = self.session.query(Temperature).filter_by(item='item_A').all()
        # self.data_frame = pd.DataFrame(query_data) #转换:这样转换不成功？

        # 方式二: pandas，需要写query，好处是直接可以用pandas算法
        conn = sqlite3.connect('/home/yin/PycharmProjects/Data/application/test.db')
        query = 'SELECT age,weight FROM People WHERE age > 15;'
        self.data_frame = pd.read_sql_query(query, conn) #方式二:

        return self.data_frame
