"""
Sensor objects - simulate data_frame equal to real sensor
"""

import random
from generator.Generator import Generator

class Simulator(Generator):
    def __init__(self, type='simulator', item='item_A', name='', time='2020_07_13_08_22_30'):
        super().__init__(type, item, name, time)

    def encode(self):
        self.data['value'] = random.randrange(1, 100, 2)

