# mean() 函数定义：
# numpy.mean(a, axis, dtype, out，keepdims )

# mean()函数功能：求取均值
# 经常操作的参数为axis，以m * n矩阵举例：

#     axis 不设置值，对 m*n 个数求均值，返回一个实数
#     axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
#     axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵

import numpy as np
# 例子：
# 1. 数组的操作
a = np.array([[1, 2], [3, 4]])
print(a)
print(np.mean(a))
print(np.mean(a, axis=0))  # axis=0，计算每一列的均值
print(np.mean(a, axis=1)) # 计算每一行的均值 

# 2.矩阵的操作
num1 = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
print(num1)
num2 = np.mat(num1)
print(num2)
print(np.mean(num2))  # 对所有元素求均值
print(np.mean(num2,0))  # 压缩行，对各列求均值
print(np.mean(num2,1))  # 压缩列，对各行求均值
