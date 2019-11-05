# 从左到右，从上向下
# 一维数组打印成行，二维数组打印成矩阵，三维数组打印成矩阵列表
import numpy as np
print(np.arange(1,6,2))
print(np.arange(12).reshape(3,4)) # 可以改变输出形状
print(np.arange(24).reshape(2,3,4))# 2页，3行，4列
