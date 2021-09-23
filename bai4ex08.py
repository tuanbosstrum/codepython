tong_tien = 0
so_nguoi_dong_gop = 0
while tong_tien <= 100000:
    dong_gop = int(input("Mời bạn góp tiền uống cà phê:"))
    tong_tien += dong_gop
    so_nguoi_dong_gop +=1
print("Đã quyên góp được{} từ {} người!".format(tong_tien, so_nguoi_dong_gop))