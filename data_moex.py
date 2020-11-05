import apimoex
import pandas as pd
import requests

def get_tickers():
    '''
    rename
    TQBR
    '''    
    request_url = ('https://iss.moex.com/iss/engines/stock/'
                   'markets/shares/boards/TQBR/securities.json')
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
    
def get_history(ticker='SNGSP'):    
    '''rename, returns historical data for give ticker'''
    with requests.Session() as session:
        data = apimoex.get_board_history(session,ticker)
        df = pd.DataFrame(data)
        df.set_index('TRADEDATE', inplace=True)
    return df

def fetch_data(tickers):
    '''
    save data locally
    # assert file present, get_tickers() otherwise    

    '''
    tickers = pd.read_csv('./data/tickers.csv')

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
