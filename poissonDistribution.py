############################################
#Poisson distribution
############################################

import pandas as pd
import numpy as np
import math as mat
import matplotlib.pyplot as plt
import seaborn as sns

#lambda is the mean and variance 
#of the poisson distribution
print("Enter lambda: ")
pLambda = input()

print("Enter k: ")
pK = input()

def poissonDistr(pLambda, pK):
    """
    plots the poisson distribution
    for a given value of lambda
    and k

    k: the number of occurances
    """
    dat = pd.DataFrame(columns=['pK', 'p'])
    dat['pK'] = np.arange(pK+1)
    # numerator = lambda x: ((pLambda**x)*(mat.exp(-1*pLambda)))
    # numerator = lambda y: pLambda**y
    denominator = lambda x: mat.factorial(x)
    print(dat['pK'])
    dat['numerator'] = pd.DataFrame(list(map(lambda y: (pLambda**y)*(mat.exp(-1*pLambda)), range(pK+1))))
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