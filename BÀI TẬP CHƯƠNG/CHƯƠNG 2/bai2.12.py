import requests
response = requests.get("https://jsonplaceholder.typicode.com/comments?")
bai = 0
if response.status_code == 200:
    json_data = response.json()
    for post in json_data:
        bai+=1
        if bai == 4:
            break
        if post['id'] == 1:
            print("post ID:",post['postId'])
            print("ID bài đăng:",post['id'])
            print("tên bài đăng:",post['name'])
            print("nội dung bài đăng:",post['body'])
            print("==================================")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
