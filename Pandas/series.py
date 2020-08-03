import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
#print(arr)
d = {'a':10,'b':20,'c':30}
#print(d)
#print(pd.Series(data=my_data)) #show the data with serial number starting from 0 as default
#print(pd.Series(data=my_data,index=labels)) #cutom serial number for data
ser1 = pd.Series(data=[1,2,3,4],index=['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series(data=[1,2,3,4],index=['USA','Germany','Italy','Japan'])
print(ser2)
print(ser1['USA'])
print(ser1+ser2)