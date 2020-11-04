#import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import tsfresh
#import apimoex
#import pypfopt
import visual as v
import moex
import util

tickers = pd.read_csv('./data/tickers.csv')
select = 'UCSS'

#df = util.random_sample( sample = 0)
df = pd.read_csv('./data/{}.csv'.format(select)).loc[:,'CLOSE']

#cheap = df.mean()<15000
#df = util.impute(df)
