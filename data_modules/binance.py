import datetime

def read_key(file = 'binance'):
    key = {}
    with open(f'./local_data/{file}') as f:
        content = f.read().splitlines()
        for i in content:
            x = i.split(sep = ': ')
            key[x[0]] = x[1]
    return key


def auth():
    key = read_key()

    from binance.client import Client
    api_key,api_secret = (i for i in key.values())

    client = Client(api_key, api_secret)
    
    return client

def fetch_candles(client,
                symbol ='BNBBTC' ,
                start_date = datetime.datetime.strptime('1 Nov 2021', '%d %b %Y'), 
                end_date = datetime.datetime.today()
                ):
    ''' loads, names columns, saves locally
    datetime required in global frame
    returns nothin
    '''
    limit = 500
    print('working...')
    filename = '{}/local_data/Binance/{}_MinuteBars.csv'.format(os.getcwd(),symbol)
    columns  = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ]

    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, start_date.strftime('%d %b %Y %H:%M:%S'), end_date.strftime('%d %b %Y %H:%M:%S'), limit)
    data = pd.DataFrame(klines, columns = columns )
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

    data.set_index('timestamp', inplace=True)
    data.to_csv(filename)
    print('finished!')
