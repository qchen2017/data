
"""
Sensor objects - generate real data
"""

from generator.DataGenerator import DataGenerator

class Sensor(DataGenerator):
    def __init__(self, type='sensor', item='item_A'):
        super().__init__(type, item)

    def generate_data_package(self):
        '''
        产生数据包
        :return:
        '''
        pass