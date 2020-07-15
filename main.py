
from database.DataBase import DataBase
from generator.Simulator import Simulator
from acqusition.Station import Station
from storage.Storage import Storage
from query.Query import Query
from analysis.Analysis import Analysis

db = DataBase()
# generate dataset
generators = []
for i in range(100):
    generator = Simulator(type='simulator', item='item_A', name='Temperature')
    generator.generate_data_package()
    generators.append(generator)

# acqusition
station = Station(generators)
station.collect_station_datas()
# storage
storage = Storage(db, station)
storage.save_data()

# query
query = Query(storage.session)
query.query()

# Analysis
analysis = Analysis(query.data_frame)
analysis.mean()

# display