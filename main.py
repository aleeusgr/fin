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
import FundamentalAnalysis as fa

graph_starting_date = '13.01.2021'
engine = 'stock'
market = 'shares'
board = 'TQBR'
api_key = 'b50abcc7c1b0959040efb9fd755f9b0f'

pf = dt.portfolio()
change = pf.pct_change()

#he.heatmap_color(pf.corr().to_numpy(),pf.columns,pf.columns)
#plt.show()
#
from compdata import comp_data as dmd # needs beautiful_soup4
#

