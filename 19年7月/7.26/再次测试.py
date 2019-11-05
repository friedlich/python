import numpy as np
a = np.arange(1,6)
print(a)
print(a.shape)
b = np.array([[1,2,3,4,5]])
print(b)
print(b.shape)

c = [1,2,3,4,5]
print(c)
print(type(c))
d = np.squeeze(c)   # 牛逼，这东西还能将列表转化为数组
print(d)
print(type(d))

print(12288**0.5)