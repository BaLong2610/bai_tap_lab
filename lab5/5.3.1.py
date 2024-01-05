import threading
import time

counter = 0  # Define the global counter variable

class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(4):
            time.sleep(2)
            counter += 1  # Increase the counter without using a lock
            print(f"Counter has increased to: {counter}")

def main():
    global counter  # Ensure the global counter is accessible within the main function
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

if __name__ == "__main__":
    main()
