#BÀI TẬP:viết chương trình tạo menu:
    #0.thoát chương trình
    #1.nhập thông tin sinh viên
    #2.sắp xếp thông tin sinh viên theo điểm
    #3.tìm kiếm sinh viên
    #4.hiển thị bảng điểm sinh viên

ds =[]
ds_diem =[]
while(0<1):
    nhap_vao = int(input("nhập menu:\
        0: thoát\
        1:thông tin sinh viên\
        2:sắp theo điểm\
        3:tìm kiếm sinh viên\
        4:hiển thị bảng điểm sinh viên"))
    if(nhap_vao == 0):
        break
    if(nhap_vao == 1):
        ten_sv = input("Nhập tên sinh viên:")
        ds.append(ten_sv)
        diem_sv = input("nhập điểm sinh viên:")
        ds_diem.append(diem_sv)
    if(nhap_vao == 2):
        ds_diem.sort()