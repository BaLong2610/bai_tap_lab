class Stack:
    def __init__(self,arr,max) :
        self.arr = arr
        self.max = max
        self.top = -1
    def __del__(self):
        print("Stack object is being deleted")
    def push(self,x):
        if self.top == self.max:
            print("stack đã đầy")
        else:
            self.top += 1
            (self.arr).insert(self.top,x)
    def pop(self):
        if self.top <0:
            print("không thể xóa")
        else:
            self.top -= 1
            print(f"đã xóa phần tử {(self.arr).pop()} ")
            
            
    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    def isFull(self):
        if self.top == self.max - 1:
            print("is Full")
        else:
            print ("is not full")
    def count(self):
        return self.top + 1
    def print(self):
        for i in self.arr:
            print(i,end= " ")
arr = []
obj1 = Stack(arr,10)
for i in range(0,10):
    x = float(input())
    obj1.push(x)
obj1.pop()
obj1.isEmpty()
obj1.isFull()
print(obj1.count())
obj1.print()
