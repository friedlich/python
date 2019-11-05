import numpy

print('数组的合并与拆分')
x = numpy.array([[1, 2, 3], [4, 5, 6]])
y = numpy.array([[7, 8, 9], [10, 11, 12]])
print(numpy.concatenate([x, y], axis = 0))
# 竖直组合 [[ 1  2  3][ 4  5  6][ 7  8  9][10 11 12]]
print(numpy.concatenate([x, y], axis = 1))  
# 水平组合 [[ 1  2  3  7  8  9][ 4  5  6 10 11 12]]
print('垂直stack与水平stack')
print(numpy.vstack((x, y))) # 垂直堆叠:相对于垂直组合
print(numpy.hstack((x, y))) # 水平堆叠：相对于水平组合
# dstack：按深度堆叠
print(numpy.split(x,2,axis=0)) 
# 按行分割 [array([[1, 2, 3]]), array([[4, 5, 6]])]
print(numpy.split(x,3,axis=1)) 
# 按列分割 [array([[1],[4]]), array([[2],[5]]), array([[3],[6]])]

# 堆叠辅助类
import numpy as np
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print('r_用于按行堆叠')
print(np.r_[arr1, arr2])
'''
[[ 0.          1.        ]
 [ 2.          3.        ]
 [ 4.          5.        ]
 [ 0.22621904  0.39719794]
 [-1.2201912  -0.23623549]
 [-0.83229114 -0.72678578]]
'''
print('c_用于按列堆叠')
print(np.c_[np.r_[arr1, arr2], arr])
'''
[[ 0.          1.          0.        ]
 [ 2.          3.          1.        ]
 [ 4.          5.          2.        ]
 [ 0.22621904  0.39719794  3.        ]
 [-1.2201912  -0.23623549  4.        ]
 [-0.83229114 -0.72678578  5.        ]]
'''
print('切片直接转为数组')
print(np.c_[1:6, -10:-5])
'''
[[  1 -10]
 [  2  -9]
 [  3  -8]
 [  4  -7]
 [  5  -6]]
'''
