class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kiem_tra_tam_giac(self):
        return (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a)

    def loai_tam_giac(self):
        if self.a == self.b == self.c:
            return "Tam giác đều"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Tam giác cân"
        elif self.kiem_tra_tam_giac_vuong():
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

    def kiem_tra_tam_giac_vuong(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

# Chương trình chính
if __name__ == "__main__":
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    tam_giac = TamGiac(a, b, c)

    if tam_giac.kiem_tra_tam_giac():
        print("Đây là một", tam_giac.loai_tam_giac())
    else:
        print("Không phải tam giác hợp lệ.")
