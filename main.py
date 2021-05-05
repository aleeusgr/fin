import os
import matplotlib.pyplot as plt
import pandas as pd
from util.tests import portfolio_test
from compdata import comp_data as dmd
#import simfin as sf
import FundamentalAnalysis as fa
from data_modules import fa_wrp
api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!
#import tds_dmdr
#portfolio_test()

to_value = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
ticker = to_value[0]

def clean_combine(ticker, api_key):
    price = fa_wrp.fetch_stock_data(ticker,api_key)
    data = fa_wrp.fetch_data(ticker, api_key)

    df = pd.concat((price,data),axis=1)
    df = df.dropna()
    #df = df.pct_change()

    return df

df = clean_combine(ticker, api_key)

def offset_correlation(df, offset = -1):
    corr = {}
    for c in df.columns:
        corr[c] = df['adjclose'].corr(df[c].shift(offset))

    return pd.Series(corr)




import numpy as np
from sklearn.linear_model import LinearRegression

x = df.drop(columns=('adjclose')).to_numpy()[:-1]
y = df['adjclose'].to_numpy()[1:]

model = LinearRegression()

model.fit(x,y)

plt.plot(y)
plt.plot(model.predict(x))
plt.show()

x = df.drop(columns='adjclose').iloc[-1,:].to_numpy().reshape(1,-1)
print(model.predict(x))
