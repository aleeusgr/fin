
def grether():
    from models.grether import grether_distribution
    
    import matplotlib.pyplot as plt
    import numpy as np
    for Ps in np.arange(0,1,0.1):
        
        dist = grether_distribution(Ps)
        for i in dist:
            plt.plot(i)
        
        plt.show()

def lucas_tree():

    from models import lucas as l
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))
    print('function has greek latters in code')
    for β in (.95, 0.98):
        tree = l.LucasTree(β=β)
        grid = tree.grid
        price_vals = l.solve_model(tree)
        label = rf'$\beta = {β}$'
        ax.plot(grid, price_vals, lw=2, alpha=0.7, label=label)

    ax.legend(loc='upper left')
    ax.set(xlabel='$y$', ylabel='price', xlim=(min(grid), max(grid)))
    plt.show()

def heatmap():
    import util.heatmap as h
    import numpy as np
    import pandas as pd
    low = -10
    high = 10
    size = 20

    data = np.random.randint(low,high,size=(size,size))
    labels = [str(i) for i in range(size)]
    h.heatmap_color(data,labels, labels) 

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

    #this was broken as of 13.09.21
    #he.heatmap_color(pf.corr().to_numpy(),pf.columns,pf.columns)
    #plt.show()

    change['PF'].plot()
    plt.show()

    pf['PF'].plot()
    plt.show()
    #

##broken:
def fin_multiples(period = 'q', verbose = False):
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
            x = compare(equity[:amount_of_tickers], metric = m, p = period)
            print(x)
        except:
            errors += m,
    print('errors in %s'%[e for e in errors])


def HRP_test(df,amount = 60000):

    '''needs reworking, load df: price by ticker'''
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

