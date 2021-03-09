'''
http://ftp.moex.com/pub/Terminals/ASTS/Equities/MOEX_Trade_SE_QuickStart_English.pdf

this is project idea to build a portfolio dynamics calculator/vusialiser in jupyter lab'''

#TODO
# import ticker volumes
# graph
import pandas as pd
import apimoex as mx
import requests
from data_modules import data_moex as dtm
from data_modules import dt

graph_starting_date = '13.01.2021'
engine = 'stock'
market = 'shares'
board = 'TQBR'
tickers = dt.import_tickers()

