# fin
## Remember to save pictures!!!
### Refactor:

*0.1: online data 
moex interface: fetch ticker list, fetch data, load data from disk
TODO:

http://ftp.moex.com/pub/Terminals/ASTS/Equities/MOEX_Trade_SE_QuickStart_English.pdf

https://wlm1ke.github.io/apimoex/build/html/api.html

https://towardsdatascience.com/python-comparables-financial-data-package-ee8863fe7bb1

*0.1: data cleaing
OUTLIERS:
daily change statistical analysis: mean, std, z-score. 
What to do with outliers? Regression model, mean, median, delete.
MISSING VALUES:
find number of missing values by ticker.
* procedure: impute missing values based on timeseries model preservine return and volatility
pandas fillna

*0.3: timeseries analysis.   
find frameworks  
ARIMA  (autoregression)
state space models  

*0.: pypfopt
refactor
choose optimiser
choose risk model
experiment with horizon
Read the notebooks
adjust for $
build backtesting procedures.
out of sample returns?? (another name for test set performance)

valuation: timeseries to compare to price
ML pipe ideas:
train_y(t)=pd.Series, price, train_x=[t1,t2...tn], t = ticker
train_y(t) = price, train_x = f(v,g,r), value, growth, risk
