
import numpy as np
import pandas as pd
import sqlite3 as db

class DataSet(object):

    def __init__(self, data_pack):
        self.data_set = self.parse_data_pack(data_pack)

        self.con = db.connect('/home/yin/PycharmProjects/Data/application/test.db')

    def parse_data_pack(self, data_pack):
        return data_pack

    def save_to(self):
        df = pd.DataFrame(np.array([[self.data_set.name, self.data_set.age, self.data_set.weight, self.data_set.description]]),
                     columns=['name', 'age', 'weight', 'description'])
        df['age'] = pd.to_numeric(df['age'])
        df['weight'] = pd.to_numeric(df['weight'])

        # df = pd.DataFrame([self.data_set.name, self.data_set.age, self.data_set.description])
        df.to_sql('People', con=self.con, if_exists='append', index=False)
