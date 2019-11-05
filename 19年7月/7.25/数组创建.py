# 为什么要用numpy
#     Python中提供了list容器，可以当作数组使用。但列表中的元素可以是任何对象，因此列表中保存的是对象的指针，这样一来，
#     为了保存一个简单的列表[1,2,3]。就需要三个指针和三个整数对象。对于数值运算来说，这种结构显然不够高效。
#     Python虽然也提供了array模块，但其只支持一维数组，不支持多维数组(在TensorFlow里面偏向于矩阵理解)，也没有各种运算函数。
#     因而不适合数值运算。
#     NumPy的出现弥补了这些不足。
# （——摘自张若愚的《Python科学计算》）

import numpy as np
## 常规创建方法
a = np.array([2,3,4])
b = np.array([2.0,3.0,4.0])
c = np.array([[1.0,2.0],[3.0,4.0]])
d = np.array([[1,2],[3,4]],dtype=complex) # 指定数据类型
print(a, a.dtype)
print(b, b.dtype)
print(c, c.dtype)
print(d, d.dtype)
