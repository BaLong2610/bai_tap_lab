class HinhBinhHanh:
    def __init__(self, a, b, chieu_cao):
        self.a = a
        self.b = b
        self.chieu_cao = chieu_cao

    def tinh_chu_vi(self):
        return 2 * (self.a + self.b)

    def tinh_dien_tich(self):
        return self.a * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Chương trình chính
if __name__ == "__main__":
    print("1. Hình Bình Hành")
    print("2. Hình Chữ Nhật")
    print("3. Hình Vuông")
    choice = int(input("Chọn loại hình muốn tính chu vi và diện tích: "))

    if choice == 1:
        a = float(input("Nhập độ dài cạnh a: "))
        b = float(input("Nhập độ dài cạnh b: "))
        h = float(input("Nhập chiều cao: "))
        hinh = HinhBinhHanh(a, b, h)
    elif choice == 2:
        chieu_dai = float(input("Nhập chiều dài: "))
        chieu_rong = float(input("Nhập chiều rộng: "))
        hinh = HinhChuNhat(chieu_dai, chieu_rong)
    elif choice == 3:
        canh = float(input("Nhập độ dài cạnh: "))
        hinh = HinhVuong(canh)
    else:
        print("Lựa chọn không hợp lệ.")
        exit(1)

    chu_vi = hinh.tinh_chu_vi()
    dien_tich = hinh.tinh_dien_tich()

    print(f"Chu vi của hình là {chu_vi}")
    print(f"Diện tích của hình là {dien_tich}")
