import numpy as np
print(np.random.random((3,4)))  #random函数形成的所有随机浮点数都是在0-1范围内
q = 10*np.random.random((3,4))
print(q)
a = np.floor(q)
# a = np.floor(10*np.random.random((3,4)))
print(a, a.shape) #输出a的形状
print(a.ravel()) # 输出平坦化后的a（a本身不改变）
a.shape = (6,2); print(a) # 改变a的形状
print(a.transpose()) # 输出a的转置


## 补充：reshape和resize
print()
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = a
print(b)
a.reshape((3,2))# 不改变数组本身的形状
print(a)
b.resize((3,2))# 改变数组本身形状
print(b)


