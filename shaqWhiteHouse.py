import pandas as pd
import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt


#define binomial distribution function
#binomial distribution for likelikhood
def binDistr(n, p, i):
    """
    function to compute the probability of 
    i successes from n trials with p probability
    of success
    """
    binProb = comb(n,i)*(p**i)*(1-p)**(n-i)
    return binProb


print("Enter the number of trials: ")
num = input()
print("Enter the number of successes: ")
success = input()
print("Enter the probability of successes: ")
p = input()

print(binDistr(num, p, success))


#create a dataframe for trial and probability
dat = pd.DataFrame(columns=['success', 'prob']);
dat['success'] = np.arange(num+1);
getProb = lambda x: binDistr(num, p, x)
dat['prob'] = pd.DataFrame(list(map(getProb, dat['success'])))
print(dat)

#plot the binomial distribution
plt.figure()
plt.bar(dat['success'], dat['prob'])
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.show()