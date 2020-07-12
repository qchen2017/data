
"""
DataGenerator objects - generate data
"""


class DataGenerator(object):
    def __init__(self, type='simulator', item='item_A'):
        self.type = type
        self.item = item

        self.data_package = None

    def generate_data_package(self):
        self.data_package = None

