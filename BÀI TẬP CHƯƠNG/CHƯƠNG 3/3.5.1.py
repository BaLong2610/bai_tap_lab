import numpy as np

with open(r'chuong_3\heights_1.txt','r',encoding='utf-8-sig') as f:
    height =f.readlines()
    height = list(height[0].split(','))
    list_height=list(map(lambda x:float(x),height))
print(list_height)
with open(r'G:\bai_tap\chuong_3\weights_1.txt','r',encoding='utf-8-sig') as f:
    weight =f.readlines()
    weight = list(weight[0].split(','))
    list_weight=list(map(lambda x:float(x),weight))
#1
arr_height = np.array(list_height)
#2
arr_weight = np.array(list_weight)
#3
arr_height_m = np.array([i *0.0254 for i in arr_height])
#4
arr_weight_kg  =np.array([i* 0.453592 for i in arr_weight])
#5
arr_BMI = np.array([])
for i in range(0,len(arr_height)):
    arr_BMI = np.append(arr_BMI,arr_weight_kg[i]/(arr_height_m[i]*arr_height_m[i]))
#6
print(arr_weight_kg[50])
#7
arr_height_m_100 = arr_height_m[100:111]
#8
bmi_less_than_21 = arr_BMI[arr_BMI<21]
print("Các cầu thủ có BMI < 21:", bmi_less_than_21)
#9
average_height = np.sum(arr_height_m)/arr_height_m.size
print("chiều cao trung bình:",average_height)
average_weight = np.sum(arr_weight_kg)/arr_weight_kg.size
print("cân nặng trung bình",average_weight)
#10
max_height = np.sort(arr_height_m)[-1]
print("chiều cao lớn nhất",max_height)
max_weight = np.sort(arr_weight_kg)[-1]
print("cân nạng cao nhất",max_weight)
#11
min_height = np.sort(arr_height_m)[0]
print("chiều cao nhỏ nhất",min_height)
min_weight = np.sort(arr_weight_kg)[0]
print("cân nạng nhỏ nhất",min_weight)