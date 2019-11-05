import numpy as np
print(np.zeros(5,))  #生成包含5个元素的零矩阵
# print(np.zeros(,5))
print(np.zeros((5,),dtype=np.int))  #生成包含5个元素的零矩阵，且各元素为整形
print(np.zeros((5),dtype=np.int))
print(np.zeros((2,1)))  #生成2行1列的零矩阵
print(np.zeros((2,1),dtype=np.int))
print(np.zeros((2,2)))  #生成2行2列的零矩阵
print(np.zeros((2,2),dtype=np.int))
print(np.zeros((2,),dtype=[('x','i4'), ('y','i4')]))  ## custom dtype

# 用法：zeros(shape, dtype=float, order='C')
# 返回：返回来一个给定形状和类型的用0填充的数组；
# 参数：
# shape:形状
# dtype:数据类型，可选参数，默认numpy.float64
# order:可选参数，c代表与c语言类似，行优先；F代表列优先
# dtype类型：
# t ,位域,如t4代表4位
# b,布尔值，true or false
# i,整数,如i8(64位）
# u,无符号整数，u8(64位）
# f,浮点数，f8（64位）
# c,浮点负数，
# o,对象，
# s,a，字符串，s24
# u,unicode,u24

