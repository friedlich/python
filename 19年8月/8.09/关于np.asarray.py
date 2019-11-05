from numpy import *

# np.asarray的定义：
def asarray(a, dtype=None, order=None):
    return array(a, dtype, copy=False, order=order)

# 而 np.array的定义：
def array(a, dtype=None, order=None):
    return array(a, dtype, copy=True, order=order)

# 简而言之：
# 主要区别在于 np.array（默认情况下）将会copy该对象，而 np.asarray除非必要，否则不会copy该对象