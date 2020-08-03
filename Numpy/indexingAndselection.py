import numpy as np
arr = np.arange(0,20)
print(arr)
print(arr[5])
print(arr[3:7])
print(arr[5:])
print(arr[:-1])
slice = arr[0:5]
slice[:] = 99
print(slice)
print(arr)
arr2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) #2d matrix
print(arr2d)
print(arr2d[1])
print(arr2d[1][2])
print(arr2d[:2,1:]) #grabing a section from 2d matrix
arrnew = np.arange(0,9)
print(arrnew>5) #condtional selection bool
print(arrnew[arrnew>3])

