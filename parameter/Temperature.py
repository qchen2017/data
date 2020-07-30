
from parameter.Parameter import Parameter

class Temperature(Parameter):  # each path_curve corresponds to a PathData
    def __init__(self, type, instrument_item, datas, sample_rate, time):
        super().__init__(type, instrument_item, datas, sample_rate, time)
        ## 子类比基类具体化一点，有一个输入是具体一点