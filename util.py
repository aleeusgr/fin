
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
    # assert file present, get_tickers() otherwise    
    tickers = pd.read_csv('./data/tickers.csv')

    for ticker in tickers['SECID']:

        df = get_history(ticker)
        df.to_csv('{}.csv'.format(ticker))

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

# search 'timeseries plotting'
# `
#frame = frames[0]['CLOSE']
#plt.figure()
#plt.plot(frame)
#plt.show()

