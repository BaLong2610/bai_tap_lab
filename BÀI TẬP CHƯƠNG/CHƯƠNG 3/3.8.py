import numpy as np
with open(r'G:\bai_tap\chuong_3\heights.txt','r',encoding='utf-8-sig') as f:
    read = f.readlines()
    heights = list(map(lambda x:float(x),read[0].split(',')))
with open(r'G:\bai_tap\chuong_3\positions.txt','r',encoding='utf-8-sig') as f:
    read = f.readlines()
    positions = read[0].split(',')
#1
#a
np_positions = np.array(positions)
print(np_positions.dtype)
print(type(np_positions))
#b
np_heights = np.array(heights)
print(np_heights.dtype)
print(type(np_heights))
#2
mean_gk=np_heights[np_positions == 'GK']
print('chiều cao trung bình gk:',np.mean(mean_gk))
#3
other_heights = np_heights[np_positions != 'GK']
print('chiều cao trung bình vị trí khác',np.mean(other_heights))
#4
players = np.zeros(len(np_positions), dtype={'names':('position', 'height'), 'formats':('U5', 'f8')})
players['position'] = np_positions
players['height'] = np_heights
print(players)
#5
sorted_players =np.sort(players,order='height')
print(sorted_players)
print('vị trí có chiều cao cao nhất',sorted_players[-1])
print('vị trí có chiều cao thấp nhất',sorted_players[0])