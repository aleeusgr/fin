import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
#from compdata import comp_data as dmd
#from yahoo_fin import stock_info as si
#from data_modules import yhf_wrp as yhf
from util.util import compare

#TODO: tinkoff_api!!!

#tests.portfolio_test()
#tests.metrics_test(period = 'y')

rand = ['AAPL' , 'AMZN' , 'KO' , 'BABA' , 'JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
dorsey = ['FB', 'SMAR', 'WIX' , 'EBAY' , 'PYPL' , 'UPWK' , 'GOOG' , 'DESP']
auto = ['VWAGY' , 'RYCEY']
funds = [ 'FDGRX',]
ticker = rand[1]

# e, npm  = (compare(dorsey.remove('DESP') , m) for m in ('earn', 'npm'))

# get company's industry
# get list of companies by industry?
#'earn' get top performing hedge funds? on a variable time horizon
