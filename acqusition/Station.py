
"""
Station objects - collect all the equipment you use to do an experiment.
"""

from acqusition.Acqusition import Acqusition


class Station(object):
    def __init__(self, generators):
        self.generators = generators
        self.datas = []

    def collect_station_datas(self):
        for generator in self.generators:
            collector = Acqusition(generator)
            collector.decode()
            self.datas.append(collector.data)