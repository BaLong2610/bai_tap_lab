class Date:
    def __init__(self,day,month,years) :
        self.day = day 
        self.month = month
        self.years = years
    def display(self):
        print(f"{self.day}/{self.month}/{self.years}")
class Employee(Date):
    def __init__(self,name):
        self.name = name
    def date_birth(self,day,month,years):
        super().__init__(day,month,years)
    def date_in(self,day,month,years):
        super().__init__(day,month,years)
    
obj = Employee('a')
obj.out()
obj.date_birth(7,8,2023)
