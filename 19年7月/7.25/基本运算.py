## 元素级运算
import numpy as np
a = np.array([1,2,3,4])
b = np.arange(4)
print(a, b)
print(a-b)
print(a*b)
print(a**2)
print(2*np.sin(a))
print(a>2)
print(np.exp(a)) # 指数

## 矩阵运算（二维数组）
print()
a = np.array([[1,2],[3,4]]) # 2行2列
# b = np.arange(6).reshape((2,-1)) # 2行3列
b = np.arange(6).reshape((2,3)) # 2行3列
print(a)
print(b)
print(a.dot(b)) # 2行3列
print(np.dot(a,b))
# print(np.dot(b,a)) # 这样会报错 ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0) 未对齐

## 非数组运算，调用方法
print()
a = np.random.randint(0,5,(2,3))
print(a)
print(a.sum(),a.sum(axis=1),a.sum(1),a.sum(axis=0),a.sum(0)) # axis用于指定运算轴（默认全部，可指定0或1）
print(a.min(),a.max(axis=1),a.mean(axis=1)) # axis = 0: 按列计算，axis = 1: 按行计算
print(a.cumsum(1)) # 按行计算累积和


