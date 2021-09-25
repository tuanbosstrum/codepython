# def hello(name , age):
#     print("xin chào tôi là {} - {} tuổi".format(name , age))
#     print("Tôi đang ở Việt Nam")
# hello("Hoàng Đế" , 20)
# hello(age=30, name="Emperor")

# def dientich(x , y):
#     s = x * y
#     print("Diện tích:" + str(s))
# def nhap():
#     a = int(input("Nhập x:"))
#     b = int(input("nhập y:"))
#     dientich(a , b)
# nhap()

# ##tuple
# def hello2(*name):
#     print("Số lượng tham số: {}".format(len(name)))
#     for x in name:
#         print(f"xin chào {x}")
# hello2("Bro")
# hello2("bro", "bruh", "dude")
# hello2()

# def thongtinsinhvien(**sinhvien):
#     if "hoten" in sinhvien.keys():
#         print("Họ tên: {}".format(sinhvien["hoten"]))
#     if  "diachi" in sinhvien.keys():
#         print("Địa chỉ: {}".format(sinhvien["diachi"]))
#     if "tuoi" in sinhvien.keys():    
#         print("Tuổi: {}".format(sinhvien["tuoi"]))
#     if "namsinh" in sinhvien.keys(): 
#         tuoi = 2021 - sinhvien["namsinh"]
#         print("Tuổi: {}".format(tuoi))
# thongtinsinhvien(hoten = "bro", diachi = "20 Lê Lợi", tuoi = 20)
# thongtinsinhvien(hoten = "bruhh", diachi = "20 Lê Lợi")
# thongtinsinhvien(hoten = "dude")
# thongtinsinhvien(hoten = "dude", diachi = "1 ĐBP", namsinh = 2000 , gioitinh = "nam")
# print("---------------------------------------------------")

# ##Tham số
# #Tham số mặc định:
# def hello4(name ="Hey bro"):
#     print(f"Hello, my name is {name}")
# hello4()
# hello4("bruh.... ")
# #Truyền list vào hàm:
# def hello5(dssinhvien):
#     for sv in dssinhvien:
#         print(f"hello: {sv}")
# dssinhvien = ["Hạnh", "Hoàng", "Hoa", "Huệ"]
# hello5(dssinhvien)

##Hàm ẩn danh tí hon(lambda)
#cú pháp lambda arguments: expression
x = lambda a: a + 10
y = lambda a , b: a+ b
print(x(20))
print(y(100,999))
#Hàm lambla ẩn danh trong hàm khác:
def ham_mu(n):
    x = lambda x: x ** n
    return x
ket_qua = ham_mu(5)
print(ket_qua(10))

def luythua(n):
    x = lambda x: x ** n
    return x

tinhmu = luythua(3)
y = tinhmu(10)
print(y)

tinhmu = luythua(2)
print(tinhmu(3))







