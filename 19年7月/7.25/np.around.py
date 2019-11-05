# np.around 返回四舍五入后的值，可指定精度。
# around(a, decimals=0, out=None)
# a 输入数组
# decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
# -*- coding: utf-8 -*-
"""
@author: tz_zs
"""
import numpy as np
 
n = np.array([-0.746, 4.6, 9.4, 7.447, 10.455, 11.555])
 
around1 = np.around(n)
print(around1)  # [ -1.   5.   9.   7.  10.  12.]
 
around2 = np.around(n, decimals=1)
print(around2)  # [ -0.7   4.6   9.4   7.4  10.5  11.6]
 
around3 = np.around(n, decimals=-1)
print(around3)  # [ -0.   0.  10.  10.  10.  10.]
