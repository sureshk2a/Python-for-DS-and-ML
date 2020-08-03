import numpy as np
import random
list = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(list)) #2d matrix
print(np.arange(0,8)) #1d matrix
print(np.ones((5,5))) #2d matrix filled with 1
print(np.linspace(0,3,5))
print(np.eye(4)) #Identitty matrix
print(np.random.rand(6)) #Galaxian distribution
print(np.random.randn(2,2)) #Normal ditribution
print(np.random.randint(1,200,10))
arr = np.arange(0,14)
print(arr)
ranarr = np.random.randint(0,14,10) #10 counts of random numbers between 0 and 14
print(ranarr)
print(arr.reshape(2,7))
print(arr.max())
print(arr.min())
print(arr.argmax())
print(arr.argmin())
print(arr.dtype)
