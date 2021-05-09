import os
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
#from compdata import comp_data as dmd
#import simfin as sf
import FundamentalAnalysis as fa
from data_modules import fa_wrp
api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!
#import tds_dmdr
#tests.portfolio_test()

to_value = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
#ticker = to_value[0]
ticker = 'FDGRX'

hxz = pd.read_csv('./local_data/q5_factors_quarterly_2020.csv')
stock_data = fa_wrp.price(ticker)
returns = stock_data.pct_change()
#def align_dates(
returns = returns.iloc[1:-2]
factors = hxz.iloc[len(hxz)-len(returns):]
y = returns.to_numpy()
x = factors.iloc[:,2:].to_numpy()

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

x = scaler.fit_transform(x)

model = LinearRegression()

model.fit(x,y)

plt.plot(y)
plt.plot(model.predict(x))
plt.show()

