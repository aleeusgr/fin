'''new tested functions, functions that dont have a module yet'''

def compare(tickers=(),metric ='ROCE',  p ='q'):
    '''
    generates a slice on one metric.
    p = period ('q' or 'y')
    ap and revenue_earnings need debugging
    '''
    import metrics as m
    import pandas as pd
    metrics = { # this can be made into submodules by metric type: growth, risk, cash flow.
    'ROCE' : m.ROCE,              # 'efficiency' with caveats.
    'ap'   : m.asset_price,       # Risk: from SwedishInvestor YouTube, 5 takeways from which book?
    'npm'  : m.net_profit_margin, # Risk
    'd/e'  : m.debt_to_equity,    # Risk
    'rnd'  : m.RnD,               # Growth
    'inv'  : m.investment,        # Growth
    'earn' : m.earnings,          # Momentum
    'pepb' : m.pe_pb,             # needs testing

    }
    df = {}
    for t in tickers:
        d = metrics[metric](t,p)
        d.index = pd.PeriodIndex(d.index, freq = 'Q') #
        df[t] = d
    return pd.DataFrame.from_dict(df)

def measuresecound(func):
	import functools
	import time
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		sttime = time.clock()
		res = func(*args,**kwargs)
		entime = time.clock()
		count = (entime - sttime)
		print (count)
		print ('Call %s %f second' % (func.__name__, count))
		return res
	return wrapper

def timer(f):
    import time
    start = time.time()
    print("test_start")

    f()
    end = time.time()
    print(end - start)

def save_png(df,name):
    
    #df.plot(figsize=(20,10))
    plt.savefig('./pics/{}.png'.format(name))

'''DEPRECATED'''
def linreg(df):
    '''compute regression, plot line
    input is tested with single ticker timeseries
    '''
    from sklearn import linear_model
    reg = linear_model.Lasso(alpha=0.1)
    #reg = linear_model.LinearRegression()
    x = df.index.values.astype(float)
    x = x.reshape(-1,1)
    y = df.astype(float).to_numpy().reshape(-1,1)
    reg.fit(x,y)
    pred = reg.predict(x)

    plt.figure()
    df.plot()
    pred = linreg(df)
    plt.plot(pred)
    plt.show()
def missing_data(data):
    import pandas as pd
    import numpy as np
    # Count number of missing value in a column
    total = data.isnull().sum()           
    
    # Get Percentage of missing values
    percent = (data.isnull().sum()/data.isnull().count()*100)   
    temp = pd.concat([total, percent], axis=1, keys=['Tot', '%'])

    ## Create a Type column, that indicates the data-type of the column.
    #types = []
    #for col in data.columns:
    #    dtype = str(data[col].dtype)
    #    types.append(dtype)
    #temp['Types'] = types

    return(np.transpose(temp))


def get_period_old(ticker, period=10):
    df = pd.read_csv('./data/{}.csv'.format(ticker))#one timeseries
    df.set_index('TRADEDATE', inplace=True)
    df[ticker] = df['CLOSE']
    df = df[ticker].iloc[len(df)-period:]
    return df
def get_column(frames,colname='CLOSE'):
    '''frame: tuple of dataframes'''
    for frame in frames:
        yield frame[colname]

def impute_median(df):
    '''Produces bad result'''
    import pandas as pd
    median = df.median()
    df.fillna(median, inplace = True)

def z_max(df):
    '''z-score of MAX of the column'''
    d = df.describe()
    return (d.loc['max']-d.loc['mean'])/d.loc['std']
