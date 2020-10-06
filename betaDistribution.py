import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.special.basic import factorial

#get input on alpha and beta
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
    constant = factorial(alpha+beta-1)/(factorial(alpha-1)*factorial   (beta-1))
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