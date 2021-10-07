# P(j, strong)=P(strong|j)P(j), whereP(j)=P(j|strong)P(strong)+P(j|weak)P(weak)
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def grether_disribution(P_is_strong = 4/6,n_whites = 4, length = 6):
    '''Generate custom distribution for modified structure of Grether experiment
    BAAP ch4
    P_is_strong - chances in first phase
    n_whites - number of white choices in stronge regime 
    length - size of the distribution

    returns Pj, Pstrong, Pweak
    '''
    P_is_weak = 1 - P_is_strong

    p_strong = n_whites/length
    p_weak = 0.5

    n=length
    k = np.arange(0,length+1,1)
    strong,weak = (binom.pmf(k,n,p) for p in [p_strong,p_weak])
    P = strong*P_is_strong + weak*P_is_weak
    return P,strong,weak
         

for Ps in np.arange(0,1,0.1):
    
    dist = grether_disribution(Ps)
    for i in dist:
        plt.plot(i)
    
    plt.show()



#        print(k,p,binom.pmf(k, n, p))

    
#fig, ax = plt.subplots(1, 1)
# calc 4 moments:
#mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
#x = np.arange(binom.ppf(0.01, n, p),
#
#              binom.ppf(0.99, n, p))
#ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')

#ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=6, alpha=0.5)
# frozen PMF
#rv = binom(n, p)

#ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,

#        label='frozen pmf')

#ax.legend(loc='best', frameon=False)

#plt.show()
