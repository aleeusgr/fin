import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import tsfresh
#import apimoex
#import pypfopt
import visual as v
import util,dt
'''
add usd, oil(?)
HRP portfolio 
'''

#DATA
df = dt.random_sample(sample = 9, random_state = 2)
#df = dt.outlier_sample()
cheap = df.mean()<15000

# add USD/RUB
#rub = pd.read_csv('./data/RUB.csv', index_col = 'Date', parse_dates=True)
#rub_cut = rub.loc[df.index[0]:df.index[-1]]
#df = pd.concat([df,rub])

#CLEANING

#df.fillna(method = 'ffill',inplace = True)

# how much data is missing?
isna = df.isna().sum()

# HRP 
df = df.iloc[len(df.index)-180:]

# do decomposition? depends on what I am going to do next.
from pypfopt.hierarchical_portfolio import HRPOpt
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage

mu = mean_historical_return(df)
S = CovarianceShrinkage(df).ledoit_wolf()

returns = pd.DataFrame(mu, index = df.columns) 
#covar =  pd.DataFrame(S, index = df.index) 
HRP = HRPOpt(cov_matrix = S )

portfolio = HRP.optimize()
