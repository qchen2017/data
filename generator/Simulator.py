"""
Sensor objects - simulate data equal to real sensor
"""

import random
from generator.DataGenerator import DataGenerator

class Simulator(DataGenerator):
    def __init__(self, type='simulator', item='item_A', name='', time='2020_07_13_08_22_30'):
        super().__init__(type, item, name, time)

    def generate_data_package(self):
        self.data['data_package'] = random.randrange(1, 100, 2)

