import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
from compdata import comp_data as dmd
import FundamentalAnalysis as fa
from data_modules import fa_wrp
from yahoo_fin import stock_info as si
from data_modules import yhf_wrp as yhf

api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!

#tests.portfolio_test()

equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
funds = [ 'FDGRX',]
ticker = equity[1]
#data = fa_wrp.combine(ticker)
fin = yhf.fetch(ticker, 'fin')

#momentum

def compare(tickers=(),metric ='ROCE',  p ='q'):
    metrics = {
    'ROCE' : yhf.ROCE, 
    'ap'   : yhf.asset_price,
    'npm'  : yhf.net_profit_margin,
    'd/e'  : yhf.debt_to_equity,
    'rnd'  : yhf.RnD,
    'inv'  : yhf.investment,

    }
    df = pd.DataFrame()
    for t in tickers:
        d = metrics[metric](t,p)
        # adjust dates
        d.reindex(pd.PeriodIndex(d.index, freq = 'Q'))
        print(d)
        # rename columns, 
        df = pd.concat((df,d),axis=1) 
    return df

x = compare(equity[:3])
