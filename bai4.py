danh_sach_lop = ["Khánh","Hải","Dương","Thơ"]
dia_chi = list(("176 Trần Phú","70 Lê Lợi","20 Nguyễn Huệ","1 Bà Triệu"))
print(dia_chi)
print(danh_sach_lop)

#Cập nhật giá trị
danh_sach_lop[1] = "Duy"
dia_chi[1] = "2 Bà Triệu"

#lấy từ số đầu
print(danh_sach_lop[0] + "- Địa chỉ:" +dia_chi[0])

#lấy địa chỉ sau đuôi
print(danh_sach_lop[-1] + "- Địa chỉ:" +dia_chi[-1])

#lấy giá trị khoảng đầu và cuối(Không lấy giá trị đầu và cuối)
print(danh_sach_lop[1:3])

