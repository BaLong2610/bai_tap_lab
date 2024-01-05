import numpy as np
#1
with open(r'chuong_3\heights_1.txt','r') as f:
    read = len(f.read())
    f.seek(0)
    list_height = []
    for i in range(read):
        a = f.read(2)
        if a == '':
            break
        list_height.append(a)
        if a == '':
            break
    list_height =[int(i) for i in list_height]
arr_height = np.array(list_height)
#2
with open(r'G:\bai_tap\chuong_3\weights_1.txt','r') as f:
    read = len(f.read())
    f.seek(0)
    list_weight = []
    for i in range(read):
        a = f.read(3)
        if a == '':
            break
        list_weight.append(a)
        if a == '':
            break
    list_weight =[int(i) for i in list_weight]
arr_weight =np.array(list_weight)
#3
arr_height_m = np.array([i*0.0254 for i in arr_height])
#4
arr_weight_kg = np.array([i*0.453592 for i in arr_weight])
#5
arr_BMI = np.array([])
for i in range(0,len(arr_height)-1):
    arr_BMI = np.append(arr_BMI,arr_weight_kg[i]/(arr_height_m[i]*arr_height_m[i]))
#6
print(arr_weight_kg[50])
#7
arr_height_m_100 = arr_height_m[100:111:1]
print(arr_height_m)

#8
name =[]
with open(r"G:\bai_tap\chuong_3\name.text",'r') as n:
    lenght = len(n.read())
    n.seek(0)
    for i in range(0,lenght+1):
        length2 = len(n.readline())

        read = n.read(length2-1)
        name.append(read)
print(name)
BMI = [i for i in arr_BMI if i <21]
for i in BMI:
    print('các cầu thủ có BMI<21: ',i)