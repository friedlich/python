# np.floor 返回不大于输入参数的最大整数。 即对于输入值 x ，将返回最大的整数 i ，使得 i <= x。 
# 注意在Python中，向下取整总是从 0 舍入。
# -*- coding: utf-8 -*-
"""
@author: tz_zs
"""
import numpy as np
 
n = np.array([-1.7, -2.5, -0.2, 0.6, 1.2, 2.7, 11])
 
floor = np.floor(n)
print(floor)  # [ -2.  -3.  -1.   0.   1.   2.  11.]
 