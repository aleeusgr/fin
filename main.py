import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
from compdata import comp_data as dmd
import FundamentalAnalysis as fa
from data_modules import fa_wrp
from yahoo_fin import stock_info as si

api_key = fa_wrp.read_key()
#TODO: tinkoff_api!!!

#tests.portfolio_test()

equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
funds = [ 'FDGRX',]
ticker = equity[1]
#data = fa_wrp.combine(ticker)

metrics = ('peRatio','pbRatio','capexToRevenue','debtToEquity', 'netProfitMargin','returnOnCapitalEmployed','operatingCashFlowGrowth','rdexpenseGrowth',)
data = {
'fin' : si.get_financials, #includes balance sheet,income, cash flow
'analyst_info': si.get_analysts_info,
'balance': si.get_balance_sheet,
'cash flow':si.get_cash_flow,
'price'   : si.get_data,
'summary' : si.get_quote_data,
}
