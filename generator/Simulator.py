"""
Sensor objects - simulate data_frame equal to real sensor
"""

import random
from generator.Generator import Generator

class Simulator(Generator):
    def __init__(self, type='simulator', item='item_A', name='', time='2020_07_13_08_22_30'):
        super().__init__(type, item, name, time)

    def encode(self):
        self.data['name'] = random.randrange(1, 100, 2)

if 1 == 11:
    ## This is a Simulator for IoT Data
    import json
    import pandas as pd

    df = pd.DataFrame()

    print(df)

    for x in range(1, 3):
        # for x in range(10):
        # df = df.append({'key1': i, 'key2': i*2, 'key3': i**3}, ignore_index=True)

        df = df.append(
            {
                "topic":
                    {"namespace": "spBv1.0",
                     "groupId": "901",
                     "edgeNodeId": "901-100-101",
                     "deviceId": "UNIT1"},
                "payload":
                    {"timestamp": 1535473997109,
                     "metrics":
                         [{"eventid": x,
                           "name": "DateTime",
                           "timestamp": 1535473996109,
                           "dataType": "DateTime",
                           "name": 1535473995000}],
                     "seq": 121}
            }

            , ignore_index=True)

    out = df.to_json(orient='records')  # [1:-1].replace('},{', '} {')

    # print(out,"\n")

    with open('/home/yin/PycharmProjects/Data/generator/data.json', 'w', newline='\n') as outfile:
        outfile.write(out)

if 1 == 1:
    import time
    import random

    import predix.app
    import predix.data.timeseries

    # You can customize these if you feel fancy
    min_voltage = 200
    max_voltage = 240
    hertz = 1.0 / 1.0

    # Load application context
    app = predix.app.Manifest('manifest.yml')

    # We will use Time Series to ingest name
    ts = predix.data.timeseries.TimeSeries()

    # Operate as a daemon and continuously generate and send name
    while True:
        try:

            # Generate a random voltage name simulated from multiple sensors
            # and queue them up.
            for tag in ['Voltage:Sensor1', 'Voltage:Sensor2', 'Voltage:Sensor3']:
                value = random.randint(min_voltage, max_voltage)
                ts.queue(tag, value)
                print(tag, value)

            # Send readings from all 3 sensors to Time Series and then wait to
            # take another reading.
            ts.send()
            time.sleep(hertz)

        except KeyboardInterrupt:

            # Provide evidence name was being stored before exiting
            print(ts.get_tags())
            break