# 题目 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析 判断素数的方法：用一个数分别去除2到sqrt(这个数的开方)，如果能被整除，则表明此数不是素数，反之是素数。 
# 用else可以进一步简化代码.
flag=0
if flag:
    print('6')
flag=1
if flag:
    print('66')
if 0:
    print('666')
if 1:
    print('6666')

import math
for i in range(101,201):
    flag=0
    for j in range(2,round(math.sqrt(i)+1)):
        if i%j == 0:
            flag=1
            break
    if flag:
        continue
    print(i)

print('\nSimplify the code with "else"\n')
import math
for i in range(101,201):
    for j in range(2,round(math.sqrt(i)+1)):
        if i%j == 0:
            break
    else:
        print(i)


# print(round(math.sqrt(111)))

# print(round(80.23456, 2))  #该方法返回 x 的小数点四舍五入到n个数字
# print(round(100.000556, 4))
# print(round(100.000556, 3))
# print(round(-100.000056, 3))  
