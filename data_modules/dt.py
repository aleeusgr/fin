''' tested functions to work with local data'''

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


def import_tickers():
    '''Import data from my excel file
    returns a list of tickers.
    '''
    import pandas as pd
    df = pd.read_excel('./local_data/portfolio.xlsx')
    select = df.iloc[:1,3:13] # make adaptable??
    
    #FYI
    tickers = {
        'TQTF' : list(df.iloc[0,3:11].index),
        'TQTD' : list(df.iloc[0,11:13].index)
        }

    return select

def portfolio():
    '''
    USD/RUB rate adjuctment
    RUB assets vs USD assets
    portfolio.xls to price timeseries
    '''
    import pandas as pd
    from data_modules import data_moex as dtm
    tickers = import_tickers()
    df = pd.concat([dtm.get_candles(ticker,cut='close')[ticker] for ticker in tickers.columns],axis = 1) # produce dataframe with tickers as col labels and 'close' price.
    print('USD is set to fixed rate 77.1; need to implement')
    usd = 72.1
    for c in ['TIPO','TECH']:
        df[c] *=usd    
    df['PF'] = df.dot(tickers.iloc[0])
    return df
