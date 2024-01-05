class Date:
    def __init__(self,day,month,years) :
        self.day = day 
        self.month = month
        self.years = years
    def display(self):
        print(f"{self.day}/{self.month}/{self.years}")
    def next(self):
        def is_leap(year):
            return year %4 ==0 and(year%100!=0 or year%400==0)
        if self.day == 29 and self.month == 2 and is_leap(self.years) == 1:
            self.day = 1
            self.month += 1
        elif self.day == 28 and self.month == 2 and is_leap(self.years) ==0:
            self.day = 1
            self.month +=1
        if self.month in [1,3,5,7,8,10,12] :
            if self.day <= 30:
                self.day +=1
            if self.day ==31:
                self.day = 1
                self.month +=1
                if self.month ==12:
                    self.years +=1 
                    self.month = 1
        if self.month in [4,6,9,11]:
            if self.day <=29:
                self.day += 1
                self.month +=1
            if self.day == 30:
                self.day =1
                self.month +=1
        print(f"next day: {self.day}/{self.month}/{self.years}")
obj = Date(8,12,2023)
obj.display()
obj.next()