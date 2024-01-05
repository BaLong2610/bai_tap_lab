import threading
import time
class SimpleTask:
    def run_task(self):
        for i in range(1, 4): print('Đã in lần thứ :',i) 
        time.sleep(1)
def main():
# Tạo và khởi chạy nhiều threads
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)] 
    for task in tasks:
        task.start() 
    for task in tasks:
        task.join()
if __name__ == "__main__":
    main()