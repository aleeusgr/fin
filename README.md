# fin
## Remember to save pictures!!!
main.py: new functionality
    dt.py: data handling
        data_web
        data_moex
    visual.py: visualisation
        heatmap.py: 
    util.py - 

*0.1: data loading 
moex interface: fetch ticker list, fetch data, load data from disk
TODO:
add RUBUSD, oil, (other instruments??)
pandas webreader: implement if needed
*0.1.1: data cleaing
OUTLIERS:
daily change statistical analysis: mean, std, z-score. 
What to do with outliers? Regression model, mean, median, delete.
MISSING VALUES:
find number of missing values by ticker.
* procedure: impute missing values based on timeseries model preservine return and volatility
pandas fillna

*0.2: pypfopt
refactor
choose optimiser
choose risk model
experiment with horizon
Read the notebooks
adjust for $
build backtesting procedures.
out of sample returns?? (another name for test set performance)

*0.3: timeseries analysis.   
find frameworks  
ARIMA  
state space models  

