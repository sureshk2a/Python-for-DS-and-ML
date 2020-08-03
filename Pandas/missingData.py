import numpy as np
import pandas as pd
from numpy.random import randn
d = {"A":[1,2,np.nan],"B":[5,np.nan,np.nan],"C":[1,2,3]}
df = pd.DataFrame(d)
print(df)
#print(df.dropna()) #drop all rows which has NaN
#print(df.dropna(axis=1)) #drop all columns with NaN value
#print(df.dropna(thresh=2)) #drop rows which has mpre than 1 NaN
#print(df.fillna("int"))
print(df.fillna(df["A"].mean()))