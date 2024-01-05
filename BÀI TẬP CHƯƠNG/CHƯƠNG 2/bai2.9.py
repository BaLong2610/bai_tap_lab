import json
cong_ty = '{"Tên công ty": " Công ty TNHH Đất Việt",\
            "Địa chỉ": "abc Giải Phóng - Hà Nội.",\
            "1": {\
            "tên đơn vị": "Đơn vị A1",\
            "số nhân viên": 12,\
            "tỷ lệ":    "17% "     }, \
            "2": {\
            "tên đơn vị": "Đơn vị A2",\
            "số nhân viên": 30,\
            "tỷ lệ":    "44% "     }, \
            "3": {\
            "tên đơn vị": "Đơn vị A3",\
            "số nhân viên": 5,\
            "tỷ lệ":    "7% "     } ,\
            "4": {\
            "tên đơn vị": "Đơn vị A4",\
            "số nhân viên": 13,\
            "tỷ lệ":    "19% "     } ,\
            "5": {\
            "tên đơn vị": "Đơn vị A5",\
            "số nhân viên": 7,\
            "tỷ lệ":    "10% "     } }'
            
json_obj = json.loads(cong_ty)
print("tên công ty:",json_obj['Tên công ty'])
print("địa chỉ:",json_obj['Địa chỉ'])
print("-----Thống kê nhân viên theo đơn vị------")
tong = 0
for x in range(1,6):
    print(json_obj['{}'.format(x)])
    tong += json_obj['{}'.format(x)]['số nhân viên']
print('tổng nhân viên:',tong)