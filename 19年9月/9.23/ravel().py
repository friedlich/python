# numpy中的ravel()、flatten()、squeeze()都有将多维数组转换为一维数组的功能，区别：
# ravel()：如果没有必要，不会产生源数据的副本
# flatten()：返回源数据的副本
# squeeze()：只能对维数为1的维度降维


# 另外，reshape(-1)也可以“拉平”多维数组

import numpy as np
arr = np.arange(12).reshape(3, 4)
print(arr)
print(arr.ravel())
print(arr.flatten())

arr1 = np.arange(3).reshape(3,1)
print(arr1)
print(np.squeeze(arr1))
print(arr.reshape(-1))


