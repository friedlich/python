import numpy as np
a = np.logspace(0, 0, 10)
# 让开始点为0，结束点为0，元素个数为10
print(a)

b = np.logspace(0, 9, 10)
print(b)

c = np.logspace(0, 9, 10, base=2)
print(c)

d = np.logspace(0, 2, 3, base=2)
print(d)

range_n = np.logspace(0, 2, num=3).astype(int)
print(range_n)