
"""
DataGenerator objects - generate data
"""


class DataGenerator(object):
    def __init__(self, type, item, name, time):
        self.data = dict()
        self.data['type'] = name
        self.data['type'] = type
        self.data['item'] = item
        self.data['time'] = time
        self.data['data_package'] = None

    def generate_data_package(self):
        pass

