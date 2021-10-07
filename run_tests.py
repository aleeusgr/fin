import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer
from util import tests
#from compdata import comp_data as dmd
#from yahoo_fin import stock_info as si
from data_modules import yhf_wrp as yhf
#from util.util import compare

#TODO: tinkoff_api!!!

tests.portfolio_test() # heatmap broken, missing dependency
tests.metrics_test(period = 'y') # debug needed.

