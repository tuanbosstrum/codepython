#chương trình 10 số ngẫu nhiên từ 1->10 và lưu vào dict, với keys số nguyên từ 1->10

import random

i = 1
so_ngau_nhien = {}
while(i<=10):
    a = random.randint(1,10)
    so_ngau_nhien.update({str(i) : a})
    i += 1
print(so_ngau_nhien)