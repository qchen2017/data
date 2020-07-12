"""
Sensor objects - simulate data equal to real sensor
"""

import random
from generator.DataGenerator import DataGenerator

class Simulator(DataGenerator):
    def __init__(self, type='simulator', item='item_A'):
        super().__init__(type, item)

    def generate_data_package(self):
        self.data_package = random.randrange(1, 100, 2)

