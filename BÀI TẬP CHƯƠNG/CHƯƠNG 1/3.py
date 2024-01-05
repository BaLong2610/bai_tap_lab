class PhanSo:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phanso(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số (khác 0): "))

        while not self.kiem_tra_hop_le():
            print("Mẫu số không hợp lệ (phải khác 0). Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số (khác 0): "))

    def in_phanso(self):
        print(f"{self.tu_so}/{self.mau_so}")


if __name__ == "__main__":
    phan_so = PhanSo()
    phan_so.nhap_phanso()

    if phan_so.kiem_tra_hop_le():
        print("Phân số hợp lệ:")
        phan_so.in_phanso()
    else:
        print("Phân số không hợp lệ vì mẫu số bằng 0.")
