# 题目 将一个数组逆序输出。
# 程序分析 依次交换位置，或者直接调用reverse方法。
list = [1,10,100,1000,10000,100000,1000000]
for i in range(int(len(list)/2)):
    list[i],list[len(list)-1-i] = list[len(list)-1-i],list[i]
print('第一种解法')
print(list)

list = [1,10,100,1000,10000,100000]
print('第二种解法')
print(list.reverse()) # print(list.reverse())会出现空值None
print(list)
