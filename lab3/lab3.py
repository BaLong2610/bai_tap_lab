#lab3.1
import pandas as pd
from pandas import ExcelFile

#1 Đọc file stocks1.csv và lưu vào DataFrame stocks1
stocks1 = pd.read_csv("stocks1.csv")
print(stocks1.head()) #2 Hiển thị 5 dòng đầu tiên của stocks1.
print(stocks1.dtypes) #3 Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1.
print(stocks1.info()) #4 Xem thông tin tổng quan (info) của stocks1
#lab3.2
null_check = stocks1.isnull().any()
#1 Kiểm tra xem trong stocks1 có dữ liệu Null nào không.
print("Kiểm tra dữ liệu Null trong stocks1:")
print(null_check) 
#2 Thay thế dữ liệu Null ở cột high bằng giá trị trung bình của cột high.
mean_high = stocks1['high'].mean()
stocks1['high'].fillna(mean_high, inplace=True)
#3 Thay thế dữ liệu Null ở cột low bằng giá trị trung bình của cột low.
mean_low = stocks1['low'].mean()
stocks1['low'].fillna(mean_low, inplace=True)
#4 Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Nu
print("Thông tin tổng quan sau khi xử lý: ")
print(stocks1.info())
#lab3.3 :
#1: Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv("stocks2.csv")

#2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

#3: Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks['average_price'] = stocks[['open', 'high', 'low', 'close']].mean(axis=1)

#4: Hiển thị 5 dòng đầu tiên của kết quả
print("5 dòng đầu tiên của kết quả:")
print(stocks.head())
#Đọc file companies.csv vào DataFrame companies
companies = pd.read_csv("companies.csv")

#lab3.4
#Hiển thị 5 dòng đầu tiên của companies
print("5 dòng đầu tiên của DataFrame companies:")
print(companies.head())

#Kết hợp stocks và companies dựa trên cột chung là 'symbol'
merged_data = pd.merge(stocks, companies, on='symbol')

#Tính giá đóng cửa (close) trung bình cho mỗi công ty
average_close_by_company = merged_data.groupby('name')['close'].mean().reset_index()

#Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình của mỗi công ty:")
print(average_close_by_company.head())
#Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột date và symbol làm chỉ mục
stocks.set_index(['date', 'symbol'], inplace=True)

#Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, cho mỗi mã chứng khoán
daily_avg = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
}).reset_index()

#Sắp xếp dữ liệu theo ngày và mã chứng khoán
daily_avg.sort_values(by=['date', 'symbol'], inplace=True)

#Hiển thị kết quả cho 5 ngày đầu tiên
print("Kết quả cho 5 ngày đầu tiên:")
print(daily_avg.head())
#lab3.5
#Tạo Pivot Table từ DataFrame stocks
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')

#Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
pivot_table['total_volume'] = stocks.groupby('symbol')['volume'].sum()

#Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
pivot_table = pivot_table.sort_values(by='total_volume', ascending=False)

#Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
top_5_symbols = pivot_table.head(5)
print("Kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(top_5_symbols)
