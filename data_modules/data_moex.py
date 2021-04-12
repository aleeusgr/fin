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

    
def get_history(ticker='SNGSP'):    
    '''rename, returns historical data for give ticker'''
    with requests.Session() as session:
        data = apimoex.get_board_history(session,ticker)
        df = pd.DataFrame(data)
        df.set_index('TRADEDATE', inplace=True)
    return df

def get_candles(ticker='SNGSP',start = '2021-01-13', cut = False): 
    '''rename, returns historical data for give ticker
    cut: return only data for specified col, rename col with ticker name'''
    with requests.Session() as session:

        data = mx.get_market_candles(session, security = ticker, start=start)

        df = pd.DataFrame(data)
        df['begin'] = pd.to_datetime(df['begin'])
        if cut:
            df = df.rename(columns = {cut:ticker}) # this should be separate function
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
    #tickers = pd.read_csv('./data/tickers.csv')

    for ticker in tickers['SECID']:

        df = get_history(ticker)
        df.to_csv('./data/{}.csv'.format(ticker))

def get_period(ticker):
    '''Add normalization by lotsize
    rename, reads local data
    '''

    tickers = pd.read_csv('./data/tickers.csv')
    lotsize =  tickers[tickers['SECID'] == ticker]['LOTSIZE'].values[0]
    df = pd.read_csv('./data/{}.csv'.format(ticker),parse_dates = ['TRADEDATE'])#one timeseries
    df.set_index('TRADEDATE', inplace=True)
    # price adjustment: lotsize, currency
    df[ticker] = df['CLOSE']*lotsize 
    return  df[ticker]


def get_tickers(engine = 'stock', market = 'shares', board = 'TQBR'):
    '''
    Only works with default values
    full list of tickers.
    rewrite
    '''    
    request_url = (f'https://iss.moex.com/iss/engines/{engine}/'
                   'markets/{market}/boards/{board}/securities.json')
    arguments = {'securities.columns': ('SECID,'
                                        'REGNUMBER,'
                                        'LOTSIZE,'
                                        'SHORTNAME')}
    with requests.Session() as session:
        iss = apimoex.ISSClient(session, request_url, arguments)
        data = iss.get()
        df = pd.DataFrame(data['securities'])
        df.set_index('SECID', inplace=True)

        df.to_csv('./data/tickers.csv')
