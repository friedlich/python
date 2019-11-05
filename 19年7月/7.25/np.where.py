# numpy.where(condition[, x, y])
# 根据 condition 从 x 和 y 中选择元素，当为 True 时，选 x，否则选 y。
import numpy as np
 
data = np.random.random([2, 3])
print(data)
'''
[[ 0.93122679  0.82384876  0.28730977]
 [ 0.43006042  0.73168913  0.02775572]]
'''
 
result = np.where(data > 0.5, data, 0)
print(result)
'''
[[ 0.93122679  0.82384876  0.        ]
 [ 0.          0.73168913  0.        ]]
'''
