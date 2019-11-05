# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#方法1  自由搏击
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)

#方法2  截拳道
rlist = range(1,5)
nlist = [i*100+j*10+k for i in rlist for j in rlist if j!=i for k in rlist if k!=i and k!=j]
print(nlist,len(nlist))

#方法3  概率版
import random
nlist = []
a = range(1,5)
print(a)
for i in range(100):
    n = random.sample(range(1,5),3)
    # rint(len(range(5)))
    if n not in nlist:
        nlist.append(n)
print(nlist,len(nlist))

#方法4 截拳道+集合
rlist = set(range(1,5))
nlist = [i*100+j*10+k for i in rlist for j in rlist-{i}  for k in rlist-{i,j} ]
print(nlist,len(nlist))

#方法5 道法·斗转星移·itertools模块
from itertools import permutations as permu
nlist = list(permu(range(1,5),3))
print(nlist,len(nlist))