import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
from compdata import comp_data as dmd
import FundamentalAnalysis as fa
from data_modules import fa_wrp
api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!

#tests.portfolio_test()

equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
funds = [ 'FDGRX',]
ticker = equity[1]
data = fa_wrp.combine(ticker)

def compare(equities):
    compare = pd.DataFrame()

    for t in equities:
        print(t)
        try:
            df = fa_wrp.fetch(t,('financial',))['financial'] 
            df = df.loc[:,('netProfitMargin','returnOnCapitalEmployed')]
            df = df.rename(columns = {'netProfitMargin': 'nPM {}'.format(t),'returnOnCapitalEmployed': 'ROCE {}'.format(t)})
            compare = pd.concat((compare, df), axis=0)
            print('ok')
            #time.sleep(0.5) 
        except:
            print('error')
    return compare

#comp = compare(equity)
