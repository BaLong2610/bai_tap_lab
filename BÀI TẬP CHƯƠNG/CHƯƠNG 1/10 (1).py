import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_ngan):
        super().__init__(x, y)
        self.ban_truc_lon = ban_truc_lon
        self.ban_truc_ngan = ban_truc_ngan

    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_ngan

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)

# Chương trình chính
if __name__ == "__main__":
    print("1. Elip")
    print("2. Đường Tròn")
    choice = int(input("Chọn loại hình muốn tính diện tích: "))

    if choice == 1:
        x = float(input("Nhập tọa độ x của trung tâm: "))
        y = float(input("Nhập tọa độ y của trung tâm: "))
        ban_truc_lon = float(input("Nhập bán trục lớn: "))
        ban_truc_ngan = float(input("Nhập bán trục nhỏ: "))
        elip = Elip(x, y, ban_truc_lon, ban_truc_ngan)
        dien_tich = elip.tinh_dien_tich()
    elif choice == 2:
        x = float(input("Nhập tọa độ x của trung tâm: "))
        y = float(input("Nhập tọa độ y của trung tâm: "))
        ban_kinh = float(input("Nhập bán kính: "))
        duong_tron = DuongTron(x, y, ban_kinh)
        dien_tich = duong_tron.tinh_dien_tich()
    else:
        print("Lựa chọn không hợp lệ.")
        exit(1)

    print(f"Diện tích của hình là {dien_tich}")
