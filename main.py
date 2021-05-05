import os
import matplotlib.pyplot as plt
import pandas as pd
from util import tests
from compdata import comp_data as dmd
#import simfin as sf
import FundamentalAnalysis as fa
from data_modules import fa_wrp
api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!
#import tds_dmdr
#tests.portfolio_test()

to_value = ['AAPL','GOOG','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY']
ticker = to_value[0]

