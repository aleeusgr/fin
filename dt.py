''' tested functions to clean data'''
def random_sample(sample=10,random_state = None):
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
    imputer = KNNImputer(n_neighbors=9)
    imputer = IterativeImputer(max_iter=10, random_state=0) #computationally heavy; did not converge
    imputer = SimpleImputer()
    test = df.to_numpy()

    return pd.DataFrame(imputer.fit_transform(test),index = df.index, columns = df.columns)

def outlier_sample(t = 'UCSS'):
    import pandas as pd
    return pd.read_csv('./data/{}.csv'.format(t)).loc[:,'CLOSE']
