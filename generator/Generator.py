
"""
Generator objects - generate data_frame
"""


class Generator(object):
    def __init__(self, type, item, name, time):
        self.data = dict()
        self.data['name'] = name
        self.data['type'] = type
        self.data['item'] = item
        self.data['time'] = time
        self.data['name'] = None

    def encode(self):
        pass

