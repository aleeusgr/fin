''' tested functions to work with local data'''
def random_sample(sample=3,random_state = None):
    '''load data into memory, drop empty columns'''
    import pandas as pd
    import data_moex
    
    tickers = pd.read_csv('./data/tickers.csv')
    tickers = tickers['SECID']
    if sample != 0:
            tickers = tickers.sample(sample,random_state=random_state)

    df = pd.concat([data_moex.get_period(ticker) for ticker in tickers],axis = 1)


    empty = df.loc[:,df.isna().all()].columns
    df = df.drop(empty,axis=1)
    #df = df.fillna(method = 'backfill',axis = 1)
    return df

def impute(df):
    '''try different approaches'''
    import pandas as pd
    from sklearn.experimental import enable_iterative_imputer
    from sklearn.impute import KNNImputer,IterativeImputer,SimpleImputer
    
    #df.fillna(method = 'ffill',inplace = True)
    imputer = KNNImputer(n_neighbors=2)
    #imputer = IterativeImputer(max_iter=10, random_state=0) #computationally heavy; did not converge
    #imputer = SimpleImputer()
    test = df.to_numpy()

    return pd.DataFrame(imputer.fit_transform(test),index = df.index, columns = df.columns)

def outlier_sample(t = 'UCSS'):
    import pandas as pd
    return pd.read_csv('./data/{}.csv'.format(t)).loc[:,'CLOSE']


def import_tickers():
    '''Import data from my excel file
    returns a list of tickers.
    '''
    import pandas as pd
    df = pd.read_excel('./data/portfolio.xlsx')
    select = df.iloc[:1,3:13] # make adaptable??
    
    #FYI
    tickers = {
        'TQTF' : list(df.iloc[0,3:11].index),
        'TQTD' : list(df.iloc[0,11:13].index)
        }

    return select

def portfolio():
    '''
    portfolio.xls to price timeseries
    '''
    import pandas as pd
    from data_modules import data_moex as dtm
    tickers = import_tickers()
    df = pd.concat([dtm.get_candles(ticker,cut='close')[ticker] for ticker in tickers.columns],axis = 1) # produce dataframe with tickers as col labels and 'close' price.

    df['PF'] = df.dot(tickers.iloc[0])
    return df
