import numpy as np
#1
arr = np.full((3,3),True,dtype= bool)
arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_1D.reshape((3,3))
print('arr kích thước 3x3',arr_2D)
#2
column1 = list(arr_2D[:,0])
arr_2D[:,0] = arr_2D[:,2]
arr_2D[:,2] = column1
print('chuyển cột 1 sang cột 3 và ngược lại:',arr_2D)
#3
row1 = list(arr_2D[0,:])
arr_2D[0,:] = arr_2D[1,:]
arr_2D[1,:] = row1
print('chuyển dòng 1 sang dòng 2 và ngược lại:',arr_2D)
#4
arr_2D = arr_2D[::-1,::1]
print('đảo ngược các dòng của arr_2D:',arr_2D)
#5
arr_2D = arr_2D[::1,::-1]
print('đảo ngược các cột của arr_2D',arr_2D)
#6
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
if np.isnan(arr_2D_null).any() :
    print('có giá trị rỗng')
else:
    print('không có giá trị rỗng')
#7
arr_2D_no_null = np.nan_to_num(arr_2D_null)
print('sau khi thay thế',arr_2D_no_null)