# 有时，当我们想要遍历列表时，一些方法会派上用场
# 1）filter（）
# 过滤器允许我们根据条件逻辑过滤一些值。
print(list(filter(lambda x: x>5, range(8))))
[6,7]
# 2）map（）
# Map将函数应用于iterable中的每个元素。
print(list(map(lambda x: x**2, range(8))))
[0,1,4,9,16,25,36,49]
# 3）reduce（）
# 在我们达到单个值之前，Reduce会反复减少序列顺序。
from functools import reduce
print(reduce(lambda x, y: '{}{}'.format(x,y), [1,2,3,4,5]))
-13