
import traceback
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from application.datareceiver import DataReceiver
from application.database import DataBase
from application.dataset import DataSet
from application.query import Query
from application.analysis import Analysis
from application.graphics import plot_timeseries


data_receiver = DataReceiver()
# db = DataBase()
# db.create_table()

data = []
while data is not None:
    data = data_receiver.get_data()
    if data is None:
        break
    dataset = DataSet(data)
    dataset.save_to()

query = Query()
df = query.query()

# analysis
mv = Analysis.get_mean(df)

# report
# plt.figure()
# df.age.plot()
# # plot_timeseries(df, yaxis_min=0, yaxis_max=20)
# plt.savefig('./test.png', format='png')
# plt.close()

df.plot()#对A列作图，同理可对行做图

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# df =pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
# df = df.cumsum()
# print(df)
# # 图1：其中A图用左Y轴标注，B图用右Y轴标注，二者共用一个X轴
# df.A.plot()#对A列作图，同理可对行做图
plt.show()






