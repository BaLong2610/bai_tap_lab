import sqlite3

# Kết nối đến cơ sở dữ liệu sanpham.db (nếu không tồn tại, sẽ tự động tạo mới)
conn = sqlite3.connect('sanpham.db')
cursor = conn.cursor()

# Tạo bảng sản phẩm nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sanpham (
        Id INTEGER PRIMARY KEY,
        Ten TEXT NOT NULL,
        Gia REAL NOT NULL,
        SoLuong INTEGER NOT NULL
    )
''')
conn.commit()

def hien_thi_danh_sach_san_pham():
    # Hiển thị tất cả sản phẩm từ CSDL
    cursor.execute('SELECT * FROM sanpham')
    sanphams = cursor.fetchall()
    if not sanphams:
        print("Không có sản phẩm nào.")
    else:
        for sanpham in sanphams:
            print(sanpham)

def them_san_pham_moi():
    # Thêm sản phẩm mới vào CSDL
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    so_luong = int(input("Nhập số lượng sản phẩm: "))

    cursor.execute('INSERT INTO sanpham (Ten, Gia, SoLuong) VALUES (?, ?, ?)', (ten, gia, so_luong))
    conn.commit()
    print("Đã thêm sản phẩm thành công.")

def tim_kiem_san_pham_theo_ten():
    # Tìm kiếm sản phẩm theo tên
    ten_tim_kiem = input("Nhập tên sản phẩm cần tìm: ")
    cursor.execute('SELECT * FROM sanpham WHERE Ten LIKE ?', ('%' + ten_tim_kiem + '%',))
    sanphams_tim_kiem = cursor.fetchall()
    if not sanphams_tim_kiem:
        print("Không tìm thấy sản phẩm nào có tên '{}'.".format(ten_tim_kiem))
    else:
        for sanpham in sanphams_tim_kiem:
            print(sanpham)

def cap_nhat_thong_tin_san_pham():
    # Cập nhật thông tin sản phẩm dựa trên ID
    id_san_pham = int(input("Nhập ID sản phẩm cần cập nhật thông tin: "))
    gia_moi = float(input("Nhập giá mới: "))
    so_luong_moi = int(input("Nhập số lượng mới: "))

    cursor.execute('UPDATE sanpham SET Gia = ?, SoLuong = ? WHERE Id = ?', (gia_moi, so_luong_moi, id_san_pham))
    conn.commit()
    print("Đã cập nhật thông tin sản phẩm thành công.")

def xoa_san_pham():
    # Xóa sản phẩm khỏi CSDL dựa trên ID
    id_san_pham = int(input("Nhập ID sản phẩm cần xóa: "))
    cursor.execute('DELETE FROM sanpham WHERE Id = ?', (id_san_pham,))
    conn.commit()
    print("Đã xóa sản phẩm thành công.")

# Menu chương trình
while True:
    print("\n---- MENU ----")
    print("1. Hiển Thị Danh Sách Sản Phẩm")
    print("2. Thêm Sản Phẩm Mới")
    print("3. Tìm Kiếm Sản Phẩm Theo Tên")
    print("4. Cập Nhật Thông Tin Sản Phẩm")
    print("5. Xóa Sản Phẩm")
    print("6. Thoát chương trình")
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        hien_thi_danh_sach_san_pham()
    elif lua_chon == '2':
        them_san_pham_moi()
    elif lua_chon == '3':
        tim_kiem_san_pham_theo_ten()
    elif lua_chon == '4':
        cap_nhat_thong_tin_san_pham()
    elif lua_chon == '5':
        xoa_san_pham()
    elif lua_chon == '6':
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
