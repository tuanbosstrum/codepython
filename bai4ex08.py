tong_tien = int(input("Bạn đã có bao nhiêu tiền:"))
so_nguoi_dong_gop = 0
while tong_tien <= 100000:
    dong_gop = int(input("Mời bạn góp tiền uống cà phê:"))
    tong_tien += dong_gop
    so_nguoi_dong_gop +=1
else:
    print("Đã có đủ tiền mời mọi người uống cà phê, quyên gì nữa!")
print("Đã quyên góp được{} từ {} người!".format(tong_tien, so_nguoi_dong_gop))