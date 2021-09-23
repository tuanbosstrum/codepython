for x in range(5):
    print(x)
    #vòng lặp ép nó kết thúc
    if x == 2: break
else:
    print("Vòng lặp kết thúc tại x={}".format(x))

danh_sach_sinh_vien = ["An","Khánh","Minh","Lĩnh","Tỵ"]
for sinh_vien in danh_sach_sinh_vien:
    print(sinh_vien)

for char in danh_sach_sinh_vien[1]:
    print(char)

tong = 0
for i in range(11):
    tong = tong + i
print(f"Tổng từ 0-10 là: {tong}")