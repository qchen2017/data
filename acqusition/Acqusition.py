
"""
Acqusition objects - collect data_frame (a)
"""


class Acqusition(object):
    def __init__(self, generator):
        self.generator = generator
        self.data = None

    def decode(self):
        if self.generator.data['type'] == 'simulator':
            self.data = self.generator.data
        elif self.generator.data['type'] == 'sensor': #根据通讯协议解析
            pass



    # def __init__(self, data_type):
    #     self.data_frame = dict()
    #     self.data_frame['type'] = data_type.type
    #     for key in data_type.keys:
    #         self.data_frame[key] = None