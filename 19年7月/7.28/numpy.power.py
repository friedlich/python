# numpy.power(x1, x2)
# 数组的元素分别求n次方。x2可以是数字，也可以是数组，但是x1和x2的列数要相同。
import numpy as np
x1 = np.arange(6)
print(x1)
print(np.power(x1,3))

x2 = [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
print(np.power(x1,x2))

x2 = np.array([[1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1]])
print(x2)
print(np.power(x1, x2))