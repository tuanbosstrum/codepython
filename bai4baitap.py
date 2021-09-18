i = 0
thanh_vien = []
while(i<5)
    nhap = input("Nhập thành viên:")
    thanh_vien.append(nhap)
    i = i +1

#SỬA THÔNG TIN
vi_tri = int(input("Nhập vị trí muốn sửa:"))
thanh_vien[vi_tri] = input("Nhập họ tên muốn sửa:")
print(thanh_vien)