# A 1-D iterator over the array. /将数组转换为1-D的迭代器 /
# flat返回的是一个迭代器，可以用for访问数组每一个元素

import numpy as np
a = np.arange(4).reshape(2,2)
print(a)
print(a.flat)
for i in a.flat:
    print(i)
#迭代器可以用list进行输出
print(list(a.flat))
print(type(a.flat))#返回类型为 numpy.flatiter
#可以用索引对迭代器进行引号
print(a.flat[3])