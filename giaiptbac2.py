#giải phương trình bậc 2: ax2 +bx +c =0

# import math

# """
# # Giải phương trình bậc 2: ax2 + bx + c = 0
# # @param a: hệ số bậc 2
# # @param b: hệ số bậc 1
# # @param c: số hạng tự do
# """
# def ptbac2(a, b, c):
#     # kiểm tra các hệ số
#     if (a == 0):
#         if (b == 0):
#             print ("Phương trình vô nghiệm!");
#         else:
#             print ("Phương trình có một nghiệm: x = ", + (-c / b));
#         return;

#     # tính delta
#     delta = b * b - 4 * a * c;
#     # tính nghiệm
#     if (delta > 0):
#         x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
#         x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
#         print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
#     elif (delta == 0):
#         x1 = (-b / (2 * a));
#         print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
#     else:
#         print("Phương trình vô nghiệm!");

# # Nhập các hệ số
# a = float(input("Nhập hệ số bậc 2, a = "));
# b = float(input("Nhập hệ số bậc 1, b = "));
# c = float(input("Nhập hằng số tự do, c = "));
# # Gọi hàm giải phương trình bậc 2
# ptbac2(a, b, c)

from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))