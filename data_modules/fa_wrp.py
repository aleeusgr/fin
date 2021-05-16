import FundamentalAnalysis as fa
import pandas as pd

def read_key():
    with open('./local_data/fa') as f:
        content = f.read().splitlines()
    return content[0]

def price(ticker, t = 'adjclose'):
    stock_data = fa.stock_data(ticker, period="max", interval="3mo")
    stock_data.index = pd.to_datetime(stock_data.index)
    return stock_data[t]

def clean_data(df):
    df = df.transpose()
    import pandas as pd
    df.index = pd.to_datetime(df.index)
    for c in df.columns:
        df[c] = pd.to_numeric(df[c],errors='coerce') 
    df = df.drop(columns = df.columns[df.isna().sum() > (len(df)/2)])
    #df = df.fillna(method='pad')
    df = df.dropna(axis = 1)
    return df.iloc[::-1]

def fetch(ticker, parts, period = 'quarter'  ):
    '''
    parts should be tuple of str.
    '''
    api_key = read_key()
    import pandas as pd
    methods = {
    #these might not accept period
    'profile' : fa.profile,
    'enterprise_value' : fa.enterprise,
    #these should not glitch
    'balance_sheet' : fa.balance_sheet_statement,
    'income_statement' : fa.income_statement,
    'cash_flow_statement' : fa.cash_flow_statement,
    'key' : fa.key_metrics,
    'financial' : fa.financial_ratios,
    'growth': fa.financial_statement_growth
    }
    data = {}
    for m in parts:
        data[m] = clean_data(methods[m](ticker, api_key, period))
    return data
    
def combine(ticker,period = 'quarter'):
    '''load and filter out metrics for a single company
    depends on fetch_all() and price()
    
    ADD: capex?
    '''
    import pandas as pd
    select = {
    #'enterprise_value':('stockPrice'),
    'key' : ('peRatio','pbRatio','capexToRevenue','debtToEquity'),
    'financial': ('netProfitMargin','returnOnCapitalEmployed'),
    'growth': ('operatingCashFlowGrowth','rdexpenseGrowth',),
    }
    data = fetch(ticker,list(select.keys()),period)
    df = pd.DataFrame()
    for t in select:
        df = pd.concat((df,data[t].loc[:,select[t]]),axis=1)
    df = pd.concat((df,price(ticker)),axis=1) #add price
    return  df

def compare(equities):
    '''Gave 503 error'''
    compare = pd.DataFrame()

    for t in equities:
        print(t)
        try:
            df = fa_wrp.fetch(t,('financial',))['financial']
            df = df.loc[:,('netProfitMargin','returnOnCapitalEmployed')]
            df = df.rename(columns = {'netProfitMargin': 'nPM {}'.format(t),'returnOnCapitalEmployed': 'ROCE {}'.format(t)})
            compare = pd.concat((compare, df), axis=0)
            print('ok')
            #time.sleep(0.5)
        except:
            print('error')
    return compare


## Show the available companies
#companies = fa.available_companies(api_key)
#
## Collect general company information
#profile = fa.profile(ticker, api_key)
#
## Collect recent company quotes
#quotes = fa.quote(ticker, api_key)
#
## Collect market cap and enterprise value
#entreprise_value = fa.enterprise(ticker, api_key)
#
## Show recommendations of Analysts
#ratings = fa.rating(ticker, api_key)
#
## Obtain DCFs over time
#dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
#dcf_quarterly = fa.discounted_cash_flow(ticker, api_key, period="quarter")
#
## Collect the Balance Sheet statements
#balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
#balance_sheet_quarterly = fa.balance_sheet_statement(ticker, api_key, period="quarter")
#
## Collect the Income Statements
#income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
#income_statement_quarterly = fa.income_statement(ticker, api_key, period="quarter")
#
## Collect the Cash Flow Statements
#cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")
#cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, api_key, period="quarter")
#
## Show Key Metrics
#key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
#key_metrics_quarterly = fa.key_metrics(ticker, api_key, period="quarter")
#
## Show a large set of in-depth ratios
#financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
#financial_ratios_quarterly = fa.financial_ratios(ticker, api_key, period="quarter")
#
## Show the growth of the company
#growth_annually = fa.financial_statement_growth(ticker, api_key, period="annual")
#growth_quarterly = fa.financial_statement_growth(ticker, api_key, period="quarter")
#
## Download general stock data
#stock_data = fa.stock_data(ticker, period="ytd", interval="1d")
#
## Download detailed stock data
#stock_data_detailed = fa.stock_data_detailed(ticker, api_key, begin="2000-01-01", end="2020-01-01")

