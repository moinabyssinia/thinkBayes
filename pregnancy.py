import pandas as pd

#define models
dat = pd.DataFrame(['m10', 'm20', 'm30', 'm40', 'm50', 'm60', 
'm70', 'm80','m90'], columns = ['model'])
#pTreatment: the probability that a pregnancy comes from
#the treatment group
dat['pTreatment'] = pd.DataFrame([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(dat)