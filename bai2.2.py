import random

n = random.randint(1,3)
ban_chon = int(input("Đoán 1 số từ 1 đến 3:"))
if n == ban_chon:
    print("Chúc mừng bạn đã chọn đúng!")
else:
    print("Số bạn chọn ra là:", n)

#n = 10
#n = "Chuỗi"
print(n)
