###################################
#test script
###################################
import numpy as np
import pandas as pd
import math as mat

pK = 20
terms = 20

dat = pd.DataFrame(columns=['pK', 'p'])
dat['pK'] = np.arange(pK+1)
# getFactorial = lambda x: mat.factorial(x)
# dat['p'] = pd.DataFrame(list(map(getFactorial, dat['pK'])))
# getPower = lambda x: 10**x
# dat['p'] = list(map(getPower, range(terms)))
# print(dat)

# use anonymous function 
result = list(map(lambda x: 10 ** x, dat['pK'])) 

print(result)