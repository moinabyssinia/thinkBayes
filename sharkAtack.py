############################################
#Shark Attack Problem 
############################################

from gammaDistribution import gammaDistr
from poissonDistribution import poissonDistr
import math as mat
import pandas as pd
import matplotlib.pyplot as plt

#based on the observed 5 events 
#I chose alpha = 5, and beta = 0.8
#gammaPDF is the prior now
pK = 5
gammaPDF = gammaDistr(alpha = 5, beta = 0.8)
# print(gammaPDF.head(60))

#get likelihood 
denominator = mat.factorial(pK)
gammaPDF['numerator'] = pd.DataFrame(list(map(lambda y: (y**pK)*(mat.exp(-y)), gammaPDF[0])))
gammaPDF['likelihood'] = gammaPDF['numerator']/denominator
print(gammaPDF.head(60))

#plot likelihood
plt.figure()
plt.plot(gammaPDF[0], gammaPDF['likelihood'], color = 'purple')
plt.xlabel('Lambda')
plt.ylabel('Likelihood')
plt.grid()
titleName = "Likelihood - "+"K = "+str(pK)+";"
plt.title(titleName)
plt.show()

#get posterior
#p(data) = evidence == sum(likelihood*prior)
evidence = (gammaPDF['likelihood']*gammaPDF[1]).sum()
gammaPDF['posterior']= (gammaPDF['likelihood']*gammaPDF[1])/evidence
print(gammaPDF)

#plot posterior
plt.figure()
plt.plot(gammaPDF[0], gammaPDF['posterior'], color = 'blue')
plt.xlabel('Lambda')
plt.ylabel('Posterior')
plt.grid()
titleName = "Posterior Distribution"
plt.title(titleName)
plt.show()