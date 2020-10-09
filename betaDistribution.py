#######################################
#this script plots beta dsitribution
#with inputs for alpha and beta
#######################################

import math as mat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#get input on alpha and beta
##the bigger the alpha is relative
##to beta, the more we shift the
##weight of the curve to the right
print("Enter alpha: ")
alpha = input()

print("Enter beta: ")
beta = input()

# print("Enter number of trials (n): ")
# n = input()

# print("Enter number of successes (x): ")
# x = input()

def betaDistr(alpha, beta):
    '''
    plot beta distribution
    '''
    dat = pd.DataFrame(columns=['p', 'prior'])
    dat['p'] = np.arange(0,1, 0.01)
    constant = mat.gamma(alpha+beta)/(mat.gamma(alpha)*mat.gamma(beta))
    print("constant = ", constant)
    getProb = lambda x: constant*(x**(alpha-1))*(1-x)**(beta-1)
    dat['prior']= pd.DataFrame(list(map(getProb, dat['p'])))
    print(dat)

    #plot density
    plt.figure()
    plt.plot(dat['p'], dat['prior'])
    plt.xlabel('P')
    plt.ylabel('Probability Density')
    plt.title('Beta Distribution')
    plt.show()

    return dat

dat = betaDistr(alpha, beta)

#######################################
#compute posterior manually
#######################################
#case where n = 1; x = 0
#likelihood = 1-prior

dat['likelihood'] = 1- dat['p']
dat['numerator'] = dat['prior']*dat['likelihood']
dat['denominator'] = dat['numerator'].sum()
dat['posterior'] = dat['numerator']/dat['denominator']
print(dat.head(31))

# #plot density
# plt.figure()
# plt.plot(dat['p'], dat['posterior'])
# plt.xlabel('P')
# plt.ylabel('Probability Density')
# plt.title('Posterior Distribution')
# plt.show()

#######################################
#compute posterior using conjugate 
#shortcuts
#######################################
#code goes here