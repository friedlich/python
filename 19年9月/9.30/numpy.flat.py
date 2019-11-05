import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(x)
print(x.flat)
print(list(x.flat))
print(x.flat[3])  # 返回重组后的一维数组下标为3的元素
print(x.T)
print(x.T.flat[3])  # 返回x的转置重组后的一维数组下标为3的元素
x.flat = 3  # 将数组的元素均变为3
print(x)
x.flat[[1, 4]] = 1  # 将数组重组后的一维数组小标为1,4的元素变为1
print(x)
