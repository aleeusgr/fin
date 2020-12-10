'''new tested functions, functions that dont have a module yet'''

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

def timer(f):
    import time
    start = time.time()
    print("test_start")

    f()
    end = time.time()
    print(end - start)

def save_png(df,name):
    
    #df.plot(figsize=(20,10))
    plt.savefig('./pics/{}.png'.format(name))

'''DEPRECATED'''
def linreg(df):
    '''compute regression, plot line
    input is tested with single ticker timeseries
    '''
    from sklearn import linear_model
    reg = linear_model.Lasso(alpha=0.1)
    #reg = linear_model.LinearRegression()
    x = df.index.values.astype(float)
    x = x.reshape(-1,1)
    y = df.astype(float).to_numpy().reshape(-1,1)
    reg.fit(x,y)
    pred = reg.predict(x)

    plt.figure()
    df.plot()
    pred = linreg(df)
    plt.plot(pred)
    plt.show()
def missing_data(data):
    import pandas as pd
    import numpy as np
    # Count number of missing value in a column
    total = data.isnull().sum()           
    
    # Get Percentage of missing values
    percent = (data.isnull().sum()/data.isnull().count()*100)   
    temp = pd.concat([total, percent], axis=1, keys=['Tot', '%'])

    ## Create a Type column, that indicates the data-type of the column.
    #types = []
    #for col in data.columns:
    #    dtype = str(data[col].dtype)
    #    types.append(dtype)
    #temp['Types'] = types

    return(np.transpose(temp))


def get_period_old(ticker, period=10):
    df = pd.read_csv('./data/{}.csv'.format(ticker))#one timeseries
    df.set_index('TRADEDATE', inplace=True)
    df[ticker] = df['CLOSE']
    df = df[ticker].iloc[len(df)-period:]
    return df
def get_column(frames,colname='CLOSE'):
    '''frame: tuple of dataframes'''
    for frame in frames:
        yield frame[colname]

def impute_median(df):
    '''Produces bad result'''
    import pandas as pd
    median = df.median()
    df.fillna(median, inplace = True)

def z_max(df):
    '''z-score of MAX of the column'''
    d = df.describe()
    return (d.loc['max']-d.loc['mean'])/d.loc['std']
