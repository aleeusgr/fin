'''IDEA: a portfolio analyser for MOEX
TODO: example  df with 4 tickers
NEXT: pypfopt

'''
import util
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import tsfresh
import apimoex
import pypfopt


tickers = pd.read_csv('./data/tickers.csv')
ticker = tickers['SECID'][0]

#Sample data:
# dont care for length for now, just take last 100 entries.
length = 100
frames = ()
for ticker in tickers['SECID']:
    df = pd.read_csv('./data/{}.csv'.format(ticker))
    frames+= df.iloc[len(df)-length:,:],

frame = frames[0]['TRADEDATE']    

# combine dataframes into one with name and price.
def get_column(frames,colname='CLOSE'):
    for frame in frames:
        yield frame[colname]

dt = [frame['CLOSE'] for frame in frames]
#df = pd.DataFrame(data = dt,index=frames[0]["TRADEDATE"],columns= tickers['SECID'])

# search 'timeseries plotting'
# `
#frame = frames[0]['CLOSE']
#plt.figure()
#plt.plot(frame)
#plt.show()
