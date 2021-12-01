import apimoex as mx
import pandas as pd
import requests

def get_reference(n):
    '''
    placeholder reference by index. 

    '''
    with requests.Session() as session:
        place = ('engines,markets,boards,boardgroups,durations,securitytypes,securitygroups,securitycollections'.split(','))
        i = place[n]
        data = mx.get_reference(session,i) 
        #df = pd.DataFrame(data)
    return data

def get_tickers():
    '''
    Only works with default values
    full list of tickers.
    rewrite
    '''    
    engine = 'stock'
    market = 'shares'
    board = 'TQBR'
    request_url = ('https://iss.moex.com/iss/engines/{}/'
                   'markets/{}/boards/{}/securities.json'.format(engine,market,board))
    arguments = {'securities.columns': ('SECID,'
                                        'REGNUMBER,'
                                        'LOTSIZE,'
                                        'SHORTNAME')}
    with requests.Session() as session:
        iss = mx.ISSClient(session, request_url, arguments)
        data = iss.get()
        df = pd.DataFrame(data['securities'])
        #df.set_index('SECID', inplace=True)

        #df.to_csv('./data/moex_tickers.csv')
    return df
    
def get_history(ticker='SNGSP'):    
    '''rename, returns historical data for give ticker'''
    with requests.Session() as session:
        data = mx.get_board_history(session,ticker)
        df = pd.DataFrame(data)
        df.set_index('TRADEDATE', inplace=True)
    return df

def fetch_candles(ticker='SNGSP',start = '2021-01-13', cut = False, save = True): 
    '''rename, returns historical data for give ticker
    cut: return only data for specified col, rename col with ticker name'''
    with requests.Session() as session:

        data = mx.get_market_candles(session, security = ticker, start=start)

        df = pd.DataFrame(data)
        df['begin'] = pd.to_datetime(df['begin'])
        if cut:
            df = df.rename(columns = {cut:ticker}) # this should be separate function
        if save:
            df.to_csv(f'/local_data/{ticker}.csv')
    return df

def load_local(ticker = 'SNGSP'):
    df = pd.read_csv(f'./local_data/{ticker}.csv', index_col = 'begin', parse_dates = True)
    df.rename(columns = {'value':'Volume'}, inplace = True)
    df.index.rename(ticker, inplace = True)
    df.columns = df.columns.str.title()
    
    return df

def custom_request(f,ticker='SNGSP',board='TQBR'):    
    '''send custom request. 
    f should be apimoex.somthing
    add engine and market as inputs'''
    with requests.Session() as session:

        data = f(session, security = ticker)

        df = pd.DataFrame(data)
    return df
'''
old
'''

def fetch_data(tickers):
    '''
    save data locally
    # assert file present, get_tickers() otherwise    

    '''

    for ticker in tickers['SECID']:

        df = get_history(ticker)
        df.to_csv('./data/{}.csv'.format(ticker))

def get_period(ticker):
    '''Add normalization by lotsize
    rename, reads local data
    '''

    tickers = pd.read_csv('./data/moex_tickers.csv')
    lotsize =  tickers[tickers['SECID'] == ticker]['LOTSIZE'].values[0]
    df = pd.read_csv('./data/{}.csv'.format(ticker),parse_dates = ['TRADEDATE'])#one timeseries
    df.set_index('TRADEDATE', inplace=True)
    # price adjustment: lotsize, currency
    df[ticker] = df['CLOSE']*lotsize 
    return  df[ticker]




def random_sample(sample=3,random_state = None):
    '''load data into memory, drop empty columns'''
    import pandas as pd
    import data_moex
    
    tickers = pd.read_csv('./data/moex_tickers.csv')
    tickers = tickers['SECID']
    if sample != 0:
            tickers = tickers.sample(sample,random_state=random_state)

    df = pd.concat([data_moex.get_period(ticker) for ticker in tickers],axis = 1)


    empty = df.loc[:,df.isna().all()].columns
    df = df.drop(empty,axis=1)
    #df = df.fillna(method = 'backfill',axis = 1)
    return df
