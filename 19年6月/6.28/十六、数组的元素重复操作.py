import numpy

print('数组的元素重复操作')
x = numpy.array([[1,2],[3,4]])
print(x.repeat(2)) # 按元素重复 [1 1 2 2 3 3 4 4]
print(x.repeat(2,axis=0)) # 按行重复 [[1 2][1 2][3 4][3 4]]
print(x.repeat(2,axis=1)) # 按列重复 [[1 1 2 2][3 3 4 4]]
x = numpy.array([1,2])
print(numpy.tile(x,2)) # tile瓦片：[1 2 1 2]
print(numpy.tile(x, (2, 2)))  # 指定从低维到高维依次复制的次数。 
# [[1 2 1 2][1 2 1 2]]
