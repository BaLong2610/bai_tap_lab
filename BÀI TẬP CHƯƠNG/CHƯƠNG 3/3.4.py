import numpy as np
#1
arr_zeros = np.zeros(10,dtype = int)
arr_zeros[4] = 1
print(arr_zeros)
#2
arr_h = np.arange(10,25)
print(arr_h[::-1])
#3
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = np.array([i for i in arr_k if i!=0])
print(arr_l)
#4
arr_l = np.append(arr_l,10)
arr_l = np.append(arr_l,20)
print(arr_l)
#5
arr_l = np.insert(arr_l,5,100)
print(arr_l)
#6
arr_l = np.delete(arr_l,[0,1,2])
print(arr_l)