import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
#%matplotlib inline
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 8)
pd.set_option('precision', 3)

from pandas_datareader import data as web

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2012, 12, 30)

msft=web.DataReader("MSFT","yahoo",start,end)
aapl=web.DataReader("AAPL","yahoo",start,end)




