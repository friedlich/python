# 题目 对10个数进行排序。
# 程序分析 同实例005。

raw = []
for i in range(10):
    num = int(input('int{}：'.format(i)))
    raw.append(num)
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i] > raw[j]: # raw[i]要放前面，因为第一个raw[i]是raw[0]，是依照raw[i]来排序的
            raw[i],raw[j] = raw[j],raw[i]
print(raw)
