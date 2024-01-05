import requests
# Thực hiện yêu cầu HTTP đến URL 'https://jsonplaceholder.typicode.com/posts'
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# Kiểm tra xem yêu cầu thành công hay không
if response.status_code == 200:
# Nếu yêu cầu thành công, lấy dữ liệu JSON từ phản hồi
    json_data = response.json()
 # In ra màn hình thông tin các bài đăng từ dữ liệu JSON
sum =0
for post in json_data:
    sum += 1
    print("user ID bài đăng:", post['userId'])
    print("ID bài đăng:", post['id'])
    print("Tiêu đề:", post['title'])
    print("Nội dung:", post['body'])
    print("==================================")

else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
print("Tổng số bài post",sum)