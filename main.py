import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
from compdata import comp_data as dmd
from yahoo_fin import stock_info as si
from data_modules import yhf_wrp as yhf
from util.util import compare

#TODO: tinkoff_api!!!

#tests.portfolio_test()
#tests.metrics_test()

equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
funds = [ 'FDGRX',]
ticker = equity[1]

x = compare(equity[:2],'earn')
