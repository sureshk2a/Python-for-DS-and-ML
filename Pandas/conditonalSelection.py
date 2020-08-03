import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
booldf = df>0
#print(df[booldf]) #Fill with NAN where condtion is false
#print(df.W>0)
#print(df[df.W>0]) # get the row which column value is greater than 0
#print(df[df['W']<0])
print(df[df['W']>0][['Y','X']])
print(df[(df['W']>0) & (df['Y']>1)]) #check 2 conditions in dataframe using & , ||
#print(df.reset_index()) #reset index as a column name index, and assign default index
newind = "CA NY WY OR CO".split()
print(newind)
df["States"] = newind
print(df)
print(df.set_index('States')) #set an existing column as the index
print(df)


