
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
    from util.util import compare 
    from data_modules import yhf_wrp as yhf
    metrics = ('ROCE' , 'ap' , 'npm' , 'd/e' ,'rnd' , 'inv' , 'earn') 
    equity = ['AAPL','AMZN','KO','JNJ','CL', 'BUD' ,'MSFT', 'HD', 'WIX', 'UPWK', 'RUN', 'ROKU', 'PYPL', 'NVDA', 'FB', 'DESP', 'NET', 'ALXN', 'EBAY', 'GOOG',]
    amount_of_tickers = 2
    if verbose:
        amount_of_tickers = len(equity)
    errors = ()
    for m in metrics:
        try:
            print('function %s'%m)
            x = compare(equity[:amount_of_tickers], metric = m)
            print(x)
        except:
            errors += m,
    print('errors in %s'%[e for e in errors])

def invest(df,amount = 60000):
    from pypfopt.expected_returns import mean_historical_return
    from pypfopt.risk_models import CovarianceShrinkage

    mu = mean_historical_return(df)
    S = CovarianceShrinkage(df).ledoit_wolf()

    #from pypfopt.efficient_frontier import EfficientFrontier
    #ef = EfficientFrontier(mu, S)
    #weights = ef.min_volatility()
    #cleaned_weights = ef.clean_weights()
    #print(ef.portfolio_performance(verbose=True))


    from pypfopt.hierarchical_portfolio import HRPOpt
    HRP = HRPOpt(cov_matrix = S )
    portfolio = HRP.optimize()
    weights = HRP.clean_weights()
    print(HRP.portfolio_performance())
    
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(df)
    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=amount)
    allocation, leftover = da.lp_portfolio()
    print(allocation)
    
    #from pypfopt.plotting import plot_efficient_frontier
    #from pypfopt.cla import CLA
    #plot_efficient_frontier(CLA(mu,S))

