import numpy as np

# numpy.eye(N,M=None, k=0, dtype=<type 'float'>)

# 关注第一个第三个参数就行了

# 第一个参数：输出方阵（行数=列数）的规模，即行数或列数

# 第三个参数：默认情况下输出的是对角线全“1”，其余全“0”的方阵，如果k为正整数，则在右上方第k条对角线全“1”其余全“0”，
# k为负整数则在左下方第k条对角线全“1”其余全“0”。
print(np.eye(2, dtype=int))
print(np.eye(3, k=1))

y = np.ones((1,12),dtype=np.int)
print(y)
print(y.shape)
x = np.arange(1,73).reshape(2,3,3,4)
print(x.shape)
x = x.reshape(-1)
print(x)
print(x.shape)
print(y.reshape(-1))
print(y.reshape(-1).shape)
print()
C = 6
Y = np.eye(C)
print(Y)
# Y = np.eye(C)[120]
# print(Y)

# y = np.eye(C)[y.reshape(-1)].T
print(np.eye(C)[y.reshape(-1)]) # 后面的[]是索引的效果，一行一行索引，把1放到索引位置处
y = np.eye(C)[y.reshape(-1)].T
print(y.shape)
print(y)