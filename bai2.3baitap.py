import random

hoten = input("Nhập họ tên:")
msv = "PXU" + str(random.randint(1, 99))
ngaysinh = input("Ngày sinh:")
dem = int(len(msv))
if dem == 1:
    msv = "PXU" + "0" + msv
else:
    msv = "PXU" + msv
diemqt = int(input("Nhập điểm quá trình:"))
diemthi = int(input("Nhập điểm thi:"))
tong = (diemqt+diemthi)/2

#print(msv2, hoten, ngaysinh, tong)
#print(f"""
          #Họ tên: {hoten}
          #Mã SV: {msv2}
          #Ngày sinh: {ngaysinh}
          #tổng điểm: {tong}
#""")
print("Họ tên:", hoten)
print("Mã Sinh Viên:", msv)
print("Ngày sinh:", ngaysinh)
print("Điểm quá trình:", diemqt)
print("Điểm thi:", diemthi)
print("Tổng điểm:", tong)
print(msv2, hoten, ngaysinh, tong)