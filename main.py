import os
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
from compdata import comp_data as dmd
import FundamentalAnalysis as fa
from data_modules import fa_wrp
api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!
#import tds_dmdr
#tests.portfolio_test()

equity = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
funds = [ 'FDGRX',]
ticker = equity[0]

def combine(ticker):
    import pandas as pd
    cols = {
    'enterprise_value':('stockPrice'),
    'key' : ('peRatio','pbRatio','capexToRevenue','debtToEquity'),
    'financial': ('netProfitMargin','returnOnCapitalEmployed'),
    'growth': ('operatingCashFlowGrowth','rdexpenseGrowth',''),
    }
    data = fa_wrp.fetch_all(ticker)
    df = pd.DataFrame()
    for t in cols:
        df = pd.concat((df,data[t].loc[:,cols[t]]),axis=1)
    return df


data = fa_wrp.fetch_all(ticker)
#data = combine(ticker)
