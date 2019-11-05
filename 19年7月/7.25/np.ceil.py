# np.ceil 函数返回输入值的上限，即对于输入 x ，返回最小的整数 i ，使得 i> = x。
# -*- coding: utf-8 -*-
"""
@author: tz_zs
"""
import numpy as np
 
n = np.array([-1.7, -2.5, -0.2, 0.6, 1.2, 2.7, 11])
 
ceil = np.ceil(n)
print(ceil)  # [ -1.  -2.  -0.   1.   2.   3.  11.]
