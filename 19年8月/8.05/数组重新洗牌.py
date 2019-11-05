# 函数shuffle与permutation都是对原来的数组进行重新洗牌（即随机打乱原来的元素顺序）；区别在于shuffle直接在原来的数组
# 上进行操作，改变原来数组的顺序，无返回值。而permutation不直接在原来的数组上进行操作，而是返回一个新的打乱顺序的数组，
# 并不改变原来的数组。
import numpy as np
a = np.arange(12)
print(a)
np.random.shuffle(a)
print(a)
a = np.arange(12)
print(a)
b = np.random.permutation(a)
print(b)
print(a)

# np.random.shuffle(x) 现场修改序列，改变自身内容。（类似洗牌，打乱顺序）
# np.random..permutation(x) 返回一个随机排列

# 1、np.random.shuffle(x)
#现场修改序列，改变自身内容。（类似洗牌，打乱顺序）
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)
#对多维数组进行打乱排列时，默认是对第一个维度也就是列维度进行随机打乱
arr = np.arange(12).reshape(3,4)
print(arr)
#将多维数组打乱
np.random.shuffle(arr)
print(arr)

# 2、permutation(x)
# 随机排列一个序列，或者返回一个排列的范围。
# 如果x是一个多维数组，则只会沿着它的第一个索引进行随机排列。
#直接生成一个随机排列的数组
X = np.random.permutation(10)
print(X)
print(X.shape)
print(list(X))
#将数组重新排列
print(np.random.permutation([1, 4, 9, 12, 15]))

arr = np.arange(9).reshape((3, 3))
print(arr)
print(np.random.permutation(arr))
