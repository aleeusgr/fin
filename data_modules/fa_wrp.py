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

class Company:
    def __init__(self,ticker):
        self.ticker = ticker        
        self.data = {} 
    
    def fetch(self,period = 'quarter'):
        '''period is set to be 'quarter' in the code, change'''
        self.data = {
        'profile' : fa.profile(self.ticker, api_key),
        #'entreprise_value' : fa.enterprise(self.ticker, api_key),

        #'balance_sheet_quarterly' : fa.balance_sheet_statement(self.ticker, api_key, period="quarter"),
        #'income_statement_quarterly' : fa.income_statement(self.ticker, api_key, period="quarter"),
        #'cash_flow_statement_quarterly' : fa.cash_flow_statement(self.ticker, api_key, period="quarter"),
        #'key_metrics_quarterly' : fa.key_metrics(self.ticker, api_key, period="quarter"),
        #'financial_ratios_quarterly' : fa.financial_ratios(self.ticker, api_key, period="quarter"),
        #'growth_quarterly ': fa.financial_statement_growth(self.ticker, api_key, period="quarter")
        }

def offset_correlation(df, offset = -1):
    '''broken'''
    corr = {}
    for c in df.columns:
        corr[c] = df['adjclose'].corr(df[c].shift(offset))

    return pd.Series(corr)


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

#roe = key_metrics_annually.loc['roe']
#pe_ratio = key_metrics_annually.loc['peRatio']
#pb_ratio = key_metrics_annually.loc['pbRatio']
#ROCE = financial_ratios_annually.loc['returnOnCapitalEmployed']
#pfcf = financial_ratios_annually.loc['freeCashFlowPerShare']
#industry = profile.loc['industry'][0]
