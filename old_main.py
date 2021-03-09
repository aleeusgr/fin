import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import tsfresh
#import apimoex
#import pypfopt
import visual as v
import util,dt
'''
add usd, oil(?)
'''

#MY DATA
df = dt.random_sample(sample = 9, random_state = 2)
#df = dt.outlier_sample()
cheap = df.mean()<15000
isna = df.isna().sum()
df = df.iloc[len(df.index)-180:]
#CLEANING
#df.fillna(method = 'ffill',inplace = True)


