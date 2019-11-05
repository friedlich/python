# 有列表[0，1，2，3，4，5，6，7，8，9]，要求把列表里面的每个值加1

# 方法1:循环
info = [0,1,2,3,4,5,6,7,8,9]
b = []
for index,i in enumerate(info):
    print(index)
    # print(i+1)
    b.append(i+1)
print(b)
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中。

for index in info:
    info[index] += 1
    # print(info)
print(info)

##  enumerate(sequence, [start=0])
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中。

### 对比
# 普通的 for 循环
i = 0
seq = ['one','two','three']
for element in seq:
    print(i,seq[i])
    i+=1
# for 循环使用 enumerate
seq = ['one','two','three']
for i,element in enumerate(seq):
    print(i,element)
# 明显符合Python的简洁特征



