# 题目 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析 首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
list = [1,10,100,1000,10000,100000]
n = int(input('insert a number: '))
list.append(n)
for i in range(len(list)-1):
    if list[i] >= n:
        for j in range(i,len(list)):
            list[j],list[-1] = list[-1],list[j]
            break
print(list)

