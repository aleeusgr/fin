
def portfolio_test():
    '''
    data/portfolio.xls
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
    fa_api_key = 'b50abcc7c1b0959040efb9fd755f9b0f'


    '''
    FIX: data_modules.dt.portfolio uses constant rate rub/usd. Needs to be fixed'''
    pf = dt.portfolio() 
    change = pf.pct_change()

    he.heatmap_color(pf.corr().to_numpy(),pf.columns,pf.columns)
    plt.show()

    change['PF'].plot()
    plt.show()

    pf['PF'].plot()
    plt.show()
    #

def regression_test():

    import FundamentalAnalysis as fa
    from data_modules import fa_wrp
    ticker = 'AAPL'
    api_key = fa_wrp.read_key()
    df = fa_wrp.clean_combine(ticker, api_key)

    import numpy as np
    from sklearn.linear_model import LinearRegression

    price_type = 'adjclose'
    x = df.drop(columns=(price_type)).to_numpy()[:-1]
    y = df[price_type].to_numpy()[1:]

    model = LinearRegression()

    model.fit(x,y)

    plt.plot(y)
    plt.plot(model.predict(x))
    plt.show()

    x = df.drop(columns=price_type).iloc[-1,:].to_numpy().reshape(1,-1)
    print(model.predict(x))
