import os
import matplotlib.pyplot as plt
from util.tests import portfolio_test
from compdata import comp_data as dmd
import yahoo_fin as yf
import FundamentalAnalysis as fa
from data_modules import fa_wrp
# tinkoff_api!!!
#import tds_dmdr
#portfolio_test()

ticker = 'MSFT'
cik = "0000102909"
forms =( '13F-HR','13F-NT','13FCONP')

#holdings = {}
#for i in dmd_industries:
#    industry = dmd.Industry(i)
#    holdings[i] = industry.get_holdings()
#
#roe = fa_wrp.roe(ticker,fa_wrp.api_key)
save_path = './data'
filing = forms[0]
location = "{}/sec-edgar-filings/{}/{}/".format(save_path, cik, filing)
files = os.listdir(location)
f = files[0]

def parse(file, CIK,filing = forms[0], save_path = './data'):

    import datetime
    import pandas as pd

    location = "{}/sec-edgar-filings/{}/{}/{}/".format(save_path, cik, filing, file)

    with open(location + 'full-submission.txt') as f:
        lines = f.readlines()
    return lines

#for f in files:
#    try: 
#        print(parse(f,cik))
#    except:
#        pass
f = sorted(files)[-1]
(parse(f,cik))
