# 思路：numpy提供了numpy.append(arr, values, axis=None)函数。对于参数规定，要么一个数组和一个数值；要么两个数组，不能三个及以上数组直接append拼接。
import numpy as np

a = np.arange(5)
print(a)
print(np.append(a, 10))
print(a)

b = np.array([11, 22, 33])
print(b)
print(np.append(a, b))

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.append(a, b))
# numpy的数组没有动态改变大小的功能，numpy.append()函数每次都会重新分配整个数组，并把原来的数组复制到新数组中