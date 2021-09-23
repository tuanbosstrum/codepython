#viết chương trình tìm tất cả các số chia hết cho 7 nhưng không chia hết cho 5,
#nằm trong đoạn 3201 và 2000

# so_chia = []
# i = 2000
# while(i <= 3200):
#     if(i%7 == 0 and i%5 != 0):
#         so_chia.append(i)
#     i+=1
# print(so_chia)

#day_so = []
chuoi =""
for i in range(2000, 3201):
    if(i % 7 == 0) and (i % 5 != 0):
        #day_so.append(i)
        chuoi = chuoi + ',' + str(i)
print(chuoi)