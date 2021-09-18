#Hàm DICT
sanpham = {
    "Thương hiệu" : "Apple",
    "Sạc nhanh" : True,
    "Năm sản xuất" : 2021,
    "Màu sắc" : ["Bạc", "Vàng", "Đen"]
}

print(sanpham)

print(sanpham["Thương hiệu"])
print(sanpham.keys())

sanpham.update({"Thương hiệu" : "Lenovo"})
sanpham.update({"Cân nặng" : "1.2kg"})
print(sanpham)