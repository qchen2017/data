
import pandas as pd

class Analysis(object):
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def analysis(self):
        print(self.data_frame['name'].value_counts())
        # print(self.data_frame.iloc[2, 4])

        m = self.data_frame.mean(axis=0)
        print(m)


