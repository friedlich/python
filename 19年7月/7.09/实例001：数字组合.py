# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析 遍历全部可能，把有重复的剃掉
total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(j!=k)and(i!=k):
                print(i,j,k)
                total += 1
print(total)

# 简便方法 用itertools中的permutations即可
import itertools
sum = 0
a = [1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum += 1
print(sum)

