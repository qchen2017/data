import sqlite3 as db
import sys, traceback
import pandas as pd

from application.datareceiver import DataReceiver


data_receiver = DataReceiver()

while True:
    try:
        dataset = data_receiver.get_data()

        df = pd.DataFrame({'data': [dataset.name, dataset.age, dataset.description]})

        with db.connect('/home/yin/PycharmProjects/Data/test.db') as con:
            c = con.cursor()

            df.to_sql('data', con=con, if_exists='replace', index=False)

            sql = "select * from data"

            test = pd.read_sql(sql, con)  # 完成数据库的查询读取到数据框dataframe 中
            print(test)
            # df.to_sql(name='employee', con=con, if_exists='replace')

    except Exception as e:  # work on python 3.x
        traceback.print_exc()




