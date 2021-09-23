tong_tien = int(input("Bạn đã có bao nhiêu tiền:"))
so_nguoi_dong_gop = 0
while tong_tien <= 100000:
    dong_gop = int(input("Mời bạn góp tiền uống cà phê:"))
    tong_tien += dong_gop

    if tong_tien > 100000: continue
    
    so_nguoi_dong_gop +=1
else:
    print("Đã có đủ tiền mời mọi người uống cà phê, quyên gì nữa!")
print("Sao kê: Đã quyên góp được{} từ {} người!".format(tong_tien, so_nguoi_dong_gop))