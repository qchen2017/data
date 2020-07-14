
from app.DataBase import DataBase
from generator.Simulator import Simulator
from acqusition.Station import Station
from storage.Storage import Storage

db = DataBase()
# generate dataset
generator = Simulator(type='simulator', item='item_A', name='Temperature')
generator.generate_data_package()

generators = []
generators.append(generator)
# acqusition
station = Station(generators)
station.collect_station_datas()
# storage
s = Storage(db, station)
s.save_data()

# query


# analysis


# display