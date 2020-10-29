'''IDEA: a portfolio analyser for MOEX
0.1: current:
moex interface: fetch ticker list, fetch data, load data from disk
TODO: 
statistical methods: plot regression line??
Correlation map for tickers!!
combine frames into on big.

methods of timeseries analysis: volatility histogram shows bimodal distribution.
0.2: pypfopt

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
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage

tickers = pd.read_csv('./data/tickers.csv')
ticker = tickers['SECID'][0]
mus, Ss = (),()
for ticker in tickers['SECID']:
    df = pd.read_csv('./data/{}.csv'.format(ticker))#one timeseries
    df.set_index('TRADEDATE', inplace=True)

    df[ticker] = df['CLOSE']
    df = df[ticker]

    mu = mean_historical_return(df)
    mus += mu[0],
    S = CovarianceShrinkage(df).ledoit_wolf()
    Ss += S.iloc[0,0],
#OTLIER
plt.figure()
plt.scatter(Ss,mus)
plt.show()

## needs composed dataframe
#from pypfopt.efficient_frontier import EfficientFrontier
#
#ef = EfficientFrontier(mu, S)
#weights = ef.max_sharpe()
#cleaned_weights = ef.clean_weights()
#
#print(cleaned_weights)
