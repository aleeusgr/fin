'''IDEA: a portfolio analyser for MOEX
0.1: current:
moex interface: fetch ticker list, fetch data, load data from disk
TODO:
methods of timeseries analysis: volatility histogram shows bimodal distribution.
0.2: pypfopt

'''
import util
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tsfresh
import apimoex
import pypfopt
import visual as v

tickers = pd.read_csv('./data/tickers.csv')
ticker = tickers['SECID'][0]

df = pd.concat([util.get_period(ticker,period = 10) for ticker in tickers['SECID']],axis = 1)
df = df.dropna(axis=1)
#v.plot_correlation(df.sample(10,axis=1))

from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage

mu = mean_historical_return(df)

#S = CovarianceShrinkage(df).ledoit_wolf()
#OTLIER
plt.figure()
plt.scatter(volatility,mu)
plt.show()
