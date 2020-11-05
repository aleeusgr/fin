import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import tsfresh
#import apimoex
#import pypfopt
import visual as v
import util,dt

#DATA
df = dt.random_sample(sample = 0, random_state = 1)
#df = dt.outlier_sample()
cheap = df.mean()<15000

#CLEANING

#df = dt.impute(df)
#df.fillna(method = 'bfill',inplace = True)


# write a function to ID ad delete outliers
# impute missing values AFTER outliers are out, so that they dont affect the imputation process
