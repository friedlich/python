# 题目 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# 程序分析 无。
li=[3,2,5,7,8,1,5]

print(li.index(max(li)))
print(li.index(min(li)))
print(li[0])
print(li[li.index(max(li))])
index = li.index(max(li))
li[0],li[index] = li[index],li[0]
# li[0],li[li.index(max(li))] = li[li.index(max(li))],li[0]
# li[0],li[4] = li[4],li[0]
print(li)
li[-1],li[li.index(min(li))] = li[li.index(min(li))],li[-1]
print(li)
