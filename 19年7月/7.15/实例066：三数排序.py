# 题目 输入3个数a,b,c，按大小顺序输出。
# 程序分析 同实例005。
raw=[]
for i in range(5):
    x = int(input('int{}: '.format(i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i] > raw[j]:
            raw[i],raw[j] = raw[j],raw[i]
print(raw)


raw2=[]
for i in range(5):
    x = int(input('int{}: '.format(i)))
    raw2.append(x)
print(sorted(raw2))
