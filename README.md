# fin
## Remember to save pictures!!!
### Refactor:

#IDEAS:
# 3. compute and display metrics: CAPE = price_current / MovingAverageEPS(period), ROCE = return on capital employed, 
# 4. stock price: endogenous vs exogenous factors?? 

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


ML pipe ideas:
train_y(t)=pd.Series, price, train_x=[t1,t2...tn], t = ticker // factor analysis
train_y(t) = price, train_x = f(v,g,r), value, growth, risk  // systems model
