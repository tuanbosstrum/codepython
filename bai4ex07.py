#viết đoạn chương trình nhập vào 3 số, so sánh và tìm ra số lớn nhất

import random

# print("Nhập vào số thứ nhất: ")
a = float(input("Nhập vào số thứ nhất: "))
 
# print("Nhập vào số thứ hai: ")
b = float(input("Nhập vào số thứ hai: "))
 
# print("Nhập vào số thứ ba: ")
c = float(input("Nhập vào số thứ ba: "))

if a>b and a>c:
    print("a lớn nhất")
elif b>c and b>a:
    print("b lớn nhất")
else:
    print("c lớn nhất")