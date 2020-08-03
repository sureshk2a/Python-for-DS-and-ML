import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['W']) #Get the series from data frame - method1
print(df.W) #method2
print(df[['W','Z']])
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new',axis=1)
print(df.loc['A'])
print(df.iloc[2])
print(df.loc[['A','B'],['Y','Z']])





