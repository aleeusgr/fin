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


df = util.random_sample( sample = 0)
tickers = pd.read_csv('./data/tickers.csv')
imputation_test_ticker = 'UCSS'
cheap = df.mean()<15000

df = util.impute(df)
