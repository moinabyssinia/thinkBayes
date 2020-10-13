###################################
#test script
###################################
import numpy as np
import pandas as pd

product = lambda x,y : x*y
x = np.arange(10)
y = np.arange(1,11)
print(pd.DataFrame(product(x,y)))