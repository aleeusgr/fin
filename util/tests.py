
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

def metrics_test(verbose = False):
    
    metrics = ('ROCE' , 'ap' , 'npm' , 'd/e' ,'rnd' , 'inv' , 'earn') 
    equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
    amount_of_tickers = 2
    if verbose:
        amount_of_tickers = len(equity)
    errors = ()
    for m in metrics:
        try:
            print('function %s'%m)
            x = yhf.compare(equity[:amount_of_tickers], metric = m)
            print(x)
        except:
            errors += m,
    print('errors in %s'%[e for e in errors])
