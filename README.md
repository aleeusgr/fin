# fin
## Remember to save pictures!!!
### Refactor:
1. I need to remake this repo ground up. The original idea was to do a task, now I want to use it as a personal module.

*0.1: online data 
moex interface: fetch ticker list, fetch data, load data from disk
TODO:
visualise whole portfolio
add RUBUSD, oil, (other instruments??)
pandas webreader: implement if needed


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

PLANNED:
*0.5: pypfopt
refactor
choose optimiser
choose risk model
experiment with horizon
Read the notebooks
adjust for $
build backtesting procedures.
out of sample returns?? (another name for test set performance)
