import numpy as np
import matplotlib.pyplot as plt

def heatmap(plot,row_labels,col_labels,cmap_num=25):
    ''' input: np.array?
    ??
    '''
    import heatmap as h
    colors = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
    fig, ax = plt.subplots()
    im, cbar = h.heatmap(plot.T,row_labels,col_labels, ax=ax,
                       cmap=colors[cmap_num],
                       cbarlabel=" colorscheme:{}".format(colors[cmap_num]))

    fig.tight_layout()
    plt.show()
        

def correlation(df):
    '''
    using foramted heatmap
    '''
    corr = df.corr().to_numpy()
    labels = df.columns
    heatmap(corr,labels,labels)


def daily_change(df):
    '''
    
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

