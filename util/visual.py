import numpy as np
import matplotlib.pyplot as plt

        

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

