
"""
Sensor objects - generate real data_frame
"""

from generator.Generator import Generator

class Sensor(Generator):
    def __init__(self, type='sensor', item='item_A', name=''):
        super().__init__(type, item)
