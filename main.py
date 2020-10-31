'''IDEA: a portfolio analyser for MOEX
0.1: data
moex interface: fetch ticker list, fetch data, load data from disk
pandas webreader:
0.2: pypfopt
refactor
choose optimiser
choose risk model
out of sample returns??
experiment with period
Read the notebooks
check price regularization
adjust for $
outliers

0.3: probabilistic model?
0.4 timeseries analysis
 research 'timeseries analysis'
 search 'timeseries plotting'
'''
#import requests
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import tsfresh
#import apimoex
#import pypfopt
import visual as v
import moex
import util


df = util.random_sample(sample=10)
#v.plot_correlation(df)
#util.calculate(df)


