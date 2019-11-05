import numpy as np

# axis = 0：在第一维操作
# axis = 1：在第二维操作
# axis = -1：在最后一维操作
# 用维度来解释有点抽象，但确实是这样的
# 以np.argmax()
# 函数为例：

a = np.arange(24).reshape(2, 3, 4)
print(a)
print()

print(np.argmax(a, axis=0))  # 返回尺寸(3,4)
print()
print(np.argmax(a, axis=1))  # 返回尺寸(2,4)
print()
print(np.argmax(a, axis=-1))  # 返回尺寸(2,3)
