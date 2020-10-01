#######################################################
#implementation of the pregnancy proportion inference
#problem
#######################################################

import pandas as pd
import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

#define models
dat = pd.DataFrame(['m10', 'm20', 'm30', 'm40', 'm50', 'm60', 
'm70', 'm80','m90'], columns = ['model'])

#pTreatment: the probability that a pregnancy comes from
#the treatment group
dat['pTreatment'] = pd.DataFrame([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

dat['prior'] = pd.DataFrame([0.06, 0.06, 0.06, 0.06, 0.52, 0.06, 0.06, 0.06, 0.06])
# print(dat)

# #modify priors here
# dat['prior'] = 1/9.0;

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

#check sum of probabilities in priors/posteriors
print(dat['posterior'].sum())
print(dat['prior'].sum())

#plot barplots
fig, ax = plt.subplots(1,3, figsize = (16,4))


#priors
ax[0].bar(np.arange(len(dat['prior'])), dat['prior'])
ax[1].bar(np.arange(len(dat['prior'])), dat['likelihood'])
ax[2].bar(np.arange(len(dat['prior'])), dat['posterior'])

#modify tick labels
plt.sca(ax[0])
plt.title('Prior')
plt.xticks(np.arange(len(dat['prior'])), dat['model'])

plt.sca(ax[1])
plt.xticks(np.arange(len(dat['prior'])), dat['model'])
plt.title('LIkelihood')

plt.sca(ax[2])
plt.xticks(np.arange(len(dat['prior'])), dat['model'])
plt.title('Posterior')


# plt.bar(np.arange(len(dat['prior'])), dat['prior'])
# plt.xticks(np.arange(len(dat['prior'])), dat['model'])
# plt.show()

# #likelihood
# plt.bar(np.arange(len(dat['prior'])), dat['prior'])
# plt.xticks(np.arange(len(dat['prior'])), dat['model'])
# plt.show()

# #posterioirs
# plt.bar(np.arange(len(dat['prior'])), dat['prior'])
# plt.xticks(np.arange(len(dat['prior'])), dat['model'])


plt.show()