'''IDEA: a portfolio analyser for MOEX
0.1: 
moex interface: fetch ticker list, fetch data, load data from disk
0.2: pypfopt
choose optimiser
choose risk model
experiment with period
check price regularization
check price currency
out of sample returns
Read the notebooks
variance/return plot!!

TODO:
methods of timeseries analysis: volatility histogram shows bimodal distribution.
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
S = CovarianceShrinkage(df).ledoit_wolf()

from pypfopt.efficient_frontier import EfficientFrontier

ef = EfficientFrontier(mu, S)
weights = ef.min_volatility()
cleaned_weights = ef.clean_weights()
print(ef.portfolio_performance(verbose=True))
