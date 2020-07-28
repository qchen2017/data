
from database.DataBase import DataBase
from generator.Simulator import Simulator
from acqusition.Station import Station
from storage.Storage import Storage
from query.Query import Query
from analysis.Analysis import Analysis

db = DataBase()
# generate dataset
generators = []
for i in range(2):
    generator = Simulator(type='simulator', item='item_A', name='Temperature')
    generator.encode()
    generators.append(generator)

# acqusition
station = Station(generators)
station.collect_station_datas()
# storage
storage = Storage(db, station)
storage.storage()

# query
query = Query(storage.session)
query.query()

# Analysis
analysis = Analysis(query.data_frame)
analysis.analysis()

# display