
"""
Acqusition objects - collect data_frame (a)
"""


class Acqusition(object):
    def __init__(self, generator):
        self.generator = generator
        self.data = None

    def get_data(self):
        if self.generator.data_frame['type'] == 'simulator':
            self.data = self.generator.data_frame
        elif self.generator.data_frame['type'] == 'sensor': #根据通讯协议解析
            pass



    # def __init__(self, data_type):
    #     self.data_frame = dict()
    #     self.data_frame['type'] = data_type.type
    #     for key in data_type.keys:
    #         self.data_frame[key] = None