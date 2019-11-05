import numpy

print('一元ufunc示例')
x = numpy.arange(6)
print(x) # [0 1 2 3 4 5]
print(numpy.square(x)) # [ 0  1  4  9 16 25]
x = numpy.array([1.5,1.6,1.7,1.8])
y,z = numpy.modf(x)
print(y) # [ 0.5  0.6  0.7  0.8]
print(z) # [ 1.  1.  1.  1.]

print('二元ufunc示例')
x = numpy.array([[1,4],[6,7]])
y = numpy.array([[2,3],[5,8]])
print(numpy.maximum(x,y)) # [[2,4],[6,8]]
print(numpy.minimum(x,y)) # [[1,3],[5,7]]
