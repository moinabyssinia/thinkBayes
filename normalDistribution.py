############################################
#Normal Distribution PDF 
############################################

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

normalDistr(8, 1)