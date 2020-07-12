
from variables.Variable import Variable

class Temperature(Variable):  # each path_curve corresponds to a PathData
    def __init__(self, type, instrument_item, datas, sample_rate, time):
        super().__init__(type, instrument_item, datas, sample_rate, time)