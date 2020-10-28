############################################
#Gamma distribution
############################################

import pandas as pd
import numpy as np
import math as mat
import matplotlib.pyplot as plt
import seaborn as sns

def gammaDistr(alpha, beta):
    """
    this function plots the gamma distribution
    for the given values of alpha, beta, and
    x
    """
    # print("Enter alpha: ")
    # alpha = input()
    
    # print("Enter beta: ")
    # beta = input()

    # print("Enter x: ")
    # x = input()

    constant = (beta**(alpha))/mat.gamma(alpha)
    # define a continuous variable
    varx = np.arange(0,100, 0.1)
    numerator1 = varx**(alpha-1)
    getExponent = lambda x: mat.exp(-beta*x)
    numerator2 = list(map(getExponent, varx))
    gammaPDF = constant*numerator1*numerator2
    df = pd.DataFrame([varx, gammaPDF]).T
    #print(df)

    #plot 
    plt.figure()
    plt.plot(varx, gammaPDF, color = 'red')
    plt.xlabel('X')
    plt.ylabel('PDF')
    plt.grid()
    titleName = "Gamma PDF - "+"alpha = "+str(alpha)+"; beta = "+str(beta)
    plt.title(titleName)
    plt.show()

    return df

#posterior tau
n = 1;
alpha = 25;
beta = 0.5;
data = 10.2;
mu = 10.0266;

alpha = alpha + (n*0.5);
beta = beta + 0.5*(data - mu)**2;

gammaDistr(alpha, beta);

