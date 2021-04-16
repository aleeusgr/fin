'''
http://ftp.moex.com/pub/Terminals/ASTS/Equities/MOEX_Trade_SE_QuickStart_English.pdf

https://wlm1ke.github.io/apimoex/build/html/api.html

https://towardsdatascience.com/python-comparables-financial-data-package-ee8863fe7bb1
'''
from util.tests import portfolio_test
from compdata import comp_data 
import yahoo_fin as yf
import FundamentalAnalysis as fa


#portfolio_test()

#
# data sources:  
# apimoex - american stocks at MOEX; qual/non-qual
# tds_dmr - Gaussian DCF, play around with inputs, refactor
# valuation: timeseries to compare to price
# ML pipe ideas:
# train_y(t)=pd.Series, price, train_x=[t1,t2...tn], t = ticker
# train_y(t) = price, train_x = f(v,g,r), value, growth, risk
