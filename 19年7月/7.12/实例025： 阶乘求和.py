# 题目 求1+2!+3!+…+20!的和。
# 程序分析 1+2!+3!+…+20!=1+2(1+3(1+4(…20(1))))  1+2!+3!+4!+5!=1+2(1+3(1+4(1+5(1))
print(1+2*(1+3*(1+4*(1+5*(1)))))
res=1
for i in range(5,1,-1):
    res = 1 + i*res
print(res)
