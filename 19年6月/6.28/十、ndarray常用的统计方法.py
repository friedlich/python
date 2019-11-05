import numpy

print('numpy的基本统计方法')
x = numpy.array([[1,2],[3,3],[1,2]]) #同一维度上的数组长度须一致
print(x)
print(x.mean()) # 2
print(x.mean(axis=1)) # 对每一行的元素求平均
print(x.mean(axis=0)) # 对每一列的元素求平均
print(x.sum()) #同理 12
print(x.sum(axis=1)) # [3 6 3]
print(x.max()) # 3
print(x.max(axis=1)) # [2 3 2]
print(x.cumsum()) # [ 1  3  6  9 10 12]
print(x.cumprod()) # [ 1  2  6 18 18 36]

# 用于布尔数组的统计方法：
# sum : 统计数组/数组某一维度中的True的个数
# any： 统计数组/数组某一维度中是否存在一个/多个True
# all：统计数组/数组某一维度中是否都是True
print('用于布尔数组的统计方法')
x = numpy.array([[True,False],[True,False]])
print(x.sum()) # 2
print(x.sum(axis=1)) # [1,1]
print(x.any(axis=0)) # [True,False]
print(x.all(axis=1)) # [False,False]

# 使用sort对数组/数组某一维度进行就地排序（会修改数组本身）
print('.sort的就地排序')
x = numpy.array([[1,6,2],[6,1,3],[1,5,2]])
x.sort(axis=1) 
print(x)# [[1 2 6] [1 3 6] [1 2 5]]
#非就地排序：numpy.sort()可产生数组的副本




