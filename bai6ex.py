##lớp và đối tượng
# class Student:
#     def printInfo(self):
#         print(f"full name: {self.name}")

# st1 = Student()
# st1.name = "Admirals"
# st1.printInfo()

##phương thức khởi tạo(hàm dựng):__init__()
# class Sinh_vien(object):
#     #def __init__(self):
#     #    self.s=""
#     def getString(self):
#         self.s=input('Nhập tên: ')
#     def printString(self):
#         print(self.s.upper())
# str=Sinh_vien()
# str.getString()
# str.printString()

##phương thức trả về(return)
# class Car:
#     def __init__(self, year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
#     def old(self):
#         return 2022 - self.year
# mycar = Car(2021, "Mazda", "Mazda2 - Sport")
# print("My car is {} year old".format(mycar.old()))

##từ khóa del
##kế thừa
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def printage(self):
        print(self.age)
st = student("Hoàng", "Tuấn")
st.printname()
st.age = 20
st.printage()
########################################################
