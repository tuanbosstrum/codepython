hoten = "Hoàng Tuấn"
diachi = """
    176 Trần Phú
    Phường Phước Vĩnh
    Thành Phố Huế
    Thừa Thiên-Huế
"""
hoten2 = "Gruppenführer"
address = '1 "rue de" Paris'

print(hoten.upper())
print(hoten2, address)

#Input và output trong Python:
#input
tuoi = int(input("Nhập tuổi:"))
#output
print("tuổi là:", str(tuoi))
#print(hoten.title() * 3)
print(f"{hoten} có tuổi là: {tuoi}")
print("{} có tuổi là: {}".format(hoten, tuoi))