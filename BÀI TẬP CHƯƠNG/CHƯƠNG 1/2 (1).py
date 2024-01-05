class TS:
    def inp(self,name,math,physic,chemistry):
        self.name = name
        self.math = math
        self.physic = physic
        self.chemistry = chemistry
    def out(self,ds):
        self.ds = ds
        for i in ds:
            for j in i:
                print(j,end= ' ')
    def total(self):
        tong = self.math + self.physic + self.chemistry
        return tong  

obj = TS()
ds = []
while True:
    name = input("mời nhập họ và tên: ")
    math = float(input("mời nhập điểm toán: "))
    physic = float(input('mời nhập điểm Lý: '))
    chemistry = float(input('mời nhập điểm Hóa: '))
    obj.inp(name,math,physic,chemistry)
    if obj.total()>=20:
        ds.append([name,obj.total()])
    tt = int(input("nhập tiếp? 1:tiếp "))
    if tt !=1:
        break
print('học sinh trúng tuyển : ')
obj.out(sorted(ds,key=lambda x: x[1],reverse=True))