def random_sample(sample=10):
    import pandas as pd
    import moex
    
    tickers = pd.read_csv('./data/tickers.csv')
    ticker = tickers['SECID'][0]
    tickers = tickers['SECID']
    if sample != 0:
            tickers = tickers.sample(sample)

    df = pd.concat([moex.get_period(ticker) for ticker in tickers],axis = 1)
    empty = df.loc[:,df.isna().all()].columns
    df = df.drop(empty,axis=1)
    #df = df.fillna(method = 'backfill',axis = 1)
    return df

def impute(df):
    import pandas as pd
    from sklearn.impute import KNNImputer
    from sklearn.experimental import enable_iterative_imputer
    from sklearn.impute import IterativeImputer
    imputer = KNNImputer(n_neighbors=2)
    #imputer = IterativeImputer(max_iter=10, random_state=0) #computationally heavy; did not converge
    test = df.to_numpy()

    return pd.DataFrame(imputer.fit_transform(test),index = df.index, columns = df.columns)

def calculate(df):
    from pypfopt.expected_returns import mean_historical_return
    from pypfopt.risk_models import CovarianceShrinkage

    mu = mean_historical_return(df)
    S = CovarianceShrinkage(df).ledoit_wolf()

    from pypfopt.efficient_frontier import EfficientFrontier

    ef = EfficientFrontier(mu, S)
    weights = ef.min_volatility()
    cleaned_weights = ef.clean_weights()
    print(ef.portfolio_performance(verbose=True))
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(df)
    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=20000)
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

'''DEPRECATED'''
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
