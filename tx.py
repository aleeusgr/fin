#!bin/python

def fetch(save = False, dset_name = 'dataset.csv'):
    '''Get data from web
     DO:
     try different sources
     parameters 

     resamples, saves to disk'''

    import pandas_datareader.data as web
    import datetime as dt
    import world_bank_data as wb

    #wb.get_topics()

    provider = {
    0:'yahoo',  # symbols: MSFT
    1:'quandl', #has specific symbol format. symbols:??? 
    2: 'moex',  #Moscow Exchange.  symbols:??? 
    3: 'fred',  #???
    4: 'stooq', #common index data. symbols: ^DJI
    5: 'eurostat', #browse website for symbols
    6: 'iex',   # requires API key
    }

    n_prov = 0
    symbols = {
    'yahoo' : (('oil','CL=F'),('rub','RUB=X'))
    }
    web_data = {}
    start = '1998-01-01' # train_y starts here 
    end_train = '2020-08-30' 
    for name,ticker in symbols[provider[n_prov]]:
        web_data[name] = web.DataReader(ticker,provider[n_prov],start=start) 
        web_data[name] = web_data[name].loc[:,'Close'].resample('1M').mean()
        web_data[name].fillna(method='bfill',inplace=True)
    
    import pandas as pd
    dset = pd.DataFrame.from_dict(web_data)
    lengths = dset.count(0)
    dset_cut = dset.iloc[lengths.max()-lengths.min():].copy()
    if save:
        dset_cut.to_csv('{}'.format(dset_name))
    return dset_cut

def loadX(save_locally = False, dset_name = 'dataset.csv'):
    import pandas as pd
    try:
        dataX = pd.read_csv(dset_name)
        #dataX = load_local_x()
    except:
        print('local files not found, fetching..')
        dataX = fetch(save_locally, dset_name = 'dataset.csv')
    return dataX

#
#DEPRECATED

#    sortest_dataset_date = '2004-08-30' 
#
#    dataM={} # rename? resampled, monthly
#    for i in web_data.keys():
#        dataM[i] = web_data[i].resample(resample).mean()
#       


def load_local_x():
    '''Load local data
    DO: returns: pd.Dataframe?
    returns: {filename: pd.Dataframe'''
    import pandas as pd
    from os import listdir,getcwd
    from os.path import isfile, join
    mypath = getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    data = {}
    for f in onlyfiles:
        if '.csv' in f:
            data[f] =  pd.read_csv(f)

    return data
def show_train_x_graphs():
    '''deprecated?'''
    oil = pd.read_csv('oil.csv')
    rub = pd.read_csv('rub.csv')

    plt.figure(figsize=(10,5))
    plt.plot(oil['Close'],label='Crude Oil')
    plt.plot(rub['Close'],label='USD/RUB')
    plt.legend()
    plt.show()

