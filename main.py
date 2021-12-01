import os
from data_modules import data_moex as dm
import pandas as pd
from data_modules import binance as bi
import datetime

df = dm.load_local()



candles(df)
