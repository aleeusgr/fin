import os
from data_modules import data_moex as dm
import pandas as pd
from data_modules import binance as bi
import datetime

ticker = 'SNGSP'
df = pd.read_csv(f'./local_data/{ticker}.csv', parse_dates = True,index_col = ticker)

