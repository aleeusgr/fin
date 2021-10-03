# Binomial distribution.
import os
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer # use @ to measure function runtime

def draw(whites = 3, size = 6):
    '''Run a grether experiment draw
    returns a tuple of outcomes
    whites - number of whites in a box
    size - size of the box

    '''
    draw = ()
    for i in range(size): 
        draw += np.random.binomial(1,whites/size),
    return draw

def sample(whites = 3, size = 6, runs = 100):
    '''
    generates probability distribution for given conditions 
    rename runs -> resolution

    '''
    sample = np.zeros((runs , size))
    for i in range(len(sample)):
        sample[i] = draw(whites,size)
    plt.hist(sample.sum(axis = 1),bins = size)
    #plt.imshow(sample().T)
    plt.show()
    return sample


def sim(P_strong = 0.4,strong = 4, size = 6, runs = 1000):
    
    '''overengeneered''' 
    sample = ()
    regimes = ()
    for r in range(runs):
        regime = np.random.binomial(1, P_strong) 
        if regime == 0:
            x = draw(3,6)
        else:
            x = draw(4,6)
        sample += x,
        regimes += regime,
    x = np.asarray(sample)
    
    plt.hist(x.sum(axis=1),bins = size)
    plt.show()
    return x

x = sim()
