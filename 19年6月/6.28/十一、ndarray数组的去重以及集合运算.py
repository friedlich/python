import numpy

print('ndarray的唯一化和集合运算')
x = numpy.array([[1,6,2],[6,1,3],[1,5,2]])
print(numpy.unique(x)) # [1,2,3,5,6]
y = numpy.array([1,6,5])
print(numpy.in1d(x,y)) # [ True  True False  True  True False  True  True False]
print(numpy.setdiff1d(x,y)) # [2 3]
print(numpy.intersect1d(x,y)) # [1 5 6]
