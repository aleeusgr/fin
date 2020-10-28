
import apimoex
import pandas as pd
import requests

def get_tickers():
    
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

        df.to_csv('tickers.csv')
    
def get_history(ticker='SNGSP'):    
    with requests.Session() as session:
        data = apimoex.get_board_history(session,ticker)
        df = pd.DataFrame(data)
        df.set_index('TRADEDATE', inplace=True)
    return df

def fetch_data(tickers):
    

    for ticker in tickers['SECID']:

        df = get_history(ticker)
        df.to_csv('{}.csv'.format(ticker))

