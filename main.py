import os
import matplotlib.pyplot as plt
import pandas as pd
from util.tests import portfolio_test
from compdata import comp_data as dmd
#import simfin as sf
import FundamentalAnalysis as fa
from data_modules.fa_wrp import key, fetch
api_key = key()
#TODO: tinkoff_api!!!
#import tds_dmdr
#portfolio_test()

to_value = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
ticker = to_value[0]
df = fetch(ticker, api_key)

# look at corr()


#import numpy as np
#from sklearn.linear_model import LinearRegression
#
#x = df.iloc[:,2:].to_numpy()
#y = df['adjclose'].to_numpy()
#
#model = LinearRegression()
#
#model.fit(x,y)
#
#
