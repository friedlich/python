import numpy

print('where函数的使用')
cond = numpy.array([True,False,True,False])
x = numpy.where(cond,-2,2)
print(x) # [-2  2 -2  2]
cond = numpy.array([1,2,3,4])
x = numpy.where(cond>2,-2,2)
print(x) # [ 2  2 -2 -2]
y1 = numpy.array([-1,-2,-3,-4])
y2 = numpy.array([1,2,3,4])
x = numpy.where(cond>2,y1,y2) # 长度须匹配
print(x) # [1,2,-3,-4]

print('where函数的嵌套使用')
y1 = numpy.array([-1,-2,-3,-4,-5,-6])
print(y1)
y2 = numpy.array([1,2,3,4,5,6])
print(y2)
y3 = numpy.zeros(6)
print(y3)
cond = numpy.array([1,2,3,4,5,6])
print(cond)
x = numpy.where(cond>5,y3,numpy.where(cond>2,y1,y2))
print(x) # [ 1.  2. -3. -4. -5.  0.]
