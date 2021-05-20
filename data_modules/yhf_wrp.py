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

def per(p = 'q'):
    '''expand period '''
    period = {'y': 'yearly', 'q':'quarterly'}
    return period[p]

def doc(p = 'q', d = 'is'):
    '''Utility:
    p for period, d for document, 
    returns proper string for yhf.fetch(t,'fin')''' 
    document = {'is':'income_statement', 'cf':'cash_flow', 'bs':'balance_sheet'}
    return '{}_{}'.format(per(p),document[d])

def pe_pb(ticker):
    d = fetch(ticker,'summary')
    return (d['trailingPE'], d['priceToBook'])

def CE(ticker, period = 'q'):
    '''Capital Employed'''
    fin = fetch(ticker,'fin')
    CE = fin[doc(period,'bs')].loc['totalAssets'] - fin[doc(period,'bs')].loc['totalLiab']
    return CE

def asset_price(ticker,p = 'q'):
    '''price: market cap to capital employed'''
    cap = fetch(ticker, 'summary')['marketCap']
    ce = CE(ticker,p).iloc[-1]
    return cap/ce

def ROCE(ticker,p = 'q'):
    '''profitability: return on capital emploed'''
    fin = fetch(ticker,'fin')
    ebit = fin[doc(p,'is')].loc['ebit']
    ce = CE(ticker, p)

    return ebit/ce

def net_profit_margin(ticker, p = 'q'):
    '''profitability'''
    fin = fetch(ticker, 'fin')
    fin = fin[yhf.doc(p,'is')]
    return fin.loc['netIncome'] / fin.loc['totalRevenue']

def debt_to_equity(ticker, p = 'q'):
    '''financing'''
    fin = fetch(ticker,'fin')
    bs = fin[doc(p,'bs')]
    return bs.loc['totalLiab'] / (bs.loc['totalAssets'] - bs.loc['totalLiab'])

def RnD(ticker, p = 'q'):
    '''investemnt:R&D
    should I normalize?
    '''
    f = fetch(ticker,'fin')[doc(p,'is')]
    return f.loc['researchDevelopment']

def investment(ticker, p = 'q'):
    fin = fetch(ticker, 'fin')[doc(p,'cf')]
    return fin.loc['investments']
    
def revenue_earnings(ticker, p='q'):
    data = fetch(ticker,'earnings')
    return data['{}_revenue_earnings'.format(per(p))]

def surpriseEPS(t):
    # EPS over expectations 
    df = pd.DataFrame()
    df[t] = data['an'](t)['Earnings History'].iloc[3,1:]
    df[t] = df[t].str.replace('%','')
    df[t] = df[t].str.replace(',','')
    df[t] = df[t].astype(float)
    return df
