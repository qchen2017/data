
"""
DataAcqusition objects - collect data (a)
"""


class DataAcqusition(object):
    def __init__(self, generator):
        self.generator = generator
        self.data = None

    def get_data(self):
        if self.generator.type == 'simulator':
            return self.generator.data_package
        elif self.generator.type == 'sensor': #根据通讯协议解析
            pass
