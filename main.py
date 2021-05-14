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

#tests.portfolio_test()

equity = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
funds = [ 'FDGRX',]
ticker = equity[0]
#data = fa_wrp.fetch_all(ticker)
#data = fa_wrp.combine(ticker)

#compare = pd.DataFrame()
#for t in equity:
#    df = fa.financial_ratios(t, api_key, period = 'quarter' )
#    df = df.loc[('netProfitMargin','returnOnCapitalEmployed')]
#    # rename rows  
#    df = fa_wrp.clean_data(df)
#    compare = pd.concat((compare, df), axis=1)
#


#data = fetch(ticker,('key','financial','growth'))
data = fa_wrp.combine(ticker)
