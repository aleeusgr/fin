import pandas as pd
from yahoo_fin import stock_info as si

def fetch(ticker, what = 'price'):
    ''' what: str, fin, an, price, summary'''
    data = {
    'fin' : si.get_financials, #includes balance sheet,income, cash flow
    'an': si.get_analysts_info,
    'balance': si.get_balance_sheet,
    'cash flow':si.get_cash_flow,
    'price'   : si.get_data,
    'summary' : si.get_quote_data,
    'earnings': si.get_earnings,
    'earn_ist': si.get_earnings_history,#crap formatting
    }
    return data[what](ticker)

def link(p = 'y', d = 'is'):
    '''Utility: p for period, d for document, produces proper string for yhf.fetch(t,'fin')''' 
    period = {'y': 'yearly', 'q':'quarterly'}
    document = {'is':'income_statement', 'cf':'cash_flow', 'bs':'balance_sheet'}
    return '{}_{}'.format(period[p],document[d])


def pe_pb(ticker):
    d = fetch(ticker,'summary')
    return (d['trailingPE'], d['priceToBook'])

def CE(ticker, period = 'y'):
    '''Capital Employed'''
    fin = yhf.fetch(ticker,'fin')
    CE = fin[link(period,'bs')].loc['totalAssets'] - fin[link(period,'bs')].loc['totalLiab']
    return CE

def ROCE(ticker,period = 'y'):
    fin = yhf.fetch(ticker,'fin')
    ebit = fin[link(period,'is')].loc['ebit']
    CE = fin[link(period,'bs')].loc['totalAssets'] - fin[link(period,'bs')].loc['totalLiab']

    return ebit/CE

def surpriseEPS(t):
    # EPS over expectations 
    df = pd.DataFrame()
    df[t] = data['an'](t)['Earnings History'].iloc[3,1:]
    df[t] = df[t].str.replace('%','')
    df[t] = df[t].str.replace(',','')
    df[t] = df[t].astype(float)
    return df
