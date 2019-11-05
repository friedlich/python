# np.expand_dims:用于扩展数组的形状
# 原始数组：
import numpy as np
a = np.array([[[1,2,3],[4,5,6]]])
print(a)
print(a.shape)
# np.expand_dims(a, axis=0)表示在0位置添加数据,转换结果如下：
b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)
# np.expand_dims(a, axis=1)表示在1位置添加数据,转换结果如下：
c = np.expand_dims(a, axis=1)
print(c)
print(c.shape)
# np.expand_dims(a, axis=2)表示在2位置添加数据,转换结果如下：
d = np.expand_dims(a, axis=2)
print(d)
print(d.shape)
# np.expand_dims(a, axis=3)表示在3位置添加数据,转换结果如下：
e = np.expand_dims(a, axis=3)
print(e)
print(e.shape)
# 能在(1,2,3)中插入的位置总共为4个，再添加就会出现以下的警告，要不然也会在后面某一处提示AxisError

