from data_modules.yhf_wrp import fetch, doc, per

def pe_pb(ticker, p = 'q'):
    d = fetch(ticker,'summary')
    return (d['trailingPE'], d['priceToBook'])

def CE(ticker, period = 'q'):
    '''Capital Employed'''
    fin = fetch(ticker,'fin')
    CE = fin[doc(period,'bs')].loc['totalAssets'] - fin[doc(period,'bs')].loc['totalLiab']
    return CE

def asset_price(ticker,p = 'q'):
    '''price: market cap to capital employed'''
    cap = fetch(ticker, 'summary')['marketCap'] # cap should be a timeseries for proper values, now only latest value is valid
    ce = CE(ticker,p)#.iloc[-1] # for last value of CE
    df = cap/ce
    return df

def ROCE(ticker,p = 'q'):
    '''profitability: return on capital emploed'''
    fin = fetch(ticker,'fin')
    ebit = fin[doc(p,'is')].loc['ebit']
    ce = CE(ticker, p)

    return ebit/ce

def net_profit_margin(ticker, p = 'q'):
    '''profitability'''
    fin = fetch(ticker, 'fin')
    fin = fin[doc(p,'is')]
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
    
def earnings(ticker, p='q'):
    '''for momentum'''
    data = fetch(ticker,'earnings')
    x = data['{}_revenue_earnings'.format(per(p))]
    x.index = x['date']
    #x.drop(columns = ('date'), inplace = True)
    return x['revenue']


def surpriseEPS(t):
    # EPS over expectations 
    df = pd.DataFrame()
    df[t] = data['an'](t)['Earnings History'].iloc[3,1:]
    df[t] = df[t].str.replace('%','')
    df[t] = df[t].str.replace(',','')
    df[t] = df[t].astype(float)
    return df
