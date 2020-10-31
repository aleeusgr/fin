def random_sample(period=10,sample=10):
    import pandas as pd
    import moex
    tickers = pd.read_csv('./data/tickers.csv')
    ticker = tickers['SECID'][0]


    df = pd.concat([moex.get_period(ticker,period ) for ticker in tickers['SECID']],axis = 1)
    df = df.dropna(axis=1)
    if sample != 0:
        df = df.sample(sample,axis=1) 
    return df

def calculate(df):
    from pypfopt.expected_returns import mean_historical_return
    from pypfopt.risk_models import CovarianceShrinkage

    mu = mean_historical_return(df)
    S = CovarianceShrinkage(df).ledoit_wolf()

    from pypfopt.efficient_frontier import EfficientFrontier

    #ef = EfficientFrontier(mu, S)
    #weights = ef.min_volatility()
    #cleaned_weights = ef.clean_weights()
    #print(ef.portfolio_performance(verbose=True))
    #from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    #latest_prices = get_latest_prices(df)
    #da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=20000)
    #allocation, leftover = da.lp_portfolio()
    #print(allocation)
    
    from pypfopt.plotting import plot_efficient_frontier
    from pypfopt.cla import CLA
    plot_efficient_frontier(CLA(mu,S))

'''DEPRECATED'''
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

#for ticker in tickers['SECID']:
#    df = pd.read_csv('./data/{}.csv'.format(ticker))
#    frames+= df.iloc[len(df)-length:,:],
#
#frame = frames[0]['TRADEDATE']    

# combine dataframes into one with name and price.

#dt = [frame['CLOSE'] for frame in frames]
#df = pd.DataFrame(data = dt,index=frames[0]["TRADEDATE"],columns= tickers['SECID'])

# `
#frame = frames[0]['CLOSE']
#plt.figure()
#plt.plot(frame)
#plt.show()


