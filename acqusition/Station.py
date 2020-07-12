
"""
Station objects - collect all the equipment you use to do an experiment.
"""

from acqusition.DataAcqusition import DataAcqusition


class Station(object):
    def __init__(self, generators):
        self.generators = generators
        self.datas = []

    def collect_station_datas(self):
        for generator in self.generators:
            collector = DataAcqusition(generator)
            self.datas.append(collector.get_data())