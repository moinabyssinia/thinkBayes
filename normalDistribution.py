########################################################
#Normal Distribution PDF 

##conjugate analytic solution
#mu posterior = [tau0*mu0 + tau(sum(x))]/(tau0 + n*tau)
#######################################################

import pandas as pd
import numpy as np
import math as mat
import matplotlib.pyplot as plt
import seaborn as sns

def normalDistr(mu, sigma):
    """
    this function plots the normal
    distribution for the given mu 
    and sigma values for 101 data
    points
    """
    #get the 100 sequential data points
    x = np.arange(mu-10, mu+10.1, 0.1)
    print(x.mean())
    constant = 1/(((2*mat.pi)**0.5)*sigma)
    getExp = lambda x: mat.exp(-((x - mu)**2)/(2*sigma*sigma))
    pdf = pd.DataFrame(list(map(getExp, x)))*constant
    normalPDF = pd.concat([pd.DataFrame(x), pdf], axis = 1)
    print(normalPDF)

    #plot
    plt.figure()
    plt.plot(x, pdf, color = "olive")
    plt.xlabel('x')
    plt.ylabel('PDF')
    plt.title('Normal Distribution | mu = {} | sigma = {}'.format(mu, sigma))
    plt.grid()
    plt.show()


def conjugateNormal(tau0, tau, mu0, x):
    """
    this function computes the mu posterior
    based on the normal-normal conjugate 
    solution
    """
    numerator = tau0*mu0 + tau*(sum(x))
    denominaor = tau0 + len(x)*tau
    mupost = numerator/denominaor
    taupost = denominaor
    print("muPost =", mupost)
    return mupost, taupost

#get prior
normalDistr(12, 4)

#get posterior
muPost = conjugateNormal(0.31, 0.25, 10.56, [7,10,10,8,4])[0]
tauPost = conjugateNormal(0.31, 0.25, 10.56, [7,10,10,8,4])[1]
normalDistr(muPost, tauPost)

