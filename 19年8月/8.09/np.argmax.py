# np.argmax：返回沿轴最大值的索引值
import numpy as np

# 一维数组
A = np.arange(6).reshape(2,3)
print(A)

# 返回一维数组中最大值的索引值：
B = np.argmax(A)
print(B)
C = np.argmax(A, 1)
print(C)
B = np.argmax(A, 0)
print(B)
# 二维数组
# 要索引的数组：
E = np.array([[4,2,3],[2,3,4],[3,2,2]])
print(E)
print(E.shape)

F = np.argmax(E, axis=0)
print(F)

G = np.argmax(E, axis=1)
print(G)
