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


def betaDistr(alpha, beta):
    '''
    plot beta distribution
    '''
    dat = pd.DataFrame(columns=['p', 'probDensity'])
    dat['p'] = np.arange(0,1, 0.01)
    constant = mat.gamma(alpha+beta)/(mat.gamma(alpha)*mat.gamma(beta))
    print("constant = ", constant)
    getProb = lambda x: constant*(x**(alpha-1))*(1-x)**(beta-1)
    dat['probDensity']= pd.DataFrame(list(map(getProb, dat['p'])))
    print(dat)

    #plot density
    plt.figure()
    plt.plot(dat['p'], dat['probDensity'])
    plt.xlabel('P')
    plt.ylabel('Probability Density')
    plt.title('Beta Distribution')
    plt.show()

betaDistr(alpha, beta)