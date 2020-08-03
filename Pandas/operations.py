import numpy as np
import pandas as pd
from numpy.random import randn
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
print(df.head())
print(df["col2"].unique()) #Get unique values
print(df["col2"].nunique())
print(df["col2"].value_counts())
def times2(x):
    return x*2
print(df["col2"].apply(times2))
print(df["col2"].apply(lambda x: x*2)) #applying a function on series
print(df.columns)
print(df.index)
print(df.sort_values(by="col2"))
print(df.isnull())
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)

