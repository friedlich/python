# 在实践过程中，会经常遇到数组拼接的问题，基于numpy库concatenate是一个非常好用的数组操作函数

# 1、concatenate((a1, a2, …), axis=0)官方文档详解
# 2、Parameters参数
# 传入的参数必须是一个多个数组的元组或者列表
# 另外需要指定拼接的方向，默认是 axis = 0，也就是说对0轴的数组对象进行纵向的拼接（纵向的拼接沿着axis= 1方向）；
# 注：一般axis = 0，就是对该轴向的数组进行操作，操作方向是另外一个轴，即axis=1。
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6]])
print(b)
print(np.concatenate((a, b), axis=0))

# 传入的数组必须具有相同的形状，这里的相同的形状可以满足在拼接方向axis轴上数组间的形状一致即可

# 如果对数组对象进行 axis= 1 轴的拼接，方向是横向0轴，a是一个2*2维数组，axis= 0轴为2，b是一个1*2维数组，
# axis= 0 是1，两者的形状不等，这时会报错

# 将b进行转置，得到b为2*1维数组：
print(np.concatenate((a,b.T),axis = 1))
