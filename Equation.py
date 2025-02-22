import numpy as np

with open('data.csv', 'r', encoding='utf-8') as f:
    s = f.read()
    j = s.replace("\n", ",")
    d = j.split(",")
U = d[1:21:2]
I = d[:21:2]

print(U, I)

lll = 1

while lll < 10:
    kkk = I[lll::10]
    nnn = U[lll::10]
    number = float(kkk[0])
    number2 = float(nnn[0])
    R = number2 / number
    # print(number2, number)
    # for u in kkk:
    #     ttt = i/u
    #     print(ttt)
    lll += 1
    # print(kkk)
    print(R//0.01 / 100)
# R = U / I

# print()