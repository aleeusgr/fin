'''
http://ftp.moex.com/pub/Terminals/ASTS/Equities/MOEX_Trade_SE_QuickStart_English.pdf

'''
import pandas as pd
import apimoex as mx
import requests
from data_modules import data_moex as dtm
from data_modules import dt
import matplotlib.pyplot as plt
from util import heatmap as he

graph_starting_date = '13.01.2021'
engine = 'stock'
market = 'shares'
board = 'TQBR'

pf = dt.portfolio()
change = pf.pct_change()

he.heatmap_color(pf.corr().to_numpy(),pf.columns,pf.columns)
plt.show()
