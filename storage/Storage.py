
"""
Storage objects - save data to database
"""



class Storage(object):
    def __init__(self, station):
        self.station = station

    def save_data(self):
        for datas in self.station.datas:
            pass
