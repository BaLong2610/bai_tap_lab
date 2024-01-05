import numpy as np
#1
with open(r'G:\bai_tap\chuong_3\baseball_2D.txt','r',encoding='utf-8-sig') as f:
    a= f.readlines()
    a = a[0]
    a = a.replace('[',' ')
    a = a.replace(']',' ')
    a= list(map(lambda x:int(x),a.split(',')))
np_baseball =  np.array(a).reshape((1015,2))
print(type(np_baseball))
#2
print(np_baseball[49,:])
#3
np_weight = np.array([np_baseball[:,1]])
print(np_weight)
#4
print(np_baseball[123][0])
#5
print('chiều cao trung bình:',np.sum(np_baseball[:,0])/np_baseball.size)
print('cân nặng trung bình:',np.sum(np_baseball[:,1])/np_baseball.size)
#6
# 6. Bạn nhận xét gì về mối tương quan giữa chiều cao và cân nặng của các cầu thủ: có/không có tương quan, tương quan thuận/nghịch.
correlation = np.corrcoef(np_baseball[:,0],np_baseball[:,1])[0, 1]
if correlation > 0:
    correlation_type = "tương quan thuận"
elif correlation < 0:
    correlation_type = "tương quan nghịch"
else:
    correlation_type = "không có tương quan"
print(correlation_type)