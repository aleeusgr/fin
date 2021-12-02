import numpy as np
import matplotlib.pyplot as plt

        
def candles(df):
    '''
    input df, index = datetime, index name = ticker, OHLC columns with names capitalized,
    
    todo: 
    candle width is set to half day, redo
    auto width of the chart?
    
    https://docs.bokeh.org/en/latest/docs/gallery/candlestick.html
    '''
    from math import pi
    import pandas as pd
    from bokeh.plotting import figure, show

    inc = df.Close > df.Open
    dec = df.Open > df.Close
    # this needs fixing
    width = 12*60*60*1000 # half day in ms

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    ticker = df.index.name
    p = figure(x_axis_type="datetime", tools=TOOLS, width=1500, title = f"{ticker} Candlestick")
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.3


    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[inc], width, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.index[dec], width, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")

    show(p)

def correlation(df):
    '''
    
    using foramted heatmap
    '''
    corr = df.corr().to_numpy()
    labels = df.columns
    from util.heatmap import heatmap_color as heatmap
    heatmap(corr,labels,labels)


def daily_change(df):
    '''
    use df.pct_change()??? 
    '''
    import pandas as pd
    import matplotlib.pyplot as plt
    diff = df.diff()
    z = ((diff - diff.mean())/diff.std())
    z = z.round(2)
    z.plot()
    plt.show()

def regression_line(df):
    ''' input - single ticker'''
    from sklearn import linear_model as lm
    from sklearn.preprocessing import PolynomialFeatures
    
    model = lm.SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)
    model = lm.LinearRegression()

    df.fillna(method = 'bfill',inplace = True)
    X = df.index.to_numpy().reshape(-1,1)
    poly_features = PolynomialFeatures(degree=3, include_bias=False)
    X_poly = poly_features.fit_transform(X)
    Y = df.to_numpy()
    model.fit(X_poly,Y)
    plt.figure()
    df.plot()
    plt.plot(X,model.predict(X_poly))
    plt.show()

'''broken'''
def scatter(df):
    '''
    input: pd.DataFrame
    like df.hist(), but with scatterpots of pairs of features
    fix color?
    '''
    import itertools
    l = list(itertools.combinations(df.drop('Date',axis=1).columns, 2))
    for i in l:
        df.plot(x=i[0],y=i[1],kind='scatter',c=df.index)
        plt.show()

