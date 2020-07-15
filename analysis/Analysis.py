
import pandas as pd

class Analysis(object):
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.temperature_values = []

        self.temperature_values = self.get_values('value')

    def get_values(self, column_name):
        values = []
        for data in self.data_frame:
            values.append(data[column_name])

        return values

    def mean(self):
        return pd.mean(self.temperature_values)

    def max(self):

        pass

    def min(self):

        pass