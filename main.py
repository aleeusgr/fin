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


df = util.random_sample(period = 1500, sample = 0)
tickers = pd.read_csv('./data/tickers.csv')
empty = df.loc[:,df.isna().all()].columns
df = df.drop(empty,axis=1)
df = df.fillna(method = 'bfill')
#df.loc[:,'AGRO'].plot()
missing = util.missing_data(df)
print(df)
