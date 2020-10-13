############################################
#Poisson distribution
############################################

import pandas as pd
import numpy as np
import math as mat
from itertools import permutations
import matplotlib.pyplot as plt
import seaborn as sns

#lambda is the mean and variance 
#of the gamma distribution
print("Enter lambda: ")
pLambda = input()

print("Enter k: ")
pK = input()

def poissonDistr(pLambda, pK):
    """
    plots the poisson distribution
    for a given value of lambda
    and k

    k: the number of events
    """
    dat = pd.DataFrame(columns=['pK', 'p'])
    dat['pK'] = np.arange(pK+1)
    # numerator = lambda x: ((pLambda**x)*(mat.exp(-1*pLambda)))
    numerator = lambda x,y: ((x**y))
    denominator = lambda x: mat.factorial(x)
    print(dat['pK'])
    dat['numerator'] = pd.DataFrame(numerator(pLambda, dat['pK']))
    dat['denominator'] = pd.DataFrame(list(map(denominator, dat['pK'])))
    dat['p'] = dat['numerator']/dat['denominator']
    print(dat)

    #plot the distribution
    sns.set_context("notebook", font_scale=1.5)
    plt.figure()
    plt.plot(dat['pK'], dat['p'])
    plt.ylabel('P')
    plt.xlabel('K')
    plt.show()

poissonDistr(pLambda, pK)