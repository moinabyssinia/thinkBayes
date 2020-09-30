#######################################################
#implementation of the pregnancy proportion inference
#problem
#######################################################

import pandas as pd
from scipy.special import comb

#define models
dat = pd.DataFrame(['m10', 'm20', 'm30', 'm40', 'm50', 'm60', 
'm70', 'm80','m90'], columns = ['model'])

#pTreatment: the probability that a pregnancy comes from
#the treatment group
dat['pTreatment'] = pd.DataFrame([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

dat['prior'] = pd.DataFrame([0.06, 0.06, 0.06, 0.06, 0.52, 0.06, 0.06, 0.06, 0.06])
# print(dat)

#binomial distribution for likelikhood
def binDistr(n, p, i):
    """
    function to compute the probability of 
    i successes from n trials with p probability
    of success
    """
    binProb = comb(n,i)*(p**i)*(1-p)**(n-i)
    return binProb

# print(binDistr(20,0.2, 4))

#compute likelihood
dat['likelihood'] = binDistr(20, dat['pTreatment'], 4);

#multiply likelihood with priors
dat['numerator'] = dat['likelihood']*dat['prior']

#get p(data) - all outcomes producing 4 pregnancies
#this is the sum of the numerator
prData = dat['numerator'].sum()
print(prData)

#calculate the posterior probabilities
dat['posterior'] = dat['numerator']/prData
print(dat)


