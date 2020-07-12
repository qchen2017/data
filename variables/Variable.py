

class Variable(object):  # each path_curve corresponds to a PathData
    def __init__(self, type, instrument_item, datas, sample_rate, time):
        self.type = type
        self.instrument_item = instrument_item
        self.datas = datas
        self.samploe_rate = sample_rate
        self.time = time


if 1 == 11:
    import random

    name = 'temperature'
    instrument = 'Pump_A'
    datas = random.randrange(1,100,2)
    sample_rate = 1
    time = '2020_07_12_07_34_20'

    data = Variable(name, instrument, datas, sample_rate, time)
    print(data)